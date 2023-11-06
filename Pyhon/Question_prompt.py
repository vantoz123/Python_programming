from Question import Questions

questions_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#create another array
questions = [
    Questions(questions_prompt[0], "a"),
    Questions(questions_prompt[1], "c"),
    Questions(questions_prompt[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions))+ "correct")

    run_test(questions)
