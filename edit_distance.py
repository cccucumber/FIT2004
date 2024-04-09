# https://stackoverflow.com/a/65544359

# Time Complexity: O(f*s), where f is the length of the first string, and s is the length of the second string
# Auxiliary Space: O(f*s), where f is the length of the first string, and s is the length of the second string
def edit_distance(first_string, second_string):
    m = len(first_string) + 1
    n = len(second_string) + 1

    distance = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[j][i] = i
            elif first_string[i - 1] == second_string[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i][j - 1],      # insert
                                         distance[i - 1][j],      # remove
                                         distance[i - 1][j - 1])  # replace

    return distance[m - 1][n - 1]

if __name__ == "__main__":
    first_string, second_string = "edit", "reddit"
    print(f"first string: {first_string}\nsecond string: {second_string}\nedit distance: {edit_distance(first_string, second_string)}")
