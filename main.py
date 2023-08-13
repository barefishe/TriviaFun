from trivia import Quiz, Trivia
from data import get_trviadb
from intro import IntroInterface
from ui import TriviaInterface
import ttkbootstrap as ttk

intro_ui = None
quiz_ui = None
mwindow = ttk.window.Window(title="Trivia Fun!")

def user_submit(difficulty, quiz_number):
    """
    called when user click submit on the intro interface
    get the quiz question based on user's difficulty and quiz number choices
    destroy intro interface and create the quiz interface
    :param difficulty: difficulty level for trivia quiz
    :param quiz_number: number of questions
    :return: None
    """
    global intro_ui
    global quiz_ui
    global mwindow

    intro_ui.destroy_intro()
    quiz_bank = []
    trivia_db = get_trviadb(difficulty, quiz_number)
    for quiz in trivia_db:
        quiz_question = quiz["question"]
        quiz_answer = quiz["correct_answer"]
        new_quiz = Quiz(quiz_question, quiz_answer)
        quiz_bank.append(new_quiz)

    quiz = Trivia(quiz_bank)
    quiz_ui = TriviaInterface(mwindow, quiz, user_replay)


def user_replay():
    global intro_ui
    global quiz_ui
    global mwindow

    quiz_ui.destroy_ui()
    intro_ui = IntroInterface(mwindow, user_submit)


mwindow.config(padx=15, pady=15)
intro_ui = IntroInterface(mwindow, user_submit)
mwindow.mainloop()
