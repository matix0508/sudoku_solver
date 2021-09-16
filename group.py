from typing import Optional

class Group:
    def __init__(self, id: Optional[int] = None, max_number: Optional[int] = 9) -> None:
        self.id = id
        self.spaces = []
        self.max_number = max_number


    def spaces_lst(self):
        return [str(s) for s in self.spaces]

    def add_space(self, space):
        self.spaces.append(space)

    def look_for(self, number: int):
        output = 0
        for space in self.spaces:
            if space.id == number:
                output += 1

        if output == 1:
            return True
        elif output == 0:
            return False
        else:
            raise Exception(f"Too much numbers: {number}")
    
    def check(self):
        for i in range(self.max_number):
            if not self.look_for(i):
                return False
        return True
    
    def is_valid(self):
        return self.spaces_lst() == range(len(self.spaces()))

    def all_values(self):
        return list(filter(None, self.spaces_lst))

    


        
    
