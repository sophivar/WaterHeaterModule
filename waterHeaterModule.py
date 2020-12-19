import tkinter as tk
from tkinter import *
#from heater_selector import *
#from electricityBC import *
#from naturalGasBC import *
#from energyUse import *

"""
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas as pd
import xlrd
from PIL import ImageTk, Image
from PIL import Image
import PIL.Image, PIL.ImageTk
from openpyxl import *
import xlwings as xw
"""

# Heater and Building Type options - for drop down menu
heater_type_options = ["Conventional Natural Gas Storage", "Conventional Electric Storage",
                       "Conventional Oil-fired Storage", "Conventional Propane Storage",
                       "High-efficiency Natural Gas Storage", "High-efficiency Electric Storage",
                       "Minimum efficiency Electric Storage", "Condensing Gas Storage",
                       "Natural Gas Demand", "Electric Demand",
                       "Solar with Electric Back-up", "Indirect with Boiler", "Heat Pump"]

building_type_options = ["House or Flat", "Offices", "School, boarding", "School, day",
                         "Hostel", "Hotel", "Hospital, general", "Hospital, mental", "Factory"]

# Heater Replacement Database
# Index value serves as ID for each heater.
# Lists of values or strings represent the relevant heater specifications.

B_manufacturer = ["Gemco", "American Standard", "Gemco", "Gemco", "Gemco"]

B_type = ["Conventional Natural Gas Storage", "Conventional Electric Storage",
          "Conventional Oil-fired Storage", "Conventional Propane Storage",
          "High-efficiency Natural Gas Storage"]

B_size = [30, 40, 40, 50, 30] # gallons

B_EFvalue = [0.67, 0.78, 0.75, 0.69, 0.80]

B_purchaseCost = [1200, 1600, 1000, 900, 1400] # $

n = len(B_manufacturer) # the number of heaters in the database

# Focus events (for each input screen field)
# (Function to set focus (cursor))

def focus1(event):
    heater_type_field.focus_set()

def focus2(event):
    heater_size_field.focus_set()

def focus3(event):
    EF_field.focus_set()

def focus4(event):
    building_type_field.focus_set()

def focus5(event):
    numberOfOccupants_field.focus_set()

'''
def focus6(event):
    monthly_hotWaterUse_estimate_field.focus_set()

# additional parameters for calculating more precise energy (electricity or gas) costs
def focus7(event):
    location_field.focus_set()
    # this value will be passed to the energyUse.py file

def focus7(event):
    energy_tier_field.focus_set() 
    # 1, 2, or 3
    # this value will be passed to the electricityBC.py file
    
def focus7(event):
    peak_demand_field.focus_set()
    # 3 possible brackets in BC. Create a drop down menu? 
    # this value will be passed to the electricityBC.py file
'''

# Clear inputs
def clear():
    heater_type_field.delete(0, END)
    heater_size_field.delete(0, END)
    EF_field.delete(0, END)
    building_type_field.delete()
    numberOfOccupants_field.delete()
    #monthly_hotWaterUse_estimate_field.delete(0, END)

# Function to take data from GUI window
# Module calculations
# Grab inputs and turn into outputs
def evaluate():

    # Temporary values. Can create more accurate functions later.
    # Maybe plan to write .py files that calculate energy use and
    # charge ($/kWh or $/therm) based on user's inputs
    electricity_charge = 0.124  # $/kWh
    naturalGas_charge = 0.01  # $/therm
    electricity_use = 12.03  # kWh/day
        # e.g. eventually replace with electricity_use = energyUse(building_type,...  params...)
    naturalGas_use = 0.4105  # therm/day

    A_size_gal = heater_size_field.get()
    A_EF = float(EF_field.get())

    # asses current models annual operating cost
    # if fuel type = electricity
    A_annOpCost = (electricity_use / A_EF) * electricity_charge * 365
    # else if fuel type = natural gas
    # A_annOpCost = (naturalGas_use / A_EF) * naturalGas_charge * 365

    B_annOpCost = []
    B_annCostSavings = []
    B_paybackPer = []
    B_IDs = list(range(n + 1))

    for i in range(n+1):

        # narrow down database
        # EF of optionB > EF of current model to qualify for output/recommendation
        # heater size recc = heater size current
        if (B_EFvalue[i] < A_EF | | B_size[i] != A_size_gal):
            del B_IDs[i]  # could also remove by value using B_IDs.remove(i)

        # if fuel type = electricity
        B_annOpCost[i] = (electricity_use / B_EFvalue[i]) * electricity_charge * 365
        # else if fuel type = natural gas
        # B_annOpCost[i] = (naturalGas_use / B_EFvalue[i]) * naturalGas_charge * 365

        B_annCostSavings[i] = B_annOpCost[i] - A_annOpCost

        B_paybackPer[i] = B_purchaseCost[i] / B_annCostSavings[i]

    # set focus on the city_field box
    city_field.focus_set()

    output(B_annCostSavings,B_paybackPer, B_IDs)

    # ADD NPV, PERHAPS DISCOUNT RATE INPUT


