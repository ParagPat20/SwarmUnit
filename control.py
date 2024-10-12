from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame
from saves import *
import tkinter as tk
from PIL import Image, ImageTk  # For image display
import zmq  # For socket communication
import cv2  # For video capture
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./control_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def control():
    Control()

class Control(Frame):

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

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=RTL,
            relief="flat"
        )
        self.button_2.place(
            x=50.3699951171875,
            y=93.7227783203125,
            width=234.6300048828125,
            height=50.5919189453125
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=LAND,
            relief="flat"
        )
        self.button_3.place(
            x=50.3699951171875,
            y=152.445556640625,
            width=234.6300048828125,
            height=50.5919189453125
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=POSHOLD,
            relief="flat"
        )
        self.button_4.place(
            x=50.3699951171875,
            y=211.168212890625,
            width=234.6300048828125,
            height=50.5919189453125
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=TAKEOFF,
            relief="flat"
        )
        self.button_5.place(
            x=48.0,
            y=274.4080810546875,
            width=237.0,
            height=50.5919189453125
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(self.canvas,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:ARM("GUIDED"),
            relief="flat"
        )
        self.button_6.place(
            x=50.3699951171875,
            y=35.0,
            width=234.6300048828125,
            height=50.5919189453125
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(self.canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: servo_set("close"),
            relief="flat"
        )
        self.button_7.place(
            x=307.0,
            y=185.0,
            width=345.0,
            height=69.26611328125
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(self.canvas,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: servo_set('open'),
            relief="flat"
        )
        self.button_8.place(
            x=307.0,
            y=256.0,
            width=345.0,
            height=69.26611328125
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(self.canvas,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('MCU'),
            relief="flat"
        )
        self.button_9.place(
            x=307.0,
            y=31.0,
            width=100.0,
            height=67.0
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_10 = Button(self.canvas,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD2'),
            relief="flat"
        )
        self.button_10.place(
            x=310.0,
            y=107.90576171875,
            width=100.0,
            height=65.0
        )

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        self.button_11 = Button(self.canvas,
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD3'),
            relief="flat"
        )
        self.button_11.place(
            x=426.0,
            y=108.0,
            width=100.0,
            height=65.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(self.canvas,
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD5'),
            relief="flat"
        )
        self.button_12.place(
            x=662.0,
            y=35.0,
            width=100.0,
            height=65.0
        )

        self.button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        self.button_13 = Button(self.canvas,
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD4'),
            relief="flat"
        )
        self.button_13.place(
            x=545.0,
            y=33.0,
            width=100.0,
            height=65.0
        )

        self.button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        self.button_14 = Button(self.canvas,
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('ALL'),
            relief="flat"
        )
        self.button_14.place(
            x=545.0,
            y=109.0,
            width=217.0,
            height=65.0
        )

        self.button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        self.button_15 = Button(self.canvas,
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: select_drone('CD1'),
            relief="flat"
        )
        self.button_15.place(
            x=426.0,
            y=33.0,
            width=100.0,
            height=65.0
        )

        self.canvas.create_rectangle(
            771.0,
            36.0,
            1021.0,
            186.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            1034.0,
            36.0,
            1284.0,
            186.0,
            fill="#D9D9D9",
            outline="")

        rect3=self.canvas.create_rectangle(
            896.0,
            203.0,
            1146.0,
            353.0,
            fill="#D9D9D9",
            outline="")
        