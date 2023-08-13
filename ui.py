import ttkbootstrap as ttk
from trivia import Trivia

class TriviaInterface:

    def __init__(self, window: ttk.window.Window, trivia: Trivia, replay_callback):
        s = ttk.Style()
        s.configure('.', font=('Helvetica', 12))

        self.trivia = trivia
        self.window = window

        self.canvas = ttk.Canvas(height=250, width=500, bg="white")
        self.text = self.canvas.create_text(250, 125, width=400, text='Q', font=("Ariel", 20))
        self.canvas.grid(column=0, row=6, columnspan=2, pady=50)

        self.score = ttk.Label(text="Current Score: 0", bootstyle="primary")
        self.score.grid(row=5, column=1)

        self.true_button = ttk.Button(text="True🙂", bootstyle="primary", command=self.true_clicked)
        self.true_button.grid(row=8, column=0)

        self.false_button = ttk.Button(text="False🙃", bootstyle="primary", command=self.false_clicked)
        self.false_button.grid(row=8, column=1)

        self.replay_button = ttk.Button(text="Replay", bootstyle="success", command=self.replay_clicked)


        self.replay_callback = replay_callback
        self.next_quiz()

        # self.window.mainloop()

    def next_quiz(self):
        self.canvas.config(bg="white")
        if not self.trivia.trivia_finished():
            self.score.config(text=f"Current Score: {self.trivia.score}")
            text = self.trivia.next_quiz()
            self.canvas.itemconfig(self.text, text=text)
        else:
            self.canvas.itemconfig(self.text, text="Congratulations! You've finished!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.replay_button.grid(row=7, column=0, columnspan=2)

    def true_clicked(self):
        if self.trivia.check_answer("true"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_quiz)

    def false_clicked(self):
        if self.trivia.check_answer("false"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_quiz)

    def replay_clicked(self):
        self.replay_callback()

    def destroy_ui(self):
        self.canvas.destroy()
        self.replay_button.destroy()
        self.true_button.destroy()
        self.false_button.destroy()
        self.score.destroy()

