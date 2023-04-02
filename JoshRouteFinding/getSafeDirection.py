import pandas as pd
import numpy as np
import copy
import ast

from getDirection import get_directions

# from JoshRouteFinding.getDirection import get_directions

def get_safe_direction(startLocation, endLocation, crimes):
    # startLocation = copy.deepcopy(startLocation)
    # endLocation = copy.deepcopy(endLocation)
    # startLocation.reverse()
    # endLocation.reverse()

    print("start", startLocation)
    print("End", endLocation)

    route1 = get_directions(startLocation, endLocation, driving=True)
    route2 = get_directions(startLocation, endLocation, cycling=True)
    route3 = get_directions(startLocation, endLocation)

    danger1 = get_danger(crimes, route1)
    danger2 = get_danger(crimes, route2)
    danger3 = get_danger(crimes, route3)
    print("danger1: ", danger1)
    print("danger2: ", danger2)
    print("danger3: ", danger3)


    bestRoute = []
    bestDanger = 0
    if danger1 < danger2:
        bestDanger = danger1
        bestRoute = route1
        print("driving best")
    else:
        bestDanger = danger2
        bestRoute = route2
        print("cycling best")
    
    if bestDanger > danger3:
        bestDanger = danger3
        bestRoute = route3
        print("nah never mind walking is best")

    halfwayI = len(bestRoute)//2

    bestStart = bestRoute[0:halfwayI]

    halfwayCords = bestRoute[halfwayI]

    route1 = get_directions(halfwayCords, endLocation, driving=True)
    route2 = get_directions(halfwayCords, endLocation, cycling=True)
    route3 = get_directions(halfwayCords, endLocation)

    danger1 = get_danger(crimes, route1)
    danger2 = get_danger(crimes, route2)
    danger3 = get_danger(crimes, route3)

    print("danger1: ", danger1)
    print("danger2: ", danger2)
    print("danger3: ", danger3)

    bestRoute = []
    bestDanger = 0
    if danger1 < danger2:
        bestDanger = danger1
        bestRoute = route1
        print("driving best2")
    else:
        bestDanger = danger2
        bestRoute = route2
        print("cycling best2")
    
    if bestDanger > danger3:
        bestDanger = danger3
        bestRoute = route3
        print("nah never mind walking is best2")

    bestStart.append(halfwayCords)
    bestStart.extend(bestRoute)

    return bestStart
    

def get_safe_direction_old(startLocation, endLocation, crimes):
    route1 = get_directions(startLocation, endLocation, driving=True)
    route2 = get_directions(startLocation, endLocation, cycling=True)
    route3 = get_directions(startLocation, endLocation)

    danger1 = get_danger(crimes, route1)
    danger2 = get_danger(crimes, route2)
    danger3 = get_danger(crimes, route3)
    print("danger1: ", danger1)
    print("danger2: ", danger2)
    print("danger3: ", danger3)


    bestRoute = []
    bestDanger = 0
    if danger1 < danger2:
        bestDanger = danger1
        bestRoute = route1
        print("driving best")
    else:
        bestDanger = danger2
        bestRoute = route2
        print("cycling best")
    
    if bestDanger > danger3:
        bestDanger = danger3
        bestRoute = route3
        print("nah never mind walking is best")

    i = 0
    bestRoute = np.array(bestRoute)
    crimes = np.array(crimes)
    distance = (25/111139)**2
    while i < len(bestRoute):
        # d = np.linalg.norm(crimes - bestRoute[i], axis=1)
        differences = crimes - bestRoute[i]
        distances_squared = np.sum(differences ** 2, axis=1)
        if np.nonzero(distances_squared < distance) >= 1:
            pass
        i+=1
    

def get_danger(crimes, route):
    distance = (25/111139)**2
    danger = 0

    for place in route:
        for crime in crimes:
            # if ((crime[1] - place[0])**2 + (crime[0] - place[1])**2) > 200:
                # print("Check Danger function")
            # print((crime[0] - place[0])**2 + (crime[0] - place[0])**2)
            if ((crime[0] - place[0])**2 + (crime[1] - place[1])**2) < distance:
                danger+=1
        
    return danger

