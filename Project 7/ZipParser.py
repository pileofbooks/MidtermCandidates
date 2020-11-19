# Paul Le
# Oct 25, 2020
# CS A131
# Project 5


import csv
from ZipCodeClass import ZipCode
from python1_data import stateList


FILENAME1 = 'State_FIPS_Codes.csv'
FILENAME2 = 'ZIP_CD_092018.csv'


def ZipNumberProcessor(dataString: str) -> str:
    dataString = int(dataString)
    if (dataString < 10000 and dataString > 1000):
        dataString = '0' + str(dataString)
    elif (dataString < 1000):
        dataString = '00' + str(dataString)
    return dataString
        

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
        counter = 0
        for row in csvReader:
            cd = row['cd']
            if cd.isdigit() == False:
                # some of the cd numbers are not ints, so cannot be processed
                # print('cd is not an int')
                continue
            cd = int(cd)
            fips = int(cd / 100)
            if fips > 60:
                # print('fips > 60')
                continue
            district = cd % 100
            stateAbbrev = FIPSSearcher(fips)
            zipNumber = ZipNumberProcessor(int(row['zip']))
            newZip = ZipCode(zipNumber, fips, district, stateAbbrev)
            # print(stateAbbrev)
            for state in zipList:
                # print(state[0])
                if state[0] == stateAbbrev:
                    counter += 1
                    state.append(newZip)
    # print(counter)
    return zipList
