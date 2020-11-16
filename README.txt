# MidtermCandidates Search Engine(kind of)
Contained within this project are the following files:
  * Candidate.py
  * python1_data.py
    * depends on the candidates_2018_0921_edited.csv file
  * ZipCodeClass.py
  * ZipParser.py
    * depends on the ZIP_CD_092018.csv and State_FIPS_Codes.csv files
  * python_1_data_manipulator

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
* changed print function to omit candidateURL and candidateCRP if both are empty variables

### python1_data.py
Creates a 2D list of states where each state sublist contains candidates associated with said state

__Global Variables__
* FILENAME: str, contains name of the candidates_2018_0921_edited.csv file
* stateList: array containing the names of US States + American Samoa

__Functions__
* CandidateList: takes a str containing a filename
  * takes the candidate csv file and imports them into a 2D list
  * returns 2D list with Candidate objects sorted by state

### ZipCodeClass.py
Contains the definition of a ZipCode class object

__Class Variables__
* zipCode: str, contains the zip code number
* FIPS: int, contains the FIPS state code associated with the zip code
* district: int, contains the district associated with the zip code
* state: str, contains the state associated with the zip code

__PATCH NOTES__
* removed set() functions because unnecessary

### ZipParser.py
Creates a 2D list where each state sublist contains zip codes associated with said state

__Global Variables__
* FILENAME1: str, contains name of the State_FIPS_Codes.csv file
* FILENAME2: str, contains name of the ZIP_CD_092018.csv file

__Functions__
* ZipNumberProcessor: takes an str containing a zip number
  * since some of the zip numbers in the csv are less than 5 digits, this turns them into 5 digits
  * returns a str containing the edited 5 digit zip code
* FIPSSearcher: takes an int containing an FIPS code number
  * looks through FILENAME1 to find the state associated with the int parameter
  * returns a str containing the state abbreviation
* ZipList: takes an str containing a filename
  * loops through FILENAME2 to import each row into a ZipCode object
  * returns a 2D list where each ZipCode object is sorted by state

### python1_data_manipulator
Contains the IDLE shell menu as well as the search functions

__Global Variables__
* midtermCandidates: contains the 2D list of candidates from importing python1_data and its functions
* statesList: contains a list of states from python1_data
* zipList: contains the 2D list of zip codes from importing ZipParser and its functions

__Functions__
* ZipListSearcher: takes two str objects, obj1 contains a state abbreviation, obj2 contains a zip code
  * uses obj1 to find the sublist, and then loops through sublist to find ZipCode objects whose zip codes match obj2
  * returns a list containing all ZipCode objects that match both parameter strings
* searchByZip: takes a list containing ZipCode objects
  * locates candidates in midtermCandidates associated with the ZipCode data in the parameter list
  * prints the district and state, followed by any candidates associated with said district and state
* searchByBranch: takes an str containing whether they want to search by House of Reps or Senate
  * prints whatever Candidate objects match that house of Congress
* searchByFECCandidateID: takes an str containing the FEC candidate ID of a candidate
  * prints the profile of the Candidate object whose data matches the FEC candidate ID
* searchByStatus: takes an str containing the status of a candidate (incumbent, challenger, or open race)
  * prints all candidates that match said status
* main
  * contains the menu for the IDLE shell
  * has conditionals for all the search functions as well as returns to the main again after execution
  * press 5 to exit and be on your way!
