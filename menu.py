from tkinter import *
from mem import memo, memo2
from focus import *
from mind import  *
from perception import *
import os
def remove():
	os.remove('files\pupilname')
	ws.destroy()
def menu():
	global ws
	ws = Tk()
	ws.title("Диагностика познавательных процессов")
	screen_width = ws.winfo_screenwidth()
	screen_height = ws.winfo_screenheight()
	x_cordinate = int((screen_width/2) - (500/2))
	y_cordinate = int((screen_height/2) - (600/2))
	ws.geometry("{}x{}+{}+{}".format(500,600,x_cordinate,y_cordinate))
	ws.attributes('-toolwindow', True)

	butmem = Button(ws, font=("Arial",18), text="Диагностика памяти", bg='White', fg='Black',command=lambda: (ws.destroy(), memo()))
	butfocus = Button(ws, font=("Arial",18), text="Диагностика внимания", bg='White', fg='Black',command=lambda:  (ws.destroy(),foc() ))
	butmind = Button(ws,  font=("Arial",18),text="Диагностика мышления", bg='White', fg='Black',command=lambda:(ws.destroy(),mind()))
	butperc = Button(ws,  font=("Arial",18),text="Диагностика восприятия", bg='White', fg='Black',command=lambda:(ws.destroy(),percep()))
	butmem.place(x=50,y=20, width=400, height=60)
	rule=Label(ws, text='У вас будет одна минута, чтобы запомнить как можно больше слов', font=("Arial",10))
	rule.place(x=10,y=80, width=500, height=30)
	butfocus.place(x=50,y=140, width=400, height=60)
	rule2=Label(ws, text='В квадрате в случайном порядке «разбросаны» числа от 101 до 136. \n Вам предстоит нажать на них в порядке возрастания от 101 до 136. ', font=("Arial",10))
	rule2.place(x=10,y=200, width=500, height=30)
	butmind.place(x=50,y=270, width=400, height=60)
	rule2=Label(ws, text='Необходимо в каждом ряду слов найти такое, \n которое является в этом ряду лишним', font=("Arial",10))
	rule2.place(x=10,y=330, width=500, height=30)
	butperc.place(x=50,y=400, width=400, height=60)
	rule2=Label(ws, text='Подберите такие узоры кусочков, которые более всего \n подходят к рисункам ковриков и впишите их номера', font=("Arial",10))
	rule2.place(x=10,y=460, width=500, height=30)
	butclose = Button(ws, font=("Arial",12), text="Завершить диагностику", bg='White', fg='Black',command=lambda: ( remove()))
	butclose.place(x=145,y=510, width=200, height=50)
	ws.mainloop()

