class Player:
    def __init__(self, p_name):
        self.name = p_name
        self.driver_list = []

    def __str__(self):
        return self.name
