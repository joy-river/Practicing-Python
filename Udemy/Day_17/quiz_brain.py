class quiz_brain:
    def __init__(self, questions_list):
        self.question_num = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_num + 1}: {self.questions_list[self.question_num].text} (True / False)?: ")
        self.check_answer(user_answer, self.questions_list[self.question_num].answer)
        self.question_num += 1


    def question_remain(self):
        return self.question_num < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score} / {self.question_num + 1}\n")