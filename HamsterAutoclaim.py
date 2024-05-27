import pyautogui
import schedule
import time
import asyncio
import random
from telegram import Bot

# Your bot token and chat ID
TELEGRAM_BOT_TOKEN = 'TELEGRAM_BOT_TOKEN'
CHAT_ID = 'CHAT_ID'

bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def send_telegram_message(message):
    """Sends a message to the specified Telegram chat."""
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def click_account(account_number):
    """Performs a series of automated clicks for a specified account number."""
    await send_telegram_message(f"Starting with account {account_number}")

    # Randomize the coordinates for clicking
    x, y = random.randint(789, 1220), random.randint(129, 172)
    # Move to the account icon and double-click
    pyautogui.moveTo(789 + 65 * (account_number - 1), 444)
    pyautogui.doubleClick()
    time.sleep(25)
    # Move and click on a random position
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(3)
    # Move and click to a second random position
    pyautogui.moveTo(random.randint(734, 782), random.randint(1002, 1014))
    pyautogui.click()
    time.sleep(10)

    # Check the color of a specific pixel to ensure the correct screen is loaded
    cx1, cy1 = 749, 140
    pixel_color1 = pyautogui.pixel(cx1, cy1)
    expected_colors = [(91, 91, 92), (90, 91, 92)]

    if pixel_color1 not in expected_colors:
        await send_telegram_message(f"Incorrect pixel color at coordinates ({cx1}, {cy1})")
        # Close incorrect screen
        pyautogui.moveTo(1258, 18)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1111, 567)
        pyautogui.click()

    # Final series of clicks to collect rewards
    pyautogui.moveTo(random.randint(759, 1243), random.randint(927, 971))
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1258, 18)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1111, 567)
    pyautogui.click()
    time.sleep(2)

    await send_telegram_message(f"All clicks completed, reward collected from account {account_number}")


async def job():
    """Performs the job for all accounts and schedules the next run."""
    for account_number in range(1, 5):
        await click_account(account_number)

    await send_telegram_message("Next rewards will be collected in 3 hours")


def schedule_job():
    """Schedules the job to run every 3 hours."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(job())


# Schedule the job to run every 3 hours
schedule.every(3).hours.do(schedule_job)
print("Scheduled clicks every 3 hours")

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
