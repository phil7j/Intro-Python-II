# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room="outside"):  # equivalent to JS constructor
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if direction == "n":
            self.current_room = room[current_room].n_to
    # def __str__(self):
    #     s = f"Player: {self.name}\n"
    #     return s
