# Paul Le
# Nov 15, 2020
# CS A131
# Project 6


import tkinter as tk
import python1_data_manipulator


def ZipSearch():
    

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('240x270')
    window.title("An Idiot's Directory for the 2018 Midterm Election")

    zipButton = tk.Button(text="     Zip Code    ", bg='#5a4d41', fg='white',
                          command=ZipSearch)
