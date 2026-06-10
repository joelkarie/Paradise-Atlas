from urllib.request import urlretrieve


old_voyage_url = 'https://docs.google.com/spreadsheets/d/1uRJVpvtj_NJBfJsMan-ihiUcVEqTWKW91parzWwmynk/export?format=csv'
file_path = './flat_files/paradise_voyage_raw_data.csv'

urlretrieve(old_voyage_url, file_path)
print('\nDownloaded paradise_voyage_raw_data to: ' + file_path)

updated_voyage_url = 'https://docs.google.com/spreadsheets/d/1uRJVpvtj_NJBfJsMan-ihiUcVEqTWKW91parzWwmynk/export?format=csv'
file_path = './flat_files/expanded_paradise_voyage_raw_data.csv'

urlretrieve(updated_voyage_url, file_path)
print('\nDownloaded expanded_paradise_voyage_raw_data to: ' + file_path)

tour_housing_calculations_url = 'https://docs.google.com/spreadsheets/d/1wSQfZWoQlhgPkEVhqQ4PfPkcpRF2Ki4laMKu9SjFYys/export?format=csv'
file_path = './flat_files/tour_housing_calculations.csv'

urlretrieve(tour_housing_calculations_url, file_path)
print('\nDownloaded tour_housing_calculations to: ' + file_path)

us_capitol_url = 'https://docs.google.com/spreadsheets/d/12XHAwOnqXOWEEXfd3qcRA99beSRAkqX6fKjLSLgbGwc/export?format=csv'
file_path = './flat_files/us_state_capitols_with_coordinates.csv'

urlretrieve(us_capitol_url, file_path)
print('\nDownloaded us_state_capitols_with_coordinates to: ' + file_path)

canadian_legislative_buildings_url = 'https://docs.google.com/spreadsheets/d/1acjE8XfJe8qYaIU5C49JMOW11MuUzmUhsV1x74qKEtU/export?format=csv'
file_path = './flat_files/canadian_legislative_buildings.csv'

urlretrieve(canadian_legislative_buildings_url, file_path)
print('\nDownloaded canadian_legislative_buildings to: ' + file_path)