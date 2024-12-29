# подключение модулей
from tkinter import Tk, Canvas
# создание окна
root = Tk()
root.title('Ель')
root.geometry('400x300')

# создание холста
holst=Canvas(root,bg='white',width=400,height=300)

# рисуем ствол
holst.create_rectangle(180,240,210,280,outline='black',width='2',fill='brown')

# рисуем нижний ярус ёлки
holst.create_polygon(120,240,195,150,270,240,outline='black',width='2',fill='green')

# рисуем средний ярус ёлки
holst.create_polygon(140,200,195,130,250,200,outline='black',width='2',fill='green')

# рисуем верхний ярус ёлки
holst.create_polygon(160,160,195,70,230,160,outline='black',width='2',fill='green')

# отображаем холст
holst.pack()

#запускаем приложение
root.mainloop()