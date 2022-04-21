from src.Fish import Fish
import random
class Pond:
    def __init__(self):
        self.name = "sick-salmon"
        self.fishes = []

    def getPopulation(self):
        return len(self.fishes)

    def spawnFish(self, parentFish = None):
        self.fishes.append( Fish(10, 100, self.name, parentFish.getId()) )

    def pheromoneCloud(self ):
        pheromone = random.randint(2, 20)
        for f in self.fishes:
            f.increasePheromone(pheromone)
            if f.isPregnant(): ## check that pheromone >= pheromone threshold
                self.fishes.append( Fish(10, 100, self.name, f.getId()))
                f.resetPheromone()

    def migrateFish(self, fishIndex):
        pass
    #---------------implement---------------#

    def addFish(self, newFishData): #from another pond
        pass

    def update(self, injectPheromone = False):
        for ind, f in enumerate( self.fishes): #checkout all the fish in the pond
            f.updateLifeTime() # decrease life time by 1 sec
            if f.getGenesis() != self.name and f.in_pond_sec >= 5:
                self.spawnFish( f )
            elif f.getGenesis() == self.name and f.in_pond_sec <= 15:
                if random.getrandbits(1):
                    self.migrateFish( ind ) 
                    continue
            
            if self.getPopulation() > f.getCrowdThresh():
                self.migrateFish( ind )
                continue
            
        if ( injectPheromone ):
            self.pheromoneCloud()

