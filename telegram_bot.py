from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("طلب خدمة 📩", url="https://forms.gle/kyXNfqNfcAbbBgwT8")],
        [InlineKeyboardButton("قناتنا 📢", url="https://t.me/Mashro3yPlus")],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data=\'contact_us\')],
        [InlineKeyboardButton("خدماتنا 🛠️", callback_data=\'services_menu\')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 أهلاً بك في Mashro3y+! اختر من القائمة:", reply_markup=reply_markup)

async def services_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🛠️ *خدماتنا:*\n" 
        "1. مشاريع تخرج (AI – برمجة – تصميم)\n" 
        "2. كتابة وتنسيق التوثيق\n" 
        "3. واجهات UI/UX\n" 
        "4. حل واجبات وتقارير\n" 
        "\n📩 اطلب الخدمة من هنا:\n" 
        "https://forms.gle/kyXNfqNfcAbbBgwT8",
        parse_mode=\


        "MarkdownV2"
    )

async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("يمكنك التواصل معنا عبر الرسائل المباشرة على تليجرام: @Mashro3yPlusBot (هذا مجرد مثال، يرجى استبداله بمعرف تواصل حقيقي أو رابط)")

app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(services_menu, pattern=\'services_menu\'))
app.add_handler(CallbackQueryHandler(contact_us, pattern=\'contact_us\'))

app.run_polling()
