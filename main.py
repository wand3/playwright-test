#!\usr\bin\python3
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False)
    browser = playwright.firefox.launch(headless=False)
    
    context = browser.new_context()
    page = context.new_page()
    # Save storage state into the file.
    storage = context.storage_state(path="state.json")
    # Create a new context with the saved storage state.
    context = browser.new_context(storage_state="state.json") 


    # goto sporty page and login
    '''
    page.goto("https://www.sportybet.com/ng", timeout=60000)
    # https://www.sportybet.com/ng/lite/login
    page.locator("input[name=\"phone\"]").fill("8159348152")
    # page.locator("input[name=\"phone\"]").fill("8100366297")

    page.wait_for_timeout(2000)    

    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("/Poiuytrewq123")
    # page.get_by_placeholder("Password").fill("_!Qwerfy123")

    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Login").click(force=True)
    page.get_by_placeholder("Booking Code").click()
    '''
    # login lite version
    page.goto("https://www.sportybet.com/ng/lite/login", timeout=60000)
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("8159348152")
    page.wait_for_timeout(2000)    

    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("/Poiuytrewq123")
    page.wait_for_timeout(2000)    
    page.get_by_role("button", name="Log In").click()
    # loop for placing values
    numbers = ["1f3422e", "e4b74b4b3", "21197200"]
    count = 0
    while count <= len(numbers):
        for i in range(len(numbers)):
            place = numbers[i]
            """
            page.get_by_placeholder("Booking Code").fill(f'{place}')
            page.get_by_role("button", name="Load").click()
            page.get_by_placeholder("min.").click()
            page.wait_for_timeout(6000)
            # page.get_by_placeholder("min.").dblclick()
            # page.get_by_placeholder("min.").press("ArrowRight")
            # page.get_by_placeholder("min.").press("ArrowRight")
            page.get_by_placeholder("min.").fill("10")
            page.get_by_text("Load", exact=True).click()
            page.get_by_role("button", name="Place Bet").click()
            page.get_by_text("Accept Changes").click()

            page.get_by_role("button", name="Confirm").click()
            page.get_by_role("button", name="OK").click()
            page.get_by_text("Sports").click()
            """
            # mobile lite version
            page.get_by_role("link", name="Betslip(0)").click()
            page.get_by_placeholder("Booking code").click()
            page.get_by_placeholder("Booking code").click()
            page.get_by_placeholder("Booking code").fill(f"{place}")
            page.get_by_role("button", name="Load").click()
            page.get_by_placeholder("min").click()
            page.get_by_placeholder("min").fill("10")
            page.get_by_placeholder("min").click()
            page.get_by_placeholder("min").fill("10")
            page.get_by_role("button", name="Place Bet").click()
            page.get_by_role("button", name="Confirm").click()
            page.get_by_role("link", name="OK").click()





    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

