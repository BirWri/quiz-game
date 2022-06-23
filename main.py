from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    new_g = Question(item["text"], item["answer"])
    question_bank.append(new_g)

print(question_bank[0].answer)


