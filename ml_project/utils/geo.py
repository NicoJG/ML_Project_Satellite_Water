from ml_project.constants import data

import mercantile
import shapely.geometry

def get_inner_bbox_in_outer(x_i,y_i,z_i,x_o,y_o,z_o):
    # pixel width and height of the outer vector tile
    extent_o = data.VECTOR_TILE_EXTENT
    # pixel width and height of one inner tile
    extent_i = extent_o/(2**(z_i-z_o))
    # top left Tile in the outer Tile but with the inner zoom
    # https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Subtiles
    x_o_with_z_i = 2**(z_i-z_o) * x_o
    y_o_with_z_i = 2**(z_i-z_o) * y_o
    # pixel coordinates of the top left corner of the inner tile in the vector tile
    px_tl = extent_i * (x_i - x_o_with_z_i)
    py_tl = extent_i * (y_i - y_o_with_z_i)
    # bottom right corner of the inner tile in vector tile pixel coordinates
    px_br = px_tl + extent_i
    py_br = py_tl + extent_i
    # shapely Polygon
    bbox = shapely.geometry.box(px_tl, py_tl, px_br, py_br)
    return bbox

def get_outer_tile(x_i,y_i,z_i):
    z_o = data.Z_OUTER
    tile_o = mercantile.parent(x_i,y_i,z_i,zoom=z_o)
    x_o = tile_o.x
    y_o = tile_o.y
    return x_o,y_o,z_o