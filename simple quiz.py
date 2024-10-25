
a = print("Welcome to My Quiz Game!!!")
b = print("*****************************************")
question_bank = [
    {
        "text":"What is 1+2___?", "answer":"A"},
        {"text": "What is the colour of apple?","answer":"D"},
        {"text":"how many tail a Tiger has","answer":"C"},
        {"text":"what is the capital of India","answer":"C"},
        {"text":"what is the capital of odisha","answer":"B"}
]

options = [["A. 3","B. 4","C. 5","D. 6"],
          ["A. Green","B. Yellow","C. Blue","D. red"],
          ["A. 3","B. 4","C. 1","D. 6"],
          ["A. Odisha","B. Punjab","C. Delhi","D. Chennai"],
          ["A. Cuttack","B. Bhubaneswar","C. Jajpur","D. Angul"]
          ]

score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("**********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess = input("enter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("correct answer")
        score += 1
        print(score)
    else:
        print("wrong answer")
        print('correct answer is {question_bank[question_num]["answer"]}')
        print("******************************************************")
    print(f"your current score is {score}/{question_num+1}")
    print("******************************************************")
print(f"correct answer given {score}") 
print(f"your score is {(score/len(question_bank))* 100}%")