class Ucus:
    havayolu = "THY"

    def __init__(self, kod, source_place, dest_place, time, capacity, passenger):
        self.kod = kod
        self.source_place = source_place
        self.dest_place = dest_place
        self.time = time
        self.capacity = capacity
        self.passenger = passenger

    def update_capacity(self):
        return self.capacity - self.passenger


# u2 = update_capacity()

u1 = Ucus(535, "Baku", "Istanbul", "18:00", 100, 45)
# u1.update_capacity()


print(u1.update_capacity())
