# Альтернатива:

# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

import random

n=int(input('Введите кол-во оценок Василия: '))
eval=[]
def inp_eval(n):
    for i in range(n):
        eval.append(random.randint(1,5))
    return eval
  
def change_max(arr,max):
    for i in range(n):
        if arr[i]==max:
            arr[i]=1
    return arr
eval=inp_eval(n)
max=max(eval) 
print(eval)
print(change_max(eval,max))
