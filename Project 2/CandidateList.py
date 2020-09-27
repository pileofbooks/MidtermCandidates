# Paul Le
# Sept 26 2020
# CS A131
# Project 2


import Candidates
import csv


FILENAME = 'candidates_2018_0921_edited.csv'
stateList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
             "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
             "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
             "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
             "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def CandidateList(FILENAME: str) -> list:
    "creates a list of candidates sorted by state"
    candidateList = [[state] for state in stateList]
    with open(FILENAME, mode = 'r') as csv_file:
        csv_reader = csv.DictReader(FILENAME)
        while row < 100:
            for row in csv_reader(FILENAME):
                if row == 0:
                    continue
                else:
                    
    return candidateList
