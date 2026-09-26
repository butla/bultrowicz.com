{#- Used by the search page. The URL is the same as the old Sphinx search index. -#}
window.SEARCH_INDEX = [
{%- for post in blog_posts() %}
  {{ {"title": post.title, "url": post|url, "date": post.pub_date.isoformat(), "tags": post.tags|list, "text": post.body.html|plain_text}|tojson }}{{ "," if not loop.last }}
{%- endfor %}
];
