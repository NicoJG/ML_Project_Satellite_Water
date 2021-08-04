RASTER_FORMAT = 'jpg90'
PX_WIDTH = 256

MASK_FORMAT = 'png'
SATELLITE_FORMAT = 'jpg'

Z = 15
Z_OUTER = 10

VECTOR_TILE_EXTENT = 4096

# Bounding Box of our Area of Interest
# It envelopes Europe
# But excludes Russia and Iceland
# from https://boundingbox.klokantech.com/
LON_MIN_FULL, LON_MAX_FULL = -10.49, 40.27
LAT_MIN_FULL, LAT_MAX_FULL = 34.51, 71.20
# Europe without Scandinavia
LON_MIN,LAT_MIN,LON_MAX,LAT_MAX = -10.84,35.97,32.89,59.69

#EXCLUDED_COUNTRIES = ['Iceland','Russia']
EXCLUDED_COUNTRIES = ['Iceland','Russia','Norway','Sweden','Finland']

# defining the optimal ratio of water to land in a tile
WATER_RATIO_MIN = 0.05
WATER_RATIO_MAX = 0.99

# defining the order of columns in csv files
POINTS_DF_COLUMNS = ['batch_id','id','geometry','in_eu','country','tile_x','tile_y','tile_z','new_tile','outer_tile_x','outer_tile_y','outer_tile_z','accepted_water']
SAMPLES_DF_COLUMNS = ['id','tile_x','tile_y','tile_z','lon','lat','country','satellite_file','mask_file','geometry']

# different geographical projections
# and the corresponding CRS string
CRS_GEODETIC = 'EPSG:4326'
CRS_MERCATOR = 'EPSG:3857'