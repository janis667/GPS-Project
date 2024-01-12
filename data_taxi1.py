import requests
import overpy

# global variables
lat, lon, radius, amenity = 0.0000, 0.0000, 0, '?????'

#Function which gets the data around the taxi1

def get_taxi1_data(lat, lon,radius,amenity):
    
    # amenity represents the places like (school, restaurant,hospital, parking, library, place of workship)
    # lat is for latitude
    # lon is for longitude
    # radius is for the sector of search in meter

      # Exemple : you want data from parkings 500m around the Eiffel Tower
    # lat, lon, radius, amenity = 48.8599, 2.2974, 500, 'parking'

     # Ask to the user to enter the values
    print()
    print()
    print("Enter the followings informations about your location (latitude,longitude,radius,amenity)")
    print("latitude and longitude take 4 decimal places (ex: lat =50.1111, lon= 3.9999)")
    print("more radius means more results depending on location")

    
    lat = float(input("Enter the latitude : "))
    lon = float(input("Enter the longitude : "))
    radius = float(input("Enter the radius (in meters) : "))
    amenity = input("Enter the type of facility (amenity) : ")
           
    overpass_url = "https://overpass-api.de/api/interpreter"
    # Nodes
    nodes_query = f"""
        [out:json];
        (
          node(around:{radius},{lat},{lon})["amenity"="{amenity}"];
        );
        
        (._;>;);    
        out body;
        out skel qt;
    """
    # (._;>;); is a filter used to get the complete result of the data, the next version
    # out body; is to mark the end of node, way and relation closes
    #  out skel qt; is a syntax to get a skeleton of the objets and to reduce the data
    
    # Ways
    ways_query = f"""
        [out:json];
        (
          way(around:{radius},{lat},{lon})["amenity"="{amenity}"];
        );
        (._;>;);
        out body;
        out skel qt;
    """

    # Relations
    relations_query = f"""
        [out:json];
        (
          relation(around:{radius},{lat},{lon})["amenity"="{amenity}"];
        );
        (._;>;);
        out body;
        out skel qt;
    """

    # Perform queries and return results
    nodes_result = requests.get(overpass_url, params={"data": nodes_query}).json()
    ways_result = requests.get(overpass_url, params={"data": ways_query}).json()
    relations_result = requests.get(overpass_url, params={"data": relations_query}).json()

   # return nodes_result, ways_result, relations_result

    #print("Nodes:")
    for node in nodes_result['elements']:
        print(f"ID: {node['id']}, Type: {node['type']}, Tags: {node.get('tags', {})}")

    #print("\nRelations:")
    for relation in relations_result['elements']:
        print(f"ID: {relation['id']}, Type: {relation['type']}, Tags: {relation.get('tags', {})}")

    #print("\nWays:")
    for way in ways_result['elements']:
        print(f"ID: {way['id']}, Type: {way['type']}, Tags: {way.get('tags', {})}")

""""
   # Test of the function
if __name__ == "__main__":
    taxi1_data = get_taxi1_data(lat, lon, radius, amenity)

"""
# Call of the function

taxi1_data = get_taxi1_data(lat, lon, radius, amenity)
   