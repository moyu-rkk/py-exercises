class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.turn = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.turn < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.turn]
        self.turn += 1
        player_answer = input(f"Q.{self.turn}.{current_question.text} (True/False):")
        self.check_answer(player_answer, current_question.answer)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was:{correct_answer}.")
        print(f"Your current score is: {self.score}/{self.turn}.\n")
