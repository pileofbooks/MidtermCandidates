# Paul Le
# Sept 27, 2020
# CS A131
# Project 7


import python1_data
from Candidate import Candidate
from ZipCodeClass import ZipCode
import ZipParser

midtermCandidates = python1_data.CandidateList(python1_data.FILENAME)
statesList = python1_data.stateList
zipList = ZipParser.ZipList(ZipParser.FILENAME2)


def ZipListSearcher(userInput: str) -> list:
    "nested loop to find the zip code data associated with said code"
    zipCodeMatches = []
    for state in zipList:
        for zipCode in state:
            if zipCode == state[0]:
                continue
            if str(zipCode.getZip()) == userInput:
                zipCodeMatches.append(zipCode)
    return zipCodeMatches


def searchByZip(dataList: list) -> list:
    "locates your local candidate by zip code data"
    result = []
    # nested for loop to find the candidate whose data matches the zip data
    for zipCode in dataList:
        district = zipCode.getDistrict()
        # print(type(district))
        state = zipCode.getState()
        index = 0
        while state != statesList[index]:
            index += 1
        for candidate in midtermCandidates[index]:
            if candidate == midtermCandidates[index][0]:
                continue
            if int(candidate.getCandidateDistrict()) == district:
                result.append(candidate)
    return result


def searchByBranch(userInput: str) -> list:
    "returns list of all candidates running in said branch of Congress"
    result = []
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getCandidateBranch() == userInput:
                result.append(candidate)
    return result


def searchByFECCandidateID(userInput: str) -> list:
    "returns the profile of the candidate that matches said FEC Candidate ID"
    result = 0
    for state in midtermCandidates:
        candidate = 0
        for candidate in state:
            if candidate == state[0]:
                continue
            if candidate.getfecCandidateID() == userInput:
                result = candidate
    return result


def searchByStatus(userInput: str) -> None:
    "returns list of all candidates that match said status"
    result = []
    if userInput == 'C':
        # print("\nHere are all the challengers:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Challenger':
                    # print(candidate.getCandidateName())
                    result.append(candidate)
    elif userInput == 'I':
        # print("\nHere are all the incumbents:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Incumbent':
                    # print(candidate.getCandidateName())
                    result.append(candidate)
    elif userInput == 'O':
        # print("\nHere are all those competing for open seats:")
        for state in midtermCandidates:
            candidate = 0
            for candidate in state:
                if candidate == state[0]:
                    continue
                if candidate.getCandidateStatus() == 'Open':
                    # print(candidate.getCandidateName())
                    result.append(candidate)
    return result


# old UI
def main():
    print("\nHere are your search options:" +
          "\n1. by zip code" + "\n2. by branch" +
          "\n3. by FEC Candidate ID" + "\n4. by status" +
          "\n5.Quit applet\n")
    userInput = input("Type your choice here: ")
    print('')
    if int(userInput) == 1:
        userInput = input("Input your zip code: ")
        result = searchByZip(ZipListSearcher(userInput))
        for item in result:
            print(item.getCandidateName())
        main()
    elif int(userInput) == 2:
        userInput = input("Which branch of Congress are you looking into?" +
                          "(Type H or S) ")
        result = searchByBranch(userInput)
        for item in result:
            print(item.getCandidateName())
        main()
    elif int(userInput) == 3:
        userInput = input("Please input the candidate's FEC Candidate ID: ")
        result = searchByFECCandidateID(userInput)
        for item in result:
            print(item.getCandidateName())
        main()
    elif int(userInput) == 4:
        print("Please input one of the following statuses:\n" +
              "1. C\n" + "2. I\n" + "3. O")
        userInput = input("Type your choice here: ")
        result = searchByStatus(userInput)
        for item in result:
            print(item.getCandidateName())
        main()
    elif int(userInput) == 5:
        print("All done! Have a good day!")
        #exit(0)
    else:
        print("Please choose a valid option!")
        main()

if __name__ == "__main__":
    print("Welcome to the voter guide!\n" +
          "I'll get you information on your candidates in your area\n" +
          "for the upcoming 2018 midterm elections!\n" +
          "Let's get started~")
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    main()
