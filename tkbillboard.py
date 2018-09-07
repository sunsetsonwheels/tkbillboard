from tkinter import messagebox
import billboard

def logDump(ex):
    dump = str(ex)
    print("Error has happened: "+dump)
    log = open('log.txt','w')
    log.write(dump+"\n")
    log.close()
    messagebox.showerror("App Exception", "The app will now close. \nError: "+dump)

def app():

    def centerForms(win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def about():
        messagebox.showinfo("About tkbillboard.py", "tkbillboard.py is a wrapper for billboard.py. This is a demo GUI version based on Tkinter. v 2.0")

    def refresh():
        sys.stdout.flush()
        execl(executable, abspath(__file__), *argv) 
    
    def update():
        chart_date.set("Updating app...")
        confirmUpdate = messagebox.askquestion("We're deleting everything in the billpy folder", "Make sure billpy is in its own folder, because updating will DELETE everything inside the folder where billpy is! If not, click No!", icon="warning")
        if confirmUpdate == "yes": 
            try:
                import updater
                updater.configureConfigNow("me.jkelol111.tkbillboardpy", "https://github.com/jkelol111/tkbillboard.py.git", dirname(realpath(__file__)), "billpy.py", True, False)
                updater.updateNow()
                chart_date.set("App restart required.")
                messagebox.showinfo("Update was successful!", "The update process succeeded! Please click 'OK' to launch the new version.")
                refresh()
            except Exception as e:
                logDump(e)
                exit()
        elif confirmUpdate == "no":
            date_object = datetime.now()
            formatted_date = "Chart data date: "+date_object.strftime('%Y-%m-%d')
            chart_date.set(formatted_date)
            messagebox.showinfo("Update was cancelled!", "The update process was denied.")

    def customDate():
        def displayCustomDate(date):
            enterDateBox.destroy()
            print("Start listing songs from: "+date+".")
            try:
                chart = billboard.ChartData("hot-100", date)
                label1 = str("1. "+str(chart[0]))
                label2 = str("2. "+str(chart[1]))
                label3 = str("3. "+str(chart[2]))
                label4 = str("4. "+str(chart[3]))
                label5 = str("5. "+str(chart[4]))
                topSong1.set(label1)
                topSong2.set(label2)
                topSong3.set(label3)
                topSong4.set(label4)
                topSong5.set(label5)
                chart_date.set("Chart data date: "+date)
                print("Done listing songs from: "+date+".")
            except Exception as e:
                logDump(e)
                messagebox.showerror("Out of range date", "Check your dates again.")

        def cancelDialog():
            enterDateBox.destroy()
            date_object = datetime.now()
            formatted_date = "Chart data date: "+date_object.strftime('%Y-%m-%d')
            chart_date.set(formatted_date)
            
        enterDateBox = Toplevel(billpy_window)
        enterDateBox.grab_set()
        enterDateBox.title("Custom date entry")
        enterDateBox.focus_set()
        enterDate_msg = Label(enterDateBox, text="Enter the date below (YYYY-MM-DD):", font=("Segoe UI", 10))
        enterDate_entry = Entry(enterDateBox)
        enterDate_entry.focus_set()
        enterDate_confirm = Button(enterDateBox, text="OK", command=lambda: displayCustomDate(enterDate_entry.get()))
        enterDate_cancel = Button(enterDateBox, text="Cancel", command=cancelDialog)
        enterDate_msg.pack()
        enterDate_entry.pack()
        enterDate_confirm.pack()
        enterDate_cancel.pack()
        centerForms(enterDateBox)
        chart_date.set("Loading charts...")
        enterDateBox.mainloop()
    
    from tkinter import Label
    from tkinter import Toplevel
    from tkinter.ttk import Button
    from tkinter.ttk import Entry
    from tkinter.ttk import Progressbar
    from tkinter import StringVar
    import webbrowser
    from tkinter import Menu
    from tkinter import Tk
    from os.path import dirname
    from os.path import realpath
    import sys
    from os import execl
    from sys import executable
    from sys import argv
    from os.path import abspath
    from datetime import datetime
    
    billpy_window = Tk()
    billpy_window.title("tkbillboard.py")
    billpy_window.wm_resizable(False, False)
    billpy_window.focus_set()
    billpy_window["bg"] = "white"

    menubar = Menu(billpy_window)
    actionmenu = Menu(menubar, tearoff=0)
    actionmenu.add_command(label="Refresh charts...", command=refresh)
    actionmenu.add_command(label="See chart of custom date...", command=customDate)
    actionmenu.add_separator()
    actionmenu.add_command(label="Update/Reinstall...", command=update)
    menubar.add_cascade(label="Actions", menu=actionmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About tkbillboard.py...", command=about)
    helpmenu.add_separator()
    helpmenu.add_command(label="Send feedback to developer...", command=lambda: webbrowser.open("mailto:?to=vietbetatester@outlook.com&subject=Problem with FileSyncer3"))
    menubar.add_cascade(label="Help", menu=helpmenu)

    print("Start listing songs.")
    topSong1 = StringVar()
    topSong2 = StringVar()
    topSong3 = StringVar()
    topSong4 = StringVar()
    topSong5 = StringVar()
    label1 = str("1. "+str(chart[0]))
    label2 = str("2. "+str(chart[1]))
    label3 = str("3. "+str(chart[2]))
    label4 = str("4. "+str(chart[3]))
    label5 = str("5. "+str(chart[4]))
    topSong1.set(label1)
    topSong2.set(label2)
    topSong3.set(label3)
    topSong4.set(label4)
    topSong5.set(label5)
    print("Done listing songs.")

    chart_date = StringVar()
    date_object = datetime.now()
    formatted_date = "Chart data date: "+date_object.strftime('%Y-%m-%d')
    chart_date.set(formatted_date)

    topSong1_label = Label(billpy_window, textvariable=topSong1, font=("Segoe UI", 14))
    topSong1_label["bg"] = "white"
    topSong1_label.pack(anchor="nw")

    topSong2_label = Label(billpy_window, textvariable=topSong2, font=("Segoe UI", 14))
    topSong2_label["bg"] = "white"
    topSong2_label.pack(anchor="nw")

    topSong3_label = Label(billpy_window, textvariable=topSong3, font=("Segoe UI", 14))
    topSong3_label["bg"] = "white"
    topSong3_label.pack(anchor="nw")

    topSong4_label = Label(billpy_window, textvariable=topSong4, font=("Segoe UI", 14))
    topSong4_label["bg"] = "white"
    topSong4_label.pack(anchor="nw")

    topSong5_label = Label(billpy_window, textvariable=topSong5, font=("Segoe UI", 14))
    topSong5_label["bg"] = "white"
    topSong5_label.pack(anchor="nw")

    chart_date_label = Label(billpy_window, textvariable=chart_date, font=("Segoe UI Bold", 8))
    chart_date_label["bg"] = "white"
    chart_date_label.pack(anchor="nw")

    billpy_window.config(menu=menubar)

    billpy_window.mainloop()
    print("Exitting application.")

print("Start refreshing charts.")
try:
    print("Checking for network.")
    chart = billboard.ChartData("hot-100")
    print("Done checking for network.")
    print("Done refreshing charts.")
    try:
        app()
    except Exception as e:
        logDump(e)
        print("Exitting application because of 'App' exception.")
except Exception as e:
    logDump(e)
    print("Done checking for network.")
    print("Exitting application because of 'No network' exception.")