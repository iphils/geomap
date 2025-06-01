import json
import sys
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from shapely.geometry import shape


def load_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def polygon_to_gpx(polygon_coords, output_file):
    gpx = Element('gpx', version="1.1", creator="GeoJSON2GPX")
    trk = SubElement(gpx, 'trk')
    trkseg = SubElement(trk, 'trkseg')

    # polygon_coords is expected to be [ [ [lon, lat], [lon, lat], ... ] ] or MultiPolygon style
    for linearring in polygon_coords:
        for coord in linearring:
            lon, lat = coord
            trkpt = SubElement(trkseg, 'trkpt', lat=str(lat), lon=str(lon))

    tree = ElementTree(gpx)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


def export_pincode_boundary(pincode, geojson_file, output_gpx_file):
    geojson_data = load_geojson(geojson_file)

    for feature in geojson_data['features']:
        if feature['properties'].get('Pincode') == pincode:
            geometry = feature['geometry']
            geom_type = geometry['type']
            coords = geometry['coordinates']
            if geom_type == 'Polygon':
                polygon_to_gpx(coords, output_gpx_file)
                print(f"Exported GPX for pincode {pincode} to {output_gpx_file}")
                return
            elif geom_type == 'MultiPolygon':
                # Flatten multi polygon into one continuous sequence
                flat_coords = []
                for poly in coords:
                    flat_coords.extend(poly)
                polygon_to_gpx(flat_coords, output_gpx_file)
                print(f"Exported GPX for pincode {pincode} to {output_gpx_file}")
                return
            else:
                print(f"Geometry type {geom_type} not supported for GPX export")
                return
    print(f"Pincode {pincode} not found in GeoJSON data.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 export_pincode_gpx.py <pincode> <geojson_file>")
        sys.exit(1)

    pincode = sys.argv[1]
    geojson_file = sys.argv[2]
    output_gpx_file = f"{pincode}_boundary.gpx"

    export_pincode_boundary(pincode, geojson_file, output_gpx_file)


if __name__ == '__main__':
    main()
    