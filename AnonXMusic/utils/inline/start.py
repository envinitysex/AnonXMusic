from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/envynitysex"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/berlinmusic_support"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/Dukeassit"),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/Berlinmusic_support"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/envynitysex"),
        ],
    ]
    return buttons
