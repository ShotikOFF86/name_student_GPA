list_of_ratings = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
name_student = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
A=list_of_ratings[0]
GPA_A = (sum(A)/len(A))
B=list_of_ratings[1]
GPA_B = (sum(B)/len(B))
D=list_of_ratings[2]
GPA_D = (sum(D)/len(D))
S=list_of_ratings[3]
GPA_S = (sum(S)/len(S))
H=list_of_ratings[4]
GPA_H = (sum(H)/len(H))
name_student_GPA = {"Средний балл Аарон" : GPA_A,
                    "Средний балл Бильбо" : GPA_B,
                    "Средний балл Джонни" : GPA_D,
                    "Средний балл Стив" : GPA_S,
                    "Средний балл Хендрик" : GPA_H}
print(name_student_GPA)