from pyrogram import Client, filters
from PBXMUSIC import app
from PBXMUSIC.utils.database import add_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PBXMUSIC.mongo.afkdb import LOGGERS as OWNERS
from PBXMUSIC.utils.database import add_served_chat, get_assistant

app.on_message(filters.command("rejsjajapo") & filters.group)


async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BADMUSIC/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️",
                        url=f"https://github.com/Badhacker98/PbXbot/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/PBX_2.0/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork",
                    )
                ],
            ]
        ),
    )


@app.on_message(filters.command("rejsjajapo") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BADMUSIC/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️",
                        url=f"https://github.com/Badhacker98/PbXbot/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/PBX_2.0/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork",
                    )
                ],
            ]
        ),
    )


@app.on_message(filters.command("rejsjajapo") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BADMUSIC/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️",
                        url=f"https://github.com/Badhacker98/PbXbot/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/PBX_2.0/fork",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️",
                        url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork",
                    )
                ],
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #
@app.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @BrokenRobot_Bot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002093247039:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
