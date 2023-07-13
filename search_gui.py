from tkinter import *
from tkinter import ttk
from file_search import FileSearch


def search(start="", end="", keys="", path=""):
    print("Searching")

    start = start_date.get()
    end = end_date.get()
    keys = keywords.get()
    path = file_path.get()

    key_list = keys.split(",")
    print(start, end, key_list, path)

    file_search = FileSearch(path, key_list, start, end)
    file_search.file_search()


root = Tk()
root.title("Search for Files containing Keywords")

mainframe = ttk.Frame(root, padding="30 30 150 150")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

start_date = StringVar()
start_date_entry = ttk.Entry(mainframe, width=50, textvariable=start_date)
start_date_entry.grid(column=3, row=1, columnspan=2, sticky=W)
ttk.Label(mainframe, text="Start Date - YYYY-MM-DD").grid(column=2, row=1, sticky=E)

end_date = StringVar()
end_date_entry = ttk.Entry(mainframe, width=50, textvariable=end_date)
end_date_entry.grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="End Date - YYYY-MM-DD").grid(column=2, row=2, sticky=E)

keywords = StringVar()
keywords_entry = ttk.Entry(mainframe, width=50, textvariable=keywords)
keywords_entry.grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Keywords").grid(column=2, row=3, sticky=E)

file_path = StringVar()
file_path_entry = ttk.Entry(mainframe, width=50, textvariable=file_path)
file_path_entry.grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="File Path").grid(column=2, row=4, sticky=E)

ttk.Button(mainframe, text="Submit", command=search).grid(column=3, row=6, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15)

start_date_entry.focus()
root.bind("<Return>", search)

root.mainloop()


# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
#     except ValueError:
#         pass


# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="30 30 120 120")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(
#     column=3, row=3, sticky=W
# )

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()
