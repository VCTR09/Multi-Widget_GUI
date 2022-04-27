from tkinter import *

# Создаем объект окна верхнего уровня от класса Tk
window = Tk()
window.title("Converter")  

def from_kg():
    # Получаем пользовательское значение из поля ввода и умножаем на нужную величину, чтобы получить кг, фунты, унции
    grams = float(e2_value.get()) * 1000
    pounds = float(e2_value.get()) * 2.20462
    ounces = float(e2_value.get()) * 35.274

    # Очистим текстовые поля, если в них есть данные от предидущего использования, и заполним их снова
    t1.delete("1.0", END)  # Удаляет содержимое текстового поля от начала до конца
    t1.insert(END, grams)  # Заполняет текстовое поле значением переменной gram
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

# Создаем виджет кнопки
# Функция from_kg() вызывается при нажатии данной кнопки
b1 = Button(window, text='Convert', command=from_kg)
b1.grid(row=0,column=2)

# В окне приложения расположим виджет метки, обозначенный "Kg" 
e1=Label(window,text="Kg")
e1.grid(row=0,column=0) # Метка размещается в позиции 0, 0 в окне

e2_value = StringVar() # Создаем специальный объект StringVar
e2 = Entry(window, textvariable=e2_value) # Создаем поле ввода для пользователей, для ввода значений
e2.grid(row=0,column=1)

# Создаем три пустых текстовых поля, t1, t2 и t3
t1 = Text(window, height=1, width=20)
t1.grid(row=1,column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1,column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1,column=2)

# Данный код нужен для того, чтобы главное окно оставалось открытым
window.mainloop()
