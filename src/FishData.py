import random
import math

def randId():
    digits = [i for i in range(0, 10)]
    
    for i in range(6):
        index = math.floor(random.random() * 10)

    random_str += str(digits[index])

def randCrowdThresh():
    return random.randint(5, 20)

def randPheromoneThresh():
    return random.randint(30, 60)

class FishData:
    def __init__(self, genesis, parentId):
        self.id = randId()
        self.state = "in-pond"
        self.status = "alive"
        self.genesis = genesis ## Pond name
        self.crowdThreshold = randCrowdThresh()
        self.pheromone = 0
        self.pheromoneThresh = randPheromoneThresh()
        self.lifetime = 60
        self.parentId = parentId
