import html


class Trivia:

    def __init__(self, trivia_list):
        self.trivia_number = 0
        self.score = 0
        self.trivia_list = trivia_list
        self.current_quiz = None

    def next_quiz(self):
        self.current_quiz = self.trivia_list[self.trivia_number]
        self.trivia_number += 1
        trivia_question = html.unescape(self.current_quiz.question)
        current_question = f"{self.trivia_number}. {trivia_question}\nSelect True🙂 or False🙃: "
        return current_question

    def check_answer(self, user_choice):
        correct_answer = self.current_quiz.answer
        if user_choice == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def trivia_finished(self):
        if self.trivia_number < len(self.trivia_list):
            return False
        else:
            return True


class Quiz:

    def __init__(self, trivia_question, trivia_answer):
        self.question = trivia_question
        self.answer = trivia_answer
