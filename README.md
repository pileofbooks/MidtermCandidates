# MidtermCandidates Search Engine(kind of)
Contained within this project are the following files:
  * Candidate.py
  * python1_data.py
    * depends on the candidates_2018_0921_edited.csv file
  * python_1_data_manipulator
  * ZipCodeClass.py
  * ZipParser.py
    * depends on the ZIP_CD_092018.csv and State_FIPS_Codes.csv files

## Table of Contents
### Candidate.py
Contains a definition of a Candidate class object

__NOTE__: there are no functions defined to change instance variables 
because it's unnecessary at this time
Class Variables:
* fecCandidateID: str, contains candidate's FEC(Federal Election Commission) candidate ID #
* candidateName: str, contains candidate's name
* candidateParty: str, contains candidate's political party affiliation
* candidateStatus: str, tells whether candidate is an I(incumbent), a C(challenger), or if it's an O(open race)
* fecCommitteeID: str, contains candidate's FEC committee ID #
* candidateState: str, tells which state the candidate is running in
* candidateDistrict: int, tells which district the candidate is running in
* candidateBranch: str, tells which branch of Congress said candidate is running for
* candidateURL: str, contains URL link to candidate's website, if applicable
* candidateCRP: str, contains candidate's CRP code

__PATCH NOTES__
* defined different __init__ function with parameter inputs
* removed all setAttribute() functioned because of above mentioned change

###python1_data.py
creates a 2D list of states where each state sublist contains candidates associated with said state

__Global Variables__
* FILENAME: str, contains name of the candidates_2018_0921_edited.csv file
* stateList: array containing the names of US States + American Samoa
