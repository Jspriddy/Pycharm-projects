try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Grit Demo")
mainWindow.geometry('640x480+8+400')
mainWindow['padx'] = 20

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(mainWindow)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2, relief='sunken')
for zone in os.listdir('/usr/bin'):
    file_list.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=file_list.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscrollcommand'] = listScroll.set

option_frame = tkinter.LabelFrame(mainWindow, text='File Details')
option_frame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(2)
radio1 = tkinter.Radiobutton(option_frame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Widget to display the result
result_label = tkinter.Label(mainWindow, text="Result")
result_label.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
time_frame = tkinter.LabelFrame(mainWindow, text="Time")
time_frame.grid(row=3, column=0, sticky= 'new')
# Time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=':').grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
time_frame['padx'] = 36

# Frame for date spinners
date_frame = tkinter.Frame(mainWindow)
date_frame.grid(row=4, column=0, sticky='new')
# Date labels
day_label = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")
day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')
# Date spinners
month_spinner = tkinter.Spinbox(date_frame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May",
                                                             "June", "July", "Aug", "Sept", "Oct",
                                                             "Nov", "Dec"))
day_spinner = tkinter.Spinbox(date_frame, width=5, values=tuple(range(1, 32)))
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=1970, to=2050)

day_spinner.grid(row=1, column=0)
month_spinner.grid(row=1, column=1)
year_spinner.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Close", command=mainWindow.destroy)

okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

print(rbValue.get())