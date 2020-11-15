# Paul Le
# Sept 27, 2020
# CS A131
# Project 2


import python1_data
from Candidate import Candidate
from ZipCodeClass import ZipCode
import ZipParser


midtermCandidates = python1_data.CandidateList(python1_data.FILENAME)
statesList = python1_data.stateList
zipList = ZipParser.ZipList(ZipParser.FILENAME2)


# obsolete functions no longer required thanks to zip code data
##def searchByState(userInput: str) -> None:
##    "prints all candidates running in said state"
##    index = 0
##    while userInput != statesList[index]:
##        index += 1
##    print("Here are all the candidates running in your state:")
##    for candidate in midtermCandidates[index]:
##        if candidate == statesList[index]:
##            continue
##        print(candidate.getCandidateName())
##
##def searchByDistrict(userInput: str, userInput2: str) -> None:
##    "prints all candidates running in said congressional district"
##    print("Here are all the candidates running in your district:")
##    index = 0
##    while (userInput != statesList[index] and
##           index < len(statesList) - 1):
##        index += 1
##    for candidate in midtermCandidates[index]:
##        if candidate == midtermCandidates[index][0]:
##            continue
##        else:
##            if str(candidate.getCandidateDistrict()) == userInput2:
##                print(candidate.getCandidateName())

def ZipListSearcher(userInput1: str, userInput2: str) -> list:
    "nested loop to find the zip code data associated with said code"
    zipCodeMatches = []
    listIndex = 0
    while userInput1 != statesList[listIndex]:
        listIndex += 1
    assert userInput1 == statesList[listIndex]
    print(zipList[listIndex][0])
    for zipCode in zipList[listIndex]:
        if zipCode == zipList[listIndex][0]:
            continue
        temp = str(zipCode.getZip())
        print(temp)
        if temp == userInput2:
            zipCodeMatches.append(zipCode)
    return zipCodeMatches


def searchByZip(userInput: str) -> None:
    "locates your local candidate by zip code data"
    print("Here are your local candidates:")
    # nested loop to find the zip code data associated with said code
    zipCode = ZipListSearcher(userInput)
    # nested for loop to find the candidate whose data matches the zip data
    print(zipCode)
    for state in midtermCandidates:
        if state[0] != zipCode.getState():
            continue
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateDistrict() == zipCode.getDistrict():
                    print(candidate.getCandidateName())

def searchByBranch(userInput: str) -> None:
    "prints all candidates running in said branch of Congress"
    if userInput == 'H':
        print('''Here are all the candidates running for the House of
Representatives:''')
    elif userInput == 'S':
        print("Here are all the candidates running for the Senate:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateBranch() == userInput:
                print(candidate.getCandidateName())

def searchByFECCandidateID(userInput: str) -> None:
    "prints the profile of the candidate that matches said FEC Candidate ID"
    print("Here is the candidate that matches this FEC Candidate ID:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getfecCandidateID() == userInput:
                candidate.printCandidate()


def searchByStatus(userInput: str) -> None:
    "prints all candidates that match said status"
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


# old UI
##def main():
##    print("Here are your search options:\n",
##          "1. by state\n", "2. by district\n", "3. by branch\n",
##          "4. by FEC Candidate ID\n", "5. by status\n",
##          "6.Quit applet")
##    userInput = input("Type your choice here: ")
##    if int(userInput) == 1:
##        userInput = input("Which state are you looking for?" +
##                          "(abbreviations only) ")
##        searchByState(userInput)
##    elif int(userInput) == 2:
##        userInput = input("Which state are you looking for?" +
##                          "(abbreviations only) ")
##        userInput2 = input("Which district are you looking for?" +
##                          "(numbers only) ")
##        searchByDistrict(userInput, userInput2)
##        pass
##    elif int(userInput) == 3:
##        userInput = input("Which branch of Congress are you looking into?" +
##                          "(Type H or S) ")
##        searchByBranch(userInput)
##    elif int(userInput) == 4:
##        userInput = input("Please input the candidate's FEC Candidate ID: ")
##        searchByFECCandidateID(userInput)
##    elif int(userInput) == 5:
##        print("Please input one of the following statuses:\n" +
##              "1. C\n" + "2. I\n" + "3. O")
##        userInput = input("Type your choice here: ")
##        searchByStatus(userInput)
##    elif int(userInput) == 6:
##        print("All done! Have a good day!")
##        exit(0)
##    else:
##        print("Please choose a valid option!")
##        main()

##if __name__ == "__main__":
##    print("Welcome to the voter guide!\n",
##          "I'll get you information on your candidates in your area\n",
##          "for the upcoming 2018 midterm elections!\n",
##          "Let's get started~")
##    main()
