
import tkinter as tk
import random

class FakeBlueScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("BlueScreen Simulator")
        self.root.configure(bg="#0078D7")

        self.fullscreen = True
        self.progress = 0
        self.running = True

        self.root.attributes("-fullscreen", True)

        self.root.bind("<Escape>", self.close)
        self.root.bind("<F11>", self.toggle_fullscreen)

        self.canvas = tk.Canvas(
            root,
            bg="#0078D7",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.root.bind("<Configure>", self.draw)
        self.draw()

        self.update_progress()

    def draw(self, event=None):
        if not self.running:
            return

        self.canvas.delete("all")

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width < 100 or height < 100:
            return

        # Sad face
        self.canvas.create_text(
            80, 75,
            text=":(",
            fill="white",
            font=("Segoe UI", 65),
            anchor="nw"
        )

        # Main message
        self.canvas.create_text(
            85, 205,
            text="Your PC ran into a problem",
            fill="white",
            font=("Segoe UI", 30),
            anchor="nw"
        )

        self.canvas.create_text(
            85, 260,
            text="and needs to restart.",
            fill="white",
            font=("Segoe UI", 30),
            anchor="nw"
        )

        self.canvas.create_text(
            85, 335,
            text="This is a simulated Blue Screen. Your PC is safe.",
            fill="white",
            font=("Segoe UI", 15),
            anchor="nw"
        )

        # Progress
        self.canvas.create_text(
            85, 405,
            text=f"{self.progress}% complete",
            fill="white",
            font=("Segoe UI", 16),
            anchor="nw"
        )

        # Fake QR area
        qr_x = 90
        qr_y = 480
        cell = 5

        random.seed(42)

        for row in range(21):
            for col in range(21):
                if random.random() > 0.5:
                    self.canvas.create_rectangle(
                        qr_x + col * cell,
                        qr_y + row * cell,
                        qr_x + (col + 1) * cell,
                        qr_y + (row + 1) * cell,
                        fill="white",
                        outline="white"
                    )

        self.canvas.create_text(
            220, 485,
            text="For more information about this\nsimulation, close this window.",
            fill="white",
            font=("Segoe UI", 12),
            anchor="nw",
            justify="left"
        )

        self.canvas.create_text(
            85, height - 75,
            text="STOP CODE: SIMULATED_SYSTEM_ERROR",
            fill="white",
            font=("Consolas", 12),
            anchor="nw"
        )

        self.canvas.create_text(
            width - 20, height - 30,
            text="SIMULATION  |  ESC = EXIT",
            fill="white",
            font=("Segoe UI", 10),
            anchor="se"
        )

    def update_progress(self):
        if not self.running:
            return

        if self.progress < 100:
            self.progress += random.randint(1, 4)
            self.progress = min(self.progress, 100)

            self.draw()
            self.root.after(1500, self.update_progress)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def close(self, event=None):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = FakeBlueScreen(root)
    root.mainloop()
