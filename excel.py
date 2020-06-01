import numpy as np
import os
import pandas as pd
import matplotlib as plt
os.chdir("C:/Users/ivand/github/HSEProject")
import interface.py as int
SMARTPHONES = pd.read_excel('./Data/Smartphones.xlsx')
#print(SMARTPHONES)
Q = pd.DataFrame(SMARTPHONES).T
print(Q)








































#print('Возможные варианты ввода: ', Q.columns)
#e = input("Введите атрибут: ")
#t = input("Введите атрибут: ")
#while e != 'стоп':
#	if e in Q.columns:
#		print(Q[e])
#	else:
#		print('Нет такого атрибута')
#	e = input("Введите атрибут: ")
