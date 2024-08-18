import random
import time
import csv

class Vocabulary:
    def __init__(self):
        self.vocabulary={}
        self.tcount=0 #true count
        self.fcount=0 #false count

    # this method extracts words from csv and collects in atttr vocabulary dict
    def import_words(self):
        self.vocabulary={}
        with open(r"vocabulary_notes.csv", encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                key=row[0] #keys = en words
                value=row[1] #value = az words
                self.vocabulary[key]=value
    
    #this method takes wrods from vocabulary attr. and returns random question (random selected word) with possible variants.
    def get_question(self): 
        questions=['question_en'] #, 'question_az'
        quiz=random.choice(questions)
        if quiz=='question_en':
            random.shuffle(list(self.vocabulary.keys()))
            random_word=random.choice(list(self.vocabulary.keys()))
            answer_true=self.vocabulary[random_word]
            answers=list(self.vocabulary.values())
            answers.remove(answer_true)
            random.shuffle(answers)

            variants={"A": random.choice(answers), "B": random.choice(answers), "C": answer_true, "D":random.choice(answers)}

            variants_list=[answer_true]
            for key in list(variants.keys())[:-1]:
                random.shuffle(answers)
                variants[key]=random.choice(answers)
                variants_list.append(variants[key])

            random.shuffle(variants_list)
            for key in variants.keys():
                variants[key]=variants_list.pop()

            # for key, value in variants.items():
            #     print(f'{key}: {value}')
            return (random_word, variants, answer_true)
        
        else:
            random.shuffle(list(self.vocabulary.values()))
            random_word=random.choice(list(self.vocabulary.values()))
            answer_true=self.vocabulary[random_word]
            answers=list(self.vocabulary.keys())
            answers.remove(answer_true)
            random.shuffle(answers)
            
            variants={"A": random.choice(answers), "B": random.choice(answers), "C": answer_true, "D":random.choice(answers)}

            variants_list=[answer_true]
            for key in list(variants.keys())[:-1]:
                random.shuffle(answers)
                variants[key]=random.choice(answers)
                variants_list.append(variants[key])

            random.shuffle(variants_list)
            for key in variants.keys():
                variants[key]=variants_list.pop()

            # for key, value in variants.items():
            #     print(f'{key}: {value}')

            return (random_word, variants, answer_true)
        

    def start_quiz(self):
        self.import_words()
        list = self.get_question()
        print("What is the translation of given word?: ", list[0])
        for key, value in list[1].items():
                print(f'{key}: {value}')
        user_answer=input("Your answer (A/B/C/D): ")
        print(self.check_answer(list[1][user_answer.upper()], list[2]))


    def check_answer(self, user_answer, correct_answer):
        if user_answer==correct_answer:
            self.tcount=+1
        else:
            self.fcount=+1

class Question(Vocabulary):
        super()


if __name__=='__main__':
    v = Vocabulary()
    v.start_quiz()

#question - random_word, variants, correct_answer
#class question - attribute
#objects
#class Question()

# UPLOAD TO GITHUB!!!