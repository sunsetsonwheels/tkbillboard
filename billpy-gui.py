from tkinter import *
import http.client as httplib
from tkinter import messagebox
import billboard

print("Checking for network.")
conn = httplib.HTTPConnection("www.billboard.com", timeout=5)
try:
    conn.request("HEAD", "/")
    conn.close()
except:
    conn.close()
    messagebox.showerror("No network connectivity", "There isn't any internet connections at the moment. Please try again later.")
print("Done checking for network.")

print("Start refreshing charts.")
chart = billboard.ChartData("hot-100")
print("Done refreshing charts.")

print("Start listing songs.")
topSong1 = chart[0]
topSong2 = chart[1]
topSong3 = chart[2]
topSong4 = chart[3]
topSong5 = chart[4]
print("Done listing songs.")

def about():
    messagebox.showinfo("About billpy", "billpy is a wrapper for billboard.py and (not implimented yet) spotipy. This is a demo GUI version based on Tkinter.")

def error():
    messagebox.showwarning("Not here yet", "This function isn't implimented yet. Try again later.")

billpy_window = Tk()
billpy_window.title("billpy GUI")

topSong1_label = Label(billpy_window, text=topSong1, font=("Segoe UI", 14))
topSong1_label.pack()

topSong2_label = Label(billpy_window, text=topSong2, font=("Segoe UI", 14))
topSong2_label.pack()

topSong3_label = Label(billpy_window, text=topSong3, font=("Segoe UI", 14))
topSong3_label.pack()

topSong4_label = Label(billpy_window, text=topSong4, font=("Segoe UI", 14))
topSong4_label.pack()

topSong5_label = Label(billpy_window, text=topSong5, font=("Segoe UI", 14))
topSong5_label.pack()

refresh_button = Button(billpy_window, text="Refresh charts (not working yet)", font=("Segoe UI Bold", 10), command=error)
refresh_button.pack()

about_button = Button(billpy_window, text="About", font=("Segoe UI Bold", 10), command=about)
about_button.pack()

billpy_window.mainloop()
print("Exitting application.")

