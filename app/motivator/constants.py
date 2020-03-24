from typing import List

from app.motivator.users.habits.habits_data_provider import habits_config_data_provider

# habit related constants
APP_HABITS: List[str] = habits_config_data_provider.get_habits_names()
MAX_HABITS = habits_config_data_provider.get_habits_amount()


# bot related constants
REACT_START_CHOICE, REACT_HABIT_CHOICE = range(2)

NEW_USER_GREETING = 'Привет, новичок! Я мотивирую людей бросить что-то или начать. Начнем?'

KNOWN_USER_GREETING = 'Рад видеть снова! Хочешь добавить привычку?'

CANT_START_GREETING = 'Простите, у Вас полный список привычек в ходу. Вы должны удалить хотя бы одну привычку или ' \
                      'дождаться завершения '

YES = 'Да'

NO = 'Нет'

READY_TO_START_ANSWERS = [YES, NO]

CHOOSE_HABITS = "Отлично! Выбирай привычку."

HABITS_CHOICE_ANSWERS = APP_HABITS

CONFIRM_CHOICE = "Принял. Удачи в этом деле!"

SAY_GOODBYE = "Рад был видеть :)"

REACT_DELETE_CHOICE, REACT_SHOW_CHOICE = range(2)

READY_TO_DELETE_ANSWERS = [YES, NO]

CANT_DELETE = "Нет привычек для удаления. Да и не рекомендую делать этого 😤" # it's emoji here!!!

DELETE_GREETING = "Че, уже сдаешься?"

DONT_DELETE = "Надежда на то, что ты станешь человеком, еще есть!"

CHOOSE_HABITS_TO_DELETE = "Мда. Ну и от чего ты хочешь отказаться?"

CONFIRM_DELETE_CHOICE = "Короче, я удалил, но я думаю, что в следующий раз ты продержишься дольше!"

HELP = """
Работать с ботом достаточно просто. Помимо /help есть несколько управляющих команд.

/start - позволяет зарегистрировать привычки, если их количество не превышает допустимый максимум.
/delete - позволяет удалять имеющиеся у вас.
/cancel - может быть вызван в любой момент взаимодейстия с ботом после вызова двух прошлых команд в целях отмены диалога.

В случае технических проблем пишите @SabaunT. Есть предложения по улучшениям или другим привычкам? Пишите @@Mikhail_Zamarin.

Проще говоря, регистрируйте привычки через /start, удаляйте через /delete. Настоятельно рекомендую удалять привычку, если вы сорвались.
"""
