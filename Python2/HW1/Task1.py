# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_quest(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Это равносторонний треугольник")
        else:
            if a == b or a == c or b == c:
                print("Это равнобедреный треугольник")
            else: print("Это разносторонний треугольник")
    else: print("Это не треугольник")

x = int(input("Введите первое значание: "))
y = int(input("Введите второе значание: "))
z = int(input("Введите третье значание: "))
triangle_quest(x, y, z)
