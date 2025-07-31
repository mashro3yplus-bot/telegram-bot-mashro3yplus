from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text(
        "👋 أهلاً وسهلاً بك في بوت 💙 مشروعي بلس | Mashro3y+\n\n" 
        "📘 نحن هنا لخدمتك في:\n" 
        "✅ تنفيذ مشاريع التخرج (برمجة – تصميم – AI)\n" 
        "✅ كتابة وتنسيق التوثيق (عربي + إنجليزي)\n" 
        "✅ تصميم واجهات التطبيقات UI/UX\n" 
        "✅ حل واجبات وتقارير وبحوث\n\n" 
        "📩 لطلب الخدمة مباشرة:\n" 
        "🧠 https://forms.gle/kyXNfqNfcAbbBgwT8\n\n" 
        "📢 تابع قناتنا لأحدث العروض:\n" 
        "📌 https://t.me/Mashro3yPlus\n\n" 
        "💙 مشروعك… مهمتنا، ونجاحك؟ وعدنا!"
    )

import os

app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

