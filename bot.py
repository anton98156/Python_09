from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6118659428:AAErWajgtqVAhADvPJKzZ9Hfx2Cc5JbOTYM").build()

app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("game", game_bot))

print('server start')

app.run_polling()

# user_name - python98156_bot