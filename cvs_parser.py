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


def get_weather_data(data_set):
  levels = 0
  for key in weather_data_set.keys():
    if (isinstance(weather_data_set[key], dict)):
      levels += 1
      print('level', levels,  weather_data_set[key])
      next_weather_data_set = weather_data_set[key]

    for key in next_weather_data_set.keys():
      if(isinstance(next_weather_data_set[key], dict)):
        levels += 1
        print('level', levels, next_weather_data_set[key])
        final_weather_data_set = next_weather_data_set[key]

        for key in final_weather_data_set.keys():
          if (isinstance(final_weather_data_set[key], dict)):
            levels += 1
            print('level', levels, final_weather_data_set[key])

  print('Number of data levels', levels)

get_weather_data(weather_data_set)
