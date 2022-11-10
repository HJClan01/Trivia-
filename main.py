from termcolor import colored
import trivia_functions
from trivia_objects import Question, Trivia 
def main(): 
  #get_trivia
  trivia_functions.load_trivia()
  # load trivia 
  new_questions = trivia_functions.load_trivia()
  
  # new_trivia = trivia_functions.init()

  # instance of obj  
  # for question in new_question: 
  #   print()
  #   print(question.question)
  # my_question = Question('Life', 'Easy', 'What is the meaning of life', '42', ['money', 'fame', "rudra"])
  # print(my_question)
  # play trivia
  print(' ' * 10  + '*' * 50)
  print(colored(' ' * 20 + "       Welcome to Trvia     ", 'blue') )
  print(' ' * 10 + '*' * 50)
  # print(new_trivia
  
  # create new trivia game # compodotion relationship between trivia and question
  new_trivia = Trivia(new_questions)

  questions_to_ask = 5
  correct_answers = 0
  while questions_to_ask > 0: 
    new_question, display_question = new_trivia.ask_question()
    user_resp = input('\nEnter you answer: ').strip().lower()

    full_answer = display_question.get(user_resp)
    questions_to_ask -= 1
    if full_answer == new_question.answer:
      print(colored('\ncorrect\n', 'green'))
      new_trivia.total_correct += 1
      
    else: 
      print(colored("\nincorrect\n", 'red'))
    new_trivia.total_asked += 1 

  # show score 
  score = new_trivia.total_correct / new_trivia.total_asked * 100
  print(colored(f'\nSCORE: {score:.2f}%\n', 'blue'))
  

    
    

if __name__ == "__main__":
    main()