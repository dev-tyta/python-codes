import game
from game import GameObject


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has wound on its knee"
        elif self.health == 1:
            health_line = "Its left arm has been cut off"
        elif self.health == 0:
            health_line = "Its is dead"
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = f"You hit the {thing.class_name}"
        else:
            msg = f"There is no {noun}"
        return msg


