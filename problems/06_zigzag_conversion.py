class Solution:
    def convert(self, string: str, numRows: int) -> str:
        word_length = len(string)
        n_rows = numRows

        total_all_filled_cols = 1 + (word_length - 1) // (2 * n_rows - 2)
        total_single_filled_cols = total_all_filled_cols * (n_rows - 2)
        total_cols = total_all_filled_cols + total_single_filled_cols

        start = n_rows + 1
        stop = start + (n_rows - 1) * (total_all_filled_cols - 1) + 1
        step = n_rows - 1
        zigzag_values = list(reversed(range(start, stop, step)))

        table = [['' for j in range(total_cols)] for i in range(n_rows)]

        string = list(reversed(string))
        value = 0
        for j in range(total_cols):
            count = (j) % (n_rows-1)
            if count == 0:
                value = zigzag_values.pop()

            for i in range(n_rows):
                print(i+1,j+1)
                print(value)
                print(string)
                try:
                    if count > 0:
                        print('single')
                        if (i + j + 2) == value:
                            letter = string.pop()
                            table[i][j] = letter
                    else:
                        print('full')
                        letter = string.pop()
                        print(letter)
                        table[i][j] = letter
                except:
                    table[i][j] = ''
            count += 1

        print(table[0])
        print(table[1])
        print(table[2])
        zigzag_word = ''
        for row in table:
            zigzag_word += ''.join(row)

        return zigzag_word
