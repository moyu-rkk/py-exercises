from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.turn} \n")


#当需要引用一个object的attribute的时候语法是object.attribute
#脑子抽了用了dict的语法dict["key"]喜提报错object is not subscriptable

#创建题库的时候loop dict的每一项，所以赋值的时候，读取的是对应项的text和answer，而不是源数据的dict名字整个放进去（question_data["text"]，会报错
