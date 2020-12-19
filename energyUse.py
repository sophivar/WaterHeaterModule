from waterHeaterModule import *

# Determine user's total daily, monthly and annual energy use for hot water.
# In both electricity (kWh) and natural gas (therm) forms.

# Define fixed values
LtoGal = 3.78541 # 1 gal = 3.7 L

# Define some look-up tables
building_type_options = ["House or Flat", "Offices", "School, boarding", "School, day",
                         "Hostel", "Hotel", "Hospital, general", "Hospital, mental", "Factory"]

hotWaterUse_LperOccupant_daily = dict([('House or Flat', 124), ('Offices',22), ('School, boarding', 115),
                           ('School, day', 15), ('Hostel', 90), ('Hotel', 125),
                           ('Hospital, general', 160), ('Hospital, mental', 110), ('Factory', 40)])


# User Inputs:
#building_type =
#numberOfOccupants =
hw_temperature = 120 # degF. this is an assumption. Should discuss whether to be asking user for this value
incoming_hw_temperature = 58 # degF. this is an assumption. Should discuss whether to be asking user for this value
    # i.e. Assume water heaters are heating to 58 degF
    # use as an average temperature -- can change later
    # make additional inputs OR in output make a recommendation to
    # adjust/turn down temperature setting if possible with their heater type

# Estimate total hot water use/production (gal/day) based on these user inputs
hw_use_daily = (hotWaterUse_LperOccupant_daily[building_type] / LtoGal) * numberOfOccupants

# Calculate energy use. Requires:
    # hw_use_daily
    # hw_temperature
    # incoming_hw_temperature

    # research best equation to caluculate this value.

# return a value in therm/day OR in kWh/day