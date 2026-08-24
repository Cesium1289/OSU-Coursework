# Location: a location within Vacuum World.
# Each location has an id and, possibly, some dirt.

class Location:

    def __init__(self, id, dirt = None):
        self.id = id
        self.dirt = dirt

    def apply_suction(self):
        self.dirt = None
