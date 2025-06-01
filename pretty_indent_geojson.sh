#!/bin/bash

# Script to pretty print and re-indent a geojson file
# Usage: ./pretty_indent_geojson.sh <filename>

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <geojson filename>"
  exit 1
fi

INPUT_FILE="$1"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
  echo "File '$INPUT_FILE' not found!"
  exit 2
fi

# Generate output file name with 'updated' suffix
EXTENSION="${INPUT_FILE##*.}"
BASENAME="${INPUT_FILE%.*}"
OUTPUT_FILE="${BASENAME}_updated.${EXTENSION}"

# Use jq to pretty print and indent JSON
jq '.' "$INPUT_FILE" > "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
  echo "Successfully created pretty-printed file: $OUTPUT_FILE"
else
  echo "Failed to process the file. Make sure jq is installed and input is valid JSON."
  exit 3
fi
