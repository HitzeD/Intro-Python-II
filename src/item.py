class Item:

    def __init__(self, name, description):
        self.name = name
        self.desciption = description

    def __str__(self):
        return f" Name: {self.name},\nDescription: {self.desciption}"

    def __repr__(self):
        return f"Item({repr(self.name)})"