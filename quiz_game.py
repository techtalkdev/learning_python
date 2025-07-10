#⭐ quiz game 💯

questions = (
    "Who was the first black president of South Africa?",
    "What is the capital city of South Africa?",
    "Which part of the plant conducts photosynthesis?",
    "What does www stand for in a website browser?",
    "When did apartheid officially end in South Africa?",
    "Which is the longest river in South Africa?",
    "What gas do humans exhale that plants use in photosynthesis?",
    "Which South African tech entrepreneur co-founded SpaceX and Tesla?",
    "Which South African political party was founded by Nelson Mandela?",
    "Which South African city is known as the “Mother City”?",
) #TUPLE
options = (
    ("A. Jacob Zuma", "B. Thabo Mbeki", "C. Nelson Mandela", "D. Cyril Ramaphosa"),
    ("A. Johannesburg", "B. Cape Town", "C. Pretoria", "D. Durban"),
    ("A. Root", "B. Stem", "C. Flower", "D. Leaf" ),
    ("A. World Web Work", "B. Wide World Web", "C. World Wide Web", "D. Web World Window"),
    ("A. 1990", "B. 1994", "C. 1989", "D. 1996" ),
    ("A. Limpopo River", "B. Orange River", "C. Vaal River", "D. Tugela River"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide","D. Hydrogen"),
    ("A. Mark Shuttleworth", "B. Elon Musk", "C. Patrice Motsepe", "D. Vusi Thembekwayo"),
    ("A. Economic Freedom Fighters (EFF)","B. Inkatha Freedom Party (IFP)","C. African National Congress (ANC)","D. Democratic Alliance (DA)"),
    ("A. Durban", "B. Johannesburg", "C. Pretoria", "D. Cape Town")
)
answers = (
    "C",
    "C",
    "D",
    "C",
    "B",
    "B",
    "C",
    "B",
    "C",
    "C"
)

score = 0
guesses = []
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess(A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"answers{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------")
print("------Results------")
print("-----------------")

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is {score}%" )