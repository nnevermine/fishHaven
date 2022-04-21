from src.Fish import Fish
import random
class Pond:
    def __init__(self):
        self.name = "sick-salmon"
        self.fishes = []

    def population(self):
        return len(self.fishes)

    def spawnFish(self, parentFish = None):
        self.fishes.append( Fish(parentFish.getId()) )

    def pheromoneCloud(self ):
        pheromone = random.randint(2, 20)
        for f in self.fishes:
            f.increasePheromone(pheromone)
            if f.isPregnant(): ## check that pheromone >= pheromone threshold
                self.fishes.append( Fish(f.getId()))

    def migrateFish(self):
        pass

    def update(self, injectPheromone = False):
        for f in self.fishes:
            f.updateLifeTime() # decrease life time by 1 sec

        if ( injectPheromone ):
            self.pheromoneCloud()

