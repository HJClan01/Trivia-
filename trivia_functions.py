import requests 
import os 
import json 
from trivia_objects import Question
import html

def init(): 
  url = "https://opentdb.com/api.php?amount=10&category=28"
 # get data from net
  resp = requests.get(url)
  trivia_data = resp.json()
 # build fodler from filepth that we wll store data in 
  base_folder = os.path.dirname(__file__) 
  filename = os.path.join(base_folder, 'trivia_data', 'new_trivia_.json')
  # write data to file in json format 
  with open(filename, 'w', encoding = 'utf-8') as file: 
    json.dump(trivia_data, file, ensure_ascii = True, indent=4)



def load_trivia(): 
  base_folder = os.path.dirname(__file__) 
  filename = os.path.join(base_folder, 'trivia_data', 'new_trivia_.json')
  #context manager: with open ensures the file closes automatically when done
  with open(filename, 'r') as file: 
    quiz_data = json.load(file)

  
  question_object = []
  questions = quiz_data['results']


  for q in questions:
    question_object.append(parse_question(q))

  return question_object


def parse_question(question: dict):
  category = question['category']
  difficulty = question['difficulty']
  a_question = clean_question(question['question']) 
  answer =  question['correct_answer']
  incorrect_answers = question['incorrect_answers']

  return Question(category, difficulty, a_question, answer, incorrect_answers)


def clean_question(question: str):
  return html.unescape(question)