# Student Marks Data Analysis System
# Pure Python - No External Libraries

FILE_NAME = "students.csv"

def read_data():
    students = []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(",")
            students.append([data[0], int(data[1]), int(data[2]), int(data[3])])
    return students

def display_students(students):
    print("\nName\tMaths\tScience\tEnglish")
    print("-" * 30)
    for s in students:
        print(s[0], "\t", s[1], "\t", s[2], "\t", s[3])

def analyze_students(students):
    print("\nStudent Analysis")
    print("-" * 40)
    for s in students:
        total = s[1] + s[2] + s[3]
        avg = total / 3
        result = "PASS" if avg >= 40 else "FAIL"
        print(f"{s[0]} | Total: {total} | Avg: {avg:.2f} | {result}")

def class_topper(students):
    topper = ""
    highest = 0
    for s in students:
        total = s[1] + s[2] + s[3]
        if total > highest:
            highest = total
            topper = s[0]
    print("\nClass Topper:", topper, "with", highest, "marks")

def subject_topper(students):
    subjects = ["Maths", "Science", "English"]
    for i in range(1, 4):
        high = 0
        topper = ""
        for s in students:
            if s[i] > high:
                high = s[i]
                topper = s[0]
        print(subjects[i-1], "Topper:", topper, "(", high, ")")

def rank_list(students):
    totals = []
    for s in students:
        totals.append([s[0], s[1] + s[2] + s[3]])
    totals.sort(key=lambda x: x[1], reverse=True)
    print("\nRank List")
    for i, t in enumerate(totals, start=1):
        print(i, ".", t[0], "-", t[1])

def menu():
    while True:
        print("\n===== STUDENT MARKS DATA ANALYSIS =====")
        print("1. Display Student Data")
        print("2. Student Total & Average")
        print("3. Class Topper")
        print("4. Subject-wise Topper")
        print("5. Rank List")
        print("6. Exit")
        choice = input("Enter choice: ")
        students = read_data()
        if choice == "1":
            display_students(students)
        elif choice == "2":
            analyze_students(students)
        elif choice == "3":
            class_topper(students)
        elif choice == "4":
            subject_topper(students)
        elif choice == "5":
            rank_list(students)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

menu()
