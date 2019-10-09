"""
This purpose of this file is to create functions to find metro routes.
"""
import sys
def readmap(mapfile):
    """
    Reads a map file and returns a dictionary of starting locations and
    destinations.

    Args:
        mapfile: the file containing locations that will be read by readmap.

    Returns:
        mapdict (dict): the dictionary containing locations.
    """
    with open(mapfile) as file_in: #opens mapfile to read
        mapdict = dict() #initializes mapdict as an empty dictionary
        for line in file_in: #reads each line of the file
            locations = line.strip().split("\t") #splits each line at tab
            stop1 = locations[0] #sets the first list element to stop1
            stop2 = locations[1] #sets the second list element to stop2
            if stop1 not in mapdict: #if first location not in dictionary
                mapdict[stop1] = set() #initializes a set for values of stop1
            mapdict[stop1].add(stop2) #adds destination to values set
            if stop2 not in mapdict: #this section is for birdirectionality
                mapdict[stop2] = set()
            mapdict[stop2].add(stop1)
        return mapdict

def find_route(mapdict, startloc, endloc):
    """
    Finds the route between two locations.

    Args:
        mapdict (dict): the dictionary containing locations.
        startloc (list): the location the route starts at.
        endloc (list): the location the route ends at.

    Returns:
        routelist (list): a list of partial routes from one location to another.
        None: if startloc or endloc are not on map.
    """
    queue = [[startloc]] #initialize a list of lists for possible routes
    visited = [startloc] #initializes a list of visited places

    while queue:
        current = queue.pop(0) #pops first list of routes from queue
        lastloc = mapdict[current[-1]]#lastloc=values of last element in current
        for loc in lastloc:
            if loc in visited:
                continue #continues if loc has already been visited
            else:
                visited.append(loc) #appends loc to visited
            routelist = current+[loc] #routelist now has directions
            if loc == endloc:
                return routelist #this means you have reached destination
            else:
                queue.append(routelist) #adds the route to the queue
    return None

def main(mapfile, startloc, endloc):
    """
    Reads the map data and finds a route between two locations.

    Args:
        mapfile: the file containing locations that will be read by readmap.
        startloc (list): the location the route starts at.
        endloc (list): the location the route ends at.
    """
    mapdict = readmap(mapfile) #calls first function
    print(find_route(mapdict, startloc, endloc)) #calls second function

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