# Output to bring up results window
# Pass to output all the values calculated above
def output(B_CostSavings, B_payback, recommendationIDs):
    # Window 2 setup
    window2 = Tk()
    window2.configure(background='light grey')  # set the background colour of GUI window
    window2.title("Water Heater Results")  # set the title of GUI window
    window2.geometry("560x160")  # set the configuration of GUI window

    """
    # Load and show an image with Pillow
    from PIL import Image

    # Load Heater Heater Setup Image
    img = Image.open('conventional_heater.jpg')
    img.show()
    """

    # create label for spacing
    spacing_window2 = Label(window2, text=" ", bg="light grey")

    # Headers
    # .grid() is used for placing
    heading_window2 = Label(window2, text="Output Form", bg="light grey", font='Helvetica 13 bold')
    heading_window2.grid(row=2, column=0, ipadx="10")

    # Manufacturer Column
    manufacturer_window2 = Label(window2, text="Manufacturer", bg="light grey")
    manufacturer_window2.grid(row=9, column=0)

    # Heater Type Column
    type_window2 = Label(window2, text="Heater Type", bg="light grey")
    type_window2.grid(row=9, column=1, ipadx="10")

    # Size Column
    size_window2 = Label(window2, text="Size (Gallons)", bg="light grey")
    size_window2.grid(row=9, column=2, ipadx="10")

    # EF Column
    ef_window2 = Label(window2, text="Energy Factor (EF)", bg="light grey")
    ef_window2.grid(row=9, column=3, ipadx="10")

    # Purchase Cost Column
    purch_window2 = Label(window2, text="Purchase and Installation Cost ($)", bg="light grey")
    purch_window2.grid(row=9, column=4, ipadx="10")

    # Cost Savings Column
    cost_savings_window2 = Label(window2, text="Cost Savings per Year ($)", bg="light grey")
    cost_savings_window2.grid(row=9, column=5, ipadx="10")

    # Payback Period Column
    payback_window2 = Label(window2, text="Payback Period/Years", bg="light grey")
    payback_window2.grid(row=9, column=6, ipadx="10")

    # Energy Savings Column
        # Inherently this module only recommends heaters with a higher EF value.
        # A certain amount of hot water per day requires a certain amount of energy (see electricity_use variable)
        # What will change in upgrading to a heater with a better EF is the annual operating cost
    # kWh_saved_window2 = Label(window2, text="Annual kWh savings", bg="light grey")
    # kWh_saved_window2.grid(row=9, column=7, ipadx="10")

    row=9
    for val in recommendationIDs:  # these are the IDs of the qualifying recommendations.
        manufacturer_window2_field = Label(window2, text=B_manufacturer[val], bg="light grey")
        manufacturer_window2_field.grid(row=row, column=0)

        type_window2_field = Label(window2, text=B_type[val], bg="light grey")
        type_window2_field.grid(row=row, column=1, ipadx="10")

        size_window2_field = Label(window2, text=f"{B_size[val]:.0f}", bg="light grey")
        size_window2_field.grid(row=row, column=2, ipadx="10")

        ef_window2_field = Label(window2, text=f"{B_EFvalue[val]:.0f}", bg="light grey")
        ef_window2_field.grid(row=row, column=3, ipadx="10")

        purch_window2_field = Label(window2, text=f"{B_purchaseCost[val]:.0f}", bg="light grey")
        purch_window2_field.grid(row=row, column=4, ipadx="10")

        cost_savings_window2_field = Label(window2, text=f"{B_CostSavings[val]:.0f}", bg="light grey")
        cost_savings_window2_field.grid(row=row, column=5, ipadx="10")

        payback_window2 = Label(window2, text=f"{B_payback[val]:.0f}", bg="light grey")
        payback_window2.grid(row=row, column=6, ipadx="10")

        #kWh_saved_window2_field = Label(window2, text="Annual kWh savings", bg="light grey")
        #kWh_saved_window2_field.grid(row=row, column=7, ipadx="10")

        row = row+1


