import tkinter
from tkinter import messagebox as msbx

from calculations import create_solution
from plot import show


class Application:
    def __init__(self) -> None:
        self.root = tkinter.Tk()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 450
        window_width = 250
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width)

        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.maxsize(window_height, window_width)
        self.root.minsize(window_height, window_width)
        self.root.title("Differential equations course - project.")
        self.root.configure(bg='#A5E5C5')

        self.label = tkinter.Label(self.root, text="Heating transport equation", font=('Arial', 20), fg='#f00', bg='#A5E5C5')
        self.label.pack(padx=10, pady=30)

        self.label = tkinter.Label(self.root, text="Number of elements", bg='#A5E5C5')
        self.label.pack(side='top')

        self.entry = tkinter.Entry(self.root, justify='center')
        self.entry.pack(side='top', pady=5)

        self.button = tkinter.Button(self.root, justify='center', text="OK", height=1, width=8, fg='#fff', bg='#f00', command=self.solve_problem)
        self.button.pack(padx=20, pady=10)

        self.root.mainloop()

    def solve_problem(self):
        try:
            n = int(self.entry.get())
            if n < 3:
                raise Exception("Incorrect N - must be greater than 3!")

            x, y = create_solution(n)
            show(x, y, n)
        except:
             msbx.showwarning(title="Error", message="Incorrect input data!")
