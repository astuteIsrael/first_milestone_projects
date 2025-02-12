# Project 2
def computer_based_test():
    questions = (
        ("How many elements are in the periodic table?: "),
        ("Which of this animals lay the largest egg?: "),
        ("What is the most abundant gas in Earth's atmosphere?: "),
        ("How many bones are in the human body?: "),
        ("Which planet in the solar system is the hottest?: ")
    )

    options = (
        ("A. 116" ,"B. 117" ,"C. 118" ,"D. 119" ),
        ("A. Whale" ,"B. Ostrich" ,"C. Elephant" ,"D. Dog" ),
        ("A. Nitrogen" ,"B. Oxygen" ,"C. Carbon-Dioxide" ,"D. Hyroden" ),
        ("A. 206" ,"B. 207" ,"C. 208" ,"D. 209" ),
        ("A. Mercury" ,"B. Venus" ,"C. Earth" ,"D. Mars" )
    )

    answers = ("C", "B", "A", "A", "A")
    user_choice = []
    score = 0
    questions_num = 0

    for question in questions:
        # print('---------------------------------')
        print(question)
        for option in options[questions_num]:
            print(option)

        your_pick = input("Enter (A or B or C or D): ").upper()
        user_choice.append(your_pick)
        if your_pick == answers[questions_num]:
            score += 1
            print("Correct!")

        else:
            print("Incorrect!")
            print(f"{answers[questions_num]} is the correct answer")
        questions_num += 1


    print("answers: ", end="")
    for answer in answers:
        print(answer, end="")
    print()

    print("user_choice: ", end="")
    for your_pick in answers:
        print(your_pick, end="")
    print()

    score = int(score / len(questions) * 10)
    print(f"At the end of the the CBT exam, you scored {score} points")

computer_based_test()