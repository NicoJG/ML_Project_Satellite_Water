from ml_project.constants import data

TOKEN = 'pk.eyJ1Ijoibmljb2pnIiwiYSI6ImNrcHljYjR0dzA2N2Yyb2pzazNjamhtMGoifQ.KzlCg0L861hO_DnNbEQ_UQ'

# Identifiers for the different tilesets, styles, ...
MASK_STYLE_ID = 'ckpymj4h70vc717k4f8ja8wkd'
MASK_USERNAME = 'nicojg'
SATELLITE_TILESET_ID = 'mapbox.satellite'
VECTOR_TILESET_ID = 'mapbox.mapbox-streets-v8'

# URLs to the APIs (don't use these, but the URLs below)
def URL_RASTER_TILES_API(x,y,z,token,tileset_id,x2,format_):
    return f'https://api.mapbox.com/v4/{tileset_id}/{z}/{x}/{y}{x2}.{format_}?access_token={token}'

def URL_STATIC_TILES_API(x,y,z,token,username,style_id,tilesize):
    return f'https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/{tilesize}/{z}/{x}/{y}?access_token={token}'

def URL_VECTOR_TILES_API(x,y,z,token,tileset_id):
    return f'https://api.mapbox.com/v4/{tileset_id}/{z}/{x}/{y}.mvt?access_token={token}'

# URLs of our actual requests (use these)
def URL_SATELLITE(x,y,z,token=TOKEN):
    if data.PX_WIDTH == 256:
        x2 = ''
    elif data.PX_WIDTH == 512:
        x2 = '@2x'
    return URL_RASTER_TILES_API(x,y,z,token,SATELLITE_TILESET_ID,x2,data.RASTER_FORMAT)

def URL_MASK(x,y,z,token=TOKEN):
    return URL_STATIC_TILES_API(x,y,z,token,MASK_USERNAME,MASK_STYLE_ID,data.PX_WIDTH)

def URL_VECTOR(x,y,z,token=TOKEN):
    return URL_VECTOR_TILES_API(x,y,z,token,VECTOR_TILESET_ID)