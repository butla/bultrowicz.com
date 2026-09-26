bultrowicz.com
==============

The code for my blog. Built with [Lektor](https://www.getlektor.com/) and [Tailwind CSS](https://tailwindcss.com/).

Development
-----------

- `make setup_development` - install the Python (Poetry) and JS (npm) dependencies.
- `make run` - development server at http://localhost:5000 that rebuilds the pages and styles on changes.
  The admin UI for editing the content is at http://localhost:5000/admin.
- `make build` - build the site into `_website/`.
- `make deploy` - build and upload the site.

Layout
------

- `content/` - the pages. Every post is `content/<url-slug>/contents.lr`. Posts without a publication date are drafts.
- `content/contents.lr` - the main page. It's made of blocks (text, recent posts, featured posts, tag cloud)
  that can be added, removed and reordered, either in the admin UI or by editing the file.
- `content/blog/**` - post listings ("collections"). They can group posts by tag, year, etc.
  and generate a sub-page with an Atom feed for every group (e.g. `/blog/tag/python/atom.xml`).
- `databags/` - site settings (title, Disqus, etc.), the menu and the footer links.
- `models/`, `flowblocks/` - the fields of the pages and of the main page's blocks.
- `templates/` - the HTML (Jinja) templates, styled with Tailwind classes.
- `frontend/main.css` - the source of the stylesheet (Tailwind, the typography plugin, theme tweaks).
- `packages/butlablog/` - Lektor plugin with the blog features (listings, feeds, syntax highlighting).
- `assets/` - static files, copied as they are. `_static` and `_images` keep the URLs from the old (ABlog) site.
