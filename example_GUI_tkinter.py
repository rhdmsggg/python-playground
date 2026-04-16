import tkinter

window = tkinter.Tk()

window.title('FUNKING GUI')
window.geometry('500x500')
window.resizable(False, False)  # 창크기 조절 여부(상하, 좌우)

"""
  - 내부 여백은 Label(...)
  - 바깥 여백은 pack(...) 에 넣어야 합니다.
"""

label = tkinter.Label(window, text= "sefdsfsefdsㅇㅇㅇㅇㅇfsef",width=100, height=20, fg='blue', relief='solid')
label.pack(padx= 10, pady= 10)

label2 = tkinter.Label(window, text="여기도", width=10, height=5, fg='blue', relief='solid')
label2.pack()

window.mainloop()