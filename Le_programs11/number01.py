# Paul Le
# CS A131
# Nov 19 2020
# Python Practice hw11 num 1


from os import path
import random


answerKey = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
             'A', 'C', 'D', 'B', 'D', 'D', 'A', 'C', 'B', 'A']


def RandomStudentDriver() -> str:
    "generates a random student driver's test responses and writes to txt"
    fileName = 'responses.txt'
    if path.exists(fileName) == False:
        with open(fileName, 'w') as txtFile:
            responseChoices = ['A', 'B', 'C', 'D']
            studentResponses = [random.choice(responseChoices) for count in
                                range(20)]
            # print(studentResponses)
            # print("student response length:",len(studentResponses))
            txtFile.write(studentResponses.pop(0))
            for answer in studentResponses:
                txtFile.write('\n' + answer)
    return fileName
            

def AutoGrader(dataFile: str) -> list:
    "grades student answers with key and returns list of wrong questions"
    wrongAnswers = []
    with open(dataFile) as txtFile:
        studentAnswers = txtFile.readlines()
##        for answer in studentAnswers:
##            print(answer[0])
        numOfQuestions = 20
        index = 0
        for question in answerKey:
            if question != studentAnswers[index][0]:
                wrongAnswers.append(index + 1)
            index += 1
    return wrongAnswers

if __name__ == '__main__':
    fileName = RandomStudentDriver()
    testResults = AutoGrader(fileName)
    # there's no way a randomly generated file can achieve 100%, can it...
    assert len(testResults) != 0
    deductions = len(testResults)
    if deductions > 5:
        print("Sorry, you did not pass")
        print("\nYour results:")
        print("Correct:", (20 - deductions))
        print("Wrong:", deductions)
        print("\nThese are the questions you got wrong:")
        for answer in testResults:
            print(answer)
    else:
        print("Congrats! You passed!")
        print('\nYour results:')
        print("Correct:", (20 - deductions))
        print("Wrong:", deductions)
        print("\nThese are the questions you got wrong:")
        for answer in testResults:
            print(answer)
