class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) \n")
        correct_answer = current_question.answer
        self.check_answer(answer, correct_answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
        print(correct_answer)



