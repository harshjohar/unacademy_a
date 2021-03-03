# Correct this function so that the correct output is given
def get_distinct_fractions(arr):    # arr is list of tuples
    inf_n = -10000000000
    inf_p = 10000000000
    result = []
    database = {}
    keys = []
    for i in range(0, len(arr)):
        numerator = arr[i][0]
        denominator = arr[i][1]
        # infinity
        if denominator == 0:
            # -ve infinity
            if numerator < 0:
                if inf_n in database:
                    if numerator > database[inf_n][0]:
                        database[inf_n][0] = numerator
                else:
                    keys.append(inf_n)
                    database[inf_n] = [numerator, 0]
            # +ve infinity
            elif numerator > 0:
                if inf_p in database:
                    if numerator < database[inf_p][0]:
                        database[inf_p][0] = numerator
                else:
                    keys.append(inf_p)
                    database[inf_p] = [numerator, 0]     
        # other fractions
        else:
            value = numerator/denominator
            if value in database:
                if numerator > 0:
                    if denominator > 0:
                        # +/+
                        if database[value][0] < 0:
                            database[value][0] = numerator
                            database[value][1] = denominator

                        if numerator < database[value][0]:
                            database[value][0] = numerator
                            database[value][1] = denominator
                    else:
                        # +/-
                        if database[value][0] > 0:
                            if numerator < database[value][0]:
                                database[value][0] = numerator
                                database[value][1] = denominator
                else:
                    if denominator > 0:
                        # -/+
                        if database[value][0] > 0:
                            database[value][0] = numerator
                            database[value][1] = denominator
                        if numerator > database[value][0]:
                            database[value][0] = numerator
                            database[value][1] = denominator 
                    else:
                        # -/-
                        pass
            else:
                keys.append(value)
                database[value] = [numerator, denominator]
    keys.sort()
    for i in keys:
        result.append([database[i][0], database[i][1]])
    # print(database)
    return result
# ----------------------Do not change anything below this line --------------------------
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))
 
result = get_distinct_fractions(arr)
print(len(result))
for x in result:
    print(x[0], x[1], end = ' ')