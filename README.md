# Simple scripts to decipher [India's Postal Codes](https://www.data.gov.in/catalog/all-india-pincode-boundary-geo-json)

## Know the pincode from your coordinates

file:

`get_pincode.py`

This script allows you to get the pincode of a location you seek to know the pincode of.

It tells you if your location lies within the polygon boundary of a particular pincode. If not, it tells you which the nearest pincode is.

### example usage

```shell

python3 get_pincode.py <latitude,longitude>

```

## Extract the boundaries of your pincode

file:

`export_pincode_gpx.py`

This script is to export a .gpx file of the pincode boundary you seek.

Once exported, you can use it in [google mymaps](https://www.google.com/maps/about/mymaps/) to visualise the polygon to get a look and feel of the pincode in action!

### esxample usage

```shell

python3 export_pincode_gpx.py 682401 All_India_pincode_Boundary-19312.geojson 

```

## pretty_indent_geojson.sh

This script is to make the geojson file look easy to navigate visually. 
THe default download dump, as you can notice is pretty messy.