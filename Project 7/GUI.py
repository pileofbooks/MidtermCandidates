# Paul Le
# Nov 19, 2020
# CS A131
# Project 7 - GUI and Help Button


import tkinter as tk
from Candidate import Candidate
from ZipCodeClass import ZipCode
import python1_data_manipulator as dataManip


# Global Variables
candidateList = dataManip.midtermCandidates
stateList = dataManip.statesList
zipList = dataManip.zipList

# initializing the window
window = tk.Tk()
window.geometry('1024x576')
window.title("Midterm Candidate Search Engine")

def choice(userChoice: int):
    if userChoice == 1:
        dataManip.searchByZip(


