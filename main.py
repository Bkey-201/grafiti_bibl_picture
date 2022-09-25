from tkinter import *

root1 = Tk() #создание окна

#create titel
root1.title("Canvas print line GaMoy") #пишем заголовок

#size
root1.geometry('500x500') #размер окошка(проги)

def paint(zalk):

    x1,y1,x2,y2 = (zalk.x - 50), (zalk.y - 20), (zalk.x + 30), (zalk.y +30)

    color = '#000fff000'

    wulf.create_line(x1,y1,x2,y2, fill = color )

wulf = Canvas(root1, width = 500, height=450) #Область рисование

wulf.bind("<M1-Motion>", paint)

# create label.
lab = Label(root1, text="Paint line")
lab.pack()
wulf.pack()

mainloop()
