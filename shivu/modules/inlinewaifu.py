import re
import time
from html import escape
from cachetools import TTLCache
from pymongo import MongoClient, ASCENDING

from telegram import Update, InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler, CallbackContext, CommandHandler 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from shivu import user_collection, collection, application, db


# collection
db.characters.create_index([('id', ASCENDING)])
db.characters.create_index([('anime', ASCENDING)])
db.characters.create_index([('img_url', ASCENDING)])

# user_collection
db.user_collection.create_index([('characters.id', ASCENDING)])
db.user_collection.create_index([('characters.name', ASCENDING)])
db.user_collection.create_index([('characters.img_url', ASCENDING)])




async def watch_waifus(update: Update, context: CallbackContext) -> None:
    query = update.message.text

    if context.bot.username in query:
        search_terms = query.split(context.bot.username)[1].strip().split()

        if search_terms:
            regex = re.compile(' '.join(search_terms), re.IGNORECASE)
            all_characters = list(await collection.find({"$or": [{"name": regex}, {"anime": regex}]}).to_list(length=None)

            results = []
            for waifu in all_characters :
                global_count = await user_collection.count_documents({'characters.id': waifu['id']})

                caption = f"<b>Look At This Waifu !!</b>\n\n🌸:<b> {waifu['name']}</b>\n🏖️: <b>{waifu['anime']}</b>\n<b>{waifu['rarity']}</b>\n🆔️: <b>{waifu['id']}</b>\n\n<b>Globally Guessed {global_count} Times...</b>"
                results.append(
                    InlineQueryResultPhoto(
                        thumbnail_url=waifu['img_url'],
                        id=f"{waifu['id']}_{time.time()}",
                        photo_url=waifu['img_url'],
                        caption=caption,
                        parse_mode='HTML'
                    )
                )

            if results:
                await context.bot.send_message(update.effective_chat.id, 'Here are the waifus matching your search:')
                await context.bot.send_photos(update.effective_chat.id, [waifu['img_url'] for waifu in results])
            else:
                await context.bot.send_message(update.effective_chat.id, 'No waifus found matching your search.')
        else:
            await context.bot.send_message(update.effective_chat.id, 'Please provide an anime name or waifu name to search.')
    else:
        await context.bot.send_message(update.effective_chat.id, 'Please mention the bot username in your query.')
