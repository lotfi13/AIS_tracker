# AIS Tracker

> THIS IS MANLY A PROOF OF CONCEPT. IT IS NOT PRODUCTION READY.

> THIS PROJECT USES A HIDDEN API, IT MAY BREAK AT ANY MOMENT.

This Python script makes use of the MarineTraffic API to retrieve positions of vessels and keep record of their position.
This project uses GitHub Actions to automatically run the script on a schedule.

# Setup
 
## Github Action Cron Job (recommended)

Fork this repository and let the github action do the hard work for you.

## Locally
Install the requests library by running `pip install requests` and then

```python
python main.py
```

# Customization

## Set of vessels

You can customize the set of vessels you want to track by modifying the `ships.json` file. The required field
is the `shipid` from MarineTraffic. The other fields are only here for readability.

## Set of variables

You can customize the script by altering the `vars_to_keep` in `main.py` to include or exclude different variables from the API response. By default
only longitude and latitude are saved.
As it is a hidden API, no documentation is given. Here is a full response sample that you can use:

```python
{'isVesselInRange': True,
 'hasNewerSatellitePosition': False,
 'isEligibleToRequestInmarsat': False,
 'areaName': 'Caribbean Sea',
 'areaCode': 'CARIBS',
 'course': 6,
 'lastPos': 1674382124,
 'timezoneOffset': -240,
 'lat': 18.4596,
 'lon': -66.10029,
 'shipStatus': 'Moored',
 'speed': 0.1,
 'stationId': '18402',
 'stationName': 'San Juan Bay Pilots',
 'sourceType': 'terrestrial',
 'stationOperator': 'San Juan Bay Pilots',
 'windAngle': 106,
 'windSpeed': 11,
 'windTemperature': 23,
 'departurePort': {'id': '11213',
  'name': 'ROAD TOWN',
  'code': 'RAD',
  'timestamp': 1674252240,
  'offset': -240,
  'timestampLabel': 'ATD',
  'countryCode': 'VG'},
 'arrivalPort': {'id': '1023',
  'name': 'SAN JUAN',
  'code': 'SJU',
  'timestamp': 1674376920,
  'offset': -240,
  'timestampLabel': 'ATA',
  'countryCode': 'PR'},
 'draughtReported': 8.9,
 'currentPortId': 1023,
 'currentPortName': 'SAN JUAN'}
```

## Schedule
You can edit the schedule field in the `on` section of the workflow file. The schedule is set to run the script twice a day by default.
Example:
```yml
  schedule:
    - cron: "0 0 * * *" # This will run every day at midnight
```
