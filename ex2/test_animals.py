from animals import Mammals
from animals import Birds

myMammal = Mammals()
myMammal.printMembers()

myBird = Birds()
myBird.printMembers()

import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printHarmless()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printDangerous()

dangerous_mammals = animals.dangerous.Mammals()
dangerous_mammals.printDangerous()

