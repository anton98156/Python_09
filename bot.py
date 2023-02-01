# Прикрутить бота к задачам с предыдущего семинара:
# Создать телефонный справочник с возможностью импорта и экспорта данных.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from logger import *
import os
os.system("clear")

app = ApplicationBuilder().token("6118659428:AAErWajgtqVAhADvPJKzZ9Hfx2Cc5JbOTYM").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("import_contact", import_command))
app.add_handler(CommandHandler("export", export_command))

print('server start')

app.run_polling()

# user_name - python98156_bot