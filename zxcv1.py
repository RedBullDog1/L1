from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = (
        "Доступні команди:\n"
        "/menu - меню\n"
        "/whisper <текст> -  *TEXT* малими літерами\n"
        "/scream <текст> - *TEXT* великими літерами"
    )
    await update.message.reply_text(menu_text)

async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        whispered_text = ' '.join(context.args).lower()
        await update.message.reply_text(whispered_text)
    else:
        await update.message.reply_text("*TEXT* /whisper")

async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        screamed_text = ' '.join(context.args).upper()
        await update.message.reply_text(screamed_text)
    else:
        await update.message.reply_text("*TEXT*/scream")
def main():
    application = ApplicationBuilder().token("123123123123123123123123").build()
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("whisper", whisper))
    application.add_handler(CommandHandler("scream", scream))
    print("Бот запущено.")
    application.run_polling()
if __name__ == "__main__":
    main()
