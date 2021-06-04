keep_building:
	fd .rst | entr -c ablog build

run:
	ablog serve

deploy:
	cd deployment; bash deploy.sh

# requirements created with "pip install ablog; pip freeze > requirements.txt"
install_into_venv:
	pip install -r requirements.txt

# TODO I know, I should integrate it with ablog, or just redo the site with some static site tool.
# No time for that right now, though.
build_additional_page:
	mkdir -p additional_pages/terms_of_working_with_me
	pandoc -t html -o additional_pages/terms_of_working_with_me/index.html additional_pages_sources/terms_of_working_with_me.md
