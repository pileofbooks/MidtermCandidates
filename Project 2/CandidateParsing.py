# Paul Le
# Sept 26, 2020
# CS A131
# Project 2

import csv


FILENAME = 'candidates_2018_0921_edited.csv'


class Candidate:
    "contains the candidate's profile"
    def __init__(self):
        fecCandidateID = ""
        candidateName = ""
        candidateParty = ""
        candidateStatus = ""
        candidateZip = 0
        fecCommitteeID = ""
        candidateState = ""
        candidateDistrict = -1
        candidateBranch = ""
        candidateURL = ""
        candidateCRP = ""

    def setfecCandidateID(self, newID: str) -> None:
        "sets the new FEC candidate ID"
        fecCandidateID = newID

    def setCandidateName(self, newName: str) -> None:
        "sets new candidate name"
        candidateName = newName

    def setCandidateParty(self, newParty) -> None:
        "sets new candidate party"
        candidateParty = newParty

    def setCandidateStatus(self, newStatus: str) -> None:
        "sets new candidate status"
        candidateStatus = newStatus

    def setCandidateZip(self, newZip: int) -> None:
        "sets new candidate zip code"
        candidateZip = newZip

    def setfecCommitteeID(self, newID: str) -> None:
        "sets new FEC committee ID"
        fecCommitteeID = newID

    def setCandidateState(self, newState: str) -> None:
        "sets new candidate state"
        candidateState = newState

    def setCandidateDistrict(self, newDistrict: int) -> None:
        "sets new candidate district"
        candidateDistrict = newDistrict

    def setCandidateURL(self, newURL: str) -> None:
        "sets new candidate website URL"
        candidateURL = newURL

    def setCandidateCRP(self, newCRP: str) -> None:
        "sets new candidate CRP ID"
        candidateCRP = newCRP

    def getfecCandidateID(self) -> str:
        "returns FEC candidate ID"
        return fecCandidateID
