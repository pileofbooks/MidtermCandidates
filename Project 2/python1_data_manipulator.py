# Paul Le
# Sept 27, 2020
# CS A131
# Project 2


import python1_data
from Candidate import Candidate


midtermCandidates = python1_data.CandidateList(python1_data.FILENAME)
statesList = python1_data.stateList


def searchByState(userInput: str) -> None:
    index = 0
    while userInput != statesList[index]:
        index += 1
    print("Here are all the candidates running in your state:")
    for candidate in midtermCandidates[index]:
        if candidate == statesList[index]:
            continue
        print(candidate.getCandidateName())
    main()


def searchByDistrict(userInput: str) -> None:
    print("Here are all the candidates running in your district:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateDistrict() == userInput:
                print(candidate.getCandidateName())
    main()


def searchByBranch(userInput: str) -> None:
    print("Here are all the candidates running for your branch of Congress:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateBranch() == userInput:
                print(candidate.getCandidateName())
    main()


def searchByFECCandidateID(userInput: str) -> None:
    print("Here is the candidate that matches this FEC Candidate ID:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getfecCandidateID() == userInput:
                candidate.printCandidate()
    main()


def searchByStatus(userInput: str) -> None:
    if userInput == 'C':
        print("Here are all the challengers:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Challenger':
                    print(candidate.getCandidateName())
    elif userInput == 'I':
        print("Here are all the incumbents:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Incumbent':
                    print(candidate.getCandidateName())
    elif userInput == 'O':
        print("Here are all those competing for open seats:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Open':
                    print(candidate.getCandidateName())
    main()


def main():
    print("Here are your search options:\n",
          "1. by state\n", "2. by district\n", "3. by branch\n",
          "4. by FEC Candidate ID\n", "5. by status\n",
          "6.Quit applet")
    userInput = input("Type your choice here: ")
    if int(userInput) == 1:
        userInput = input("Which state are you looking for?" +
                          "(abbreviations only) ")
        searchByState(userInput)
    elif int(userInput) == 2:
        userInput = input("Which district are you looking for?" +
                          "(numbers only) ")
        searchByDistrict(userInput)
        pass
    elif int(userInput) == 3:
        userInput = input("Which branch of Congress are you looking into?" +
                          "(Type H or S) ")
        searchByBranch(userInput)
    elif int(userInput) == 4:
        userInput = input("Please input the candidate's FEC Candidate ID: ")
        searchByFECCandidateID(userInput)
    elif int(userInput) == 5:
        print("Please input one of the following statuses:\n" +
              "1. C\n" + "2. I\n" + "3. O")
        userInput = input("Type your choice here: ")
        searchByStatus(userInput)
    elif int(userInput) == 6:
        quit
    else:
        print("Please choose a valid option!")
        main()

if __name__ == "__main__":
    print("Welcome to the voter guide!\n",
          "I'll get you information on your candidates in your area\n",
          "for the upcoming 2018 midterm elections!\n",
          "Let's get started~")
    main()
