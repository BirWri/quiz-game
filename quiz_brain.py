class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        nr_of_questions = len(self.question_list)
        return self.question_number < nr_of_questions

    def new_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"You current score is {self.score}/{self.question_number}")
        print(f"The correct answer was {correct_answer}")
        print("\n")
        print("\n")
