# Paul Le
# Sept 26 2020
# CS A131
# Project 2


import Candidate
import csv


FILENAME = 'candidates_2018_0921_edited.csv'


def main():
    
    with open(FILENAME, mode = 'r') as csv_file:
        csv_reader = csv.DictReader(FILENAME)
        for row in range(99):
            if row == 0:
                
