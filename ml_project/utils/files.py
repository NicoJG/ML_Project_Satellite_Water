from ml_project.constants import paths,mapbox,data

from pathlib import Path
import os
import errno

import requests
import shutil

import numpy as np
import pandas as pd
import mapbox_vector_tile
import geopandas as gpd

import json

# https://stackoverflow.com/a/39217788/13440768
def download_file(file_path,url,override=False,is_vector_tile=False,is_text=False):
    """
    Downloads the given URL into the given File Path, but checks if the File already exists
    
    Parameters
    ----------
    file_path : str or path-like-object
        The path to the file which should be written
        can be an absolute path
        or a relative path to the active working directory
    url : str
        The full URL to the file/response that should be downloaded
    override : bool
        Should the file at file_path be overriden if it already exists?
        
    Returns
    -------
    bool
        Did the File already exist?
    """
    path = Path(file_path)
    
    if not path.parent.is_dir():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(path.parent))
    
    if path.is_dir():
        raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), str(path))
        
    exists = path.is_file()
    if exists and not override:
        return exists
    
    r = requests.get(url,stream=True)
    r.raise_for_status()
    if is_vector_tile:
        with open(path,'wb') as file:
            file.write(r.content)
    elif is_text:
        with open(path,'w') as file:
            file.write(r.text)
    else:
        with open(path, 'wb') as file:
            shutil.copyfileobj(r.raw, file)
    del r
    
    return exists
    
    
def read_vector_tile(file_path):
    with open(file_path, mode='rb') as file:
        return mapbox_vector_tile.decode(file.read(),y_coord_down=True)
        
def load_water_df(x,y,z):
    # get the information of an outer tile of water via a Vector Tile
    file_path = paths.FILE_VECTOR_TILE(x,y,z)
    url = mapbox.URL_VECTOR(x,y,z)
    download_file(file_path,url,is_vector_tile=True)
    vector_tile = read_vector_tile(file_path)
    if 'water' not in vector_tile.keys():
        return None
    return gpd.GeoDataFrame.from_features(vector_tile['water']['features'])

def read_csv_as_geodataframe(file_path,geometry='geometry',crs=None):
    df = pd.read_csv(file_path)
    df[geometry] = gpd.GeoSeries.from_wkt(df[geometry])
    gdf = gpd.GeoDataFrame(df,crs=crs,geometry=geometry)
    return gdf

def save_points_df(points_df,override=False):
    points_df = points_df[data.POINTS_DF_COLUMNS]
    if paths.FILE_POINTS.is_file() and not override:
        points_df.to_csv(paths.FILE_POINTS,mode='a', header=False, index=False)
    else:
        points_df.to_csv(paths.FILE_POINTS,mode='w', header=True,  index=False)
    
def load_points_df():
    if paths.FILE_POINTS.is_file():
        return read_csv_as_geodataframe(paths.FILE_POINTS,crs=data.CRS_GEODETIC)
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(paths.FILE_POINTS))
        
def save_samples_df(samples_df,override=False):
    samples_df = samples_df[data.SAMPLES_DF_COLUMNS]
    if paths.FILE_SAMPLES.is_file() and not override:
        samples_df.to_csv(paths.FILE_SAMPLES,mode='a', header=False, index=False)
    else:
        samples_df.to_csv(paths.FILE_SAMPLES,mode='w', header=True,  index=False)

def load_samples_df():
    if paths.FILE_SAMPLES.is_file():
        return read_csv_as_geodataframe(paths.FILE_SAMPLES,crs=data.CRS_GEODETIC)
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(paths.FILE_SAMPLES))
    
def load_ne_countries_eu_110m():
    # Read the Natural Earth Dataset of the Countries coarse
    # https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
    countries_110m = gpd.read_file(paths.NE_110M_COUNTRIES_SHP)
    # select only the eu and exclude countries
    countries_eu_110m = countries_110m[countries_110m['CONTINENT']=='Europe'].copy()
    drop_countries_mask = countries_eu_110m['NAME_EN'].isin(data.EXCLUDED_COUNTRIES)
    countries_eu_110m.drop(index=countries_eu_110m[drop_countries_mask].index,inplace=True)
    return countries_eu_110m
    
def load_ne_countries_eu_10m():
    # Read the Natural Earth Dataset of the Countries coarse
    # https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
    countries_10m = gpd.read_file(paths.NE_10M_COUNTRIES_SHP)
    # select only the eu and exclude countries
    countries_eu_10m = countries_10m[countries_10m['CONTINENT']=='Europe'].copy()
    drop_countries_mask = countries_eu_10m['NAME_EN'].isin(data.EXCLUDED_COUNTRIES)
    countries_eu_10m.drop(index=countries_eu_10m[drop_countries_mask].index,inplace=True)
    return countries_eu_10m

def load_random_state(seed=42):
    rng = np.random.default_rng(seed=seed)
    if paths.FILE_RANDOM_STATE.is_file():
        with open(paths.FILE_RANDOM_STATE,'r') as file:
            rng.__setstate__(json.load(file))
    return rng

def save_random_state(rng):
    with open(paths.FILE_RANDOM_STATE,'w') as file:
        json.dump(rng.__getstate__(), file, indent=2)