def compare_route_2(crimes, route1, route2):
    crimes2 = copy.deepcopy(crimes)
    distance = (25/111139)**2
    danger1 = 0
    for place in route1:
        for crime in crimes:
            # check

            if ((crime[1] - place[0])**2 + (crime[0] - place[1])**2) < distance:
                danger1+=1

    danger2 = 0
    for place in route2:
        for crime in crimes2:
            if ((crime[1] - place[0])**2 + (crime[0] - place[1])**2) < distance:
                danger2+=1

    # print("danger1: ", danger1)
    # print("danger2: ", danger2)
    # # print(min(distances2))
    # print(distance)
    return danger1 < danger2
                

if __name__ == "__main__":
    data = pd.read_csv('Bath_Police_Data.csv')
    longitudes = data["Longitude"].to_numpy()
    latitudes = data["Latitude"].to_numpy()
    route1 = [[51.380822, -2.356731], [51.380818, -2.356944], [51.380818, -2.357017], [51.380816, -2.357202], [51.380844, -2.35733], [51.380871, -2.357475], [51.380915, -2.357686], [51.38094, -2.357723], [51.380965, -2.357745], [51.381003, -2.35775], [51.381026, -2.357869], [51.380983, -2.358589], [51.380965, -2.358795], [51.38096, -2.358828], [51.380906, -2.359138], [51.3809, -2.359161], [51.38089, -2.359219], [51.380782, -2.359765], [51.380746, -2.359958], [51.380719, -2.360111], [51.380793, -2.360142], [51.380793, -2.360185], [51.380813, -2.360263], [51.380865, -2.360356], [51.380895, -2.360382], [51.380836, -2.360767], [51.380776, -2.361188], [51.380807, -2.361222], [51.380873, -2.361349], [51.380901, -2.36143], [51.380908, -2.361507], [51.380905, -2.361571], [51.381007, -2.361582], [51.381201, -2.361586], [51.38143, -2.361628], [51.381371, -2.36235], [51.38136, -2.362465], [51.381359, -2.362574], [51.381357, -2.362653], [51.381353, -2.362714], [51.381289, -2.362558], [51.381268, -2.362542], [51.38127, -2.362769], [51.381251, -2.362816], [51.381215, -2.362826], [51.381219, -2.362857], [51.381301, -2.362864], [51.381318, -2.36288], [51.381296, -2.362923], [51.381323, -2.362954], [51.381389, -2.363147], [51.381395, -2.363168], [51.381391, -2.363226], [51.381229, -2.363536], [51.381194, -2.363584], [51.381114, -2.363639], [51.381049, -2.363676], [51.380975, -2.363746], [51.380913, -2.363788], [51.380808, -2.363895], [51.380857, -2.364008], [51.380998, -2.364335], [51.381245, -2.364939], [51.3813, -2.365093], [51.381484, -2.365582], [51.38156, -2.365824], [51.381513, -2.365869], [51.381475, -2.365899], [51.381459, -2.365912], [51.38149, -2.366024], [51.381425, -2.366178], [51.381414, -2.366225], [51.381413, -2.366242], [51.381373, -2.367678], [51.381373, -2.367693], [51.381373, -2.367789], [51.38143, -2.36783], [51.381421, -2.368035], [51.38145, -2.368127], [51.381453, -2.368182], [51.381483, -2.368184], [51.381479, -2.368233], [51.381477, -2.368259], [51.381455, -2.368383], [51.38145, -2.368441], [51.381436, -2.368686], [51.381419, -2.369106], [51.38141, -2.369149], [51.381428, -2.36918], [51.381412, -2.369349], [51.38139, -2.370094], [51.381396, -2.370124], [51.381505, -2.37014], [51.381578, -2.370217], [51.381933, -2.370784], [51.382067, -2.371024], [51.382094, -2.37111], [51.382103, -2.371173], [51.382139, -2.371269], [51.38218, -2.371281], [51.382218, -2.371278], [51.382151, -2.373253], [51.382146, -2.373384], [51.382185, -2.373762], [51.382102, -2.373791], [51.382119, -2.373886], [51.382172, -2.374298], [51.382235, -2.374738], [51.382276, -2.374997], [51.382379, -2.375656], [51.382477, -2.376282], [51.382515, -2.376515], [51.382545, -2.376719], [51.382114, -2.376788], [51.380443, -2.381321], [51.380442, -2.38143], [51.380438, -2.381428]]
    # route2 = [[51.380438, -2.381428], [51.380442, -2.38143], [51.380443, -2.381321], [51.380377, -2.380219], [51.380327, -2.379809], [51.380613, -2.379739], [51.380715, -2.379681], [51.380617, -2.37834], [51.380641, -2.378301], [51.380694, -2.378253], [51.380747, -2.37821], [51.380818, -2.378156], [51.380846, -2.377985], [51.380896, -2.377698], [51.381571, -2.377379], [51.381523, -2.377032], [51.381504, -2.376876], [51.382114, -2.376788], [51.382545, -2.376719], [51.382515, -2.376515], [51.382477, -2.376282], [51.382379, -2.375656], [51.382276, -2.374997], [51.382235, -2.374738], [51.382172, -2.374298], [51.382119, -2.373886], [51.382102, -2.373791], [51.382185, -2.373762], [51.382146, -2.373384], [51.382151, -2.373253], [51.382218, -2.371278], [51.38218, -2.371281], [51.382139, -2.371269], [51.382103, -2.371173], [51.382094, -2.37111], [51.382067, -2.371024], [51.381933, -2.370784], [51.381578, -2.370217], [51.381505, -2.37014], [51.381396, -2.370124], [51.38139, -2.370094], [51.381412, -2.369349], [51.381428, -2.36918], [51.38141, -2.369149], [51.381419, -2.369106], [51.381436, -2.368686], [51.38145, -2.368441], [51.381455, -2.368383], [51.381477, -2.368259], [51.381479, -2.368233], [51.381483, -2.368184], [51.381453, -2.368182], [51.38145, -2.368127], [51.381421, -2.368035], [51.38143, -2.36783], [51.381373, -2.367789], [51.381373, -2.367693], [51.381373, -2.367678], [51.381413, -2.366242], [51.381414, -2.366225], [51.381425, -2.366178], [51.38149, -2.366024], [51.381459, -2.365912], [51.381475, -2.365899], [51.381513, -2.365869], [51.38156, -2.365824], [51.381484, -2.365582], [51.3813, -2.365093], [51.381245, -2.364939], [51.380998, -2.364335], [51.380857, -2.364008], [51.380808, -2.363895], [51.380913, -2.363788], [51.380975, -2.363746], [51.381049, -2.363676], [51.381114, -2.363639], [51.381194, -2.363584], [51.381229, -2.363536], [51.381391, -2.363226], [51.381395, -2.363168], [51.381389, -2.363147], [51.381323, -2.362954], [51.381296, -2.362923], [51.381318, -2.36288], [51.381301, -2.362864], [51.381219, -2.362857], [51.381215, -2.362826], [51.381251, -2.362816], [51.38127, -2.362769], [51.381268, -2.362542], [51.381289, -2.362558], [51.381353, -2.362714], [51.381357, -2.362653], [51.381359, -2.362574], [51.38136, -2.362465], [51.381371, -2.36235], [51.38143, -2.361628], [51.381201, -2.361586], [51.381007, -2.361582], [51.380905, -2.361571], [51.380908, -2.361507], [51.380901, -2.36143], [51.380873, -2.361349], [51.380807, -2.361222], [51.380776, -2.361188], [51.380836, -2.360767], [51.380895, -2.360382], [51.380865, -2.360356], [51.380813, -2.360263], [51.380793, -2.360185], [51.380793, -2.360142], [51.380719, -2.360111], [51.380746, -2.359958], [51.380782, -2.359765], [51.38089, -2.359219], [51.3809, -2.359161], [51.380906, -2.359138], [51.38096, -2.358828], [51.380965, -2.358795], [51.380983, -2.358589], [51.381026, -2.357869], [51.381003, -2.35775], [51.380965, -2.357745], [51.38094, -2.357723], [51.380915, -2.357686], [51.380871, -2.357475], [51.380844, -2.35733], [51.380816, -2.357202], [51.380818, -2.357017], [51.380818, -2.356944], [51.380822, -2.356731]]
    # compare_route(zip(longitudes, latitudes), route1, route2)

    starting_location = [51.380679, -2.3567243]
    ending_location = [51.3804147, -2.3815838]
    with open('JoshRouteFinding/crimes.txt', 'r') as f:
        crimes = f.read()
    # print(crimes.shape)
    crimes = ast.literal_eval(crimes)
    # print(get_danger(crimes, route1))
    result = get_safe_direction(starting_location, ending_location, crimes)
    # print(result)