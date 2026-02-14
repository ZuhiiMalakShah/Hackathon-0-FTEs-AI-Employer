import argparse
import os
import asyncio
from playwright.async_api import async_playwright

async def post_linkedin(text):
    email = os.environ.get("LINKEDIN_EMAIL")
    password = os.environ.get("LINKEDIN_PASSWORD")

    if not email or not password:
        print("Error: LINKEDIN_EMAIL or LINKEDIN_PASSWORD environment variables not set.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Headless=False for debugging/login
        context = await browser.new_context()
        page = await context.new_page()

        print(f"Logging into LinkedIn as {email}...")
        await page.goto("https://www.linkedin.com/login")
        await page.fill("#username", email)
        await page.fill("#password", password)
        await page.click("button[type='submit']")

        # Wait for login to complete or handle security checks manually if needed
        await page.wait_for_selector(".share-box-feed-entry__trigger", timeout=30000)
        
        print("Creating post...")
        await page.click(".share-box-feed-entry__trigger")
        await page.wait_for_selector(".ql-editor")
        await page.fill(".ql-editor", text)
        
        await page.click(".share-actions__primary-action")
        print("Post submitted successfully!")
        
        await asyncio.sleep(5)
        await browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post to LinkedIn using Playwright.")
    parser.add_argument("--text", required=True, help="Post content")
    
    args = parser.parse_args()
    asyncio.run(post_linkedin(args.text))
