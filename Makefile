WEBSITE_DIST_FOLDER:=_website/
WEBSITE_PACKAGE:=bultrowicz_com_dist.tar.gz

TAILWIND:=npx @tailwindcss/cli --input frontend/main.css --output assets/static/main.css
PYGMENTS_CSS:=frontend/generated/pygments.css
# Syntax highlighting color schemes. See the list with `uv run pygmentize -L styles`.
PYGMENTS_LIGHT_STYLE:=xcode
PYGMENTS_DARK_STYLE:=github-dark

.PHONY: setup_development
setup_development:
	uv sync --locked
	npm ci

.PHONY: build
build: css
	uv run lektor build --output-path $(WEBSITE_DIST_FOLDER)

# Development server with live reloading of both the content and the styles.
# Lektor's admin UI (for editing the pages, including the main page's blocks) is at http://localhost:5000/admin
.PHONY: run
run: $(PYGMENTS_CSS)
	$(MAKE) --jobs=2 css_continuously serve

.PHONY: serve
serve:
	uv run lektor server --port 5000

.PHONY: css
css: $(PYGMENTS_CSS)
	$(TAILWIND) --minify

.PHONY: css_continuously
css_continuously:
	$(TAILWIND) --watch=always

$(PYGMENTS_CSS): Makefile
	mkdir -p $(dir $@)
	uv run pygmentize -S $(PYGMENTS_LIGHT_STYLE) -f html -a .highlight > $@
	uv run pygmentize -S $(PYGMENTS_DARK_STYLE) -f html -a '.dark .highlight' >> $@

.PHONY: clean
clean:
	rm -rf $(WEBSITE_DIST_FOLDER) assets/static/main.css frontend/generated
	uv run lektor clean --yes

.PHONY: deploy
deploy: build
	@echo === Building done, preparing package... ===
	# .lektor holds the build state, not a part of the website
	tar caf $(WEBSITE_PACKAGE) --exclude=.lektor $(WEBSITE_DIST_FOLDER)
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
	uv run python cv/build_cv_pdf.py

.PHONY: cv-rebuilding
# watch CV HTML and keep rebuilding the PDF
cv-rebuilding:
	fd '(.*\.html$$)|(.*\.css$$)' cv | entr uv run python cv/build_cv_pdf.py
