import random
import typing 

class Trivia:
  def __init__(self, questions: list):
      self.questions = questions
      self.total_asked = 0
      self.total_correct = 0
    

  
  def ask_question(self):
     # ltr_dict = {

     #   0: 'b',
     #   1: 'c', 
     #   2: 'd',
     # }
     # new_question = random.choice(self.questions)
     # print(new_question)
     # print(f'a. {new_question.answer} ')
     # for i, incorrect in enumerate(new_question.incorrect_answers): 
     #   print(f'{ltr_dict.get(i)}. {incorrect} ')
     displayed_question = {}
     letters = 'abcd'
     new_question = random.choice(self.questions)
     print(new_question)
     # adding new_question.incorrect answer to list of new_question.answer
     answers = [new_question.answer] + new_question.incorrect_answers 

     random.shuffle(answers) 

     for i, answer in enumerate(answers): 
       print(f'{letters[i]}. {answer} ')
       displayed_question[letters[i]] = answer    
     return new_question, displayed_question

       
class Question: 
  #build constructor methothed, making instance of class
  def __init__(self, category: str, difficulty: str, question: str, answer: str, incorrect_answers: list):
    # instance attr
    self.category = category 
    self.difficulty = difficulty 
    self.question = question
    self.answer = answer 
    self.incorrect_answers = incorrect_answers


    # repr method - what python uses to display the object when its name is refrenced 
  def __repr__(self):
    return f'{self.question}\n'
    

  
