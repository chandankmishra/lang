
import sys

from tkinter import*

# print (sys.version)
# print (sys.executable)
# print (sys.path)
# root = Tk()
# frame = Frame(root)
# frame.pack()
# root.title('Calculator')
# root.mainloop()


def main():
    root = Tk()
    # frame = Frame(root)
    # frame.pack()
    root.title('Calculator')
    root.minsize(width=300, height=300)
    root.maxsize(width=400, height=350)
    button = Button(root, text="Click Me!", width=20, height=20)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
