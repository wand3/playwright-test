#!/usr/bin/env python3
"""
    Playwright test

"""
import asyncio
from playwright.sync_api import Playwright, sync_playwright, expect


# async function for running test
async def place(playwright : Playwright) -> None:
    # browser configs
    browser = await playwright.chromium.launch_persistent_context(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    # goto site
    page.goto("https://www.google.com/search?q=sportyng&oq=sportyng&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEwMDY3ajBqMagCALACAA&sourceid=chrome&ie=UTF-8")
    
# and login

# save storage state like login cookies

# create a new context with the saved strage state


# clear popup dialog

