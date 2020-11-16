# Paul Le
# Sept 26, 2020
# CS A131
# Project 2


class Candidate:
    "contains the candidate's profile"
    #def __init__(self):
    #    self.fecCandidateID = ""
    #    self.candidateName = ""
    #    self.candidateParty = ""
    #    self.candidateStatus = ""
    #    self.fecCommitteeID = ""
    #    self.candidateState = ""
    #    self.candidateDistrict = -1
    #    self.candidateBranch = ""
    #    self.candidateURL = ""
    #    self.candidateCRP = ""
    def __init__(self, newfecCandID, newName, newParty, newStatus,
                 newCommID, newState, newDistrict, newBranch, newURL,
                 newCRP):
        self.fecCandidateID = newfecCandID
        self.candidateName = newName
        self.candidateParty = newParty
        self.candidateStatus = newStatus
        self.fecCommitteeID = newCommID
        self.candidateState = newState
        self.candidateDistrict = newDistrict
        self.candidateBranch = newBranch
        self.candidateURL = newURL
        self.candidateCRP = newCRP

    def setfecCandidateID(self, newID: str) -> None:
        "sets the new FEC(Federal Election Commission) candidate ID"
        self.fecCandidateID = newID

    def setCandidateName(self, newName: str) -> None:
        "sets new candidate name"
        self.candidateName = newName

    def setCandidateParty(self, newParty) -> None:
        "sets new candidate party"
        self.candidateParty = newParty

    def setCandidateStatus(self, newStatus: str) -> None:
        "sets new candidate status"
        self.candidateStatus = newStatus

    def setfecCommitteeID(self, newID: str) -> None:
        "sets new FEC(Federal Election Commission) committee ID"
        self.fecCommitteeID = newID

    def setCandidateState(self, newState: str) -> None:
        "sets new candidate state"
        self.candidateState = newState

    def setCandidateDistrict(self, newDistrict: str) -> None:
        "sets new candidate district"
        self.candidateDistrict = newDistrict

    def setCandidateBranch(self, newBranch: str) -> None:
        "sets new candidate branch of Congress"
        self.candidateBranch = newBranch

    def setCandidateURL(self, newURL: str) -> None:
        "sets new candidate website URL"
        self.candidateURL = newURL

    def setCandidateCRP(self, newCRP: str) -> None:
        "sets new candidate CRP(Center for Responsive Politics) ID"
        self.candidateCRP = newCRP

    def getfecCandidateID(self) -> str:
        "returns FEC(Federal Election Commission) candidate ID"
        return self.fecCandidateID

    def getCandidateName(self) -> str:
        "returns candidate name"
        return self.candidateName

    def getCandidateParty(self) -> str:
        "returns candidate party"
        return self.candidateParty

    def getCandidateStatus(self) -> str:
        "returns candidate status"
        if self.candidateStatus == 'C':
            self.candidateStatus = "Challenger"
        elif self.candidateStatus == 'I':
            self.candidateStatus = "Incumbent"
        else:
            self.candidateStatus = "Open"
        return self.candidateStatus

    def getfecCommitteeID(self) -> str:
        "returns candidate's FEC(Federal Election Commission) committee ID"
        return self.fecCommitteeID

    def getCandidateState(self) -> str:
        "returns candidate's state"
        return self.candidateState

    def getCandidateDistrict(self) -> str:
        "returns candidate's district"
        return self.candidateDistrict

    def getCandidateBranch(self) -> str:
        "returns candidate's branch of Congress"
        return self.candidateBranch

    def getCandidateURL(self) -> str:
        "returns candidate's website URL"
        return self.candidateURL

    def getCandidateCRP(self) -> str:
        "returns candidate's CRP(Center for Responsive Politics) ID"
        return self.candidateCRP

    def printCandidate(self) -> None:
        "prints candidate profile"
        print("Candidate Profile:")
        print("Name:", self.candidateName)
        print("Party:", self.candidateParty)
        print("Location:", self.candidateState + ',', self.candidateDistrict)
        print("Branch:", self.candidateBranch)
        print("Status:", self.candidateStatus)
        print("FEC Candidate ID:", self.fecCandidateID)
        print("FEC Committee ID:", self.fecCommitteeID)
        if self.candidateCRP:
            print("CRP ID:", self.candidateCRP)
        if self.candidateURL:
            print("Candidate URL:")
            print(self.candidateURL)
