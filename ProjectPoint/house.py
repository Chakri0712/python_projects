class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5
       
        
class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets
        
    def total_price(self):
        if self.color == 'white':
            return 1.99*self.buckets
        else:
            return 2.19*self.buckets