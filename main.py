import requests 
from tkinter import *
from quiz import QuizGenerator
import html 
from ui import App


window = Tk()
data = QuizGenerator().get_data()
quiz = App(window, data)
while quiz.game_on():
    quiz.new_question()





