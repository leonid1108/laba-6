"""
Формируется матрица F следующим образом: скопировать в нее А и если в Е количество нулей
в нечетных столбцах больше, чем произведение чисел, то поменять в местами С и В симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: (A^(-1)*A^T – K*F^(-1)), иначе вычисляется выражение (A + G - F^T)*K,
где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А,
F и все матричные операции последовательно.
"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt

def print_matrix(Matrix, matrix_name, timetime):
    print(f"Матрица {matrix_name} промежуточное время = {round(timetime, 2)} seconds.")
    for i in Matrix:  # Делаем перебор всех строк матрицы
        for j in i:  # Деребираем все элементы в строке
            print("%5d" % j, end=" ")
        print()
print("\n-------Результат работы программы-------")
try:
    matrix_size = int(input("Введите количество строк (столбцов) квадратной матрицы больше 4 : "))
    while matrix_size < 4 or matrix_size > 100:
        matrix_size = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы больше 4 :"))
    K = int(input("Введите число К="))
    start = time.time()
    A = np.zeros((matrix_size, matrix_size))
    F = np.zeros((matrix_size, matrix_size))
    time_next = time.time()
    for i in range(matrix_size):  # Формируем матрицу А
        for j in range(matrix_size):
            A[i][j] = np.random.randint(-10, 10)
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)

    for i in range(matrix_size):    # Формируем матрицу F, копируя из матрицы А
        for j in range(matrix_size):
            F[i][j] = A[i][j]

    submatrix_size = matrix_size // 2    # Фазмерность подматрицы
    E = np.zeros((submatrix_size, submatrix_size))  # Формируем матрицу Е

    for i in range(submatrix_size):
        for j in range(submatrix_size):
            E[i][j] = A[i][j]

    kol_vo = 0
    multiplication = 1
    for i in range(0, submatrix_size, 1):
        for j in range(0, submatrix_size, 1):  # Обработка подматрицы Е
            if E[i][j] == 0 and j % 2 == 0:
                kol_vo += 1 # Подсчёт кол-ва нулей в нечётных столбцах

    for i in range(0, submatrix_size, 1):
        for j in range(0, submatrix_size, 1):
            if j % 2 == 0:
                multiplication *= E[i][j] # Произведение чисел в нечётных столбцах

    if kol_vo > multiplication:
        for i in range(0, submatrix_size + matrix_size % 2):  # Меняем подматрицы B и C местами симметрично
            for j in range(submatrix_size + matrix_size % 2, matrix_size):
                F[i][j], F[matrix_size - i - 1][j] = F[matrix_size - i - 1][j], F[i][j]
    else:
        for i in range(0, submatrix_size):  # Меняем подматрицы Е и С местами несимметрично
            for j in range(0, submatrix_size, 1):
                F[i][j], F[submatrix_size + matrix_size % 2 + i][submatrix_size + matrix_size % 2 + j] = F[submatrix_size + matrix_size % 2 + i][submatrix_size + matrix_size % 2 + j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0: # A или F вырожденая матрица,т.е вычислить нельзя
        print("A или F вырожденая матрица,т.е вычислить нельзя")
    elif np.linalg.det(A) > sum(F.diagonal()):
        A = ((np.dot(np.linalg.matrix_power(A, -1), np.transpose(A))) - (np.dot(K, np.linalg.matrix_power(F, -1))))
    else:
        A = np.dot((A + np.tril(A) - np.transpose(F)), K)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)


    plt.title('Examples', fontsize=15)
    plt.xlabel("Numbers", fontsize=13)
    plt.ylabel("Values", fontsize=13)
    plt.grid()
    plt.gcf().canvas.manager.set_window_title("Вывод значений")
    for j in range(matrix_size):
        plt.plot([i for i in range(matrix_size)], A[j][::], marker='8')
    plt.show()
    print(f"\nProgramm time {time.time() - start}")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.")
