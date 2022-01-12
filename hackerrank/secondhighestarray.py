if __name__ == '__main__':

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    x = 100
    y = 100

second_highest = sorted(list(set([marks for name, marks in students])))[1]

print('\n'.join([a for a,b in sorted(students) if b == second_highest]))

# print([a for a,b in sorted(students) if b == second_highest])