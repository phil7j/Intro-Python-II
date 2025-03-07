# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):  # equivalent to JS constructor
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        for item in self.items:
            print(item.name)

    def __repr__(self):
        return f'{self.name}'
