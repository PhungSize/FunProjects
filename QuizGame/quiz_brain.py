# class Quiz_Brain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#         self.score = 0
    
#     def stillHasQuestions(self):
#         return self.question_number == len(self.question_list)
    
#     def nextQuestion(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"\nQ{self.question_number}: {current_question.text}? (True/False): ")
#         correct_answer = current_question.answer
#         self.checkAnswer(user_answer, correct_answer)
    
#     def checkAnswer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("Nope! You guessed wrong.")
#         print(f"Your current score is {self.score}/{self.question_number}")
    
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ{self.question_number}: {current_question.text}? (True/False) ")
        correct_answer = current_question.answer
        self.checkAnswer(answer, correct_answer)
    
    def checkAnswer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print(f"You guessed right!")
        else:
            print(f"You guessed wrong! Maybe next time")
        print(f"Your current score is {self.score}/{self.question_number}")
    
    def stillHasQuestions(self):
        return self.question_number == len(self.question_list)