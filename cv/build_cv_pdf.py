from pathlib import Path

from playwright.sync_api import sync_playwright


def render_cv_pdf():
    cv_source_file = (Path(__file__) / '../cv_Michał_Bultrowicz.html').resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path='/usr/bin/chromium')
        page = browser.new_page()
        page.goto(cv_source_file)
        # Looks like `await page.emulate_media(media='screen')` from the docs
        # (https://playwright.dev/python/docs/api/class-page#page-pdf) doesn't change anything.
        page.pdf(
            path='cv_Michał_Bultrowicz.pdf',
            format='A4',
            # Looks like you can do the below or add `-webkit-print-color-adjust: exact;` in CSS to preserve
            # background colors.
            print_background=True,
        )


if __name__ == "__main__":
    render_cv_pdf()
    print('CV built!')
