# netatmoToInfluxDB
This simple tool pushes your netatmo measurements into an [InfluxDB](https://github.com/influxdata/influxdb) instance. I use [Grafana](https://grafana.com/)  to visualize them.

## Requirements

- Python 3 (may work with Python 2 - didn't test it)
- netatmo API Access - you need to register an App on the netatmo website
- [lnetatmo](https://github.com/philippelt/netatmo-api-python) and [influxdb](https://github.com/influxdata/influxdb-python) packages

## Setup

- Place .influxdb.credentials and .netatmo.credentials in your **home directory**. Set proper values.
- If not already installed, install lnetatmo and influxdb (`pip3 install lnetatmo`, `pip3 install influxdb`)

## What the script does

The scripts loads all available stations from the netatmo API. All latest sensor values are written to InfluxDB. Values are tagged with "station" or "module" as tag key and the mac address of the station or module as tag value.

## Run the script

Run the script like `python3 netatmoToInfluxDB.py`. 

You can add the script to your crontab to run it every 5 minutes or so:

`*/5 * * * * /path/to/netatmoToInfluxDB.py >/dev/null 2>&1`

You have to make the script executable first: `chmod +x netatmoToInfluxDB.py`
