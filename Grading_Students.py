def gradingStudents(grades):
    answ=[]
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                answ.append(i+(5-(i%5)))
            else:
                answ.append(i)
        else:
            answ.append(i)
    return answ
