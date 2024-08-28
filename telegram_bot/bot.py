from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start(update: Update, context: CallbackContext) -> None:
    """إرسال رسالة ترحيبية عند بدء المحادثة مع البوت"""
    update.message.reply_text('مرحباً! أنا بوت التداول الآلي الخاص بك.')
    logging.info("تم بدء المحادثة مع المستخدم")

def main():
    """تشغيل البوت وتحديد الأوامر"""
    updater = Updater("TOKEN")  # ضع هنا رمز التوكن الخاص ببوت التليجرام
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
