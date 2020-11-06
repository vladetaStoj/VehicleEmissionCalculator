import sys

class VehicleEmissions:
  def __init__(self, vehicleType):
    self.emission = 0 #Emission is in grams / km by default
    self.co2 = 0
    self.vehicleType = vehicleType
    self.SetupVehicleType()

  def SetupVehicleType(self):
    if (self.vehicleType == "small-diesel-car"):
      self.emission = 142
    elif (self.vehicleType == "small-petrol-car"):
      self.emission = 154
    elif (self.vehicleType == "small-plugin-hybrid-car"):
      self.emission = 50
    elif (self.vehicleType == "medium-diesel-car"):
      self.emission = 171
    elif (self.vehicleType == "medium-petrol-car"):
      self.emission = 192
    elif (self.vehicleType == "medium-plugin-hybrid-car"):
      self.emission = 110
    elif (self.vehicleType == "medium-electric-car"):
      self.emission = 58
    elif (self.vehicleType == "large-diesel-car"):
      self.emission = 209
    elif (self.vehicleType == "large-petrol-car"):
      self.emission = 282
    elif (self.vehicleType == "large-plugin-hybrid-car"):
      self.emission = 126
    elif (self.vehicleType == "large-electric-car"):
      self.emission = 73
    elif (self.vehicleType == "bus"):
      self.emission = 27
    elif (self.vehicleType == "train"):
      self.emission = 6
    else:
      sys.exit("Invalid vehicle type! Exiting...")

  def CalculateEmission(self, distance):
    if (distance <= 0):
      sys.exit("Distance cannot be 0 or negative! Exiting")
    else:
      self.co2 = self.emission * distance 

  def GetEmissionGrams(self):
    return self.co2

  def GetEmmisionKG(self):
    return self.co2 / 1000.0