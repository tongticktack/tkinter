import tkinter as tk
import redis
from math import factorial

def is_even(n) -> bool:
    try:
        n = int(n)
    except:
        n = 0
    if n % 2 == 0:
        return True
    return False


def process(n) -> None:
    if(is_even(n)):
        lbl.config(text=f'{n} is even')
    else:
        lbl.config(text=f'{n} is not even')


# conn = redis.Redis(host='localhost', port=6379)

main_window = tk.Tk()
main_window.title('Test 01')
main_window.geometry('400x300+0+0')



lbl = tk.Label(main_window, text='Hi')
lbl.grid(column=0, row=0, columnspan=2)

txt = tk.Entry(main_window)
txt.grid(column=1, row=1)

lbl2 = tk.Label(main_window, text='Enter the number :')
lbl2.grid(column=0,row=1)

btn = tk.Button(main_window, text="Button", command=lambda : process(txt.get()))
btn.grid(column=0, row=2, columnspan=2)

main_window.mainloop()