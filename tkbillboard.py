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
        
    print("Start listing songs.")
    topSong1 = chart[0]
    topSong2 = chart[1]
    topSong3 = chart[2]
    topSong4 = chart[3]
    topSong5 = chart[4]
    print("Done listing songs.")

    def about():
        messagebox.showinfo("About billpy", "billpy is a wrapper for billboard.py. This is a demo GUI version based on Tkinter. v 1.0")

    def refresh():
        import sys
        from os import execl
        from sys import executable
        from os.path import abspath
        from sys import argv
        sys.stdout.flush()
        execl(executable, abspath(__file__), *argv) 
    
    def update():
        confirmUpdate = messagebox.askquestion("We're deleting everything in the billpy folder", "Make sure billpy is in its own folder, because updating will DELETE everything inside the folder where billpy is! If not, click No!", icon="warning")
        if confirmUpdate == "yes": 
            try:
                import updater
                from os.path import dirname
                from os.path import realpath
                updater.configureConfigNow("me.jkelol111.tkbillboardpy", "https://github.com/jkelol111/tkbillboard.py.git", dirname(realpath(__file__)), "billpy.py", True, False)
                updater.updateNow()
            except Exception as e:
                logDump(e)
                exit()
            messagebox.showinfo("Update was successful!", "The update process succeeded! Please click 'OK' to launch the new version.")
            refresh()
        elif confirmUpdate == "no":
            messagebox.showinfo("Update was cancelled!", "The update process was denied.")

    def customDate():

        parsed_date = date.replace("")
        print("Start listing songs according to selected date.")
        global topSong1
        global topSong2
        global topSong3
        global topSong4
        global topSong5
        chart2 = billboard.ChartData("hot-100", parsed_date)
        topSong1 = chart2[0]
        topSong2 = chart2[1]
        topSong3 = chart2[2]
        topSong4 = chart2[3]
        topSong5 = chart2[4]
        message = "1. "+topSong1+"\n"+"2. "+topSong2+"\n"+"3. "+topSong3+"\n"+"4. "+topSong4+"\n"+"5. "+topSong5
        messagebox.showinfo("Chart on specific date", message)
        print("Done listing songs according to selected date.")
    
    from tkinter import Label
    from tkinter.ttk import Button
    from tkinter import Tk

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

    refresh_button = Button(billpy_window, text="Refresh charts", command=refresh)
    refresh_button.pack()

    spotify_button = Button(billpy_window, text="Add songs to Spotify[R] (not implimented)")
    spotify_button.pack()

    customdate_button = Button(billpy_window, text="See chart on specific date (not implimented)")
    customdate_button.pack()

    about_button = Button(billpy_window, text="About", command=about)
    about_button.pack()

    update_button = Button(billpy_window, text="Update/Reinstall", command=update)
    update_button.pack()

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
