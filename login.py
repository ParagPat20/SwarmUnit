from pathlib import Path

from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from mainWindow import mainWindow

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./login_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginWindow():
    Login()


class Login(Toplevel):

    # Login check
    def loginFunc(self):
        entered_username = self.username.get().lower()
        entered_password = self.password.get()

        if entered_username == "parag" and entered_password == 'oxitech':
            self.destroy()
            mainWindow()
            return
        else:
            messagebox.showerror(
                title="Error",
                message="Incorrect username or password"
            )

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Login - SwarmUnit")
        
        self.geometry("1012x506")
        self.configure(bg = "#5E95FF")

        self.canvas = Canvas(
        self,
        bg = "#5E95FF",
        height = 506,
        width = 1012,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            469.0,0.0,1012.0,506.0,fill="#FFFFFF",outline=""
            )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(736.0,331.0,image=entry_image_1)
        entry_1 = Entry(bd=0,bg="#EFEFEF",fg="#000716",highlightthickness=0)
        entry_1.place( x=568.0, y=294.0, width=336.0, height=72.0 )

        entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image( 736.0, 229.0, image=entry_image_2 )
        entry_2 = Entry( bd=0, bg="#EFEFEF", fg="#000716", highlightthickness=0 )
        entry_2.place( x=568.0, y=192.0, width=336.0, height=72.0 )

        self.canvas.create_text(
            573.0,
            306.0,
            anchor="nw",
            text="Password",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.canvas.create_text(
            573.0,
            204.0,
            anchor="nw",
            text="Username",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.canvas.create_text(
            553.0,
            66.0,
            anchor="nw",
            text="Enter your login details",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            85.0,
            77.0,
            anchor="nw",
            text="OxiTech",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1)
        )

        self.canvas.create_text(
            553.0,
            109.0,
            anchor="nw",
            text="Enter the credentials that the admin gave",
            fill="#CCCCCC",
            font=("Montserrat SemiBold", 16 * -1)
        )

        self.canvas.create_text(
            553.0,
            130.0,
            anchor="nw",
            text="you while signing up for the program",
            fill="#CCCCCC",
            font=("Montserrat SemiBold", 16 * -1)
        )

        entry_image_3 = PhotoImage( file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image( 736.0, 241.0, image=entry_image_3 )
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
        )
        self.username.place( x=573.0, y=229.0, width=326.0, height=22.0 )


        entry_image_4 = PhotoImage( file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image( 736.0, 342.0, image=entry_image_4 )
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
            show="•",
        )
        self.password.place( x=573.0, y=330.0, width=326.0, height=22.0 )

        self.canvas.create_text(
            90.0,
            150.0,
            anchor="nw",
            text="This is the Python based GUI to Control the Swarm Drones.\nSpecially made for Robofest Competition.",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1)
        )

        self.canvas.create_text(
            90.0,
            431.0,
            anchor="nw",
            text="@ParagPat20",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            275.0,
            354.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            469.0,
            33.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginFunc,
            relief="flat"
        )
        button_1.place( x=641.0, y=412.0, width=190.0, height=48.0 )

        self.username.bind("<Return>", lambda event: self.loginFunc())
        self.password.bind("<Return>", lambda event: self.loginFunc())

        self.resizable(False, False)
        self.mainloop()


