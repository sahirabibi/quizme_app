from tkinter import *
import html
import requests



class QuizGenerator:
    
    def __init__(self):
        """Takes category in form of integer (17, etc)"""
        parameters = {"amount":10,"difficulty":"medium", "type":"boolean"}
        self.res = requests.get("https://opentdb.com/api.php", params=parameters)
        self.res.raise_for_status()
        self.data = self.res.json()
        self.q_data = self.data["results"]        

    def get_data(self):
        self.question_data = []
        for item in self.q_data:
            self.question = html.unescape(item["question"])
            self.answer = item["correct_answer"]
            self.question_data.append((self.question, self.answer))
        return self.question_data

    
        








            




