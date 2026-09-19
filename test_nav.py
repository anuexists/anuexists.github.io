from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on("pageerror", lambda err: print(f"PAGE ERROR: {err.message}"))
    page.goto('http://localhost:8000')

    # Click Projects
    page.locator('button[data-nav-link]:has-text("Projects")').click()
    page.wait_for_timeout(500)

    projects_page = page.locator('article[data-page="projects"]')
    print("Projects active class:", projects_page.get_attribute("class"))

    browser.close()
