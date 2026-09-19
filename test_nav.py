from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1024, 'height': 800})
    page.goto('http://localhost:8000')
    page.wait_for_timeout(1000)

    # Hover over third item (Experience)
    item = page.locator('.navbar-item:nth-child(3)')
    item.hover()
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/screenshots/nav_dock_hover.png")
    browser.close()
