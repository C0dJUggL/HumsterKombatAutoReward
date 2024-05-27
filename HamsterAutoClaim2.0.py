import pyautogui
import schedule
import time
import asyncio
import random
from telegram import Bot

# Your bot token and chat ID
TELEGRAM_BOT_TOKEN = '6861546370:AAHfkESWsszzlfseAqrEpPOKcJFTkK8X6ZA'
CHAT_ID = '882510248'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def click_account(account_number):
    message = f"Приступаю к {account_number} аккаунту"
    await send_telegram_message(message)

    x, y = random.randint(789, 1220), random.randint(129, 172)
    pyautogui.moveTo(789 + 65 * (account_number - 1), 444)
    pyautogui.doubleClick()
    time.sleep(25)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(random.randint(734, 782), random.randint(1002, 1014))
    pyautogui.click()
    time.sleep(10)
    cx1, cy1 = 749, 140
    pixel_color1 = pyautogui.pixel(cx1, cy1)
    expected_color1 = (91, 91, 92)
    expected_color2 = (90, 91, 92)
    if pixel_color1 != expected_color1 and pixel_color1 != expected_color2:
        message = f"Неверный цвет пикселя на координатах ({cx1}, {cy1})"
        await send_telegram_message(message)
        pyautogui.moveTo(1258, 18)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1111, 567)
        pyautogui.click()
    pyautogui.moveTo(random.randint(759, 1243), random.randint(927, 971))
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1258, 18)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1111, 567)
    pyautogui.click()
    time.sleep(2)
    message = f"Все клики выполнены, награда с {account_number} аккаунта забрана"
    await send_telegram_message(message)

async def job():
    for account_number in range(1, 5):
        await click_account(account_number)

    message = "Следующие награды будут собраны через 3 часа"
    await send_telegram_message(message)

def schedule_job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(job())

schedule.every(3).hours.do(schedule_job)
print("Запланировано выполнение кликов каждые 3 часа")
while True:
    schedule.run_pending()
    time.sleep(1)