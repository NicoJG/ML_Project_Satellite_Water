from ml_project.constants import paths,mapbox

from pathlib import Path
import errno
import os
import requests
import shutil
import mapbox_vector_tile
import geopandas as gpd

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
        
def get_water_df(x,y,z):
    file_path = paths.FILE_VECTOR_TILE(x,y,z)
    url = mapbox.URL_VECTOR(x,y,z)
    download_file(file_path,url,is_vector_tile=True)
    vector_tile = read_vector_tile(file_path)
    if 'water' not in vector_tile.keys():
        return None
    return gpd.GeoDataFrame.from_features(vector_tile['water']['features'])