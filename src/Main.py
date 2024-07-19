
from PIL import Image

import _
import TileGeometry
import TileInfo

permutations = TileInfo.generatePermutations()

# This function is called once for each tile permutation to generate the base
# image for that tile. These images will be saved into the permutations object
# and eventually included on a single sprite sheet.
def createTileGraphics(signature):
    print(f'Generate Tile [{signature}]')

    edges = permutations[signature]['edges']

    tileImage = Image.new('RGBA',(_.TILE_SIZE,_.TILE_SIZE),(0,0,0))

    # Features should be drawn in the order they are layered.
    # The last feature drawn will be on top.
    drawFeatures(edges, _.HALL,   drawHall)
    drawFeatures(edges, _.CHANEL, drawChanel)
    drawFeatures(edges, _.ROOM,   drawRoom)

    tileImage.show()


def drawFeatures(edges, symbol, drawFunction):
    for index, edge in enumerate(edges):
        if edge == symbol:
            drawFunction(_.DIRECTION_MAP[index])


def drawHall(direction):
    print(f'   - {direction} draw hall.')


def drawRoom(direction):
    print(f'   - {direction} draw room.')


def drawChanel(direction):
    print(f'   - {direction} draw chanel.')



# for signature in permutations:
#     createTileGraphics(signature)

createTileGraphics('HRSS')
