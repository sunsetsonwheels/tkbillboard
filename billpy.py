from tkinter import messagebox
import billboard

def logDump(ex):
    dump = str(ex)
    log = open('log.txt','w')
    log.write("\n"+dump)
    log.close()

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
        import os
        import sys
        sys.stdout.flush()
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    
    def update():
        messagebox.showwarning("We're deleting everything in the billpy folder", "Make sure billpy is in its own folder, because updating will DELETE everything inside the folder where billpy is!")
        messagebox.showinfo("Have you got 'git' installed", "Updating/Reinstalling billpy relies on a program called git. If you have not got it installed, close this window.")
        import git
        import os
        from shutil import rmtree
        app_path = os.path.dirname(os.path.realpath(__file__))
        try:
            print("Update/Reinstall running.")
            print("[1/2] Deleting previous version of application.")
            rmtree(app_path)
            print("[2/2] Downloading and installing new version of application")
            os.mkdir(app_path)
            git.Git(app_path).clone("https://github.com/jkelol111/billpy.git")
            print("Update/Reinstall completed.")
            refresh()
        except Exception as e:
            logDump(e)
            messagebox.showerror("Bug reporter", "The application is facing an updating error. Please re-download this application or contact the developer at https://github.com/jkelol111/billpy/issues.")
            print("Exitting application because of 'Update Failed' exception.")
            exit()
    
    from tkinter import Label
    from tkinter import Button
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

    refresh_button = Button(billpy_window, text="Refresh charts", font=("Segoe UI Bold", 10), command=refresh)
    refresh_button.pack()

    about_button = Button(billpy_window, text="About", font=("Segoe UI Bold", 10), command=about)
    about_button.pack()

    update_button = Button(billpy_window, text="Update/Reinstall", font=("Segoe UI Bold", 10), command=update)
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
        messagebox.showerror("Bug reporter", "The application is facing an unknown error. Please re-download this application or contact the developer at https://github.com/jkelol111/billpy/issues.")
        print("Exitting application because of 'App' exception.")
except Exception as e:
    logDump(e)
    messagebox.showerror("No network connectivity", "There isn't any internet connections at the moment. Please try again later.")
    print("Done checking for network.")
    print("Exitting application because of 'No network' exception.")