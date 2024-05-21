class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.cont = 0

    def still_has_question(self):
        number_questions = len(self.question_list)
        if self.question_number >= number_questions:
            end_quiz = False
            print("You've complete the quiz")
            print(f"You final score was {self.cont}/{self.question_number}")
        else:
            end_quiz = True
        return end_quiz

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():

            print("You got it right ")
            print(f"The correct answer was: {correct_answer}")
            self.cont += 1
            print(f"You current score is {self.cont}/{self.question_number} ")


        else:
            print("That's wrong")
            print(f"The correct answer is {correct_answer}")
            print(f"You current score is {self.cont}/{self.question_number} ")

