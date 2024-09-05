import random
import mysql.connector

class Vocabulary:
    def __init__(self):
        self.vocabulary={}
        self.tcount=0 #true count
        self.fcount=0 #false count

    def import_words(self): # connect to db
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="zoey_464852",
            database="web_vocabulary"
        )
        mycursor = mydb.cursor()

        self.vocabulary={}

        mycursor.execute("SELECT * FROM idk_name")
        myresult = mycursor.fetchall()

        for x in myresult:
            key=x[0]
            value=x[1]
            self.vocabulary[key]=value
        return self.vocabulary

    
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
        while True:
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
        return f"You've made {self.tcount} truths\nYou've made {self.fcount} mistakes"

class Question(Vocabulary):
        def __init__(self):
            super().__init__()

if __name__=='__main__':
    v = Vocabulary()
    v.start_quiz()
    #v.check_answer()
    
# WELL, I DON'T KNOW.

# UPLOAD TO GITHUB!!!
