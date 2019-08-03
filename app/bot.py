import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

from complex_generators import *
from config import BOT_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    # Send the message with menu
    update.message.reply_text("*Welcome to Text Fomatting Bot!*\n\n"
                              "Currently I only work via inline query, "
                              "on any conversation summon me using @txtfrmtbot"
                              ", type your message and choose the style you"
                              " want.\n\n"
                              "My code can be found [here]"
                              "(https://github.com/eitchtee/TextStylesBot).\n"
                              "Report any issue or suggestions [here]"
                              "(https://github.com/eitchtee/TextStylesBot/issues).\n\n"
                              "🤖 Hope you like me!",
                              parse_mode='Markdown',
                              disable_web_page_preview=True)


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Zalgo",
            description="Z̙͑͘a̵̺̳̫̅́́͋l̝̠͑̃͘͢ǵ̨͎̰͈͂͆̑ơ̳͚̳͒ W̹͛͝a̛͙̫̤͌ṋ͖̙̇ͧ̊͜"
                        "t͙ͮ̀̈́ͣ͞ͅsͭ̐ͥ͢͜ Ÿ̶͈́ͣ͋o̡͖̜͓͆̿ų̜͍͎͛͌̏ͨ",
            input_message_content=InputTextMessageContent(
                message_text=zalgo_txt(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Up and Down",
            description="bRoKeN cApSlOcK",
            input_message_content=InputTextMessageContent(
                message_text=upper_and_lower(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Binary",
            description="0s and 1s",
            input_message_content=InputTextMessageContent(
                message_text=' '.join(format(ord(x), 'b') for x in query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Double Struck",
            description="𝔽𝕒𝕟𝕔𝕪",
            input_message_content=InputTextMessageContent(
                message_text=double_struck(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Cursive",
            description="𝓐𝓵𝓼𝓸 𝓯𝓪𝓷𝓬𝔂",
            input_message_content=InputTextMessageContent(
                message_text=cursive(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Spaced",
            description="S P A C E D",
            input_message_content=InputTextMessageContent(
                message_text=' '.join([char.upper() for char in
                                       ' '.join(query.split(sep=None))]))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Circled",
            description="Ⓒⓘⓡⓒⓛⓔⓢ",
            input_message_content=InputTextMessageContent(
                message_text=circled(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Filled Circled",
            description="🅒🅘🅡🅒🅛🅔🅢 🅑🅤🅣 🅕🅘🅛🅛🅔🅓",
            input_message_content=InputTextMessageContent(
                message_text=negative_circled(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Parenthesis",
            description="🄟⒜⒭⒠⒩⒯⒣⒠⒮⒤⒮",
            input_message_content=InputTextMessageContent(
                message_text=parenthesis(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Gothic",
            description="𝔊𝔬𝔱𝔥𝔦𝔠",
            input_message_content=InputTextMessageContent(
                message_text=fraktur(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Leet Speak",
            description="1337, y0!",
            input_message_content=InputTextMessageContent(
                message_text=leet(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Full-width",
            description="ＢＩＧ！",
            input_message_content=InputTextMessageContent(
                message_text=large(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Reversed",
            description="desreveR",
            input_message_content=InputTextMessageContent(
                message_text=query[::-1])),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            description="*text*",
            input_message_content=InputTextMessageContent(
                message_text="*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            description="_text_",
            input_message_content=InputTextMessageContent(
                message_text="_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Monospace",
            description="```text```",
            input_message_content=InputTextMessageContent(
                message_text="```{}```".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Cebolinha",
            description="Troque seu R por um L",
            input_message_content=InputTextMessageContent(
                message_text=cebolinha(query))),
    ]
    if query:
        update.inline_query.answer(results)


def error(bot, update, erro):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, erro)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
