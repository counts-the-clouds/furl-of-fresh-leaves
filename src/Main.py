
import TileInfo

from PIL import Image

def createTileGraphics(signature, edges):
    print(f'Generate Tile [{signature}]')

permutations = TileInfo.generatePermutations()
for signature in permutations:
    createTileGraphics(signature, permutations[signature])

# createTileGraphics('SHRR',('S','H','R','R'))
