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


def ZipListSearcher(userInput1: str, userInput2: str) -> list:
    "nested loop to find the zip code data associated with said code"
    zipCodeMatches = []
    listIndex = 0
    while userInput1 != statesList[listIndex]:
        listIndex += 1
    # print(zipList[listIndex][0]) (testing for userInput1='CA')
    for zipCode in zipList[listIndex]:
        if zipCode == zipList[listIndex][0]:
            continue
        temp = str(zipCode.getZip())
        # print(temp)
        if temp == userInput2:
            zipCodeMatches.append(zipCode)
    return zipCodeMatches

def searchByZip(dataList: list) -> None:
    "locates your local candidate by zip code data"
    print("\nHere are your local candidates:")
    # nested for loop to find the candidate whose data matches the zip data
    for zipCode in dataList:
        district = zipCode.getDistrict()
        # print(type(district))
        state = zipCode.getState()
        print('\nFrom district', district, 'in', state,
              'you have:')
        index = 0
        while state != statesList[index]:
            index += 1
        for candidate in midtermCandidates[index]:
            if candidate == midtermCandidates[index][0]:
                continue
            if int(candidate.getCandidateDistrict()) == district:
                print(candidate.getCandidateName())
                
def searchByBranch(userInput: str) -> None:
    "prints all candidates running in said branch of Congress"
    if userInput == 'H':
        print('\nHere are all the candidates running for the House',
              'of Representatives:')
    elif userInput == 'S':
        print("\nHere are all the candidates running for the Senate:")
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateBranch() == userInput:
                print(candidate.getCandidateName())

def searchByFECCandidateID(userInput: str) -> None:
    "prints the profile of the candidate that matches said FEC Candidate ID"
    print("\nHere is the candidate that matches this FEC Candidate ID:\n")
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
        print("\nHere are all the challengers:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Challenger':
                    print(candidate.getCandidateName())
    elif userInput == 'I':
        print("\nHere are all the incumbents:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Incumbent':
                    print(candidate.getCandidateName())
    elif userInput == 'O':
        print("\nHere are all those competing for open seats:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Open':
                    print(candidate.getCandidateName())


# old UI
def main():
    print("\nHere are your search options:" +
          "\n1. by zip code" + "\n2. by branch" +
          "\n3. by FEC Candidate ID" + "\n4. by status" +
          "\n5.Quit applet\n")
    userInput = input("Type your choice here: ")
    print('')
    if int(userInput) == 1:
        userInput = input("Which state are you in? " +
                          "(abbreviations only) ")
        userInput2 = input("Input your zip code: ")
        searchByZip(ZipListSearcher(userInput, userInput2))
        main()
    elif int(userInput) == 2:
        userInput = input("Which branch of Congress are you looking into?" +
                          "(Type H or S) ")
        searchByBranch(userInput)
        main()
    elif int(userInput) == 3:
        userInput = input("Please input the candidate's FEC Candidate ID: ")
        searchByFECCandidateID(userInput)
        main()
    elif int(userInput) == 4:
        print("Please input one of the following statuses:\n" +
              "1. C\n" + "2. I\n" + "3. O")
        userInput = input("Type your choice here: ")
        searchByStatus(userInput)
        main()
    elif int(userInput) == 5:
        print("All done! Have a good day!")
        # exit(0)
    else:
        print("Please choose a valid option!")
        main()

if __name__ == "__main__":
    print("Welcome to the voter guide!\n" +
          "I'll get you information on your candidates in your area\n" +
          "for the upcoming 2018 midterm elections!\n" +
          "Let's get started~")
    main()
