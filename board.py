from space import Space
from row import Row
from col import Col
from square import Square

class Board:
    def __init__(self) -> None:
        self.rows = []
        self.cols = []
        self.squares = []
        self.spaces = []
        self.max_number = 9

    def load_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            rows = f.read().split('\n')
            for irow, row in enumerate(rows):
                cols = [int(item) for item in row.split('  ')]
                # cols = list(filter(None, cols))
                # print(cols)
                self.rows.append(Row(id=irow))
                for icol, space in enumerate(cols):
                    if irow == 0:
                        current_col = Col(id=icol)
                        self.cols.append(current_col)
                    else:
                        current_col = self.cols[icol]
                    
                    s = Space(space, irow, icol)
                    s.row = self.rows[-1]
                    s.col = current_col
                    if self.has_id(s.get_square(), 'square'):
                        s.square = self.squares[s.get_square()]
                    else:
                        s.sqaure = Square(s.get_square())
                    s.save()
                    self.spaces.append(s)

    def eliminate(self):
        for space in self.space:
            space.eliminate()
                    

    def __repr__(self) -> str:
        output = "_\t" * self.max_number
        output = output[-1]
        for row in self.rows:
            output = output + '\n' + '|' + str(row) + '|'
        output = output + "_\t" * self.max_number
        return output

    def has_id(self, id: int, item: str):
        if item == 'row':
            for row in self.rows:
                if row.id == id:
                    return True
        if item == 'col':
            for col in self.cols:
                if col.id == id:
                    return True
        if item == 'square':
            for sq in self.squares:
                if sq.id == id:
                    return True
        return False
        
if __name__ == "__main__":
    b = Board()
    b.load_file('board.sudoku')
    print(b)
