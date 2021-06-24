from pathlib import Path
from ml_project.utils import mapbox,data
import ml_project

# points to the main directory (the directory with the .git directory in it)
BASE = Path(ml_project.__file__).parent.parent.absolute()

# main directories
DATA = BASE / 'data'

DATASET = DATA / 'dataset'
DATASET_META = DATA / 'dataset_metadata'
NATURAL_EARTH = DATA / 'natural_earth'

# external datasets
NE_10M_COUNTRIES_SHP = NATURAL_EARTH / 'ne_10m_admin_0_countries' / 'ne_10m_admin_0_countries.shp'
NE_110M_COUNTRIES_SHP = NATURAL_EARTH / 'ne_110m_admin_0_countries' / 'ne_110m_admin_0_countries.shp'

# data for the dataset creation
VECTOR_TILES = DATASET_META / 'vector_tiles'

def FILE_VECTOR_TILE(x,y,z):
    return VECTOR_TILES / f'z{z}x{x}y{y}_{mapbox.VECTOR_TILESET_ID}.mvt'

FILE_POINTS = DATASET_META / 'points.csv'

FILE_RANDOM_STATE = DATASET_META / 'random_state.json'

# actual dataset
IMAGES = DATASET / 'images'
SATELLITE_IMAGES = IMAGES / 'satellite'
MASK_IMAGES = IMAGES / 'mask'

def FILE_SATELLITE_IMAGE(x,y,z,size=data.PX_WIDTH):
    return SATELLITE_IMAGES / f'z{z}x{x}y{y}_px{size}.{data.SATELLITE_FORMAT}'

def FILE_MASK_IMAGE(x,y,z,size=data.PX_WIDTH):
    return MASK_IMAGES / f'z{z}x{x}y{y}_px{size}.{data.MASK_FORMAT}'

FILE_SAMPLES = DATASET / 'samples.csv'
FILE_METADATA = DATASET / 'metadata.csv'


# automatically create the directories when this file is imported
def check_dir(path):
    if not Path(path).is_dir():
        Path(path).mkdir()
        print(f'NOTE: Directory "{str(path)}" did not exist and was now created')
    
check_dir(DATA)
check_dir(DATASET)
check_dir(DATASET_META)
check_dir(NATURAL_EARTH)

check_dir(VECTOR_TILES)

check_dir(IMAGES)
check_dir(SATELLITE_IMAGES)
check_dir(MASK_IMAGES)
