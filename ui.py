from tkinter import *
from quiz import QuizGenerator

# colors
RED = "#ee9595"
BROWN = "#eaac7f"
BEIGE = "#ffcda3"
GREEN = "#96bb7c"
PINK = "#eaac7f"


class App:

    def __init__(self, window, data):
        self.score = 0
        self.question_number = 0
        self.quiz_data = data
        self.window = window
        window.title("QuizMe")
        window.config(padx=20, pady=20, bg=BEIGE)
        self.canvas = Canvas(width=400, height=300,
                             highlightthickness=0, bg=BROWN)
        self.question_text = self.canvas.create_text(
            200, 150, text="QUESTION", fill="white", justify="center", width=300, font=("Courier", 20, "normal"))
        self.canvas.grid(column=0, row=2, columnspan=3)

        self.score_text = Label(text=f"SCORE: {self.score}", font=(
            "Courier", 30, "normal"), fg="#91684a", bg=BEIGE)
        self.score_text.grid(column=1, row=1)
        # buttons
        title_img = PhotoImage(file="title.png")
        self.title = Label(image=title_img, highlightthickness=0)
        self.title.grid(row=0, column=0, columnspan=3, pady=(10, 10))
        tru_img = PhotoImage(file="check_symbol.png")
        self.true_button = Button(
            image=tru_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(column=0, row=3, pady=(10, 10))
        false_img = PhotoImage(file="x_symbol.png")
        self.wrong_button = Button(
            image=false_img, highlightthickness=0, command=self.false_click)
        self.wrong_button.grid(column=2, row=3, pady=(10, 10))
        self.new_question()
        window.mainloop()

    def game_on(self):
        if self.question_number < len(self.quiz_data):
            return True
        else:
            self.canvas.itemconfig(self.question_text, text=f"GAME OVER!")
            self.score_text.config(text=f"SCORE: {self.score}/10")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            return False

    def check_answer(self, response):
        self.response = response
        if self.response == self.answer:
            self.canvas.config(bg=GREEN)
            self.score += 1
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.new_question)

    def new_question(self):
        self.canvas.config(bg=BROWN)
        if self.game_on():
            self.current_question = self.quiz_data[self.question_number]
            self.score_text.config(text=f"SCORE: {self.score}")
            self.question = self.current_question[0]
            self.answer = self.current_question[1]
            self.canvas.itemconfig(self.question_text, text=self.question)
            self.question_number += 1

    def false_click(self):
        response = "False"
        self.check_answer(response)

    def true_click(self):
        response = "True"
        self.check_answer(response)
