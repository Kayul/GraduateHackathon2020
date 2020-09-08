# Code written by Kyle
print("Program starting...")

import json
import pathlib
import os
import flask
from flask import Flask, request, render_template
from flask import jsonify

from datetime import datetime


# Location class used to store longitude and latitude
# Can return a formatted string
class Location:
    def __init__(self, longitude=0, latitude=0):
        self.lon = longitude
        self.lat = latitude

    def getLongLatAsString(self):
        return "[{0}, {1}]".format(self.lon, self.lat)

    def getLong(self):
        return self.lon

    def getLat(self):
        return self.lat


# Class used to store all device data
class Device:
    def __init__(self, deviceID, location, pollutionLevel, uploadTime):
        self.location = location
        self.deviceID = deviceID
        self.pollutionLevel = pollutionLevel
        self.uploadTime = uploadTime
        print("New Device Found.")

    def getDataAsString(self):
        return "{0} Pollution: {1} | Device ID: {2}".format(self.location.getLongLatAsString(), self.pollutionLevel, self.deviceID)

    def getPollution(self):
        return self.pollutionLevel

    def getDeviceID(self):
        return self.deviceID

    def getUploadTime(self):
        # TODO: convert to datetime
        return self.uploadTime

    def serialize(self):
        data = {
            "DeviceID": self.deviceID,
            "PollutionLevel": self.pollutionLevel,
            "TimeStamp": self.uploadTime,
            "Longitude": self.location.getLong(),
            "Latitude": self.location.getLat()
        }
        return data


deviceList = []

# Read from JSON file and input database results here
# will iterate through and create new device objects
def loadDevices(databaseQueryResult):
    for device in databaseQueryResult:
        # TODO: Convert json timestamp to datetime object
        deviceList.append(Device(databaseQueryResult.deviceID,
                                databaseQueryResult.location,
                                databaseQueryResult.pollutionLevel,
                                databaseQueryResult.uploadTime))
    return 1

# Function used to return a list of device IDs based on the
# amount of pollution recorded by the device
# @param value      The general value to look for
# @param precision  The range + - of value to find
def getDevicesFromPollution(value, precision):
    tempDevices = []

    for device in deviceList:
        pollutionValue = device.getPollution()
        if pollutionValue >= (value-precision) and pollutionValue <= (value+precision):
            tempDevices.append(device)

    return tempDevices

# Function used to return a Device object based on a deviceID
# @param deviceID    The unique device ID to get
def getDeviceFromID(deviceID):
    for device in deviceList:
        if deviceID == device.getDeviceID():
            return device
    
    print("No device found with that ID.")
    return None

# Function used to get a list of Device objects based
# on a range from a stated location
def getDeviceFromLocationRange(location, range):
    lon = location.getLong()
    lat = location.getLat()

    # TODO: FINISH

    return None

# DEBUGGING, TEST DEVICES
deviceList.append(Device(15, Location(2, 5), 12, 555))
deviceList.append(Device(16, Location(1, 8), 13, 555))
deviceList.append(Device(17, Location(4, 9), 14, 555))
deviceList.append(Device(18, Location(5, 5), 15, 555))
deviceList.append(Device(19, Location(6, 63), 30, 555))
# print(device.getDataAsString())

# DEBUG: Getting devices based on pollutors
print("Pollutors: {0}".format(len(getDevicesFromPollution(13, 1))))

# DEBUG: Getting a device from a device ID
print("Get Device: {0}".format(getDeviceFromID(16).getDataAsString()))

# DEBUG: Print memory location of each device in the device list
print(deviceList)

data = {

    "uploadTime": "18:36",
    "id": "3",
    "GPS": 3,
    "pollution": 4
}

# API Functionality
p = os.path.dirname(os.path.realpath(__file__))
p = os.path.join(p, "index.html")

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
@app.route("/api")
@app.route("/index", methods=['GET', 'POST', 'PUT'])

def getAllData():
    device = getDeviceFromID(16)
    print(device.serialize())
    return jsonify(device.serialize())

app.run()
