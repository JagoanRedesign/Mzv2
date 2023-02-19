from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Kazu.helpers.basic import edit_or_reply
from Kazu.helpers.PyroHelpers import ReplyCheck

from .help import add_command_help


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    Kazu = await edit_or_reply(message, "`Tunggu Sebentar...`")
    await gather(
        Kazu.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command(["ayang", "ayng"], cmd) & filters.me)
async def ayang_cmd(client: Client, message: Message):
    Kazu = await edit_or_reply(message, "🔎 `Search Ayang...`")
    await gather(
        Kazu.delete(),
        client.send_photo(
            message.chat.id,
            choice(
                [
                    ayang.photo.file_id
                    async for ayang in client.search_messages(
                        "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command(["mzpp", "ppcp"], cmd) & filters.me)
async def couple_cmd(client: Client, message: Message):
    Kazu = await edit_or_reply(message, "🔎 `Search PP Couple...`")
    await gather(
        Kazu.delete(),
        client.send_photo(
            message.chat.id,
            choice(
                [
                    couple.photo.file_id
                    async for couple in client.search_messages(
                        "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command(["bokep", "bkp"], cmd) & filters.me)
async def bokep_cmd(client: Client, message: Message):
    Kazu = await edit_or_reply(message, "`Mencari bahan...`")
    await gather(
        Kazu.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "Untuk Mengirim video asupan secara random.",
        ],
        [
            f"asupan atau {cmd}ptl",
            "Untuk Mengirim video asupan secara random.",
        ],
        
         [f"ayang", "Mencari Foto ayang kamu."],
        [f"ppcp", "Mencari Foto PP Couple Random."],
        [f"bokep", "to send random porno videos."]
       
    ],
)
