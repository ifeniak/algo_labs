

def find_ways(matrix: [()], width: int, height: int):
    ways_num = [[0 for _ in range(width)] for i in range(height)]
    letters = {}
    for i in range(height):
        letters[matrix[i][0]] = 0
    for i in range(height):
        ways_num[i][0] = 1
        letters[matrix[i][0]] += 1

    def find_new_starts(lim):
        if lim == width:
            return
        letters_in_column = {}
        for k in range(height):
            letter = matrix[k][lim]
            if letter not in letters:
                letters[letter] = 0
            if letter not in letters_in_column:
                letters_in_column[letter] = 0
            ways_num[k][lim] += letters[letter]
            if letter != matrix[k][lim - 1]:
                ways_num[k][lim] += ways_num[k][lim - 1]
            letters_in_column[letter] += ways_num[k][lim]

        for letter in letters_in_column:
            letters[letter] += letters_in_column[letter]

    for vertical in range(1, width):
        find_new_starts(vertical)
    if height == 1:
        return ways_num[0][width - 1]
    return ways_num[0][width - 1] + ways_num[height - 1][width - 1]


matrix1 = [
    ["a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a"]
]


# matrix1 = [
#     ["a", "b", "c", "d", "e", "f", "a", "g", "h", "i"]
# ]
print(find_ways(matrix1, 7, 6))
