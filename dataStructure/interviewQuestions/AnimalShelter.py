 # Implement a cat and dog queue for an animal shelter where first come animal will be
 # the first out for adoption

class CatDogAdoption():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.cats) == 0:
            res = self.dogs.pop(0)
        else:
            res = self.cats.pop(0)
        return res

    def dequeueCat(self):
        if len(self.cats) == 0:
            return "No cats for adoption"
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return "NO dogs for adoption"
        else:
            dog = self.dogs.pop(0)
            return dog

animalAdopt = CatDogAdoption()
animalAdopt.enqueue("c1", "Cats")
animalAdopt.enqueue("d1", "Dogs")
animalAdopt.enqueue("d2", "Dogs")
animalAdopt.enqueue("c2", "Cats")
animalAdopt.enqueue("d3", "DOgs")
print(animalAdopt.dequeueAny())
print(animalAdopt.dequeueCat())
print(animalAdopt.dequeueDog())
