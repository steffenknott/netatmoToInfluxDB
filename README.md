# netatmoToInfluxDB
This simple tool pushes your netatmo measurements into an InfluxDB instance.

## Requirements

- Python 3 (may work with Python 2 - didn't test it)
- netatmo API Access - you need to register an App on the netatmo website
- lnetatmo and influxdb packages

## Setup

- Place .influxdb.credentials and .netatmo.credentials in your **home directory**. Set proper values.
- If not already installed, install lnetatmo and influxdb (`pip3 install lnetatmo`, `pip3 install influxdb`)

## What the script does

The scripts loads all available stations from the netatmo API. All available sensor values are written to InfluxDB. Values are tagged with "station" or "module" as tag key and the mac address of the station or module as tag value.
