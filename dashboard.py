from pathlib import Path

from tkinter import Canvas, Entry, Text, Button, PhotoImage, Frame, Listbox, Menu
import tkinter as tk
from saves import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./dashboard_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dashboard():
    Dashboard()

class Dashboard(Frame):

    def send_custom_command1(self):
        cmd = self.MCU_entry.get()
        send(MCU_host,cmd)

    def send_custom_command2(self):
        cmd = self.CD2_entry.get()
        send(CD1_host,cmd)

    def send_custom_command3(self):
        cmd = self.CD1_entry.get()
        send(CD2_host,cmd)

    def set_selected_mode(self, mode):
        self.selected_mode = mode
        logger.log("Selected Mode:{}".format(self.selected_mode))

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 370,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage( file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image( 476.0, 188.0, image=self.entry_image_1 )
        self.MCU_entry = Entry(self.canvas, bd=0, bg="#EFEFEF", fg="#000716", highlightthickness=0, font=("Montserrat Bold", 16 * -1), foreground="#777777", )
        self.MCU_entry.place( x=325.0, y=160.0, width=302.0, height=54.0 )

        self.entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image( 476.0, 254.0, image=self.entry_image_2 )
        self.CD2_entry = Entry(self.canvas, bd=0, bg="#EFEFEF", fg="#000716", highlightthickness=0, font=("Montserrat Bold", 16 * -1), foreground="#777777", )
        self.CD2_entry.place( x=325.0, y=226.0, width=302.0, height=54.0 )

        self.entry_image_3 = PhotoImage( file=relative_to_assets("entry_3.png")) 
        self.entry_bg_3 = self.canvas.create_image( 476.0, 318.0, image=self.entry_image_3 )
        self.CD1_entry = Entry(self.canvas, bd=0, bg="#EFEFEF", fg="#000716", highlightthickness=0, font=("Montserrat Bold", 16 * -1), foreground="#777777", )
        self.CD1_entry.place( x=325.0, y=290.0, width=302.0, height=54.0 )


        
        #################33

        self.menu = Menu(self.canvas, tearoff=0, font=("Montserrat Bold", 16))

        modes = ["GUIDED", "STABILIZE", "RTL", "BREAK", "LAND", "AUTOTUNE"]
        for mode in modes:
            self.menu.add_command(
                label=mode, command=lambda m=mode: self.set_selected_mode(m))

        self.mode_button = Button(
            self.canvas,
            text="Select Mode",
            font=("Montserrat Bold", 16),
            command=lambda: self.menu.post(1300,760)
        )
        self.mode_button.place(x=1000, y=160, width=200, height=50)


        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.send_custom_command1,
            relief="flat"
        )
        self.button_1.place(
            x=658.0,
            y=159.0,
            width=141.056884765625,
            height=56.8194580078125
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.send_custom_command2,
            relief="flat"
        )
        self.button_2.place(
            x=658.0,
            y=224.950927734375,
            width=141.056884765625,
            height=56.8194580078125
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.send_custom_command3,
            relief="flat"
        )
        self.button_3.place(
            x=658.0,
            y=289.8876953125,
            width=141.056884765625,
            height=56.8194580078125
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda :ARM(mode=self.selected_mode),
            relief="flat"
        )
        self.button_4.place(
            x=50.3699951171875,
            y=31.0,
            width=125.6099853515625,
            height=50.20562744140625
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: RTL(),
            relief="flat"
        )
        self.button_5.place(
            x=50.3699951171875,
            y=94.98760986328125,
            width=138.64498901367188,
            height=55.12774658203125
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: LAND(),
            relief="flat"
        )
        self.button_6.place(
            x=50.3699951171875,
            y=158.97503662109375,
            width=158.78997802734375,
            height=55.12774658203125
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(self.canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: POSHOLD(),
            relief="flat"
        )
        self.button_7.place(
            x=50.3699951171875,
            y=222.962646484375,
            width=234.6300048828125,
            height=55.12774658203125
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(self.canvas,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: TAKEOFF(),
            relief="flat"
        )
        self.button_8.place(
            x=48.0,
            y=291.8721923828125,
            width=225.14996337890625,
            height=55.127685546875
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(self.canvas,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda :ARM(mode=self.selected_mode),
            relief="flat"
        )
        self.button_9.place(
            x=50.3699951171875,
            y=31.0,
            width=125.6099853515625,
            height=55.12774658203125
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_10 = Button(self.canvas,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ctrlON(self.parent),
            relief="flat"
        )
        self.button_10.place(
            x=893.0,
            y=17.0,
            width=345.0,
            height=69.26605224609375
        )

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        self.button_11 = Button(self.canvas,
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ctrlOFF(self.parent),
            relief="flat"
        )
        self.button_11.place(
            x=893.0,
            y=88.0,
            width=345.0,
            height=69.26605224609375
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(self.canvas,
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('MCU'),
            relief="flat"
        )
        self.button_12.place(
            x=307.0,
            y=8.0,
            width=100.0,
            height=67.0
        )

        self.button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        self.button_13 = Button(self.canvas,
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD2'),
            relief="flat"
        )
        self.button_13.place(
            x=310.0,
            y=84.90570068359375,
            width=100.0,
            height=65.0
        )

        self.button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        self.button_14 = Button(self.canvas,
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD3'),
            relief="flat"
        )
        self.button_14.place(
            x=426.0,
            y=85.0,
            width=100.0,
            height=65.0
        )

        self.button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        self.button_15 = Button(self.canvas,
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD5'),
            relief="flat"
        )
        self.button_15.place(
            x=662.0,
            y=12.0,
            width=100.0,
            height=65.0
        )

        self.button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
        self.button_16 = Button(self.canvas,
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD4'),
            relief="flat"
        )
        self.button_16.place(
            x=545.0,
            y=10.0,
            width=100.0,
            height=65.0
        )

        self.button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
        self.button_17 = Button(self.canvas,
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('ALL'),
            relief="flat"
        )
        self.button_17.place(
            x=545.0,
            y=86.0,
            width=217.0,
            height=65.0
        )

        self.button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
        self.button_18 = Button(self.canvas,
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD1'),
            relief="flat"
        )
        self.button_18.place(
            x=426.0,
            y=10.0,
            width=100.0,
            height=65.0
        )
        
