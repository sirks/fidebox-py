#!/usr/bin/python

import serial


def open():
    global ser
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=115200
    )

    if not ser.is_open:
        ser.open()


def write(serailData):
    ser.write(bytes(serailData, encoding="ascii"))