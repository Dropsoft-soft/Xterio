from tkinter import *

if __name__ == '__main__':
  root = Tk()
  root.title('XTerio')
  root.geometry("500x600")
  root.resizable(height=False, width=False)

  labelFrame = LabelFrame(root, text="seeds")
  labelFrame.place(x=10, y=10, width=100, height=40)

  def select_file():
    print('select file')

  btn = Button(root, text="Select", command=select_file)
  btn.place(x=120, y=10, width=60, height=30)

  labelFrame2 = LabelFrame(root, text="proxies")
  labelFrame2.place(x=10, y=60, width=100, height=40)
  





  root.mainloop()


