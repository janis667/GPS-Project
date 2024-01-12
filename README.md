What does this project consists of ?

The aim of a project like this is to retrieve the car's position in real time,
as well as its specific characteristics such as fuel consumption,
routes taken and information on the environment around the vehicle.
The technology I found to receive requests from a map full of datas is OpenStreetMap and its Overpass API.
However, with the OpenStreetMap mapping tool and Overpass,
we can retrieve all kinds of data on places around the world but not really in real time like tracking a moving car.
So for 3 given fictive vehicles from a taxi fleet, with their own travel, we're going to retrieve data from any number of stations,
locations,parkings, zones and roads. 
Once the data has been retrieved, we'll organize it into figures and recommendations to analyze this travel


/!\ In data_taxi2, the function get_route_taxi2 doesn't give the graphic route because of a problem of convertion to float of
the "route" variable which contains the data. I tried to convert it all but the problem remains.


Conclusion : The purpose of the main file : fleet_management.py which calls the data_taxi functions is to give recommendation 
depending on the data we get from the data_taxi files and their functions.
This part of the project is incomplete because of the the mass of complex information
that my functions send back, even though they are simple. I don't know how to extract the important ones to organize a recommendation.
