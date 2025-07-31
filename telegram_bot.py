from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os

# دالة البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("طلب خدمة 📩", url="https://forms.gle/kyXNfqNfcAbbBgwT8")],
        [InlineKeyboardButton("قناتنا 📢", url="https://t.me/Mashro3yPlus")],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact_us')],
        [InlineKeyboardButton("خدماتنا 🛠️", callback_data='services_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 أهلاً بك في *Mashro3y\\+*! اختر من القائمة:",
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

# دالة عرض الخدمات
async def services_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔙 الرجوع للقائمة", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🛠️ *خدماتنا*:\n"
        "1\\. مشاريع تخرج \\(AI – برمجة – تصميم\\)\n"
        "2\\. كتابة وتنسيق التوثيق\n"
        "3\\. واجهات UI/UX\n"
        "4\\. حل واجبات وتقارير\n"
        "\n📩 اطلب الخدمة من هنا:\n"
        "https://forms\\.gle/kyXNfqNfcAbbBgwT8",
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )

# دالة التواصل معنا
async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔙 الرجوع للقائمة", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "يمكنك التواصل معنا عبر الرسائل المباشرة على تليجرام:\n"
        "@Mashro3yPlusBot\n\n"
        "(هذا مجرد مثال، يرجى استبداله بمعرف تواصل حقيقي أو رابط)",
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )

# دالة الرجوع للقائمة الرئيسية
async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("طلب خدمة 📩", url="https://forms.gle/kyXNfqNfcAbbBgwT8")],
        [InlineKeyboardButton("قناتنا 📢", url="https://t.me/Mashro3yPlus")],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact_us')],
        [InlineKeyboardButton("خدماتنا 🛠️", callback_data='services_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "👋 رجعت للقائمة الرئيسية *Mashro3y\\+*: اختر من الخيارات:",
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

# إعداد التطبيق والمعالجات
app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(services_menu, pattern='services_menu'))
app.add_handler(CallbackQueryHandler(contact_us, pattern='contact_us'))
app.add_handler(CallbackQueryHandler(back_to_menu, pattern='back_to_menu'))

app.run_polling()
