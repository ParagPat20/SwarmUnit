from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, OptionMenu, StringVar, Listbox, Scrollbar, font
from saves import *
from tkinter import filedialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Edit_Mission")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def edit_mission():
    EDIT()

class EDIT(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.paths = []


        self.configure(bg = "#1D1C1D")


        self.canvas = Canvas(
            self,
            bg = "#1D1C1D",
            height = 370,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            -1.9793701171875,
            58.1875,
            638.041259765625,
            60.1875,
            fill="#636363",
            outline="")
        self.overlay_win_active = False

        self.canvas.create_text(
            7.0,
            14.0,
            anchor="nw",
            text="Edit Mission",
            fill="#CDCDCD",
            font=("Inter Black", 15 * -1)
        )

        self.add_path_button = Button(
            self.canvas,
            text="Add Path",
            command=self.add_path,
            bg="#2A282C",
            fg="#FFFFFF",
            relief="flat",
            activebackground="#2A282C"
        )
        self.add_path_button.place(
            x=250.0,
            y=177.0,
            width=150.0,
            height=40.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.handle_btn_press(self.parent.form_btn,"form"),
            relief="flat", activebackground="#2A282C"
        )
        self.button_2.place(
            x=365.0,
            y=11.0,
            width=37.0,
            height=35.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            201.0,
            120.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            26.0,
            84.0,
            anchor="nw",
            text="Path_1",
            fill="#44FFE8",
            font=("Inter Light", 11 * -1)
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat", activebackground="#2A282C"
        )
        self.button_3.place(
            x=28.0,
            y=122.0,
            width=60.0,
            height=23.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            157.0,
            133.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            132.0,
            124.0,
            anchor="nw",
            text="x",
            fill="#FFFFFF",
            font=("Inter ExtraLight", 15 * -1)
        )

        self.drone_names = ["MCU", "CD1", "CD2"]  # Add your drone names here
        self.selected_drone = StringVar(self)
        self.selected_drone.set(self.drone_names[0])
        self.drone_menu = OptionMenu(self.canvas, self.selected_drone, *self.drone_names)
        self.drone_menu.place(x=28.0, y=122.0, width=60.0, height=23.0)


        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            163.0,
            134.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self.canvas,
            bd=0,
            bg="#1D1C1D",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=143.0,
            y=128.0,
            width=40.0,
            height=10.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            246.0,
            133.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            221.0,
            126.0,
            anchor="nw",
            text="Y",
            fill="#FFFFFF",
            font=("Inter ExtraLight", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            252.0,
            134.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self.canvas,
            bd=0,
            bg="#1D1C1D",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=232.0,
            y=128.0,
            width=40.0,
            height=10.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            335.0,
            133.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            310.0,
            126.0,
            anchor="nw",
            text="T",
            fill="#FFFFFF",
            font=("Inter ExtraLight", 12 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            341.0,
            134.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(self.canvas,
            bd=0,
            bg="#1D1C1D",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=321.0,
            y=128.0,
            width=40.0,
            height=10.0
        )

        # Listbox to display saved paths
        self.path_listbox = Listbox(
            self.canvas,
            bg="#1D1C1D",
            fg="#44FFE8",
            bd=0,
            font=("Inter Light", 10),
            selectbackground="#2A282C",
            selectforeground="#FFFFFF"
        )
        self.path_listbox.place(
            x=28.0,
            y=220.0,
            width=340.0,
            height=150.0
        )

        self.mission_name_entry = Entry(self.canvas,
            bd=0,
            bg="#000000",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.mission_name_entry.place(
            x=850.0,
            y=100.0,
            width=340.0,
            height=25.0
        )

        self.save_button = Button(
            self.canvas,
            text="Save",
            command=self.save_paths,
            bg="#2A282C",
            fg="#FFFFFF",
            relief="flat",
            activebackground="#2A282C"
        )
        self.save_button.place(
            x=850.0,
            y=200.0,
            width=100.0,
            height=30.0
        )
        self.extra_cmd_entry = Entry(self.canvas,
            bd=0,
            bg="#000000",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.extra_cmd_entry.place(
            x=450.0,
            y=100.0,
            width=340.0,
            height=25.0
        )

        # Scrollbar for the listbox
        self.scrollbar = Scrollbar(self.canvas)
        self.scrollbar.place(x=368.0, y=220.0, height=150.0)

        self.path_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.path_listbox.yview)

        self.path_listbox.bind("<Double-Button-1>", self.on_listbox_double_click)
        self.send_to_pi_button = Button(
            self.canvas,
            text="Send to Pi Zero",
            command=lambda: self.send_to_pi(),
            bg="#2A282C",
            fg="#FFFFFF",
            relief="flat",
            activebackground="#2A282C"
        )
        self.send_to_pi_button.place(
            x=950.0,
            y=250.0,
            width=150.0,
            height=30.0
        )
        self.open_file_button = Button(
            self.canvas,
            text="Open File",
            command=self.open_file,
            bg="#2A282C",
            fg="#FFFFFF",
            relief="flat",
            activebackground="#2A282C"
        )
        self.open_file_button.place(
            x=450.0,
            y=150.0,
            width=100.0,
            height=30.0
        )

    def open_file(self):
        # Open a file dialog to select the file to open
        file_path = filedialog.askopenfilename(
            initialdir=OUTPUT_PATH,
            title="Select File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            # Read the commands from the selected file
            with open(file_path, 'r') as file:
                commands = file.readlines()

            # Set the mission name from the file name
            mission_name = Path(file_path).stem
            self.mission_name_entry.delete(0, 'end')
            self.mission_name_entry.insert(0, mission_name)

            # Display the commands in the Listbox
            self.paths = [command.strip() for command in commands]
            self.display_paths()
    def send_to_pi(self):
        threading.Thread(target=self.send_to_pi_thread).start()

    def send_to_pi_thread(self):
        # Get the mission name from the entry widget
        mission_name = self.mission_name_entry.get()

        if not mission_name:
            logger.log("Mission name is required.")
            return

        # Specify the file path to save the data
        file_path = OUTPUT_PATH / f"{mission_name}.txt"

        # Open the file in write mode and save the paths
        with open(file_path, 'w') as file:
            for path in self.paths:
                file.write(path + "\n")
        logger.log("File Path Successfully achieved\n{}".format(file_path))
        send(MCU_host,"file_server()")
        time.sleep(1)
        try:
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            logger.log("Made Socket")

            # Change 'your_pi_zero_ip' and 'your_port' to the actual IP and port of your Pi Zero
            socket.connect("tcp://{}:5577".format(MCU_host))
            socket.send_string(mission_name)
            logger.log("Sent Filename")
            socket.recv_string()
            logger.log("Filename sent successfully")

            with open(file_path, 'rb') as file:
                file_data = file.read()
                socket.send(file_data)

            response = socket.recv_string()
            logger.log(response)

        except Exception as e:
            logger.log(f"Error sending file to Pi Zero: {e}")
            print(f"Error sending file to Pi Zero: {e}")

    def add_path(self):
        drone_name = self.selected_drone.get()
        x_value = self.entry_1.get()
        y_value = self.entry_2.get()
        t_value = self.entry_3.get()
        extra_cmd = self.extra_cmd_entry.get()
        if extra_cmd and drone_name:
            extra_cmd=str(extra_cmd)
            if extra_cmd.startswith("sleep"):
                path_info = f"time.{extra_cmd}"
            else:
                path_info = f"send({drone_name}_host,'{drone_name}.{extra_cmd}')"
            self.extra_cmd_entry.delete(0, 'end')
            self.paths.append(path_info)
            self.display_paths()

        if drone_name and x_value and y_value and t_value:
            # Save the path information
            path_info = f"send({drone_name}_host,'{drone_name}.send_pos({x_value},{y_value},0,{t_value})')"
            
            # Include extra command if provided
            
            self.paths.append(path_info)

            # Clear the entry fields
            self.selected_drone.set(self.drone_names[0])
            self.entry_1.delete(0, 'end')
            self.entry_2.delete(0, 'end')
            self.entry_3.delete(0, 'end')
            

            # Display the saved paths in the Listbox
            self.display_paths()


    def on_listbox_select(self, event):
        selected_index = self.path_listbox.curselection()

        if selected_index:
            selected_path = self.paths[selected_index[0]].split(", ")

            # Update the Entry widgets with the selected path values
            self.selected_drone.set(selected_path[0].split(": ")[1])
            self.entry_1.delete(0, 'end')
            self.entry_1.insert(0, selected_path[1].split(": ")[1])
            self.entry_2.delete(0, 'end')
            self.entry_2.insert(0, selected_path[2].split(": ")[1])
            self.entry_3.delete(0, 'end')
            self.entry_3.insert(0, selected_path[3].split(": ")[1])

    def on_listbox_double_click(self, event):
        selected_index = self.path_listbox.curselection()

        if selected_index:
            # Remove the selected path from the list
            removed_path = self.paths.pop(selected_index[0])

            # Display the updated paths in the Listbox
            self.display_paths()

    def display_paths(self):
        # Clear the Listbox
        self.path_listbox.delete(0, 'end')

        # Insert saved paths into the Listbox
        for path in self.paths:
            self.path_listbox.insert('end', path)

    def save_paths(self):
        global mission
        # Get the mission name from the entry widget
        mission_name = self.mission_name_entry.get()

        if not mission_name:
            logger.log("Mission name is required.")
            return

        # Specify the file path to save the data
        file_path = OUTPUT_PATH / f"{mission_name}.txt"

        # Open the file in write mode and save the paths
        with open(file_path, 'w') as file:
            for path in self.paths:
                file.write(path + "\n")

        logger.log("Paths saved to {}".format(file_path))