import ttkbootstrap as ttk


class IntroInterface:
    def __init__(self, window: ttk.window.Window, on_submit):
        self.window = window

        self.introlabel = ttk.Label(text="Welcome to TriviaFun! Please make your choices:")
        self.introlabel.grid(column=0, row=0, columnspan=2)
        self.difficulty = ttk.StringVar(None, "easy")
        self.difficulty_button_easy = ttk.Radiobutton(text="Easy", value="easy", variable=self.difficulty)
        self.difficulty_button_medium = ttk.Radiobutton(text="Medium", value="medium", variable=self.difficulty)
        self.difficulty_button_hard = ttk.Radiobutton(text="Hard", value="hard", variable=self.difficulty)
        self.difficulty_button_easy.grid(row=1, column=0, sticky="w")
        self.difficulty_button_medium.grid(row=2, column=0, sticky="w")
        self.difficulty_button_hard.grid(row=3, column=0, sticky="w")

        self.quiznumber = ttk.IntVar(None, 10)
        self.quiznumber_button_10 = ttk.Radiobutton(text="10", value=10, variable=self.quiznumber)
        self.quiznumber_button_20 = ttk.Radiobutton(text="20", value=20, variable=self.quiznumber)
        self.quiznumber_button_50 = ttk.Radiobutton(text="50", value=50, variable=self.quiznumber)
        self.quiznumber_button_10.grid(row=1, column=1, sticky="w")
        self.quiznumber_button_20.grid(row=2, column=1, sticky="w")
        self.quiznumber_button_50.grid(row=3, column=1, sticky="w")

        self.submit_button = ttk.Button(text="Submit", command=self.submit_clicked)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        self.submit_callback = on_submit

    def submit_clicked(self):
        difficulty = self.difficulty.get()
        quiz_number = self.quiznumber.get()
        self.submit_callback(difficulty, quiz_number)

    def destroy_intro(self):
        self.introlabel.destroy()
        self.difficulty_button_easy.destroy()
        self.difficulty_button_medium.destroy()
        self.difficulty_button_hard.destroy()
        self.quiznumber_button_10.destroy()
        self.quiznumber_button_20.destroy()
        self.quiznumber_button_50.destroy()
        self.submit_button.destroy()





