import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

import Constants

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

PLATFORM, SUPPORT, SOLVED, HARDWARE = range(4)

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about topic."""
    reply_keyboard = [['No Internet', 'Hardware Problem', 'Communication Platform Problem', 'I want to take a Quiz!']]

    update.message.reply_text(
        'Hi! My name is HomeOfficeBot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'What topic would you like to know more about?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return PLATFORM


def platform(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Problem of %s: %s", user.first_name, update.message.text)

    if update.message.text.lower() == 'hardware problem':
        reply_keyboard = [['USB not connecting', 'Overheating', 'WIFI not connecting', 'Back']]
        update.message.reply_text(
            'Alright, what kind of hardware problem do you have?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return HARDWARE
    else:
        reply_keyboard = [['Slack', 'Google Meet', 'Microsoft Teams', 'Discord', 'Back']]
        update.message.reply_text(
            'I see! Please tell me which platform you are using, '
            'so I know what support website to send you.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )

    return SUPPORT


def support(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info("Platform of %s: %s", user.first_name, update.message.text)
    if update.message.text == 'Slack':
        update.message.reply_text(
            'Please visit the link to find support',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Slack Support',
                                      url='https://slack.com/intl/de-de/help/articles/205138367-Behebung-von-Verbindungsfehlern#hu228ufige-probleme')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    elif update.message.text == 'Google Meet':
        update.message.reply_text(
            'Please visit the link to find support',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Google Support',
                                      url='https://support.google.com/meet/answer/7380413?hl=de')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    elif update.message.text == 'Microsoft Teams':
        update.message.reply_text(
            'Please visit the link to find support',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Microsoft Support',
                                      url='https://docs.microsoft.com/en-us/microsoftteams/troubleshoot/teams-welcome')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    elif update.message.text == 'Discord':
        update.message.reply_text(
            'Please visit the link to find support',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Discord Support',
                                      url='https://support.discord.com/hc/de/categories/115000168371-F-A-Q-Problembehebung')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    else:
        return start(update, context)


    return SOLVED


def solved(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Solved: %s", update.message.text)

    if update.message.text == 'Yes':
        update.message.reply_text('Thank you! I hope we can talk again some day. If you have more question type /start')
    else:
        update.message.reply_text(
            'I am sorry! Please contact: \n\n'
            'Companies IT Support\n'
            'support@email.at\n'
            '0660/123456')

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def hardware(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Hardware of %s: %s", user.first_name, update.message.text)
    if update.message.text == 'USB not connecting':
        update.message.reply_text(
            'Pick the closest question: ',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='USB not connecting',
                                      url='https://support.microsoft.com/en-us/topic/usb-port-may-stop-working-after-you-remove-or-insert-a-usb-device-1eaf82a6-04b1-2604-f096-2345d9c215ef')],
                [InlineKeyboardButton(text='USB not connecting',
                                      url='https://support.microsoft.com/en-us/topic/usb-port-may-stop-working-after-you-remove-or-insert-a-usb-device-1eaf82a6-04b1-2604-f096-2345d9c215ef')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    elif update.message.text == 'Overheating':
        update.message.reply_text(
            'Here is a link that can help you: ',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Overheating',
                                      url='https://www.makeuseof.com/tag/fix-overheating-laptop/')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    elif update.message.text == 'WIFI not connecting':
        update.message.reply_text(
            'Here is a link that can help you: ',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='WIFI not connecting',
                                      url='https://softwarekeep.com/help-center/wifi-keeps-disconnecting-on-windows')]
            ]))
        reply_keyboard = [['Yes', 'No']]
        update.message.reply_text(
            'Did you find a solution?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    else:
        return start(update, platform)

    return SOLVED

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(Constants.API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PLATFORM: [MessageHandler(Filters.regex('^(No Internet|Hardware Problem|Communication Platform Problem)$'),
                                      platform)],
            SUPPORT: [MessageHandler(Filters.regex('^(Slack|Google Meet|Microsoft Teams|Discord|Back)$'), support)],
            HARDWARE: [MessageHandler(Filters.regex('^(USB not connecting|Overheating|WIFI not connecting|Back)$'), hardware)],
            SOLVED: [MessageHandler(Filters.regex('^(Yes|No)$'), solved)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
