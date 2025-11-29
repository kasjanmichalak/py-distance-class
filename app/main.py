class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance: {self.km} kilometers."

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def  __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self.km

    def __mul__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        else:
            return Distance(self.km * other)

    def __truediv__(self, other):
        if other == 0:
            raise ValueError("Division by zero")
        if isinstance(other, Distance):
            return Distance(self.km / other.km)
        else:
            return Distance(self.km / other)

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other):
            if isinstance(other, Distance):
                return self.km <= other.km
            else:
                return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
