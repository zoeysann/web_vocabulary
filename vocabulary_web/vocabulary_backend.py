import random
import time
import csv

class Vocabulary:
    def __init__(self):
        self.vocabulary={}
        self.tcount=0

    def import_words(self):
        self.vocabulary={}
        with open("vocabulary_notes.csv", encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                key=row[0] #keys = en words
                value=row[1] #value = az words
                self.vocabulary[key]=value
        return self.vocabulary

    def generate_quiz(self):
        # WILL SHUFFLE A LIST AND PICK THE QUESTION.
        questions=['question_en', 'question_az']
        quiz=random.choice(questions)
        if quiz=='question_en':
            random.shuffle(list(self.vocabulary.keys()))
            random_word=random.choice(list(self.vocabulary.keys()))
            answer_true=self.vocabulary[random_word]
            answers=list(self.vocabulary.values())
            answers.remove(answer_true)
            random.shuffle(answers)
        else:
            random.shuffle(list(self.vocabulary.values()))
            random_word=random.choice(list(self.vocabulary.values()))
            answer_true=self.vocabulary[random_word]
            answers=list(self.vocabulary.keys())
            answers.remove(answer_true)
            random.shuffle(answers)
            pass

        return quiz
        
    def check_answer(self, your_answer):
        # your_answer=int(input("Your answer: "))
        if your_answer==self.answer_true:
            self.tcount=+1
            


            # UPLOAD TO GITHUB!!!
            