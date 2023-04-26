import random

def generate_answers():
    questions = []
    answers = []
    final = []

    number_of_questions = int(input('\nHow many questions do you want to input? '))

    # Inser date such as question content and number of answers it has into tables
    for i in range(number_of_questions):
        question = str(input(f"\nInsert question number {i+1}: "))
        answer = int(input("How many answers? "))
        questions.append(question)
        answers.append(answer)

    number_of_people = int(input('\nHow many people should fill it up? '))
    print('\n\n-- Your randomly generated answers --\n')

    for i, question in enumerate(questions):
        print(f"\n-- {question} --")
        total_answers = 0

        # Generate random answers
        for j in range(answers[i]):
            # Last answer gets the remaining number of people
            if j == answers[i] - 1:
                num = number_of_people - total_answers
            else:
                num = random.randint(0, number_of_people - total_answers)
            final.append(num)
            total_answers += num

        # Print answers
        for k, answer in enumerate(final):
            print(f"Answer number {k+1}: {answer}")

        final.clear()

if __name__ == '__main__':
    choice = int(input("\nWelcome! My job is to help you with generating randomly answers to your questionnaire.\n\n[1] Start\n[2] Close\n"))

    if choice == 1:
        while choice != 0:
            generate_answers()
            choice2 = int(input("\n\n\n[1] Start again\n[2] Close\n"))

            if choice2 == 2:
                break
