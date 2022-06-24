class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def still_has_questions(self):
        nr_of_questions = len(self.question_list)
        return self.question_number < nr_of_questions

    def new_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text}. (True/False)?: ")
