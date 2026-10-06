'''
Notas:
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2. Es ver cuanto crece el numero de 
operaciones en mi algoritmo conforme 
crece el tamaño de la entrada
Agrego las BigO identicas
Teniendo en cuenta la Cota superior asintotica
O(n) + O(4) = O(4 + n) = O(n)
'''


# Creando una lista de estudiantes
student_list_01 = ['Jordan', 'Pipen', 'Curry', 'Shark']
student_list_02 = ['Mike', 'Saul', 'Walter', 'Jessy']

#Verificando la precencia de un estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # O(n)
            print("✅ Estudiante encontrado") # O(1)
            return student 
    # Si no encuentro al estudiantw.
    print("✖️ Estudiante no encontrado") # O(1)
    return None # O(1)
# Probando algoritmo
check_student("Walter", student_list_01)