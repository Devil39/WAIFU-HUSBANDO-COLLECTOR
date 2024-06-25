from pymongo import  ReturnDocument
from pyrogram.enums import ChatMemberStatus, ChatType
from shivu import user_totals_collection, shivuu
from pyrogram import Client, filters
from pyrogram.types import Message
from shivu import  sudo_users
ADMINS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
GOD = [sudo_users]

@shivuu.on_message(filters.command("changetime"))
async def change_time(client: Client, message: Message):
    
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await shivuu.get_chat_member(chat_id,user_id)
        

    if member.status not in ADMINS :
        await message.reply_text('You are not an Admin.')
        return

    try:
        args = message.command
        if len(args) != 2:
            await message.reply_text('Please use: /changetime NUMBER')
            return

        new_frequency = int(args[1])
        if new_frequency < 100:
            await message.reply_text('The message frequency must be greater than or equal to 100.')
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

#sudo

@shivuu.on_message(filters.command("changetime"))
async def change_time(client: Client, message: Message):
    
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await shivuu.get_chat_member(chat_id,user_id)
        

    if member.status  in GOD :
        await message.reply_text('You are a GOD.')
        return

    try:
        args = message.command
        if len(args) != 2:
            await message.reply_text('Please use: /changetime NUMBER')
            return

        new_frequency = int(args[1])
        if new_frequency < 1:
            await message.reply_text('The message frequency must be greater than or equal to 100.')
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



async def upload(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id)  in sudo_users:
        await update.message.reply_text('Ask My Owner...')
        return

    try:
        args = message.command
        if len(args) != 2:
            await message.reply_text('Please use: /changetime NUMBER')
            return

        new_frequency = int(args[1])
        if new_frequency < 1:
            await message.reply_text('The message frequency must be greater than or equal to 100.')
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

