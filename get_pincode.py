import sys
import json
from shapely.geometry import shape, Point
from shapely.ops import nearest_points


def load_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_pincode(lat, lon, geojson_data):
    point = Point(lon, lat)  # GeoJSON uses lon,lat order
    closest_pincode = None
    closest_distance = float('inf')

    # Iterate through features to find which polygon contains the point
    for feature in geojson_data['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature['properties']['Pincode'], True
        else:
            # If not contained, check distance to polygon
            nearest_point = nearest_points(polygon, point)[0]
            dist = point.distance(nearest_point)
            if dist < closest_distance:
                closest_distance = dist
                closest_pincode = feature['properties']['Pincode']

    return closest_pincode, False


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 get_pincode.py <latitude,longitude>")
        sys.exit(1)

    lat_lon = sys.argv[1].split(",")
    if len(lat_lon) != 2:
        print("Invalid input format. Use: latitude,longitude")
        sys.exit(1)

    lat = float(lat_lon[0].strip())
    lon = float(lat_lon[1].strip())

    geojson_file = 'All_India_pincode_Boundary-19312.geojson'
    geojson_data = load_geojson(geojson_file)

    pincode, contained = find_pincode(lat, lon, geojson_data)
    if pincode:
        if contained:
            print(f"Location is within pincode area: {pincode}")
        else:
            print(f"Location is outside any boundary. Closest pincode: {pincode}")
    else:
        print("No pincode found for the location.")


if __name__ == '__main__':
    main()
