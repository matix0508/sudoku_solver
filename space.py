class Space:
    def __init__(self, value: int, row: int, col: int) -> None:
        self.id = None
        self.value = value
        self.sqaure = None
        self.row = None
        self.col = None
        self.available_values = None
        self.changable = True

    def get_square(self):
        return 3 * (self.row.id % 3) + (self.col.id % 3)

    def set_available_values(self, max_number):
        self.available_values = list(range(1, max_number+1))
        self.changable = self.value == 0
    
    def eliminate(self):
        self.set_available_values()
        for group in [self.row, self.col, self.square]:
            for val in group.all_values():
                try:
                    self.available_values.remove(val)
                except ValueError: # when there is no such value
                    pass

    def __repr__(self) -> str:
        return str(self.value) if self.value else str(0)

    def save(self):
        # print(self.sqaure)
        self.row.add_space(self)
        self.col.add_space(self)
        self.sqaure.add_space(self)

    

