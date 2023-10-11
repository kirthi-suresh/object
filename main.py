from model import Question
from data import question_data
from brain import QuizBrain

question_bank = []

for questions in question_data:
    q = questions['text']
    a = questions['answer']
    question = Question(q, a)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your score is {quiz.score}")