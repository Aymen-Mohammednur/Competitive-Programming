def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if (grades[i] < 38):
            continue
        temp = grades[i] % 5
        if (temp >= 3):
            grades[i] = grades[i] + (5 - temp)

    return grades
