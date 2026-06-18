from urllib.request import urlretrieve


# This script downloads the most recent versions of the flat files used for importing data into the database.
old_voyage_url = 'https://docs.google.com/spreadsheets/d/1uRJVpvtj_NJBfJsMan-ihiUcVEqTWKW91parzWwmynk/export?format=csv'
file_path = './flat_files/paradise_voyage_raw_data.csv'
urlretrieve(old_voyage_url, file_path)
print('\nDownloaded paradise_voyage_raw_data to: ' + file_path)

# The expanded_paradise_voyage_raw_data file includes the same data as paradise_voyage_raw_data, but with additional columns for visit number and housing distance. These columns were added after the initial import, so they are not included in the original file.
updated_voyage_url = 'https://docs.google.com/spreadsheets/d/1RWUVlGamiYoALi72beJZuxogaPo3lccTQ9-8LRI9CWg/export?format=csv'
file_path = './flat_files/expanded_paradise_voyage_raw_data.csv'
urlretrieve(updated_voyage_url, file_path)
print('\nDownloaded expanded_paradise_voyage_raw_data to: ' + file_path)

# The tour_housing_calculations file includes the housing distance calculations for each visit, which were added after the initial import. This file is used to update the housing_distance column in the visit table.
tour_housing_calculations_url = 'https://docs.google.com/spreadsheets/d/1wSQfZWoQlhgPkEVhqQ4PfPkcpRF2Ki4laMKu9SjFYys/export?format=csv'
file_path = './flat_files/tour_housing_calculations.csv'
urlretrieve(tour_housing_calculations_url, file_path)
print('\nDownloaded tour_housing_calculations to: ' + file_path)

# The us_state_capitols_with_coordinates file includes the names, states, and coordinates of the US state capitols, which are used to populate the location table and calculate housing distances for visits to state capitols.
us_capitol_url = 'https://docs.google.com/spreadsheets/d/12XHAwOnqXOWEEXfd3qcRA99beSRAkqX6fKjLSLgbGwc/export?format=csv'
file_path = './flat_files/us_state_capitols_with_coordinates.csv'
urlretrieve(us_capitol_url, file_path)
print('\nDownloaded us_state_capitols_with_coordinates to: ' + file_path)

# The canadian_legislative_buildings file includes the names, provinces, and coordinates of the Canadian legislative buildings, which are used to populate the location table and calculate housing distances for visits to Canadian legislative buildings.
canadian_legislative_buildings_url = 'https://docs.google.com/spreadsheets/d/1acjE8XfJe8qYaIU5C49JMOW11MuUzmUhsV1x74qKEtU/export?format=csv'
file_path = './flat_files/canadian_legislative_buildings.csv'
urlretrieve(canadian_legislative_buildings_url, file_path)
print('\nDownloaded canadian_legislative_buildings to: ' + file_path)

# The trip_dates file includes the dates of each visit, which are used to populate the date column in the visit table and calculate the visit number for each visit.
trip_dates_url = 'https://docs.google.com/spreadsheets/d/1Ws02OpUDF6pkYNBhZ6drc0dPfRNTnIiVs7XOIq7Tqlw/export?format=csv'
file_path = './flat_files/trip_dates.csv'
urlretrieve(trip_dates_url, file_path)
print('\nDownloaded trip_dates to: ' + file_path)

# The patagonia_visit_data file includes the names, locations, and coordinates of the places visited in Patagonia, which are used to populate the location table and calculate housing distances for visits to Patagonia.
patagonia_url = 'https://docs.google.com/spreadsheets/d/176hkB3rx-bl4Lx2OD1bMPDXBW49-_BGQDtJWbYtE7II/export?format=csv'
file_path = './flat_files/patagonia_visit_data.csv'
urlretrieve(patagonia_url, file_path)
print('\nDownloaded patagonia_visit_data to: ' + file_path)

quaker_meeting_houses_url = 'https://docs.google.com/spreadsheets/d/1-kFSMoJqrOZbNR61nNoQsu_cWf6zj8n2yxkZ3m-LR5s/export?format=csv'
file_path = './flat_files/quaker_meeting_houses.csv'
urlretrieve(quaker_meeting_houses_url, file_path)
print('\nDownloaded quaker_meeting_houses to: ' + file_path)