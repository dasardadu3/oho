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

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo Bandoeng Gabut! Kumaha damang? 🤔.\n\n🇮🇩 Kumaha carana make bot ? ↓.\n\nRead / Baca → [Panduan menggunakan bot](https://t.me/joinchat/yKtu9r4qkas2ZDM1) ←.\n\n👤 Own [irfan](https://t.me/developerantibucin) 🇮🇩""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Panduan menggunakan bot", url="https://t.me/joinchat/yKtu9r4qkas2ZDM1")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/dvgrup"
                    ),
                    InlineKeyboardButton(
                        "Channel Kita", url="https://t.me/bandunglawak"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar musik sedang online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/dvgrup"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/developerantibucin"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar musik sedang online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/dvgrup"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/developerantibucin"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Panduan menggunakan bot", url="https://t.me/joinchat/yKtu9r4qkas2ZDM1"
                    )
                ]
            ]
        ),
    )
