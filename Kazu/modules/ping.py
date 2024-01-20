# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from config import BOT_VER, BRANCH as brch
from Kazu import CMD_HELP, StartTime
from Kazu.helpers.basic import edit_or_reply
from Kazu.helpers.constants import WWW
from Kazu.helpers.PyroHelpers import SpeedConvert
from Kazu.utils.tools import get_readable_time
from Kazu.helpers.adminHelpers import DEVS

from .help import add_command_help

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )



@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **𝙼𝚉 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✨**\n"
        f"├• **Pɪɴɢᴇʀ** - `%sms`\n"
        f"├• **Uᴘᴛɪᴍᴇ -** `{uptime}` \n"
        f"└• **User :** {client.me.mention}" % (duration)
    )


@Client.on_message(
    filters.command("cek", [".", ""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, 
     f"█▀█ █▀█ █▄░█ █▀▀ █ \n"
     f"█▀▀ █▄█ █░▀█ █▄█ ▄"
   )
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
           f"➠**Ping !! -** `%sms`\n"
           f"➠**Uptime -** `{uptime}` \n"
           f"➠**User -**  {client.me.mention}" " % (duration)
           )


