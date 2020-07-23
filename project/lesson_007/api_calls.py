from urllib.request import urlopen
import pprint
import json

##############################################################################################

# Vars with target data
api_key = "f57f78b88df782edef2d267985a11166"  # insert your own API key!!!
location = "Barcelona,ES"
units = "metric"

# URL to query
url = r'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'

# Make request
response = urlopen(url.format(location, units, api_key)).read()
data = json.loads(response)

# Print data in output
# pprint.pprint(data)

##############################################################################################
# weather widget

city = data["name"]
temperature_data = data["main"]
temperature = temperature_data["temp"]
high_temp = temperature_data["temp_max"]
low_temp = temperature_data["temp_min"]
conditions = data["weather"][0]["description"]

weather_message = """
    
    Your weather information in {} provided by Smart-ninja Coding Academy
    
    Current temperature ~ {}
    Conditions ~ {}
    High ~ {}
    Low ~ {}

"""

# Widget message
print(weather_message.format(city,
                             temperature,
                             conditions,
                             high_temp,
                             low_temp))
