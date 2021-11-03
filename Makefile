build_continuously:
	fd .rst | entr -c ablog build

run:
	ablog serve

deploy:
	cd deployment; bash deploy.sh

# requirements created with "pip install ablog; pip freeze > requirements.txt"
install_into_venv:
	pip install -r requirements.txt

# TODO ' and " get replaced with other characters, display incorrectly. Fix
# https://stackoverflow.com/questions/53678363/stopping-pandoc-from-escaping-single-quotes-when-converting-from-html-to-markdow
# TODO I know, I should integrate it with ablog, or just redo the site with some static site tool.
# No time for that right now, though.
build_additional_page:
	mkdir -p additional_pages/terms_of_working_with_me
	pandoc -t html -o additional_pages/terms_of_working_with_me/index.html additional_pages_sources/terms_of_working_with_me.md

# TODO translate GBP rates to USD, and EUR (i take all of them), round up to closest 10.
# - don't replaced if not replaced already
