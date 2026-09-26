"""Blog features for the site: post queries, grouped listings with generated sub-pages and Atom feeds,
and Markdown rendering tweaks (syntax highlighting, heading anchors).

A "collection" page (see models/collection.ini) lists posts, optionally grouped by one of the GROUPINGS,
and can generate a sub-page with a feed for every group, e.g. /blog/tag/python/ and /blog/tag/python/atom.xml.
"""
import posixpath
import re
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date

import jinja2
import pygments
import pygments.formatters
import pygments.lexers
import pygments.util
from lektor.build_programs import BuildProgram
from lektor.context import get_ctx
from lektor.pluginsystem import Plugin
from lektor.sourceobj import VirtualSourceObject
from markupsafe import Markup

VIRTUAL_PATH_PREFIX = "blog"
FEED_FILENAME = "atom.xml"


def slugify(text):
    """The same slugs that ABlog made, so that the old URLs stay the same."""
    text = unicodedata.normalize("NFKD", str(text))
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def anchor_id(text):
    """Heading IDs in the style of docutils, so that the old in-page links keep working."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


@dataclass(frozen=True)
class Grouping:
    # how to get the group keys of a post
    keys: Callable
    # title of the page of a single group
    title: str
    newest_first: bool = False


GROUPINGS = {
    "tag": Grouping(lambda post: post["tags"], "Posts tagged {}"),
    "year": Grouping(lambda post: [post["pub_date"].year], "Posted in {}", newest_first=True),
    "author": Grouping(lambda post: [post["author"]], "Posts by {}"),
    "language": Grouping(lambda post: [post["language"]], "Posts in {}"),
    "initial": Grouping(lambda post: [post["title"][:1].upper()], "{}"),
}


@dataclass
class Group:
    key: object
    posts: list = field(default_factory=list)

    @property
    def slug(self):
        return slugify(self.key)


def is_post(record):
    return record.datamodel.id == "post"


def is_published(post):
    return bool(post["pub_date"])


def iter_records(record):
    yield record
    for child in record.children.include_undiscoverable(True):
        yield from iter_records(child)


def get_posts(pad, drafts=False, tag=None):
    posts = [
        record
        for record in iter_records(pad.root)
        if is_post(record) and is_published(record) != drafts and (not tag or tag in record["tags"])
    ]
    if drafts:
        return sorted(posts, key=lambda post: post["title"].casefold())
    return sorted(posts, key=lambda post: (post["pub_date"], post["title"]), reverse=True)


def group_posts(posts, grouping_name):
    grouping = GROUPINGS[grouping_name]
    groups = {}
    for post in posts:
        for key in grouping.keys(post):
            if key:
                groups.setdefault(key, Group(key)).posts.append(post)
    return sorted(
        groups.values(),
        key=lambda group: str(group.key).casefold(),
        reverse=grouping.newest_first,
    )


@dataclass
class Listing:
    """What a collection page or one of its group sub-pages shows. The same template renders both."""

    title: str
    posts: list
    group_by: str | None = None
    intro: str | None = None
    feed_url: str | None = None

    @property
    def groups(self):
        return group_posts(self.posts, self.group_by) if self.group_by else []


def collection_listing(record):
    return Listing(
        title=record["title"],
        posts=get_posts(record.pad, drafts=record["posts"] == "drafts"),
        group_by=record["group_by"],
        intro=record["intro"],
        feed_url=Feed(record).url_path if record["feed"] else None,
    )


class GroupPage(VirtualSourceObject):
    """Page listing the posts of a single group, e.g. of a single tag."""

    def __init__(self, record, group):
        super().__init__(record)
        self.group = group

    @property
    def grouping_name(self):
        return self.record["group_pages"]

    @property
    def path(self):
        return f"{self.record.path}@{VIRTUAL_PATH_PREFIX}/{self.group.slug}"

    @property
    def url_path(self):
        return posixpath.join(self.record.url_path, self.group.slug, "")

    @property
    def listing(self):
        return Listing(
            title=GROUPINGS[self.grouping_name].title.format(self.group.key),
            posts=self.group.posts,
            feed_url=Feed(self).url_path,
        )


class Feed(VirtualSourceObject):
    """Atom feed of a collection page or a group page."""

    def __init__(self, listing_source):
        super().__init__(listing_source.record)
        self.listing_source = listing_source

    @property
    def path(self):
        if isinstance(self.listing_source, GroupPage):
            return f"{self.record.path}@{VIRTUAL_PATH_PREFIX}/feed/{self.listing_source.group.slug}"
        return f"{self.record.path}@{VIRTUAL_PATH_PREFIX}/feed"

    @property
    def url_path(self):
        return posixpath.join(self.listing_source.url_path, FEED_FILENAME)

    @property
    def listing(self):
        return get_listing(self.listing_source)


def get_listing(source):
    if isinstance(source, GroupPage):
        return source.listing
    return collection_listing(source)


def get_group_pages(record):
    grouping_name = record["group_pages"]
    if not grouping_name:
        return []
    groups = group_posts(get_posts(record.pad, drafts=record["posts"] == "drafts"), grouping_name)
    return [GroupPage(record, group) for group in groups]


def find_group_page(record, slug):
    return next((page for page in get_group_pages(record) if page.group.slug == slug), None)


class VirtualPageBuildProgram(BuildProgram):
    template = None

    def produce_artifacts(self):
        url_path = self.source.url_path
        artifact_name = posixpath.join(url_path, "index.html") if url_path.endswith("/") else url_path
        self.declare_artifact(artifact_name, sources=list(self.source.iter_source_filenames()))

    def build_artifact(self, artifact):
        artifact.render_template_into(self.template, this=self.source)


class GroupPageBuildProgram(VirtualPageBuildProgram):
    template = "collection.html"


class FeedBuildProgram(VirtualPageBuildProgram):
    template = FEED_FILENAME


class HighlightingRendererMixin:
    def block_code(self, code, lang=None):
        try:
            lexer = pygments.lexers.get_lexer_by_name(lang) if lang else pygments.lexers.TextLexer()
        except pygments.util.ClassNotFound:
            lexer = pygments.lexers.TextLexer()
        formatter = pygments.formatters.HtmlFormatter(cssclass="highlight")
        return pygments.highlight(code, lexer, formatter)

    def header(self, text, level, raw=None):
        heading_id = anchor_id(raw or re.sub(r"<[^>]+>", "", text))
        # docutils gives the repeated IDs numbers, like "id1"
        used_ids = self.meta.setdefault("heading_ids", set())
        if heading_id in used_ids:
            self.meta["duplicate_ids_count"] = self.meta.get("duplicate_ids_count", 0) + 1
            heading_id = f"id{self.meta['duplicate_ids_count']}"
        used_ids.add(heading_id)
        return f'<h{level} id="{heading_id}">{text}</h{level}>\n'


class ButlablogPlugin(Plugin):
    name = "butlablog"
    description = "Blog listings, feeds and Markdown tweaks for bultrowicz.com."

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(HighlightingRendererMixin)

    def on_setup_env(self, **extra):
        env = self.env
        env.jinja_env.globals.update(
            blog_posts=self.blog_posts,
            group_posts=group_posts,
            listing=get_listing,
            group_url=self.group_url,
            today=date.today,
        )
        env.jinja_env.filters.update(excerpt=self.excerpt, plain_text=self.plain_text, anchor_id=anchor_id)
        env.add_build_program(GroupPage, GroupPageBuildProgram)
        env.add_build_program(Feed, FeedBuildProgram)

        @env.generator
        def generate_collection_pages(source):
            if getattr(source, "datamodel", None) is None or source.datamodel.id != "collection":
                return
            group_pages = get_group_pages(source)
            yield from group_pages
            yield from (Feed(page) for page in group_pages)
            if source["feed"]:
                yield Feed(source)

        @env.virtualpathresolver(VIRTUAL_PATH_PREFIX)
        def resolve_virtual_path(record, pieces):
            if pieces == ["feed"]:
                return Feed(record)
            if len(pieces) == 2 and pieces[0] == "feed":
                page = find_group_page(record, pieces[1])
                return Feed(page) if page else None
            if len(pieces) == 1:
                return find_group_page(record, pieces[0])
            return None

        @env.urlresolver
        def resolve_url(record, url_path):
            if record.datamodel.id != "collection":
                return None
            if url_path == [FEED_FILENAME] and record["feed"]:
                return Feed(record)
            page = find_group_page(record, url_path[0]) if url_path else None
            if page and len(url_path) == 1:
                return page
            if page and url_path[1:] == [FEED_FILENAME]:
                return Feed(page)
            return None

    @staticmethod
    @jinja2.pass_context
    def blog_posts(context, drafts=False, tag=None):
        pad = context.get("site") or get_ctx().pad
        return get_posts(pad, drafts=drafts, tag=tag)

    @staticmethod
    @jinja2.pass_context
    def group_url(context, grouping_name, key):
        """URL of the sub-page of a group, e.g. of a tag, generated by any collection."""
        pad = context.get("site") or get_ctx().pad
        for record in iter_records(pad.root):
            if record.datamodel.id == "collection" and record["group_pages"] == grouping_name:
                return posixpath.join(record.url_path, slugify(key), "")
        return None

    @staticmethod
    def excerpt(post):
        if post["summary"].source.strip():
            return post["summary"].html
        html = str(post["body"].html)
        match = re.search(r"<p>.*?</p>", html, re.S)
        # footnote references would point nowhere outside of the post
        return Markup(re.sub(r'<sup class="footnote-ref".*?</sup>', "", match.group(0)) if match else "")

    @staticmethod
    def plain_text(html):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(html))).strip()
