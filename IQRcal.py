import math
#assumed that list is already in order
def find_median(plist):
    if len(plist) % 2 == 0:
        median = (plist[(len(plist)/2)-1] + plist[(len(plist)/2)])/2
    else:
        median = (plist[(len(plist)-1)/2])


