from .audition import Audition

class Role:
    all = []

    def __init__(self, character_name):
        self.character_name = character_name

        type(self).all.append(self)

    def auditions(self):
        return [audition for audition in Audition.all if audition.role_chosen == self]

    def actors(self):
        return [audition.actor for audition in Audition.all
                if audition.role_chosen == self]

    def locations(self):
        return list({audition.location for audition in Audition.all
                if audition.role_chosen == self})

    def lead(self):
        hired = [audition for audition in Audition.all
                        if audition.hired == True]
        hired_actors = [audition for audition in hired
                        if audition.role_chosen == self]
        if len(hired_actors) > 0:
            return hired_actors[0]
        else:
            return "no actor has been hired for this role"

    def understudy(self):
        hired = [audition for audition in Audition.all
                        if audition.hired == True]
        hired_actors = [audition for audition in hired
                        if audition.role_chosen == self]
        if len(hired_actors) > 1:
            return hired_actors[1]
        else:
            return "no actor has been hired for understudy for this role"
