# Paul Le
# Sept 26 2020
# CS A131
# Project 2


from Candidate import Candidate
import csv


FILENAME = 'candidates_2018_0921_edited.csv'
stateList = ["AL", "AK", "AZ", "AR", "AS", "CA", "CO", "CT", "DC", "DE", "FL",
             "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
             "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
             "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
             "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def CandidateList(FILENAME: str) -> list:
    "creates a list of candidates sorted by state"
    candidateList = [[state] for state in stateList]
    with open(FILENAME) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            index = 0
            while (row["office_state"] != stateList[index] and
                   index < len(stateList) - 1):
                index += 1
            currentCandidate = Candidate(row['fec_candidate_id'],
                                         row['name'], row['party'],
                                         row['status'],
                                         row['fec_committee_id'],
                                         row['office_state'],
                                         row['district'], row['branch'],
                                         row['url'], row['crp_id'])
            candidateList[index].append(currentCandidate)

    return candidateList
