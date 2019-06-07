
BULLET_POINTS = [ "a", "b", "c", "d", "e", "f" ]

def number2letter(number):
    if number > len(BULLET_POINTS):
        raise Exception("Number is too high for available bullet points")

    return BULLET_POINTS[number - 1]


def letter2number(letter):
    if letter not in BULLET_POINTS:
        return None

    letter_index = BULLET_POINTS.index(letter)
    return letter_index + 1


class Answer:
    def __init__(self, text, correct = False):
        self.text = text
        self.correct = correct


class Question:
    def __init__(self, question, possible_answers):
        self.question = question
        self.possible_answers = possible_answers

        if len(self.get_correct_answers()) == 0:
            raise Exception("Question must have at least one correct possible answer")
    
    def get_correct_answers(self):
        #return [ possible_answer.text for possible_answer in self.possible_answers if possible_answers.correct ]
        correct_answers = []

        for possible_answer in self.possible_answers:
            if possible_answer.correct:
                correct_answers.append(possible_answer.text)

        return correct_answers

    def create_prompt(self):
        prompt = self.question + "\n"

        for answer_index, possible_answer in enumerate(self.possible_answers):
            prompt += "(" + number2letter(answer_index + 1) + ") " + possible_answer.text + "\n"

        return prompt


QUESTIONS = [
    Question(
        question = "Who made this game?",
        possible_answers=[
            Answer("Jesse"),
            Answer("Josh"),
            Answer("Jelle", correct = True),
            Answer("Gabor", correct = True)
        ]
    ),
    Question(
        question = "Did he make these questions without making a mistake?",
        possible_answers=[
            Answer("YES!"),
            Answer("Nope", correct=True),
            Answer("Only god knows")
        ]
    ),
    Question(
        question="Are you ready for some serious questions?",
        possible_answers=[
            Answer("Sorry what?"),
            Answer("Na mate"),
            Answer("Yes please!", correct=True)
        ]
    ),
    Question(
        question="What is the beginning of PI?",
        possible_answers=[
            Answer("3.141592", correct=True),
            Answer("3.141692"),
            Answer("3.141990")
        ]
    ),
    Question(
        question="How would you refer to the randint function if it was imported like this? \n"
                 "'from random import randint as rnd_int'",
        possible_answers=[
            Answer("rnd_int", correct=True),
            Answer("random.rnd_int"),
            Answer("randint")
        ]
    ),
    Question(
        question="What is the highest number output by this code? \n"
                 "def print_nums(x): \n"
                 " for i in range(x): \n"
                 "  print(i) \n"
                 "  return \n"
                 "print_nums(10)",
        possible_answers=[
            Answer("0", correct=True),
            Answer("9"),
            Answer("10")
        ]
    ),
    Question(
        question="What is the output of this code? \n"
                 "list = [1, 2, 5, 3, 5, 8, 21, 82] \n"
                 "print(list[list[4]])",
        possible_answers=[
            Answer("3"),
            Answer("5"),
            Answer("8", correct=True)
        ]
    ),
    Question(
        question="How many lines will this code print? \n"
                 "while False: \n"
                 "print('Looping...')",
        possible_answers=[
            Answer("0", correct=True),
            Answer("1"),
            Answer("Infinitely many")
        ]
    ),
    Question(
        question="What name is given to Python's preinstalled modules?",
        possible_answers=[
            Answer("Unix"),
            Answer("The Standard Library", correct=True),
            Answer("import")
        ]
    ),
    Question(
        question="What does PyPI stand for?",
        possible_answers=[
            Answer("Python Package Installer"),
            Answer("Python Package Index", correct=True),
            Answer("Python Project Index")
        ]
    )
]


def run_questionnaire():
    score = 0

    for question_index, question in enumerate(QUESTIONS):
        question_text = "[Question " + str(question_index + 1) + "] "
        question_text += question.create_prompt()
        print(question_text)

        user_answer_valid = False
        user_answer_num = None

        while not user_answer_valid:
            user_answer_letter = input("Your answer> ")
            user_answer_num = letter2number(user_answer_letter)

            if user_answer_num is None:
                print("That's not a valid letter, please try again")
            elif user_answer_num > len(question.possible_answers):
                print("That's not a valid answer option letter, please try again")
            else:
                user_answer_valid = True

        if question.possible_answers[user_answer_num - 1].correct:
            score += 1
            print("That's correct!")
        else:
            correct_answers = question.get_correct_answers()
            if len(correct_answers) == 1:
                print("That is not correct, the right answer is: " + correct_answers[0])
            else:
                print("That is not correct, the right answer is any of: " + (", or ".join(correct_answers)))

        print("")

    print("Your final score: " + str(score))
    print("Bye!")


run_questionnaire()

