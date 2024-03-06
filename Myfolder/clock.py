import tkinter as tk
import time
import datetime

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Bootstyle

class ClockFrame:
    def __init__(self,frame):
        style_color = INFO
        Bootstyle.ttkstyle_widget_color(INFO)

        self.frame = frame
        self.frameweek = ttk.Frame(self.frame)
        self.frameweek.pack(side=BOTTOM)
        self.week_label = tk.Label(self.frameweek, text="")
        self.week_label.pack(side=RIGHT)

        self.framedate = ttk.Frame(self.frame)
        self.framedate.pack(side=BOTTOM)
        self.date_label = tk.Label(self.framedate, text="")
        self.date_label.pack(side=RIGHT)


        self.frametime = ttk.Frame(self.frame)
        self.frametime.pack(side=BOTTOM)
        self.time_label = tk.Label(self.frametime, text="",font={'size':24})
        self.time_label.pack(side=RIGHT)


        self.after_id_time = None
        self.after_id_date = None
        self.after_id_week = None
        self.update_time()
        self.update_date()
        self.update_week()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        # self.destroy()
        self.after_id_time = self.time_label.after(1000, self.update_time)
    def update_date(self):
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        self.date_label.config(text=current_date)
        # self.destroy()
        self.after_id_date = self.date_label.after(1000, self.update_date)
    def update_week(self):
        current_week = datetime.date.today().strftime('%A')
        self.week_label.config(text=current_week)
        # self.destroy()
        self.after_id_week = self.date_label.after(1000, self.update_week)
    def destroy(self):
        if self.after_id_time:
            self.time_label.after_cancel(self.after_id_time)
        if self.after_id_date:
            self.date_label.after_cancel(self.after_id_date)
        if self.after_id_week:
            self.week_label.after_cancel(self.after_id_week)
if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    app = ClockFrame(frame)
    root.mainloop()



