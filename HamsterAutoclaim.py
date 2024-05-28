import pyautogui
import schedule
import time
import asyncio
import random
from telegram import Bot
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Your bot token and chat ID
TELEGRAM_BOT_TOKEN = 'TELEGRAM_BOT_TOKEN'
CHAT_ID = 'CHAT_ID'

bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def send_telegram_message(message):
    """Sends a message to the specified Telegram chat."""
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def get_income():
    """Captures a screenshot and extracts the balance text."""
    x, y, width, height = 878, 777, 273, 64
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    screenshot = screenshot.convert('L')


    income_text = pytesseract.image_to_string(screenshot)

    return income_text.strip()


async def get_balance():
    """Captures a screenshot and extracts the balance text."""
    x, y, width, height = 838, 252, 350, 65
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    screenshot = screenshot.convert('L')


    balance_text = pytesseract.image_to_string(screenshot)

    return balance_text.strip()


async def click_account(account_number):
    """Performs a series of automated clicks for a specified account number."""
    await send_telegram_message(f"Starting with account {account_number}")
    # Randomize the coordinates for clicking
    x, y = random.randint(794, 1162), random.randint(121, 134)
    # Move to the account icon and double-click
    pyautogui.moveTo(789 + 65 * (account_number - 1), 444)
    pyautogui.doubleClick()
    start_x = 999
    start_y = 666
    end_x = 999
    end_y = 345
    time.sleep(25)
    # Move and click on a random position
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.3)  # Свайп за 0.5 секунды
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(3)
    # Move and click to a second random position
    pyautogui.moveTo(random.randint(734, 782), random.randint(1002, 1014))
    pyautogui.click()
    time.sleep(10)
    cx1, cy1 = 749, 140
    pixel_color1 = pyautogui.pixel(cx1, cy1)
    expected_color1 = (91, 91, 92)
    expected_color2 = (90, 91, 92)
    expected_color3 = (91, 91, 93)
    if pixel_color1 != expected_color1 and pixel_color1 != expected_color2 and pixel_color1 != expected_color3:
        await send_telegram_message(f"Incorrect pixel color at coordinates ({cx1}, {cy1})")
        # Close incorrect screen
        pyautogui.moveTo(1258, 18)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1111, 567)
        pyautogui.click()
    income = await get_income()
    time.sleep(1)
    # Final series of clicks to collect rewards
    pyautogui.moveTo(random.randint(759, 1243), random.randint(927, 971))
    pyautogui.click()
    time.sleep(2)
    balance = await get_balance()
    time.sleep(2)
    pyautogui.moveTo(1258, 18)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1111, 567)
    pyautogui.click()
    time.sleep(2)
    await send_telegram_message(f"Income for account {account_number}: {income}, balance: {balance}")
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
