from question import Question

question_prompts = [
    "What color is the Nigerian flag?\n (a) Yellow/Black\n (b) Green/Red (c) Green/White (d) Black/White\n\n",
    "What year did Nigeria gain her independence?\n (a) 1842\n (b) 1784\n (c) 1960\n (d) 1963\n\n",
    "What year did Nigeria become a republic?\n (a) 1842\n (b) 1784\n (c) 1960\n (d) 1963\n\n",
    "What is the capital of Cameroun?\n (a) Yaounde\n (b) Lagos\n (c) Lome\n (d) Dutshe\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
         answer = input(question.prompt)
         if answer == question.answer:
             score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")
    
print(run_test)