from tkinter import *
import tkinter.messagebox as mb
import random


guess_number = []
guessed_numbers = ''



def generate_random_number():
    for i in range(6):
        guess_number.append(str(random.randint(0,9)))

def btn_click(number):
    global guessed_numbers, guess_number
    if number == guess_number[0]:
        guess_number.pop(0)
        guessed_numbers += number
        title['text'] = str(guessed_numbers) + '*' * len(guess_number)
        if not guess_number:
            mb.showinfo(title='Победа', message='Вы угадали число: ' + guessed_numbers)
            guessed_numbers = ''
            title['text'] = '******'
            generate_random_number()


generate_random_number()

root = Tk()
root['bg'] = 'yellow'
root.title('Угадай число')
root.wm_attributes('-alpha', 0.96)
root.geometry('450x570')
root.resizable(width=False, height=False)

frame = Frame(root, bg='lightblue')
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

title = Label(frame, text='******', bg='white', font=40)
title.place(x=130, y=140, width=190, height=40)

btn1 = Button(frame, text='1', bg='purple', command=lambda: btn_click('1'))
btn1.place(x=130, y=200, width=50, height=50)
btn2 = Button(frame, text='2', bg='purple', command=lambda: btn_click('2'))
btn2.place(x=200, y=200, width=50, height=50)
btn3 = Button(frame, text='3', bg='purple', command=lambda: btn_click('3'))
btn3.place(x=270, y=200, width=50, height=50)
btn4 = Button(frame, text='4', bg='purple', command=lambda: btn_click('4'))
btn4.place(x=130, y=270, width=50, height=50)
btn5 = Button(frame, text='5', bg='purple', command=lambda: btn_click('5'))
btn5.place(x=200, y=270, width=50, height=50)
btn6 = Button(frame, text='6', bg='purple', command=lambda: btn_click('6'))
btn6.place(x=270, y=270, width=50, height=50)
btn7 = Button(frame, text='7', bg='purple', command=lambda: btn_click('7'))
btn7.place(x=130, y=340, width=50, height=50)
btn8 = Button(frame, text='8', bg='purple', command=lambda: btn_click('8'))
btn8.place(x=200, y=340, width=50, height=50)
btn9 = Button(frame, text='9', bg='purple', command=lambda: btn_click('9'))
btn9.place(x=270, y=340, width=50, height=50)
btn0 = Button(frame, text='0', bg='purple', command=lambda: btn_click('0'))
btn0.place(x=200, y=410, width=50, height=50)

if __name__ == '__main__':
    root.mainloop()
