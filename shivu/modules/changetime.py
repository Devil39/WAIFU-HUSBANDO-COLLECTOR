from pymongo import  ReturnDocument
from pyrogram.enums import ChatMemberStatus, ChatType
from shivu import user_totals_collection, shivuu
from pyrogram import Client, filters
from pyrogram.types import Message
from shivu import application, sudo_users, collection, db, CHARA_CHANNEL_ID, SUPPORT_CHAT

ADMINS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
SUDO = [5137934602 , 5005777092 ]

@shivuu.on_message(filters.command("changetime"))
async def change_time(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await client.get_chat_member(chat_id, user_id)

    if member.status not in ADMINS:
        await message.reply_text('You are not an Admin.')
        return

    if user_id not in SUDO:
        try:
            args = message.command
            if len(args) != 2:
                await message.reply_text('Please use: /changetime NUMBER')
                return

            new_frequency = int(args[1])
            if not (100 <= new_frequency <= 10000):
                await message.reply_text('The message frequency must be between 100 and 10,000.')
                return

            chat_frequency = await user_totals_collection.find_one_and_update(
                {'chat_id': str(chat_id)},
                {'$set': {'message_frequency': new_frequency}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )

            await message.reply_text(f'Successfully changed {new_frequency}')
        except Exception as e:
            await message.reply_text(f'Failed to change {str(e)}')
    else:
        try:
            args = message.command
            if len(args) != 2:
                await message.reply_text('Please use: /changetime NUMBER')
                return

            new_frequency = int(args[1])

            chat_frequency = await user_totals_collection.find_one_and_update(
                {'chat_id': str(chat_id)},
                {'$set': {'message_frequency': new_frequency}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )

            await message.reply_text(f'Successfully changed {new_frequency}')
        except Exception as e:
            await message.reply_text(f'Failed to change {str(e)}')
