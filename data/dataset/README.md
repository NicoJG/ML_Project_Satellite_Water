# Dataset Specifications

A dataset containing random satellite images in Europe with a mask of water in these satellite images.

## Contents  

| Path | Description |
|------|-------------|
| images/satellite/ | Satellite Images from Mapbox of a specific Tile |
| images/mask/ | Water Mask Images from a Custom Mapbox Style of the same Tile |
| samples.csv | Tabular Data containing extra information about every Image Pair |

## samples.csv

| Column Name | Description |
|-------------|-------------|
| id | A specific ID that corresponds to the ID's of one Point in the dataset_metadata/points.csv |
| tile_x | Tile x-Coordinate |
| tile_y | Tile y-Coordinate |
| tile_z | Tile z-Coordinate (Zoom) |
| lon | Longitude of the Center of the Tile |
| lat | Latitude of the Center of the Tile |
| country | Country Name (in English) to which the Center of the Tile belongs to |
| geometry | Polygon of the Bounding Box of the Tile in Geodetic Coordinates |

## Images  

- Resolution: 256x256 pixel
- Uniformly distributed locations on european land
- Only selected images where it's likely that water is inside the Tile