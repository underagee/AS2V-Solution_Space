if __name__ == '__main__':
    student_records = []
    num_students = int(input())
    
    for _ in range(num_students):
        name = input()
        grade = float(input())
        student_records.append([name, grade])
    
    # Finding the second lowest grade
    sorted_grades = sorted(set([record[1] for record in student_records]))
    second_lowest_grade = sorted_grades[1]
    
    # Finding the names of students with the second lowest grade
    second_lowest_students = [record[0] for record in student_records if record[1] == second_lowest_grade]
    
    # Sorting the names alphabetically
    second_lowest_students.sort()
    
    # Printing the names of students with the second lowest grade
    for student in second_lowest_students:
        print(student)
