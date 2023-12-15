#!/usr/bin/env python3
"""
    Playwright test

"""
import asyncio
from playwright.async_api import Playwright, async_playwright


# async function for running test
async def place():
    async with async_playwright() as p:
        
        # browser configs
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        page = await context.new_page()
        # goto site
        # await page.goto("https://www.google.com/search?q=sportyng&oq=sportyng&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEwMDY3ajBqMagCALACAA&sourceid=chrome&ie=UTF-8", timeout=50000)
        # await page.get_by_role("link", name="Login", exact=True).click()
        await page.goto("https://www.sportybet.com/ng", timeout=60000)
        # dismiss dialog
        # if page.on("dialog"):
        #     await page.on("dialog", lambda dialog: dialog.dismiss())
        # else:
        #     # goto login 
        await page.locator("input[name=\"phone\"]").click()
        await asyncio.sleep(2)    
        await page.locator("input[name=\"phone\"]").fill("8159348152")
        await asyncio.sleep(5)
        await page.get_by_placeholder("Password").click()
        await page.get_by_placeholder("Password").fill("/Poiuytrewq123")
        # await page.get_by_role("button", name="Login").click(force=True)
        await page.get_by_placeholder("Booking Code").click()

        
# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("http://playwright.dev")
#         print(await page.title())
#         await browser.close()

    await context.close()

asyncio.run(place())
