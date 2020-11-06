#SAP DevelopmentChallange solution, written by Vladeta Stojanovic (vladeta_stojanovic@yahoo.co.uk)
#Version: 01_28082020
#License: MIT 

import sys
import argparse
from emissions import VehicleEmissions

#Important note: ArgumentParser converts any "-" to "_"
ap = argparse.ArgumentParser()
ap.add_argument("--distance", "-dist", help = "Total distance travelled")
ap.add_argument("--unit-of-distance", "-unit-dist", help = "Unit of distance: kilometers (default) or meters")
ap.add_argument("--transportation-method", "-tran-mthd", help = "Type of vehicle used for calculation")
ap.add_argument("--output", "-out", help = "Output of emissions in either kilograms or grams (default)")
args = vars(ap.parse_args())

#Get distance
if (args["distance"] == None):
  sys.exit("No input distance given! Exiting...")
else:
  input_distance = float(args["distance"])

#Get distance unit
if (args["unit_of_distance"] == None):
  print("No unit of distance given, using KM by default")
  distance_unit = "km"
else:
  distance_unit = args["unit_of_distance"]

#Get vehcile type
if (args["transportation_method"] == None):
  sys.exit("No vehicle type given! Exiting...")
else:
  vehicle_type = args["transportation_method"] #one more name validity check is performed internally by the vehicle class

#Get output (optional)
output = args["output"]

#Global variables and parsing conditions
if (distance_unit == "m"):
  input_distance = input_distance / 1000.0

#Create instance of vehicle object and calculate the emissions 
vehicle = VehicleEmissions(vehicle_type)
vehicle.CalculateEmission(input_distance) 

outputEmission = 0

if (output == "g"):
  outputEmission = vehicle.GetEmissionGrams()
  print("Your trip caused " + str(outputEmission) + "g of CO2-equivalent.")
elif (output == "kg"):
  outputEmission = vehicle.GetEmmisionKG()
  print("Your trip caused " + str(outputEmission) + "kg of CO2-equivalent.")
elif (output == None):
  outputEmission = vehicle.GetEmmisionKG()
  print("Your trip caused " + str(outputEmission) + "kg of CO2-equivalent.")