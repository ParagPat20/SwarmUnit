from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, messagebox, StringVar, font
from dashboard import Dashboard
from control import Control
from edit_mission import EDIT
from Initialization import Initialize
from formation import Formation
import login
from saves import logger, MapApplication
from saves import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path('./mainWindow_assets')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainWindow():
    MainWindow()

class MainWindow(Toplevel):
    
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("SwarmUnit")

        self.geometry("1500x760+5+0")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=760,
            width=1500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            200.0,
            0.0,
            1500.0,
            760.0,
            fill="#FFFFFF",
            outline=""
        )

        self.canvas.create_text(
            20.0,
            30.0,
            anchor="nw",
            text="OxiTech",
            fill="#FFFFFF",
            font=("Montserrat Bold", 36 * -1)
        )

        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
        self.dash_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.dash_btn, "dash"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.dash_btn.place(
            x=7.0,
            y=192.0,
            width=193.0,
            height=47.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.init_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.init_btn, "init"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.init_btn.place(
            x=7.0,
            y=145.0,
            width=193.0,
            height=47.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.form_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.form_btn, "form"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.form_btn.place(
            x=7.0,
            y=239.0,
            width=193.0,
            height=47.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.ctrl_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.ctrl_btn, "ctrl"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.ctrl_btn.place(
            x=7.0,
            y=286.0,
            width=193.0,
            height=47.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat"
        )
        self.logout_btn.place(
            x=0.0,
            y=713.0,
            width=200.0,
            height=47.0
        )

        self.canvas.create_rectangle(
            249.0,
            42.0,
            549.0,
            342.0,
            fill="#EFEFEF",
            outline="")
        
        
        self.canvas.create_rectangle(
            249.0,
            42.0,
            549.0,
            342.0,
            fill="#EFEFEF",
            outline="")
        
        self.map_app = MapApplication(self)
        self.map_app.map_widget.place(x=-350.0, y=-190.0, width=295.0, height=295.0)

        self.canvas.create_rectangle(
            587.0,
            119.0,
            1476.0,
            342.0,
            fill="#000000",
            outline="")
        
        self.log_text = Text(
            self.canvas,
            wrap="word",
            font=("Montserrat Bold", 20),
            bg="#000000",
            relief="flat",
            state="disabled"
        )
        self.log_text.place(x=587.0, y=119.0, width=889.0, height=223.0)

        self.log_text_sec = Text(
            self.canvas,
            wrap="word",
            font=("Montserrat Bold", 20),
            bg="#FFFF00",
            relief="flat",
            state="disabled"
        )
        self.log_text_sec.place(x=1185.0, y=42.0, width=300.0, height=300.0)
        logger.set_log_text_sec(self.log_text_sec)

        # Pass the log_text to the logger
        logger.set_log_text(self.log_text)
        logger_thread = threading.Thread(target=logger.logger_server)
        logger_thread.start()

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            1445.0,
            53.0,
            image=image_image_1
        )
        bold_font = font.Font(family='Gill Sans Ultra Bold', weight='bold', size=50)

        self.canvas.create_text(
            587.0,
            33.0,
            anchor="nw",
            text="SWARM CONTROL",
            fill="#5E95FF",
            font=(bold_font, 64 * -1)
        )
        self.current_window = Initialize(self)

        
        self.windows = {

            "init": Initialize(self),
            "dash": Dashboard(self),
            "ctrl": EDIT(self),
            "form": Formation(self)
            
        }

        self.sidebar_indicator.place(x=0, y=133)


        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()
    
    def place_sidebar_indicator(self):
        pass


    def logout(self):
        confirm = messagebox.askyesno(
            "Confirm log-out", "Do you really want to log out?"
        )
        if confirm == True:
            self.destroy()
            login.loginWindow()

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        if name == 'dash':
            self.current_window = Dashboard(self)
        elif name == 'init':
            self.current_window = Initialize(self)
        elif name == 'ctrl':
            self.current_window = EDIT(self)
        elif name == 'form':
            self.current_window = Formation(self)
        
        # Place the new window
        self.current_window.place(x=200, y=390, width=1300.0, height=370.0)
        self.animate_slide_in()

    def animate_slide_in(self):
        # Animate the sliding in of the window
        height = 370.0
        y = 760

        def update_position():
            nonlocal y
            y -= height / 15  # Adjust the speed by changing the divisor

            self.current_window.place(x=200, y=y, width=1300.0, height=height)
            self.update()

            if y > 390:  # Adjust the final position as needed
                self.after(10, update_position)  # Adjust the delay as needed for speed

        update_position()


    def handle_dashboard_refresh(self):
        # Recreate the dash window
        self.windows["init"] = Initialize(self)
