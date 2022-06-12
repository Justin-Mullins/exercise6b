'''

Excercise 6b

Write a function that transposes a list of string_list, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'] .

'''

def transpose(string_list):
    new_list = []
    index = 0
    # Convert the list of strings into a 2 dimentional list
    temp_list = list(map(lambda string: string.split(), string_list))
    for i in range(len(string_list)):
        new_list.append([])
    # Transpose the matrix values by switching the rows and columns.
    for row in range(len(temp_list)):
        for col in range(len(new_list)):
            new_list[index].append(temp_list[col][row])
        index += 1
    # Covnert 2 dimentional list back into list of strings.
    new_list = list(map(lambda x: ' '.join(x), new_list))
    return new_list

print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
