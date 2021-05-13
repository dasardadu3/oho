# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkeun hela urang jadi admin atuh</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "BandungGaboetVCG"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Urang gabung didieu kusabab pamenta sia")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Helper engges aya siateh</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n Assistant Bot {user.first_name} teu bisa milu nimbrung ka grup anjeun kumargi loba pamenta nimbrung kanggo userbot! Pastikeun pengguna teu dibanned ti grup ya NGENTOT!."
            "\n\nAtau tambahkan secara manual Assistant Bot ke Grup Anda dan coba lagi</b>",
        )
        return
    await message.reply_text(
            "<b>Helper userbot bergabung dengan obrolan sia</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Pengguna teu bisa meninggalkan grup sia! Meren ngadagoan dibayar."
            "\n\nAtau keluarkan urang secara manual ti grup maraneh</b>",
        )
        return
