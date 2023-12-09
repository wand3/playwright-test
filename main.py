#!/usr/bin/env python3
import asyncio
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
    page.goto("https://www.google.com/search?q=sportyng&oq=sportyng&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEwMDY3ajBqMagCALACAA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="Login", exact=True).click()
    page.goto("https://www.sportybet.com/ng/m/")
    page.locator("input[name=\"phone\"]").fill("8159348152")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("/Poiuytrewq123")
    page.get_by_role("button", name="Login").click(force=True)


    # page.get_by_role("button", name="Go to Confirm").click()
    # page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("link", name="OK").click()

    # page.locator(".icon-cross").click()
    # page.get_by_text("Bets").click()
    # page.get_by_text("Winnings").click()
    # page.get_by_text("Bets").click()
    page.locator("#header_nav_sports").click()
    page.get_by_placeholder("Booking Code").click()
    page.get_by_placeholder("Booking Code").fill("0687d016")
    page.get_by_role("button", name="Load").click()
    page.get_by_placeholder("min.").click()
    # page.get_by_placeholder("min.").dblclick()
    # page.get_by_placeholder("min.").press("ArrowRight")
    # page.get_by_placeholder("min.").press("ArrowRight")
    page.get_by_placeholder("min.").fill("10")
    page.get_by_text("Load", exact=True).click()
        
    page.get_by_role("button", name="Place Bet").click()
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("button", name="OK").click()
    # page.get_by_role("button", name="Place Bet").click()
    # await page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("button", name="Cancel").click()
    # page.get_by_role("button", name="Place Bet").click()
    # page.get_by_role("button", name="Cancel").click()
    # page.locator("div:nth-child(31) > div:nth-child(2) > .m-lay-mid > .m-item-play").click()
    # page.get_by_placeholder("min.").click()
    # page.get_by_placeholder("min.").press("ArrowRight")
    # page.get_by_placeholder("min.").press("Enter")
    # page.get_by_placeholder("min.").click()
    # page.get_by_placeholder("min.").press("ArrowRight")
    # page.get_by_placeholder("min.").press("ArrowRight")
    # page.get_by_placeholder("min.").fill("15")
    # page.get_by_role("button", name="Place Bet").click()
    # page.get_by_role("button", name="Place Bet").click()
    # page.get_by_role("button", name="Confirm").click()
    # page.locator("#esDialog1").get_by_role("img").first.click()
    # page.get_by_placeholder("min.").click()
    page.goto("https://www.sportybet.com/ng/m/")
    # page.get_by_placeholder("Booking Code").click()
    # page.get_by_placeholder("Booking Code").click()
    # page.get_by_placeholder("Booking Code").dblclick()
    # page.get_by_placeholder("Booking Code").fill("0687d016")
    # page.get_by_text("Load", exact=True).click()
    # page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("button", name="OK").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
