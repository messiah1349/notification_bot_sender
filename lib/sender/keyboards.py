from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_deed_after_notify(deed_id: int) -> InlineKeyboardMarkup:

    button_timer = InlineKeyboardButton('🔔', callback_data=f"notify_timer_deed_id={deed_id}")
    button_done = InlineKeyboardButton('✅', callback_data=f"notify_done_deed_id={deed_id}")

    reply_markup = InlineKeyboardMarkup([[button_timer, button_done]])
    return reply_markup