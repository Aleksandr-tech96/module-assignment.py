grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = sorted(students)
print(students_1)
grades_students = {'Aaron': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Johnny': [4, 5, 5, 2], 'Khendrik': [4, 4, 3], 'Steve': [5, 5, 5, 4, 5]}
print(grades_students)
Aaron = sum([5, 3, 3, 5, 4]) / len([5, 3, 3, 5, 4])
print(Aaron)
Bilbo = sum([2, 2, 2, 3]) / len([2, 2, 2, 3])
print(Bilbo)
Johnny = sum([4, 5, 5, 2]) / len([4, 5, 5, 2])
print(Johnny)
Khendrik = sum([4, 4, 3]) / len([4, 4, 3])
print(Khendrik)
Steve = sum([5, 5, 5, 4, 5]) / len([5, 5, 5, 4, 5])
print(Steve)
theAverageValue = {'Aaron': Aaron, 'Bilbo': Bilbo, 'Johnny': Johnny, 'Khendrik': Khendrik, 'Steve': Steve}
print(theAverageValue)