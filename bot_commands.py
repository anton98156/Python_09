from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from game import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def game_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'{update.start()}')