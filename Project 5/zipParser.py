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
    state = ''
    with open(FILENAME1) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            if row['FIPS'] == searchNum:
                state = row['Abbreviation']
    return state
        

def ZipList(dataFile: str) -> list:
    zipList = [[state] for state in stateList]
    with open(dataFile) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            zipNumber = int(row['zip'])
            if zipNumber < 1000:
                zipNumber = '00' + str(zipNumber)
                # print(zipNumber)
            elif (zipNumber > 1000 and zipNumber < 10000):
                zipNumber = '0' + str(zipNumber)
                # print(zipNumber)
            newZip = ZipCode(zipNumber, int(row['cd'] / 1000),
                             (row['cd'] % 100),
                             FIPSSearcher((row['cd'] % 100)))
            index = 0
            stateAbbrev = newZip.getState()
            while (index < len(stateList) and
                   stateAbbrev != stateList[index]):
                index += 1
            
