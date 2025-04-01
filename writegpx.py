# This program converts a csv file of coordinate pairs into a gpx file

import pandas as pd


loc = input("Enter location: ")
df = pd.read_csv(loc + ".csv")

XML_H = r"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>"""
GPX_H = r"""<gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="User"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">"""

GPX_T = "</gpx>"



f = open(loc+".gpx", "w")

f.write(XML_H + "\n")
f.write(GPX_H + "\n")
for index, row in df.iterrows():
    f.write(f"<wpt lat=\"{row["y"]}\" lon=\"{row["x"]}\"/>\n")
f.write(GPX_T)

f.close()