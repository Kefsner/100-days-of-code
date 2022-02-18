from Day17_quiz_question_model import Question
from Day17_quiz_data import question_data
from Day17_quiz_quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
quiz_brain.result()