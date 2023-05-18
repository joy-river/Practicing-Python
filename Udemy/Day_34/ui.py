THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class quiz_ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.label_score = Label()
        self.label_score.config(padx=20, pady=20, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="placeholder", font=("Ariel", 20, "italic"))
        self.canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)
        self.image_true = PhotoImage(file="images/true.png")
        self.image_false = PhotoImage(file="images/false.png")
        self.true_button = Button()
        self.true_button.config(width= 100, height=97, bg=THEME_COLOR, highlightthickness=0, image=self.image_true, command=self.true_pressed)
        self.true_button.grid(padx=20, pady=20, row=2, column=0)
        self.false_button = Button()
        self.false_button.config(width=100, height=97, bg=THEME_COLOR, highlightthickness=0, image=self.image_false, command=self.false_pressed)
        self.false_button.grid(padx=20, pady=20, row=2, column=1)


        self.change_question()

        self.window.mainloop()

    def true_pressed(self):
        self.quiz_brain.check_answer("True")
        self.change_question()


    def false_pressed(self):
        self.quiz_brain.check_answer("False")
        self.change_question()

    def change_question(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz_brain.next_question())
        else:
            self.window.destroy()


