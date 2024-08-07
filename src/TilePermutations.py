
import _

edgeTypes = [_.STONE, _.ROOM, _.HALL, _.CHANEL]

# Generate the permutations by looping through all the edges in 4 nested loops,
# one for each of the cardinal directions.
def generatePermutations():
    permutations = {}
    for n in edgeTypes:
        for s in edgeTypes:
            for e in edgeTypes:
                for w in edgeTypes:
                    r = findLowestRotation(n,s,e,w)
                    permutations[f'{r[0]}{r[1]}{r[2]}{r[3]}'] = { 'edges':r }

    permutations.pop('SSSS') # Remove the all stone tile.
    return permutations

# Because the tiles can be rotated we only want to generate a single tile that
# would match all the rotated versions of that tile. To do this, we sorts the
# edge list lexicography. We only save these lowest rotations in the list of
# permutations to then turn into tiles.
def findLowestRotation(n,s,e,w):
    rotations = [
        (n,s,e,w),
        (w,e,n,s),
        (s,n,w,e),
        (e,w,s,n)]

    rotations.sort(key=lambda tuple: tuple[0])

    return rotations[0]


Permutations = generatePermutations()
