from .commandList import commandList
from .serialInterface import SerialInterface


class Laser:
    def __init__(self, com):
        self.com = com

    def laserOn(self):
        self.com.write(commandList.COMMAND_LASER_ON)

    def laserOff(self):
        self.com.write(commandList.COMMAND_LASER_OFF)

    def singleMeasurement(self):
        self.com.write(commandList.COMMAND_SINGLE_MEASUREMENT)

    def contiMeasurement(self):
        self.com.write(commandList.COMMAND_CONTINUOS_MEASUREMENT)

    def stopMeasurement(self):
        self.com.write(commandList.COMMAND_STOP_MEASUREMENT)

    def getData(self, length):
        result = self.com.read(length)
        result = result.decode("ascii")

        measurement = ""
        address = ""
        command = ""
        parameter = ""
        crc = ""
        for i in range(0, len(result)):
            if i in range(1, 3):
                address += result[i]
            elif i in range(3, 5):
                command += result[i]
            elif i in range(5, 9):
                parameter += result[i]
            elif i in range(9, 13):
                measurement += result[i]
            elif i in range(13, 17):
                crc += result[i]

        return result, measurement, address, command, parameter, crc

    def getDistance(self):
        result, measurement, address, command, parameter, crc = self.getData(19)

        return int(measurement, 16)
