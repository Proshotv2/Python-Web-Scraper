from tkinter import *
import requests
import bs4


class guiScraper(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.title("Gui")
        self.root.geometry("680x600")

        weburl = StringVar()

        def close():
            self.root.destroy()

        def requestMade():
            web = webEntry.get()
            req = requests.get(web)
            soup = bs4.BeautifulSoup(req.text, 'html.parser')
            radio = self.var.get()
            element = soup.select(radio)

            for i in element:
                result.insert(INSERT, i)


        self.var = StringVar()
        self.var.set("title")

        # Menu
        menu = Menu()
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Exit")
        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About")

        frame = Frame(self.root, width=600)
        frame.pack(side=TOP, fill=BOTH, expand=True, anchor=N)

        framebottom = Frame(self.root)
        framebottom.pack(side=RIGHT, fill=BOTH, expand=True)

        # Labels
        webLabel = Label(frame, text="Website to Scrape: ", padx=5, pady=5)
        tagLabel = Label(frame, text="Tags to Pull: ", padx=5, pady=5)
        resLabel = Label(frame, text="Results: ", padx=5, pady=5)

        webLabel.grid(row=0, column=0, sticky="en")
        tagLabel.grid(row=1, column=0, columnspan=2, sticky="wn")
        resLabel.grid(row=2, column=0, columnspan=2, sticky="wn")

        # Buttons
        closeButton = Button(framebottom, text="Exit", command=close, padx=5, pady=5)
        closeButton.pack(side=RIGHT)

        submitButton = Button(frame, text="Go!", padx=5, pady=3, fg="green", command=requestMade)
        submitButton.place(x=270)

        # RadioButtons
        r1 = Radiobutton(frame, text="Title", padx=5, pady=3, variable=self.var, value="title")
        r2 = Radiobutton(frame, text="H1", padx=5, pady=3, variable=self.var, value="h1")
        r3 = Radiobutton(frame, text="H2", padx=5, pady=3, variable=self.var, value="h2")
        r4 = Radiobutton(frame, text="H3", padx=5, pady=3, variable=self.var, value="h3")
        r5 = Radiobutton(frame, text="H4", padx=5, pady=3, variable=self.var, value="h4")
        r6 = Radiobutton(frame, text="H5", padx=5, pady=3, variable=self.var, value="h5")
        r7 = Radiobutton(frame, text="Span", padx=5, pady=3, variable=self.var, value="span")

        r1.grid(row=1, column=1)
        r2.grid(row=1, column=2)
        r3.grid(row=1, column=3)
        r4.grid(row=1, column=4)
        r5.grid(row=1, column=5)
        r6.grid(row=1, column=6)
        r7.grid(row=1, column=7)

        # Entries
        webEntry = Entry(frame)
        webEntry.place(x=120, y=5)

        # Text
        result = Text(frame, width=80)
        result.place(x=5, y=100)

        self.root.grid_rowconfigure(6, weight=1, minsize=100)
        self.root.grid_columnconfigure(6, weight=1, minsize=100)

        self.root.mainloop()


guiScraper()