#Credit Bye Geez|Ram
#Thanks To All Dev


from Kazu import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Mz Userbot Telah Aktif")


@app.on_message(filters.command("help") & filters.private)
async def start(client, message):
   await message.reply_text("ini help")
