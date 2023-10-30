
class Audition:
    all = []

    def __init__(self, actor, location, hired, role_chosen):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role_chosen = role_chosen

        type(self).all.append(self)

    @property
    def actor(self):
        return self._actor
    @actor.setter
    def actor(self, new_actor):
        if not isinstance(new_actor, str):
            raise TypeError("Actor must be a string")
        else:
            self._actor = new_actor

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, new_location):
        if not isinstance(new_location, str):
            raise TypeError("Location must be a string")
        else:
            self._location = new_location

    @property
    def hired(self):
        return self._hired
    @hired.setter
    def hired(self, status):
        if not isinstance(status, bool):
            raise TypeError("Hired must be a boolean")
        else:
            self._hired = status

    def role(self):
        return self.role

    def call_back(self):
        self.hired = True
