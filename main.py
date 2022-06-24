from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_g = Question(item["text"], item["answer"])
    question_bank.append(new_g)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():

    quiz.new_question()



