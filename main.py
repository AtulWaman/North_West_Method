# North West Cornner Method
def take_2d(r, c):
    box = []
    for i in range(r):
        row_lst = []
        for j in range(c):
            var = int(input(f"enter the element  of cost matrix at a[{i}][{j}] :"))
            row_lst.append(var)
        box.append(row_lst)
    return box


def take_1d(x, str):
    lst = [int(input(f"Enter element {i + 1} for {str}: ")) for i in range(x)]
    return lst


def init():
    supply = take_1d(row, "supply")
    demand = take_1d(column, "demand")
    cost_matrix = take_2d(row, column)
    return cost_matrix, demand, supply


def print_cost_matrix():
    for lst in cost_matrix:
        print("     ")
        for item in lst:
            print(item, end="    ")
    print("\n")


def North_West(cost_matrix, supply, demand):
    print("ORIGINAL COST MATRIX")
    print_cost_matrix()
    total_cost = 0
    row_ledge = 0
    column_ledge = 0
    while row_ledge < len(supply) and column_ledge < len(demand):
        if supply[row_ledge] > demand[column_ledge]:
            allotment = demand[column_ledge]
            demand[column_ledge] = 0
            supply[row_ledge] = supply[row_ledge] - allotment
        elif supply[row_ledge] < demand[column_ledge]:
            allotment = supply[row_ledge]
            supply[row_ledge] = 0
            demand[column_ledge] = demand[column_ledge] - allotment
        else:
            allotment = demand[column_ledge]
            demand[column_ledge] = 0
            supply[row_ledge] = 0
        total_cost = total_cost + cost_matrix[row_ledge][column_ledge] * allotment
        value = cost_matrix[row_ledge][column_ledge] = cost_matrix[row_ledge][column_ledge]
        cost_matrix[row_ledge][column_ledge] = str(value) + "*" + str(allotment)
        if supply[row_ledge] == 0 and demand[column_ledge] > 0:
            row_ledge += 1
            continue
        elif demand[column_ledge] == 0 and supply[row_ledge] > 0:
            column_ledge += 1
        else:
            row_ledge += 1
            column_ledge += 1
    return total_cost


print(r'''
    _   __           __  __       _       __          __     ______                          
   / | / /___  _____/ /_/ /_     | |     / /__  _____/ /_   / ____/___  _________  ___  _____
  /  |/ / __ \/ ___/ __/ __ \    | | /| / / _ \/ ___/ __/  / /   / __ \/ ___/ __ \/ _ \/ ___/
 / /|  / /_/ / /  / /_/ / / /    | |/ |/ /  __(__  ) /_   / /___/ /_/ / /  / / / /  __/ /    
/_/ |_/\____/_/   \__/_/ /_/     |__/|__/\___/____/\__/   \____/\____/_/  /_/ /_/\___/_/     
                                                                                             
''')

row = int(input("Enter the number of Rows: "))
column = int(input("Enter the number of Columns: "))
cost_matrix, demand, supply = init()

if sum(demand) == sum(supply):
    print("total cost is ", North_West(cost_matrix, supply, demand))
else:
    print("not balance!! Thus this program cant not work with given matrix")
print("ALLOTMENTS")
print_cost_matrix()

# North_West(cost_matrix,supply,demand)
