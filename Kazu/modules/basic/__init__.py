import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Kazu"])

async def join(client):
    try:
        await client.join_chat("kazusupportgrp")
        await client.join_chat("Html12text")
        await client.join_chat("StoryMan01")
        await client.join_chat("kynansupport")
    except BaseException:
        pass
