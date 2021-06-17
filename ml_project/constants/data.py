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
LON_MIN, LON_MAX = -10.49, 40.27
LAT_MIN, LAT_MAX = 34.51, 71.20