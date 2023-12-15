from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame
from saves import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./initializtion_assets")

drone_list=[]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def initialize():
    Initialize()

class Initialize(Frame):
    
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg = "#FFFFFF")
        
        self.canvas = Canvas( self, bg = "#FFFFFF", height = 370, width = 1300, bd = 0, highlightthickness = 0, relief = "ridge" )

        self.canvas.place(x = 0, y = 0)
        
        self.canvas.create_text(
            96.0,
            85.0,
            anchor="nw",
            text="____________________Connected Drones List____________________",
            fill="#5E95FF",
            font=("LexendExa Black", 28 * -1)
        )

        self.button_image_7 = PhotoImage( file=relative_to_assets("button_7.png"))
        #MCU
        self.button_7 = Button(self.canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("MCU"),
            relief="flat"
        )
        self.button_7.place( x=77.0, y=148.0, width=100.0, height=50.0 )

        self.button_image_8 = PhotoImage( file=relative_to_assets("button_8.png"))
        #CD1
        self.button_8 = Button(self.canvas,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("CD1"),
            relief="flat"
        )
        self.button_8.place( x=77.0, y=219.0, width=100.0, height=50.0 )

        self.button_image_9 = PhotoImage( file=relative_to_assets("button_9.png"))
        #CD2
        self.button_9 = Button(self.canvas,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("CD2"),
            relief="flat"
        )
        self.button_9.place( x=77.0, y=292.0, width=100.0, height=50.0 )

        self.button_image_10 = PhotoImage( file=relative_to_assets("button_10.png"))
        #CD3
        self.button_10 = Button(self.canvas,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("CD3"),
            relief="flat"
        )
        self.button_10.place( x=561.0, y=149.0, width=100.0, height=50.0 )

        self.button_image_11 = PhotoImage( file=relative_to_assets("button_11.png"))
        #cd4
        self.button_11 = Button(self.canvas,
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("CD1"),
            relief="flat"
        )
        self.button_11.place( x=561.0, y=219.0, width=100.0, height=50.0 )

        self.button_image_12 = PhotoImage( file=relative_to_assets("button_12.png"))
        #cd5
        self.button_12 = Button(self.canvas,
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle("CD5"),
            relief="flat"
        )
        self.button_12.place( x=561.0, y=294.0, width=100.0, height=50.0 )

        self.canvas.create_text(
            96.0,
            12.0,
            anchor="nw",
            text="ADD\nDRONE",
            fill="#5E95FF",
            font=("LexendZetta Black", 24 * -1)
        )

        self.canvas.create_text(
            677.0,
            12.0,
            anchor="nw",
            text="REMOVE\nDRONE",
            fill="#5E95FF",
            font=("LexendZetta Black", 24 * -1)
        )

        self.MCU_initialized = False
        self.CD1_initialized = False
        self.CD2_initialized = False
        self.CD3_initialized = False

    def toggle(self, drone_str):
        global drone_list

        if drone_str not in drone_list:
            drone_list.append(drone_str)
            logger.log(drone_list)
            
            if 'MCU' in drone_list and not self.MCU_initialized:
                send(MCU_host, 'initialize_MCU()')
                self.MCU_initialized = True
                logger.log("\nMCU initialized")

            if 'CD1' in drone_list and not self.CD1_initialized:
                send(CD1_host,'initialize_CD1()')
                self.CD1_initialized = True
                logger.log("\nCD1 initialized")

            if 'CD2' in drone_list and not self.CD2_initialized:
                send(CD2_host, 'initialize_CD2()')
                self.CD2_initialized = True
                logger.log("\nCD2 initialized")

            if 'CD3' in drone_list and not self.CD3_initialized:
                send(CD2_host,'initialize_CD3()')
                self.CD3_initialized = True
                logger.log("\nCD3 initialized")

            if drone_str == 'MCU':
                send(MCU_host,'drone_list_update('+str(drone_list)+')')

            if drone_str == 'CD2':
                send(CD2_host,'drone_list_update('+str(drone_list)+')')

            if drone_str == 'CD1':
                send(CD1_host,'drone_list_update('+str(drone_list)+')')

        if 'MCU' in drone_list and logger.mcu_status == True:

            self.image_image_1 = PhotoImage(
                file=relative_to_assets("image_1.png"))
            self.image_1 = self.canvas.create_image(
                204.0,
                173.0,
                image=self.image_image_1
            )

            self.canvas.create_text(
                280.0,
                173.0,
                anchor="ne",
                text=self.get_status('MCU','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )


            self.image_image_2 = PhotoImage(
                file=relative_to_assets("image_2.png"))
            self.image_2 = self.canvas.create_image(
                350.0,
                173.0,
                image=self.image_image_2
            )

            self.canvas.create_text(
                430.0,
                173.0,
                anchor="ne",
                text=self.get_status('MCU','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.button_image_1 = PhotoImage(
                file=relative_to_assets("button_1.png"))
            #MCU-re#
            self.button_1 = Button(self.canvas,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: send(MCU_host,'MCU.reconnect()'),
                relief="flat"
            )
            self.button_1.place(
                x=481.0,
                y=151.0,
                width=44.0,
                height=45.0
            )

        if 'CD1' in drone_list and logger.cd1_status == True:

            self.image_image_3 = PhotoImage(
                file=relative_to_assets("image_3.png"))
            self.image_3 = self.canvas.create_image(
                204.0,
                244.0,
                image=self.image_image_3
            )

            self.canvas.create_text(
                280.0,
                244.0,
                anchor="ne",
                text=self.get_status('CD1','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.canvas.create_text(
                430.0,
                244.0,
                anchor="ne",
                text=self.get_status('CD1','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.image_image_4 = PhotoImage(
                file=relative_to_assets("image_4.png"))
            self.image_4 = self.canvas.create_image(
                350.0,
                244.0,
                image=self.image_image_4
            )

            self.button_image_2 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            #CD1-re
            self.button_2 = Button(self.canvas,
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:  send(MCU_host,'CD1.reconnect()'),
                relief="flat"
            )
            self.button_2.place(
                x=481.0,
                y=222.0,
                width=44.0,
                height=45.0
            )

        if 'CD2' in drone_list and logger.cd2_status == True:

            self.image_image_5 = PhotoImage(
                file=relative_to_assets("image_5.png"))
            self.image_5 = self.canvas.create_image(
                204.0,
                316.0,
                image=self.image_image_5
            )

            self.canvas.create_text(
                280.0,
                316.0,
                anchor="ne",
                text=self.get_status('CD2','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.canvas.create_text(
                430.0,
                316.0,
                anchor="ne",
                text=self.get_status('CD2','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.image_image_6 = PhotoImage(
                file=relative_to_assets("image_6.png"))
            self.image_6 = self.canvas.create_image(
                350.0,
                316.0,
                image=self.image_image_6
            )


            self.button_image_3 = PhotoImage(
                file=relative_to_assets("button_3.png"))
            #cd2-re
            self.button_3 = Button(self.canvas,
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:  send(CD2_host,'CD2.reconnect()'),
                relief="flat"
            )
            self.button_3.place(
                x=481.0,
                y=294.0,
                width=44.0,
                height=45.0
            )

        if 'CD3' in drone_list and logger.cd3_status == True:

            self.image_image_11 = PhotoImage(
                file=relative_to_assets("image_11.png"))
            self.image_11 = self.canvas.create_image(
                692.0,
                175.0,
                image=self.image_image_11
            )

            self.canvas.create_text(
                775.0,
                175.0,
                anchor="ne",
                text=self.get_status('CD3','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.canvas.create_text(
                920.0,
                175.0,
                anchor="ne",
                text=self.get_status('CD3','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.image_image_12 = PhotoImage(
                file=relative_to_assets("image_12.png"))
            self.image_12 = self.canvas.create_image(
                838.0,
                175.0,
                image=self.image_image_12
            )

            self.button_image_6 = PhotoImage(
                file=relative_to_assets("button_6.png"))
            #CD3-re
            self.button_6 = Button(self.canvas,
                image=self.button_image_6,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:  send(CD2_host,'CD3.reconnect'),
                relief="flat"
            )
            self.button_6.place(
                x=969.0,
                y=153.0,
                width=44.0,
                height=45.0
            )

        if 'CD4' in drone_list and logger.cd4_status == True:

            self.image_image_9 = PhotoImage(
                file=relative_to_assets("image_9.png"))
            self.image_9 = self.canvas.create_image(
                692.0,
                244.0,
                image=self.image_image_9
            )

            self.canvas.create_text(
                720.0,
                222.0,
                anchor="ne",
                text=self.get_status('CD1','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )


            self.canvas.create_text(
                576.0,
                222.0,
                anchor="ne",
                text=self.get_status('CD5','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )

            self.image_image_10 = PhotoImage(
                file=relative_to_assets("image_10.png"))
            self.image_10 = self.canvas.create_image(
                838.0,
                244.0,
                image=self.image_image_10
            )

            button_image_5 = PhotoImage(
                file=relative_to_assets("button_5.png"))
            #cd4-re
            button_5 = Button(self.canvas,
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:  send(CD1_host,'CD1.reconnect'),
                relief="flat"
            )
            button_5.place(
                x=969.0,
                y=222.0,
                width=44.0,
                height=45.0
            )

        if 'CD5' in drone_list:

            self.image_image_7 = PhotoImage(
                file=relative_to_assets("image_7.png"))
            self.image_7 = self.canvas.create_image(
                692.0,
                313.0,
                image=self.image_image_7
            )

            self.canvas.create_text(
                720.0,
                291.0,
                anchor="ne",
                text=self.get_status('CD5','battery'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )


            self.canvas.create_text(
                576.0,
                291.0,
                anchor="ne",
                text=self.get_status('CD5','gs'),
                fill="#5E95FF",
                font=("Montserrat Bold", 16 * -1),
            )


            self.image_image_8 = PhotoImage(
                file=relative_to_assets("image_8.png"))
            self.image_8 = self.canvas.create_image(
                838.0,
                313.0,
                image=self.image_image_8
            )

            button_image_4 = PhotoImage(
                file=relative_to_assets("button_4.png"))
            #cd5-re
            button_4 = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:  send(CD1_host,'CD5.reconnect'),
                relief="flat"
            )
            button_4.place(
                x=969.0,
                y=291.0,
                width=44.0,
                height=45.0
            )

    def get_status(self, drone_str,param):
        if drone_str in drone_list:
            if drone_str == 'MCU':
                if param == 'battery':
                    recv_status(MCU_host,60001,'battery')
                    return recv_status(MCU_host,60001,'battery')
                elif param == 'gs':
                    recv_status(MCU_host,60001,'gs')
                    return recv_status(MCU_host,60001,'gs')
            if drone_str == 'CD1':
                if param == 'battery':
                    recv_status(CD1_host,60002,'battery')
                    return recv_status(CD1_host,60002,'battery')
                elif param == 'gs':
                    recv_status(CD1_host,60002,'gs')
                    return recv_status(CD1_host,60002,'battery')
            if drone_str == 'CD2':
                if param == 'battery':
                    recv_status(CD2_host,60003,'battery')
                    return recv_status(CD2_host,60003,'battery')
                elif param == 'gs':
                    recv_status(CD2_host,60003,'gs')
                    return recv_status(CD2_host,60003,'battery')
            # if drone_str == 'CD3':
            #     if param == 'battery':
            #         recv_status(MCU_host,60004,'battery')
            #         print("None")
            #     elif param == 'gs':
            #         recv_status(MCU_host,60004,'gs')
            #         print("None")
            # if drone_str == 'CD4':
            #     if param == 'battery':
            #         return recv_status(CD1_host,60005,'battery')
            #     elif param == 'gs':
            #         return recv_status(CD1_host,60005,'gs')
            # if drone_str == 'CD5':
            #     if param == 'battery':
            #         return recv_status(CD1_host,60006,'battery')
            #     elif param == 'gs':
            #         return recv_status(CD1_host,60006,'gs')


