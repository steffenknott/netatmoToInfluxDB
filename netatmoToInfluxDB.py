#!/usr/bin/python3
# encoding=utf-8

# Steffen Knott, 2018-04-30
# @steffenknott

import lnetatmo
from influxdb import InfluxDBClient
from os.path import expanduser, exists
import json

influxcred = {
    "Host" : "",
    "Port" : 8086,
    "Username" : "",
    "Password" : "",
    "Database" : "",
    "Measurement" : ""
}
influxcred_file = expanduser("~/.influxdb.credentials")

if exists(influxcred_file) :
    with open(influxcred_file, "r") as f:
        influxcred.update({k:v for k,v in json.loads(f.read()).items()})

def create_json_stub (measurementName, tagkey, tagvalue):
    json_item = {}
    json_item.update({"measurement": measurementName})
    json_item.update({"tags": {tagkey: tagvalue} })
    json_item.update({"fields": {} })
    return json_item

# Connect to InfluxDB
client = InfluxDBClient(influxcred['Host'], influxcred['Port'], influxcred['Username'], influxcred['Password'], influxcred['Database'])

# Connect to netatmo
authorization = lnetatmo.ClientAuth()
weatherData = lnetatmo.WeatherStationData(authorization)

# Preparing JSON for InfluxDB request
json_body = []

# Iterate over stations
for station in weatherData.stations:
    # print (station)
    json_item = create_json_stub (influxcred['Measurement'], "station", station)
    for sensor in weatherData.stationById(station)['data_type']:
        json_item['fields'].update({sensor: weatherData.stationById(station)['dashboard_data'][sensor] })
        # print (sensor)
    # print (json_item)
    json_body.append(json_item)

# Iterate over modules (whatever stations they are connected to)
for module in weatherData.modules:
    # print(module)
    json_item = create_json_stub (influxcred['Measurement'], "module", module)
    for sensor in weatherData.moduleById(module)['data_type']:
        json_item['fields'].update({sensor: weatherData.moduleById(module)['dashboard_data'][sensor] })
        # print (sensor)
    # print (json_item)
    json_body.append(json_item)

print("GENERATED JSON: {0}".format(json_body))
client.write_points(json_body)
