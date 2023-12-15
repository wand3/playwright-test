#!\usr\bin\python3
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context()
    page = context.new_page()
    # Save storage state into the file.
    storage = context.storage_state(path="state.json")
    # Create a new context with the saved storage state.
    context = browser.new_context(storage_state="state.json") 


    # goto sporty page and login
    page.goto("https://www.sportybet.com/ng", timeout=60000)
    page.locator("input[name=\"phone\"]").fill("8159348152")
    time.sleep(2)    

    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("/Poiuytrewq123")
    time.sleep(2)
    page.get_by_role("button", name="Login").click(force=True)


    # page.get_by_role("button", name="Go to Confirm").click()
    # page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("link", name="OK").click()

    # page.locator(".icon-cross").click()
    # page.get_by_text("Bets").click()
    # page.get_by_text("Winnings").click()
    page.get_by_placeholder("Booking Code").click()
    
    # loop for placing values
    numbers = ["c53d424", "92d558b7", "21197200"]
    count = 0
    while count <= len(numbers):
        for i in range(len(numbers)):
            place = numbers[i]
            page.get_by_placeholder("Booking Code").fill(f'{place}')
            page.get_by_role("button", name="Load").click()
            page.get_by_placeholder("min.").click()
            time.sleep(9) 
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



    # page.get_by_placeholder("Booking Code").fill("")
    # page.get_by_role("button", name="Load").click()
    # page.get_by_placeholder("min.").click()
    # time.sleep(9) 
    # # page.get_by_placeholder("min.").dblclick()
    # # page.get_by_placeholder("min.").press("ArrowRight")
    # # page.get_by_placeholder("min.").press("ArrowRight")
    # page.get_by_placeholder("min.").fill("10")
    # page.get_by_text("Load", exact=True).click()
        
    # page.get_by_role("button", name="Place Bet").click()
    # page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("button", name="OK").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
