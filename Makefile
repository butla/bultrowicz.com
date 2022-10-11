# TODO how to run this through poetry?
# It'd be amazing if I didn't need to think about activating a venv for this.
build_continuously:
	fd .rst | entr -c poetry run ablog build

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

# TODO translate GBP rates to USD, and EUR (i take all of them), round up to closest 10.
# - don't replaced if not replaced already
