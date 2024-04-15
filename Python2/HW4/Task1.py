# Напишите функцию для транспонирования матрицы

def transp_matrix(lis_mtx):
   fin_matrix = [list(row) for row in zip(*lis_mtx)]
   print(fin_matrix) 


mtx_a = [[1, 4, 5], 
         [2, 6, 3]]

transp_matrix(mtx_a)