midterm_candidates_string = '''
          2018 Midterm Candidate List(CA)

Name                          Party  District  Branch
-----------------------------------------------------
Bradley, James                REP    0         S
De Leon, Kevin                DEM    0         S
Feinstein, Dianne             DEM    0         S
Denney, Audrey                DEM    1         H
Lamalfa, Doug                 REP    1         H
Huffman, Jared                DEM    2         H
Mensing, Dale                 REP    2         H
Garamendi, John               DEM    3         H
Schaupp, Charlie              REP    3         H
McClintock, Tom               REP    4         H
Morse, Jessica                DEM    4         H
...
'''

midterm_candidates_tuple = [
    ("Bradley, James", "REP", 0, "S"),
    ("De Leon, Kevin", "DEM", 0, "S"),
    ("Feinstein, Dianne", "DEM", 0, "S"),
    ("Denney, Audrey", "DEM", 1, "H"),
    ("Lamalfa, Doug", "REP", 1, "H"),
    ("Huffman, Jared", "DEM", 2, "H"),
    ("Mensing, Dale", "REP", 2, "H"),
    ("Garamendi, John", "DEM", 3, "H"),
    ("Shcaupp, Charlie", "REP", 3, "H"),
    ("McClintock, Tom", "REP", 4, "H"),
    ("Morse, Jessica", "DEM", 4, "H")]

class MidtermCandidates:
    def __init__(self):
        self._name = ""
        self._party = ""
        self._district = 0
        self._branch = ""

    def __init__(self, new_name, new_party, new_district, new_branch):
        self._name = new_name
        self._party = new_party
        self._district = new_district
        self._branch = new_branch

    def setName(self, new_name):
        self._name = new_name

    def setParty(self, new_party):
        self._party = new_party

    def setDistrict(self, new_district):
        self._district = new_district

    def setBranch(self, new_branch):
        self._branch = new_branch

    def getName(self) -> str:
        return self._name

    def getParty(self) -> str:
        return self._party

    def getDistrict(self) -> int:
        return self._district

    def getBranch(self) -> str:
        return self._branch

    def printCandidate(self) -> None:
        print("Candidate Profile\n",
              "Name: " + self._name + "\n",
              "Party: " + self._party + "\n",
              "District: " + str(self._district) + "\n",
              "Branch: " + self._branch + "\n")
