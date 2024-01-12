import requests
import json
import overpy
import folium
from folium import PolyLine

# global variable
start_lon, start_lat, end_lon, end_lat = 0,0,0,0
#coords test : -1.5490,47.2058;-1.5504,47.2103

# In get_route_taxi2 function, you enter the coords of a starting point and an ending point then the functions calculates datas 
# like distance...
# Then the route is drew on the map 


def get_route_taxi2(start_lon, start_lat, end_lon, end_lat):

    start_lon = float(input("Enter start_lon : "))
    start_lat = float(input("Enter start lat : "))
    end_lon = float(input("Enter end lon : "))
    end_lat = float(input("Enter end lat : "))


    osrm_url = "https://routing.openstreetmap.de/routed-car/route/v1/driving/{},{};{},{}?overview=false&alternatives=true&steps=true".format(
        start_lon, start_lat, end_lon, end_lat
    )
    response = requests.get(osrm_url)
    data = response.json()

    if "code" in data and data["code"] == "Ok":      
        route_geometry = data["routes"][0]#["geometry"]["coordinates"]
        return route_geometry
    else:
        print("Error fetching route:", data)
        return None


route = get_route_taxi2(start_lon, start_lat, end_lon, end_lat)

json_route = json.dumps(route, indent=2)
print(json_route)
if route:
    # Creation of the map with folium
    m = folium.Map(location=[start_lat, start_lon], zoom_start=15)


for item in route:
    try:
        float_value = float(item)
        print(f"Type de {item}: {type(float_value)}")
    except ValueError:
        print(f"Can't convert {item} in float.")

route_float = [[float(coord[1]), float(coord[0])] for coord in route]


    # Add line representing route
folium.PolyLine(locations=route, color="blue", weight=2.5, opacity=1).add_to(m)
folium.PolyLine(route, color="blue", weight=2.5, opacity=1).add_to(m)

    # Add markers for start and finish points
folium.Marker([start_lat, start_lon], popup="Start point").add_to(m)
folium.Marker([end_lat, end_lon], popup="End point").add_to(m)

    # Map display
m.save("map_route.html")


# Call of the function

taxi2_data = get_route_taxi2(start_lon, start_lat, end_lon, end_lat)
