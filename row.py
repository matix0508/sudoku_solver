from group import Group

class Row(Group):
    def __repr__(self) -> str:
        print(self.spaces_lst())
        output = '    '.join(self.spaces_lst())
        
        return output