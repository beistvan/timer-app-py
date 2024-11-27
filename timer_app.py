import tkinter as tk
from tkinter import ttk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.running = False
        self.countdown_mode = False
        self.time = 0

        self.label = ttk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.countdown_button = ttk.Button(root, text="Start Countdown", command=self.start_countdown)
        self.countdown_button.pack(side=tk.LEFT, padx=20)

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.update_timer()

    def start(self):
        if not self.running:
            self.running = True
            self.countdown_mode = False
            self.update_timer()

    def pause(self):
        if self.running:
            self.running = False

    def stop(self):
        self.running = False
        self.time = 0
        self.update_label()

    def start_countdown(self):
        if not self.running:
            self.running = True
            self.countdown_mode = True
            self.time = 60 * 15 + 1  # Set countdown time in seconds (e.g., 60 seconds)
            self.update_timer()

    def update_timer(self):
        if self.running:
            if self.countdown_mode:
                if self.time > 0:
                    self.time -= 1
                else:
                    self.running = False
            else:
                self.time += 1
            self.update_label()
            self.root.after(1000, self.update_timer)

    def update_label(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
