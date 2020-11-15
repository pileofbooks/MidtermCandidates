# Paul Le
# Oct 25, 2020
# CS A131
# Project 5


import csv
from ZipCodeClass import ZipCode
from python1_data import stateList


FILENAME1 = 'State_FIPS_Codes.csv'
FILENAME2 = 'ZIP_CD_092018.csv'


def FIPSSearcher(searchNum: int) -> str:
    "takes an int and looks through the key to find the state abbreviation"
    state = ''
    with open(FILENAME1) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            if int(row['FIPS']) == searchNum:
                state = row['Abbreviation']
    return state
        

def ZipList(dataFile: str) -> list:
    "sorts zip codes into a 2d list of states using the ZipCode class"
    zipList = [[state] for state in stateList]
    with open(dataFile) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            cd = row['cd']
            if cd.isdigit() == False:
                # some of the cd numbers are not ints, so cannot be processed
                continue
            else:
                cd = int(cd)
            if (int(cd / 100) > 60):
                continue
            zipNumber = int(row['zip'])
            if zipNumber < 1000:
                zipNumber = '00' + str(zipNumber)
                # print(zipNumber)
            elif (zipNumber > 1000 and zipNumber < 10000):
                zipNumber = '0' + str(zipNumber)
                # print(zipNumber)
            newZip = ZipCode(zipNumber, int(cd / 100),
                             (cd % 100),
                             FIPSSearcher(cd % 100))
            # print(newZip)
            index = 0
            stateAbbrev = newZip.getState()
            # print(stateAbbrev)
            for state in zipList:
                # print(state[0])
                if state[0] == stateAbbrev:
                    state.append(newZip)
    return zipList
