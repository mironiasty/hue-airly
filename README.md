# hue-airly
Simple script to set hue light based on airly readings for current location

# usage
Create `apikeys.py` that looks more or less like this:
```py
hueuser = "heu_id" # use register.py to obtain key
airlykey = 'airly key' # register on airly

location = {'longitude': 19.123,
            'latitude': 50.123} # your location
```

# add to cron
```cron
*/15 6-9 * * * python3 /home/pi/hue-airly/checkAirly.py
15 9 * * * python3 /home/pi/hue-airly/disable.py
```

It will run every 15 minutes in mornings
