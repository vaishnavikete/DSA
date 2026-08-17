
salary = [10000,23000,10004,10009,21000]

n = len(salary)

for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if salary[j] > salary[j + 1]:
            swap = salary[j]
            salary[j] = salary[j + 1]
            salary[j + 1] = swap
print("salary nin assending order")
print(salary)

for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if salary[j] > salary[max_index]:
            max_index = j

    salary[i], salary[max_index] = salary[max_index], salary[i]

print("Salaries in descending order:")
print(salary)
