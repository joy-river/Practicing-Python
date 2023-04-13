from data import question_data
from question_model import Question
from quiz_brain import quiz_brain

Question_bank = []

for i in question_data[0]["results"]:
    Question_bank.append(Question(i["question"], i["correct_answer"]))

Quiz = quiz_brain(Question_bank)

while Quiz.question_remain():
    answer = Quiz.next_question()

print(f"You completed the quiz!")
print(f"Your final score is {Quiz.score} / {Quiz.question_num}!")
