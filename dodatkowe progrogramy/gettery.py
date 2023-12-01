class Circle:
    def __init__(self, radius):
        self.radius = radius  # Nieprywatny atrybut

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

# Użycie gettera dla nieprywatnego atrybutu
circle = Circle(5)

print(circle.area)  # Wywołanie gettera


# zastosowanie gettera umożliwia opuszczenie nawiasów w 12 linijce po circle.area