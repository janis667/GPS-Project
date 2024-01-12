import requests
import overpy
from data_taxi1 import *
from data_taxi2 import *


# This program call data_taxi functions who give data that we want on certain cars of the fleet 
# in order to give recommendations

# Exemple : Test get_taxi1_data with the values
#lat, lon, radius, amenity = 48.8599, 2.2974, 500, 'library'


# Exemple : Test get_route_taxi2 with the values
#start_lon, start_lat = -1.543579, 47.2087  
#end_lon, end_lat = -1.1872, 47.3760


# The suite of the script would be the recommandation depending on the data we get from the data_taxi files and their functions.