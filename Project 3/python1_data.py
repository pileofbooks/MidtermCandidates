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
            if row == 0:
                print(f'Column names are {", ".join(row)}')
            index = 0
            while row["office_state"] != stateList[index]:
                    if index < len(stateList) - 1:
                        index += 1
            currentCandidate = Candidate()
            currentCandidate.setfecCandidateID(row["fec_candidate_id"])
            currentCandidate.setCandidateName(row["name"])
            currentCandidate.setCandidateParty(row["party"])
            currentCandidate.setCandidateStatus(row["status"])
            currentCandidate.setfecCommitteeID(row["fec_committee_id"])
            currentCandidate.setCandidateState(row["office_state"])
            currentCandidate.setCandidateDistrict(row["district"])
            currentCandidate.setCandidateBranch(row["branch"])
            currentCandidate.setCandidateURL(row["url"])
            currentCandidate.setCandidateCRP(row["crp_id"])
            candidateList[index].append(currentCandidate)
    return candidateList
