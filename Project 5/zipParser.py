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
        

def zipList(dataFile: str) -> list:
    with open(dataFile) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            zipNumber = int(row['zip'])
            if zipNumber < 1000:
                zipNumber = '00' + str(zipNumber)
                # print(zipNumber)
            elif zipNumber < 10000:
                zipNumber = '0' + str(zipNumber)
                # print(zipNumber)
            
            
