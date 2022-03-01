from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
i = 0
for question in question_data:
    newQuestion = Question(question['text'], question['answer'])
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)
while quiz.stillHasQuestions() == False:
    quiz.nextQuestion()