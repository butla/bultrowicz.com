.PHONY: build
build:
	poetry run ablog build

.PHONY: build_continuously
build_continuously:
	fd '.rst|.md' | entr -c make build

.PHONY: setup_development
setup_development:
	poetry install --no-root

.PHONY: run
run:
	poetry run ablog serve

WEBSITE_PACKAGE:=bultrowicz_com_dist.tar.gz
WEBSITE_DIST_FOLDER:=_website/

.PHONY: deploy
deploy: build build_additional_page
	@echo === Building done, preparing package... ===
	cp -r additional_pages/terms_of_working_with_me _website/
	tar caf $(WEBSITE_PACKAGE) $(WEBSITE_DIST_FOLDER)
	@echo === Package prepared, uploading... ===
	scp $(WEBSITE_PACKAGE) bultrowicz.com:~
	@echo === Extracting package... ===
	ssh bultrowicz.com "tar xaf $(WEBSITE_PACKAGE)"
	@echo === Swapping old website files for the new... ===
	ssh bultrowicz.com -t "sudo rsync -av --del $(WEBSITE_DIST_FOLDER) /var/www/html/"
	@echo === Cleaning up... ===
	ssh bultrowicz.com "rm -rf $(WEBSITE_DIST_FOLDER) $(WEBSITE_PACKAGE)"
	rm $(WEBSITE_PACKAGE)

.PHONY: cv
cv:
	poetry run python cv/build_cv_pdf.py


.PHONY: cv-rebuilding
# watch CV HTML and keep rebuilding the PDF
cv-rebuilding:
	fd '(.*\.html$$)|(.*\.css$$)' cv | entr poetry run python cv/build_cv_pdf.py


# TODO I know, I should integrate it with ablog, or just redo the site with some static site tool.
# No time for that right now, though.
.PHONY: build_additional_page
build_additional_page:
	mkdir -p additional_pages/terms_of_working_with_me
	# markdown_strict used so that ' and " don't get rendered to characters that can not render on the page
	pandoc -t html -o additional_pages/terms_of_working_with_me/index.html -f markdown_strict additional_pages_sources/terms_of_working_with_me.md
