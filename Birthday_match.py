import csv
record = []
with open("C:/Users/kssrivas/Desktop/New folder/Python_practice/Introduction to Algorithms/Lec-1_students.csv",'r',encoding='utf-8') as file:
    students = csv.reader(file)
    for row in students:
        record.append(row)

def Birthday_match(record):
    n = len(record)
    for k in range(n):
        [Name1, Birthday1] = record[k]
        for i in range(k):
            [Name2, Birthday2] = record[i]
            if Birthday1 == Birthday2:
                return [Name1, Name2]
        record[k]=[Name1, Birthday1]
    return None
result = Birthday_match(record)
print(result)
