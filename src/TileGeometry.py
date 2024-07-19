
import _

from collections import namedtuple


def getFeatureExtent(width):
    lo = (_.TILE_SIZE / 2) - (width / 2)
    hi = (_.TILE_SIZE / 2) + (width / 2)
    return (round(lo),round(hi))


# These dimensions are all rectangles that go from an upper left coordinate to
# the lower right. Because the dimensions are rotated in a square the point
# coordinates are reused, just rearranged depending on what edge is being
# referenced. This function returns the tuple (x1,y1, x2,y2)
def calculateDimensions(code):
    extent = extents[code]
    low = extent[0]
    high = extent[1]
    top = 0
    bot = _.TILE_SIZE - 1
    topSize = top + 15
    botSize = bot - 15

    return {
        _.N: [low,top,     high,topSize],
        _.S: [low,botSize, high,bot],
        _.E: [botSize,low, bot,high],
        _.W: [top,low,     topSize,high]}


extents = {
    _.CHANEL: getFeatureExtent(_.CHANEL_WIDTH),
    _.HALL: getFeatureExtent(_.HALL_WIDTH),
    _.ROOM: getFeatureExtent(_.ROOM_WIDTH)}


dimensions = {
    _.CHANEL: calculateDimensions(_.CHANEL),
    _.HALL: calculateDimensions(_.HALL),
    _.ROOM: calculateDimensions(_.ROOM)}


def getDimensions(feature,direction):
    return dimensions[feature][direction]


def getExtents(x):
    return extents


Geometry = namedtuple('Geometry',[
    'getDimensions', 'getExtents'
    ])(getDimensions, getExtents)
