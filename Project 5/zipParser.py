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
    with open(FILENAME) as csvFile:
        csvReader = csv.DictReader(csvFile)
        while csvReader[

def zipList(file1, file2) -> list:
    with open(FILENAME2) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            zipNumber = row['zip']
            
            
