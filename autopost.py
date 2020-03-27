import schedule
import glob
import os
import sys
import time
from io import open

from instabot import Bot  
bot = Bot()
bot.login()

def job():
	nama_file = "gambar"
	gambar = nama_file+".jpg"
	with open(nama_file+".txt", "r") as file:
		caption = file.read()
	bot.upload_photo(gambar, caption=caption)
	if bot.api.last_response.status_code != 200:
		print(bot.api.last_response)

schedule.every().day.at("14:58").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)