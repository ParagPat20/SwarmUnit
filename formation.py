from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage, Frame
from saves import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./formation_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def formation():
    Formation()

class Formation(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg = "#FFFFFF")
        self.dis = 1
        self.dis = str(self.dis)
        self.alt = 2
        self.alt = str(self.alt)
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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.custom_dis(),
            relief="flat"
        )
        self.button_1.place( x=78.0, y=245.0, width=220.0, height=55.0 )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: logger.log("Button_2 clicked"),
            relief="flat"
        )
        self.button_2.place( x=771.0, y=245.0, width=220.0, height=55.0 )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.custom_dis1(),
            relief="flat"
        )
        self.button_3.place( x=309.0, y=245.0, width=220.0, height=55.0 )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.custom_dis2(),
            relief="flat"
        )
        self.button_4.place( x=540.0, y=245.0, width=220.0, height=55.0 )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: logger.log("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place( x=1002.0, y=245.0, width=220.0, height=55.0 )

        self.canvas.create_text(
            90.0,
            145.0,
            anchor="nw",
            text="CD1 Path",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            90.0,
            107.0,
            anchor="nw",
            text="MCU Path",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            554.0,
            109.0,
            anchor="nw",
            text="1  CD1\n2  CD2\n3  CD3",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            673.0,
            108.0,
            anchor="nw",
            text="4  CD1\n5  CD5\n6  CD6",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            90.0,
            182.0,
            anchor="nw",
            text="CD2 Path",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            392.0,
            163.9276123046875,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D4D4D4",
            fg="#000716",
            highlightthickness=0,
            font = ("Montserrat Bold", 20 * -1)
        )
        self.entry_1.place(
            x=316.9276123046875,
            y=152.0,
            width=150.144775390625,
            height=21.855224609375
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            392.0,
            127.9276123046875,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D4D4D4",
            fg="#000716",
            font = ("Montserrat Bold", 20 * -1),
            highlightthickness=0
        )
        self.entry_2.place(
            x=316.9276123046875,
            y=116.0,
            width=150.144775390625,
            height=21.855224609375
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            392.0,
            199.9276123046875,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#D4D4D4",
            fg="#000716",
            highlightthickness=0,
            font = ("Montserrat Bold", 20 * -1)
        )
        self.entry_3.place(
            x=316.9276123046875,
            y=188.0,
            width=150.144775390625,
            height=21.855224609375
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            955.5,
            117.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0,
            font = ("Montserrat Bold", 20 * -1)
        )
        self.entry_4.place(
            x=823.0,
            y=20.0,
            width=265.0,
            height=193.0
        )

        self.canvas.create_text(
            924.0,
            69.0,
            anchor="nw",
            text="X,Y,Z,T",
            fill="#5E95FF",
            font=("Montserrat Bold", 20 * -1)
        )

        self.canvas.create_text(
            924.0,
            112.0,
            anchor="nw",
            text="0,0,-0.5,2",
            fill="#5E95FF",
            font=("Montserrat Bold", 20 * -1)
        )

        self.canvas.create_text(
            924.0,
            158.0,
            anchor="nw",
            text="0,1,0,2",
            fill="#5E95FF",
            font=("Montserrat Bold", 20 * -1)
        )

        self.canvas.create_text(
            827.0,
            30.0,
            anchor="nw",
            text="Custom Path",
            fill="#5E95FF",
            font=("Montserrat Bold", 24 * -1)
        )

    # def custom_goto(self):

    #     try:
    #         self.dis = float(self.entry_1.get())
    #         logger.log("dis = {}".format(self.dis))
    #         self.angle = int(self.entry_3.get())
    #         logger.log("angle = {}".format(self.angle))
    #         self.drones = str(self.entry_2.get())
    #         self.drone1 = int(self.drones[0])
    #         self.drone2 = int(self.drones[1])
    #         self.alt = 2
    #         a = [self.drone1, self.drone2, self.dis, self.angle, self.alt]
    #         a = str(a)
    #         logger.log("Running Custom_goto command with {}".format(a))
    #         # send(MCU_host,'custom_goto('+ a +')')

    #     except Exception as e:
    #         logger.log("ERROR:{}".format(e), "#FF4545")

    def custom_dis(self):
        try:
            self.dis = str(self.entry_2.get())
            logger.log("Path = {}".format(self.dis))
            
            split_values = self.dis.split(',')
            print("Split Values:", split_values)  # Add this line to see the split values
            
            x, y, z, time = split_values

            logger.log("Sending to MCU X:{}, Y:{}, Z:{} for {} seconds".format(x, y, z, time))
            
            send(MCU_host, 'MCU.send_ned_velocity({}, {}, {}, {})'.format(x, y, z, time))
                    
        except Exception as e:
            logger.log("here_error{}".format(e))

    def custom_dis1(self):
        try:
            self.dis = str(self.entry_1.get())
            logger.log("Path = {}".format(self.dis))
            
            split_values = self.dis.split(',')
            print("Split Values:", split_values)  # Add this line to see the split values
            
            x, y, z, time = split_values

            logger.log("Sending to CD1 X:{}, Y:{}, Z:{} for {} seconds".format(x, y, z, time))
            
            send(CD1_host, 'CD1.send_ned_velocity({}, {}, {}, {})'.format(x, y, z, time))
                    
        except Exception as e:
            logger.log("here_error{}".format(e))

    def custom_dis2(self):
        try:
            self.dis = str(self.entry_3.get())
            logger.log("Path = {}".format(self.dis))
            
            split_values = self.dis.split(',')
            print("Split Values:", split_values)  # Add this line to see the split values
            
            x, y, z, time = split_values

            logger.log("Sending to CD2 X:{}, Y:{}, Z:{} for {} seconds".format(x, y, z, time))
            
            send(CD2_host, 'CD2.send_ned_velocity({}, {}, {}, {})'.format(x, y, z, time))
                    
        except Exception as e:
            logger.log("here_error{}".format(e))