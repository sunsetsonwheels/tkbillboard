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
    topSong1 = str(chart[0])
    topSong2 = str(chart[1])
    topSong3 = str(chart[2])
    topSong4 = str(chart[3])
    topSong5 = str(chart[4])
    print("Done listing songs.")

    def about():
        messagebox.showinfo("About tkbillboard.py", "tkbillboard.py is a wrapper for billboard.py. This is a demo GUI version based on Tkinter. v 1.0")

    def refresh():
        import sys
        from os import execl
        from sys import executable
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
                from threading import Thread
                updateprogressBox = Toplevel(billpy_window)
                updateprogress_label = Label(updateprogressBox, text="Updating/Reinstalling the app, please wait...", font=("Segoe UI", 10))
                updateprogress_bar = Progressbar(updateprogressBox, orient="horizontal", length=200, mode="indeterminate")
                updateprogress_label.pack()
                updateprogress_bar.pack()
                updateprogress_bar.start()
                updater.configureConfigNow("me.jkelol111.tkbillboardpy", "https://github.com/jkelol111/tkbillboard.py.git", dirname(realpath(__file__)), "billpy.py", True, False)
                exeupdate = Thread(target=updater.updateNow())
                exeupdate.start()
                updateprogressBox.mainloop()
            except Exception as e:
                logDump(e)
                exit()
            updateprogressBox.destroy()
            messagebox.showinfo("Update was successful!", "The update process succeeded! Please click 'OK' to launch the new version.")
            refresh()
        elif confirmUpdate == "no":
            messagebox.showinfo("Update was cancelled!", "The update process was denied.")

    def customDate():
        def displayDialogCustomDate(date):
            enterDateBox.destroy()
            print("Start listing songs according to selected date.")
            global topSong1
            global topSong2
            global topSong3
            global topSong4
            global topSong5
            try:
                chart2 = billboard.ChartData("hot-100", date)
                topSong1 = str(chart2[0])
                topSong2 = str(chart2[1])
                topSong3 = str(chart2[2])
                topSong4 = str(chart2[3])
                topSong5 = str(chart2[4])
                message = "Chart of "+date+":\n"+"1. "+topSong1+"\n"+"2. "+topSong2+"\n"+"3. "+topSong3+"\n"+"4. "+topSong4+"\n"+"5. "+topSong5
                messagebox.showinfo("Chart on specific date", message)
                print("Done listing songs according to selected date.")
            except:
                messagebox.showerror("Out of range date", "Check your dates again.")
        enterDateBox = Toplevel(billpy_window)
        enterDateBox.title("Custom date entry")
        enterDateBox.focus_set()
        enterDate_msg = Label(enterDateBox, text="Enter the date below (YYYY-MM-DD):", font=("Segoe UI", 10))
        enterDate_entry = Entry(enterDateBox)
        enterDate_entry.focus_set()
        enterDate_confirm = Button(enterDateBox, text="OK", command=lambda: displayDialogCustomDate(enterDate_entry.get()))
        enterDate_cancel = Button(enterDateBox, text="Cancel", command=lambda: enterDateBox.destroy())
        enterDate_msg.pack()
        enterDate_entry.pack()
        enterDate_confirm.pack()
        enterDate_cancel.pack()
        enterDateBox.mainloop()

    def getTokenSpotify():
        try:
            from spotipy import oauth2
            from os.path import abspath
            clientid_app = "fd0faa7123584102b5893a4639ff7288"
            clientsecret_app = "347e543d63a94921b2455a26f0320481"
            redirecturi_app = "localhost"
            scope_app = "playlist-modify-private"
            authSpotify = oauth2.SpotifyOAuth(client_id=clientid_app, client_secret=clientsecret_app, redirect_uri=redirecturi_app, scope=scope_app, cache_path=abspath(__file__))
            print(authSpotify.get_authorise_url())
            print("ok")
        except:
            messagebox.showerror("Failed log in", "tkbillboard cannot log in to Spotify[R] at the moment.")
    def spotifyAddSongs():
        print("?")
    def getSpotifyLinks():
        from spotipy import oauth2
        from spotipy import Spotify
        cached_token = str("")
    
    from tkinter import Label
    from tkinter.ttk import Button
    from tkinter import Toplevel
    from tkinter.ttk import Entry
    from tkinter.ttk import Progressbar
    import webbrowser
    from tkinter import Menu
    from tkinter import Tk

    billpy_window = Tk()
    billpy_window.title("tkbillboard.py")
    billpy_window.wm_resizable(False, False)
    billpy_window["bg"] = "white"

    menubar = Menu(billpy_window)
    actionmenu = Menu(menubar, tearoff=0)
    actionmenu.add_command(label="Refresh charts...", command=refresh)
    actionmenu.add_command(label="See chart of custom date...", command=customDate)
    actionmenu.add_command(label="Add songs to Spotify[R]... (not yet working)")
    actionmenu.add_separator()
    actionmenu.add_command(label="Update/Reinstall...", command=update)
    menubar.add_cascade(label="Actions", menu=actionmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About tkbillboard.py...", command=about)
    helpmenu.add_separator()
    helpmenu.add_command(label="Send feedback to developer...", command=lambda: webbrowser.open("mailto:?to=vietbetatester@outlook.com&subject=Problem with FileSyncer3"))
    menubar.add_cascade(label="Help", menu=helpmenu)

    topSong1_label = Label(billpy_window, text="1. "+topSong1, font=("Segoe UI", 14))
    topSong1_label["bg"] = "white"
    topSong1_label.pack(anchor="nw")

    topSong2_label = Label(billpy_window, text="2. "+topSong2, font=("Segoe UI", 14))
    topSong2_label["bg"] = "white"
    topSong2_label.pack(anchor="nw")

    topSong3_label = Label(billpy_window, text="3. "+topSong3, font=("Segoe UI", 14))
    topSong3_label["bg"] = "white"
    topSong3_label.pack(anchor="nw")

    topSong4_label = Label(billpy_window, text="4. "+topSong4, font=("Segoe UI", 14))
    topSong4_label["bg"] = "white"
    topSong4_label.pack(anchor="nw")

    topSong5_label = Label(billpy_window, text="5. "+topSong5, font=("Segoe UI", 14))
    topSong5_label["bg"] = "white"
    topSong5_label.pack(anchor="nw")

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
