# a program to compute marks for a given number of questions
from testclass import*

question_prompt = [
"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
"What color are Bananas?\n (a) Teal\n(b) Magneta\n(c) Yellow\n\n",
"What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]

def run_test(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
run_test(questions)