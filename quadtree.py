class Quadtree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # Rectangular boundary of the quadtree
        self.capacity = capacity  # Capacity of each node (max creatures)
        self.creatures = []
        self.divided = False

    def subdivide(self):
        x, y, w, h = self.boundary
        half_w, half_h = w / 2, h / 2

        # Create four children (sub-quadrants)
        self.nw = Quadtree((x, y, half_w, half_h), self.capacity)
        self.ne = Quadtree((x + half_w, y, half_h, half_h), self.capacity)
        self.sw = Quadtree((x, y + half_h, half_w, half_h), self.capacity)
        self.se = Quadtree((x + half_w, y + half_h, half_w, half_h), self.capacity)

        self.divided = True

    def insert(self, creature):
        x, y, w, h = self.boundary
        cx, cy = creature["pos"]

        if not (x <= cx < x + w and y <= cy < y + h):
            return False  # Creature is out of bounds

        if len(self.creatures) < self.capacity:
            self.creatures.append(creature)
            return True

        if not self.divided:
            self.subdivide()

        return (self.nw.insert(creature) or self.ne.insert(creature) or
                self.sw.insert(creature) or self.se.insert(creature))

    def query(self, range_rect, found):
        x, y, w, h = self.boundary
        rx, ry, rw, rh = range_rect

        if not (rx + rw >= x and rx <= x + w and ry + rh >= y and ry <= y + h):
            return  # Out of range

        for creature in self.creatures:
            cx, cy = creature["pos"]
            if rx <= cx < rx + rw and ry <= cy < ry + rh:
                found.append(creature)

        if self.divided:
            self.nw.query(range_rect, found)
            self.ne.query(range_rect, found)
            self.sw.query(range_rect, found)
            self.se.query(range_rect, found)
