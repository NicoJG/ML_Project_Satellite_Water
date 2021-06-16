from pathlib import Path
import ml_project

# points to the main folder (the folder with the .git folder in it)
BASE = Path(ml_project.__file__).parent.parent.absolute()

# main folders
DATA = BASE / 'data'

DATASET = DATA / 'dataset'
DATASET_META = DATA / 'dataset_metadata'
NATURAL_EARTH = DATA / 'natural_earth'

# external datasets
NE_10M_COUNTRIES_SHP = NATURAL_EARTH / 'ne_10m_admin_0_countries' / 'ne_10m_admin_0_countries.shp'
NE_110M_COUNTRIES_SHP = NATURAL_EARTH / 'ne_110m_admin_0_countries' / 'ne_110m_admin_0_countries.shp'

# data for the dataset creation
VECTOR_TILES = DATASET_META / 'vector_tiles'

def FILE_VECTOR_TILE(x,y,z,tileset_ids):
    return VECTOR_TILES / f'z{z}x{x}y{y}_{",".join(tileset_ids)}.mvt'

FILE_POINTS = DATASET_META / 'points.csv'

# actual dataset
IMAGES = DATASET / 'images'
SATELLITE_IMAGES = IMAGES / 'satellite'
MASK_IMAGES = IMAGES / 'mask'

def FILE_SATELLITE_IMAGE(x,y,z,size):
    return SATELLITE_IMAGES / f'z{z}x{x}y{y}_px{size}.jpg'

def FILE_MASK_IMAGE(x,y,z,size):
    return MASK_IMAGES / f'z{z}x{x}y{y}_px{size}.png'

FILE_METADATA = DATASET / 'metadata.csv'


