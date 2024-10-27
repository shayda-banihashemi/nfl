import pandas as pd

weather_data_set = {
  'location': {
    'name': 'Baltimore',
    'region': 'Maryland',
    'country': 'UnitedStatesofAmerica',
    'lat': 39.29,
    'lon': -76.61,
    'tz_id': 'America/New_York',
    'localtime_epoch': 1725403815,
    'localtime': '2024-09-0318: 50'
  },
  'current': {
    'last_updated_epoch': 1725403500,
    'last_updated': '2024-09-0318: 45',
    'temp_c': 25.6,
    'temp_f': 78.1,
    'is_day': 1,
    'condition': {
      'text': 'Sunny',
      'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png',
      'code': 1000,
      'zipcode': {
        'code one': '21234',
        'code two': '21087',
      }
    },
    'wind_mph': 2.2,
    'wind_kph': 3.6,
    'wind_degree': 48,
    'wind_dir': 'NE',
    'pressure_mb': 1026.0,
    'pressure_in': 30.3,
    'precip_mm': 0.0,
    'precip_in': 0.0,
    'humidity': 29,
    'cloud': 0,
    'feelslike_c': 25.1,
    'feelslike_f': 77.2,
    'windchill_c': 22.8,
    'windchill_f': 73.0,
    'heatindex_c': 23.8,
    'heatindex_f': 74.8,
    'dewpoint_c': 4.9,
    'dewpoint_f': 40.8,
    'vis_km': 10.0,
    'vis_miles': 6.0,
    'uv': 6.0,
    'gust_mph': 8.2,
    'gust_kph': 13.2
  }
}

"""def parse_json(data):
    keys = list(data.keys())
    for key in keys:
      if isinstance(data[key], dict):
        print('1:', key, ':', data[key])
        print('2: ', data[key])
        parse_json((data[key]))"""


def parse_json(data):
  if not isinstance(data, dict):
    print('3:', data)
    return data
  keys = list(data.keys())
  print('1:', keys)
  # print(f"{len(data)=}")
  for key in keys:
    for i in data.items():
      print(key, ' - ', data[key], i)
      parse_json((data[key]))


if __name__ == '__main__':
   a = parse_json(weather_data_set)


#1 how do you easily join dicts together?
#2 what is the skip condition?
#3 what is the stop condition? when there are no more keys

