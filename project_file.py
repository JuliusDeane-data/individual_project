# The Quiz Game
""" 
- Player inputs name
- Player answers 5 questions
- player gets score
"""
questions = {
    1: {
        "question": "What is the standard file extension for Python files?",
        "options": ["a) .py", "b) .python", "c) .pyt", "d) .txt"],
        "answer": "a"
    },
    2: {
        "question": "How can you write a comment in Python?",
        "options": ["a) // comment", "b) # comment", "c) /* comment */", "d) <!-- comment -->"],
        "answer": "b"
    },
    3: {
        "question": "Which function is used to print output in Python?",
        "options": ["a) echo()", "b) print()", "c) output()", "d) display()"],
        "answer": "b"
    },
    4: {
        "question": "How is a list created in Python?",
        "options": ["a) {}", "b) []", "c) ()", "d) <>"],
        "answer": "b"
    },
    5: {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["a) ^", "b) **", "c) %", "d) //"],
        "answer": "b"
    },
    6: {
        "question": "Which function returns the length of a list?",
        "options": ["a) size()", "b) count()", "c) len()", "d) length()"],
        "answer": "c"
    },
    7: {
        "question": "How do you declare a variable in Python?",
        "options": ["a) int x = 5", "b) x := 5", "c) x = 5", "d) var x = 5"],
        "answer": "c"
    },
    8: {
        "question": "Which loop is used to iterate through a list?",
        "options": ["a) for", "b) while", "c) do-while", "d) foreach"],
        "answer": "a"
    },
    9: {
        "question": "Which method is used to convert a string to lowercase?",
        "options": ["a) lower()", "b) lowercase()", "c) toLower()", "d) case_lower()"],
        "answer": "a"
    },
    10: {
        "question": "What is used to define a block of code in Python?",
        "options": ["a) Brackets {}", "b) Indentation", "c) Semicolon ;", "d) Colon :"],
        "answer": "b"
    },
    11: {
        "question": "What is the value of `5 // 2` in Python?",
        "options": ["a) 2.5", "b) 2", "c) 3", "d) 1"],
        "answer": "b"
    },
    12: {
        "question": "Which library is commonly used to work with DataFrames?",
        "options": ["a) NumPy", "b) Pandas", "c) SciPy", "d) Matplotlib"],
        "answer": "b"
    },
    13: {
        "question": "What is the difference between a list and a tuple?",
        "options": ["a) Tuples are immutable", "b) Lists are immutable", "c) No difference", "d) Tuples are faster"],
        "answer": "a"
    },
    14: {
        "question": "Which function is used to convert a string to an integer?",
        "options": ["a) parseInt()", "b) str()", "c) int()", "d) convert()"],
        "answer": "c"
    },
    15: {
        "question": "How do you open a file in Python?",
        "options": ["a) open()", "b) file()", "c) fopen()", "d) read()"],
        "answer": "a"
    },
    16: {
        "question": "How can you import a module in Python?",
        "options": ["a) include module", "b) use module", "c) import module", "d) load module"],
        "answer": "c"
    },
    17: {
        "question": "Which method is used to add an element to a list?",
        "options": ["a) add()", "b) append()", "c) push()", "d) insert()"],
        "answer": "b"
    },
    18: {
        "question": "What does `range(3)` return?",
        "options": ["a) [1, 2, 3]", "b) [0, 1, 2]", "c) (0, 1, 2)", "d) range-object"],
        "answer": "d"
    },
    19: {
        "question": "What is the difference between `is` and `==`?",
        "options": ["a) No difference", "b) `is` compares identity, `==` compares values", "c) `is` compares values, `==` compares identity", "d) `is` works only with strings"],
        "answer": "b"
    },
    20: {
        "question": "What value is returned when a function does not have a return statement?",
        "options": ["a) 0", "b) False", "c) None", "d) Null"],
        "answer": "c"
    }
}

player = input("What's your name? ")

def show_score(player_name = 'Unknown', points = 0):
    """Shows the final score to the player"""
    if points == 5:
        return f'Amazing job {player_name}! A perfect 5/5 score, are you Linus Torwalds or Chris Sawyer?'
    elif points < 5 and points >= 3:
        return f'Good job {player_name}! A {points}/5 score is nothing to sneeze at.'
    elif points < 3 and points >= 1:
        return f'You can do better {player_name}! With a {points}/5 score you have a lot of room for improvement.'       
    else:
        return f'Are you okay {player_name}? A {points}/5 score is not so good. Please see a doctor.'

def show_question(number_of_question):
    """returns the question and answer options to the user"""
    print(f'{questions[number_of_question]["question"]}\n{"  ".join(questions[number_of_question]["options"])}')
    

def check_answer(player_answer, number_of_question):
    """checks if given answer is correct"""
    if player_answer == questions[number_of_question]['answer']:
        print(f'Correct! You get +1 point')
        return 1
    else:
        print(f"Sorry, you're wrong. The correct answer is {questions[number_of_question]['answer']}")
        return 0

def main_quiz(name, score):
    """present questions to the player, check answers, track score"""
    print(f"Your current score is {score}.")
    question_number = int(input(f"{name} pick a number betweeen 1 - 20 to get your next question: "))
    show_question(question_number)
    answer_choice = input(f"Please choose your answer (a, b, c, d): ")
    score = check_answer(answer_choice, question_number)
    return score
    
score = 0   
n = 0
while n < 5:
    score += main_quiz(player, score)
    n += 1

print(show_score(player, score))

