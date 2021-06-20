# Dataset Metadata Specifications

Additional information to the dataset, that was collected during the dataset creation.

# Vector Tiles

In `vector_tiles` many Mapbox Vector Tiles (.mvt files) are saved, that are used to get additional information about a certain Tile.  
Used while the selection of tiles which should go into the dataset based on that water content of the tile at a zoomed out resolution. (e.g. Vector Tile Zoom = 10 and Image Tile Zoom = 15)

# points.csv

| Column Name | Description |
| ----------- | ----------- |
| batch_id | ID corresponding to the batch this point was drawn in |
| id | unique ID of each point (just counting up) |
| geometry | shapely Point containing uniformly distributed random coordinates in the european region |
| in_eu | if the point is on european land based on the 110m natural earth countries dataset |
| country | to which country (in English) the coordinates belong to (based on the same NE dataset) |
| tile_x | x coordinate of the Tile the Point belongs |
| tile_y | y coordinate of the Tile the Point belongs |
| tile_z | z coordinate of the Tile the Point belongs |
| new_tile | is the tile already in the dataset, at the time of drawing this point? |
| outer_tile_x | x coordinate of the Tile the Point belongs to but at a zoomed out resolution for downloading the corresponding Vector Tile |
| outer_tile_y | y coordinate of the Tile the Point belongs to but at a zoomed out resolution for downloading the corresponding Vector Tile |
| outer_tile_z | z coordinate of the Tile the Point belongs to but at a zoomed out resolution for downloading the corresponding Vector Tile |
| accepted_water | whether the Tile was accepted based on checking if water is in the Tile (at zoomed out resolution) |