
import random, string

class Board():

    def __init__(self, number_of_symbols) -> None:
        self.number_of_symbols = number_of_symbols
        self.number_of_rows = 3
        self.number_of_columns = self.number_of_rows
        self.symbols = self.get_symbols()
        self.data = None
    
    def __repr__(self) -> str:
        '''
        for i in range(self.number_of_columns):
            print("-" * self.number_of_rows * 2 + "-")
            print("", end=' ')
            for j in range(self.number_of_rows):
                print(self.data[i][j], end= ' ')
            print("\n", end='')
        print("-" * self.number_of_rows * 2 + "-")
        '''
        printable_board = "\n"
        for i in range(self.number_of_columns):
            horizontal_divider = "-" * self.number_of_rows * 4 + "-\n"
            printable_board += horizontal_divider
            printable_board += "| "
            for j in range(self.number_of_rows):
                printable_board += self.data[i][j] + " | "
            printable_board += "\n"
        printable_board += horizontal_divider
        return printable_board
        '''
        printable_board = "\n"
        for i in range(self.number_of_columns):
            horizontal_divider = "-" * self.number_of_rows * 16
            printable_board += horizontal_divider + "-\n|" + (("\t"*2) + "|")*3 + "\n"
            printable_board += "|\t"
            for j in range(self.number_of_rows):
                printable_board += self.data[i][j] + "\t|\t"
            printable_board += "\n|" + (("\t"*2) + "|")*3 + "\n"
        printable_board += horizontal_divider + "-\n"
        return printable_board
        '''

    def __call__(self, *args: any, **kwds: any) -> any:
        print(self)
        wins = self.check_win()
        return self.data, wins

    def get_symbols(self) -> list:
        symbols = random.sample(string.punctuation, self.number_of_symbols)
        return symbols

    def get_board(self):
        self.data = [[random.choice(self.symbols) for x in range(self.number_of_rows)] \
                     for i in range(self.number_of_columns)]
        return self.data
    
    def check_win(self) -> list:
        counts = [[0, 0] for _ in range(3)]

        for row in self.data:
            if len(set(row)) == 1:
                counts[0][0] += 1
            elif len(set(row)) == 2:
                counts[0][1] += 1

        for col in range(len(self.data[0])):
            column_symbols = [row[col] for row in self.data]
            if len(set(column_symbols)) == 1:
                counts[1][0] += 1
            elif len(set(column_symbols)) == 2:
                counts[1][1] += 1
        
        diagonal_symbols = [self.data[i][i] for i in range(min(self.number_of_rows, self.number_of_columns))]
        anti_diagonal_symbols = [self.data[i][self.number_of_columns - i - 1] for i in range(min(self.number_of_rows, self.number_of_columns))]
        if len(set(diagonal_symbols)) == 1:
            counts[2][0] += 1
        if len(set(anti_diagonal_symbols)) == 1:
            counts[2][0] += 1

        wins = counts

        return wins

    
