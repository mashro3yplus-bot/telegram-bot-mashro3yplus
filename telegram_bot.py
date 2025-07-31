from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً بك في Mashro3y+")

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠️ *خدماتنا:*
" 
        "1. مشاريع تخرج (AI – برمجة – تصميم)
" 
        "2. كتابة وتنسيق التوثيق
" 
        "3. واجهات UI/UX
" 
        "4. حل واجبات وتقارير
" 
        "\n📩 اطلب الخدمة من هنا:
" 
        "https://forms.gle/kyXNfqNfcAbbBgwT8"
    )

app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("services", services))
app.run_polling()

