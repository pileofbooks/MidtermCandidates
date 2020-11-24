# Paul Le
# Nov 19, 2020
# CS A131
# Project 7 - GUI and Help Button


import tkinter as tk
from Candidate import Candidate
from ZipCodeClass import ZipCode
import python1_data_manipulator_gui_version as dataManip


# Global Variables
candidateList = dataManip.midtermCandidates
stateList = dataManip.statesList
zipList = dataManip.zipList


def choice(userChoice: int):
    if userChoice == 1:
        # user enters input into a text box
        pass

def help():
    popup = tk.Tk()
    popup.geometry('480x600')
    popup.title("User Guide")
    label = tk.Label(popup,
                     text="Below is a help menu for this search engine!",
                     font=('Times)
    label.font.configure(size=20)
    lable.grid(column=5, row=1)


if __name__ == '__main__':
    # initializing the window
    window = tk.Tk()
    window.geometry('1024x576')
    window.title("Midterm Candidate Search Engine")

    # labels
    header = tk.Label(window,
                      text="Welcome! Please select a filter for candidates!",
                      )
    header.grid(column=0, row=1)

    # Buttons
    button1 = tk.Button(text = "  Zip Code  ", bg="#53a6c2", command=help)
    button1.grid(column=0, row=4)
                      
    window.mainloop()
