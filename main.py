from question_model import Questionary
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questionary(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

end_quiz = True

while end_quiz:
    quiz.next_question()
    end_quiz = quiz.still_has_question()