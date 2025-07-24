import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Aviyaa import LOGGER, app, userbot
from Aviyaa.core.call import Aviyaa
from Aviyaa.misc import sudo
from Aviyaa.plugins import ALL_MODULES
from Aviyaa.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Aviyaa.plugins" + all_module)
    LOGGER("Aviyaa.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Aviyaa.start()
    try:
        await Aviyaa.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Aviyaa").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Aviyaa.decorators()
    LOGGER("Aviyaa").info(
        "\x0a\x0a"
        "\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x41\x76\x69\x79\x61\x61\x20\x42\x6f\x74\x20\x68\x61\x73\x20\x62\x65\x65\x6e\x20\x44\x65\x70\x6c\x6f\x79\x65\x64\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x21\x0a"
        "\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x76\x69\x73\x69\x74\x20\x40\x41\x76\x69\x79\x61\x61\x4d\x75\x73\x69\x63\x20\x66\x6f\x72\x20\x75\x70\x64\x61\x74\x65\x73\x20\x26\x20\x73\x75\x70\x70\x6f\x72\x74\x2e\x0a"
        "\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x44\x65\x76\x65\x6c\x6f\x70\x65\x72\x3a\x20\x40\x50\x79\x4e\x6f\x78\x69\x5f\x44\x65\x76\x0a"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Aviyaa").info("Stopping Aviyaa Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