# Driver code
if __name__ == "__main__":
    # window 1 setup
    window1 = Tk()
    window1.configure(background='light grey')  # set the background colour of GUI window
    window1.title("Water Heater Inputs")  # set the title of GUI window
    window1.geometry("560x160")  # set the configuration of GUI window

    # Labels
    # Grid method is used for placing the widgets at respective positions in table like structure.
    # create a text entry box for typing the information
    # bind method of widget is used for the binding the function with the events
    #               whenever the enter key is pressed then call the focus1 function
    # Grid method is used for placing the widgets at respective positions in table like structure.

    #Headings
    heading = Label(window1, text="Input Form", bg="light grey", font='Helvetica 13 bold')
    heading.grid(row=0, column=1)

    city = Label(window1, text="City", bg="light grey")
    city.grid(row=1, column=0)
    city_field = Entry(window1)
    city_field.bind("<Return>", focus1)
    city_field.grid(row=1, column=1, ipadx="100")

    energy_metrics_heading = Label(window1, text="Energy Metrics", bg="light grey", font='Helvetica 9 bold')
    energy_metrics_heading.grid(row=2, column=1)

    heater_details_heading = Label(window1, text="Heater Details", bg="light grey",font='Helvetica 9 bold')

    # Heater Configuration and Fuel Type Row
    heater_type = Label(window1, text="Heater Configuration and Fuel Type", bg="light grey")
    heater_type.grid(row=3, column=0)
    heater_type_field = StringVar(window1)
    heater_type_field.set(heater_type_options[0])
    htype = OptionMenu(window1, heater_type_field, *heater_type_options)  # drop down selection
    htype.config(width=13, font=('Helvetica', 8))
    htype.bind("<Return>", focus1)
    htype.grid(row=3, column=1, ipadx="100")

    # Heater Size Row
    heater_size = Label(window1, text="Heater Size (Gal) or L??", bg="light grey")
    heater_size.grid(row=4, column=0)
    heater_size_field = Entry(window1)
    heater_size_field.bind("<Return>", focus2)
    heater_size_field.grid(row=4, column=1, ipadx="100")

    # Heater EF Row
    heater_type = Label(window1, text="Heater Energy Factor (EF)", bg="light grey")
    heater_type.grid(row=5, column=0)
    heater_type_field = Entry(window1)
    heater_type_field.bind("<Return>", focus3)
    heater_type_field.grid(row=5, column=1, ipadx="100")

    # Building Type Row
    building_type = Label(window1, text="Building Type", bg="light grey")
    building_type.grid(row=6, column=0)
    building_type_field = Entry(window1)
    building_type_field.bind("<Return>", focus4)
    building_type_field.grid(row=6, column=1, ipadx="100")

    # Number of Occupants Row
    building_type = Label(window1, text="Number of Occupants", bg="light grey")
    building_type.grid(row=7, column=0)
    building_type_field = Entry(window1)
    building_type_field.bind("<Return>", focus5)
    building_type_field.grid(row=7, column=1, ipadx="100")

    # create a Submit Button and place into the window1 window to call evaluate()
    submit = Button(window1, text="Submit", fg="Black",
                    bg="grey", command=lambda: [f() for f in [evaluate]])
    submit.grid(row=20, column=1)

    # start the GUI
    window1.mainloop()