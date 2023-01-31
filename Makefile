build:
	poetry run ablog build

build_continuously:
	fd .rst | entr -c make build

run:
	poetry run ablog serve

deploy:
	cd deployment; ANSIBLE_NOCOWS=1 poetry run ansible-playbook playbook.yml -i inventory.yml --ask-become-pass

# TODO I know, I should integrate it with ablog, or just redo the site with some static site tool.
# No time for that right now, though.
build_additional_page:
	mkdir -p additional_pages/terms_of_working_with_me
	# markdown_strict used so that ' and " don't get rendered to characters that can not render on the page
	pandoc -t html -o additional_pages/terms_of_working_with_me/index.html -f markdown_strict additional_pages_sources/terms_of_working_with_me.md
