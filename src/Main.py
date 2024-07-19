
import _

from collections import namedtuple
from PIL import Image, ImageDraw
from TileGeometry import Geometry
from TilePermutations import Permutations


context = { 'draw':None }


# This function is called once for each tile permutation to generate the base
# image for that tile. These images will be saved into the permutations object
# and eventually included on a single sprite sheet.
def createTileGraphics(signature):
    print(f'Generate Tile [{signature}]')

    edges = Permutations[signature]['edges']

    image = Image.new('RGBA',(_.TILE_SIZE,_.TILE_SIZE),(0,0,0))
    context['draw'] = ImageDraw.Draw(image)

    # Features should be drawn in the order they are layered.
    # The last feature drawn will be on top.
    drawFeatures(edges, _.HALL,   drawHall)
    drawFeatures(edges, _.CHANEL, drawChanel)
    drawFeatures(edges, _.ROOM,   drawRoom)

    image.save(f'tiles/tile-{signature}-0.png')


def drawFeatures(edges, symbol, drawFunction):
    for index, edge in enumerate(edges):
        if edge == symbol:
            drawFunction(_.DIRECTION_MAP[index])


def drawHall(direction):
    dimensions = Geometry.getDimensions(_.HALL,direction)
    context['draw'].rectangle(dimensions,(250,0,0))


def drawRoom(direction):
    dimensions = Geometry.getDimensions(_.ROOM,direction)
    context['draw'].rectangle(dimensions,(0,0,250))


def drawChanel(direction):
    dimensions = Geometry.getDimensions(_.CHANEL,direction)
    context['draw'].rectangle(dimensions,(0,250,0))


for signature in Permutations:
    createTileGraphics(signature)
