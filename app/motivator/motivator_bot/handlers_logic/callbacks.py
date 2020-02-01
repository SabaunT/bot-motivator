from telegram import Update
from telegram.ext import CallbackContext

from app.motivator.motivator_bot.handlers_logic.presenters import (
    StartPresenter, ShowHabitsPresenter, ChoiceConfirmPresenter, CancellationPresenter
)
from app.motivator.motivator_bot.handlers_logic.update_data_handlers import (
    StartUpdateDataHandler, ShowHabitsUpdateHandler, ChoiceConfirmUpdateHandler
)


# todo имплицитное определение context.user_data между хэндлероом и презентером
def start(update: Update, context: CallbackContext) -> int:
    """
    Greets user and asks whether he is ready to add habits, if user
    has adding ability.
    """
    StartUpdateDataHandler(update, context).handle_data()

    start_presenter = StartPresenter(update, context)
    start_presenter.present_response()
    return start_presenter.next_state


def react_start_choice(update: Update, context: CallbackContext) -> int:
    """
    Called after start. Process user choice, which was done in start handler.
    """
    ShowHabitsUpdateHandler(update, context).handle_data()

    show_habits_presenter = ShowHabitsPresenter(update, context)
    show_habits_presenter.present_response()
    return show_habits_presenter.next_state


def react_habit_choice(update: Update, context: CallbackContext) -> int:
    """
    Saves user habit choice and finishes conversation
    """
    ChoiceConfirmUpdateHandler(update, context).handle_data()

    confirm_presenter = ChoiceConfirmPresenter(update)
    confirm_presenter.present_response()
    return confirm_presenter.next_state


def cancel(update: Update, context: CallbackContext) -> int:
    cancellation_presenter = CancellationPresenter(update)
    cancellation_presenter.present_response()
    return cancellation_presenter.next_state