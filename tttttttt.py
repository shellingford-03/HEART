import tkinter as tk
import random

# Danh sách màu cho trước
mau_choices = ["#ffffff", "#00ff00", "#0000ff", "#ff0000"]

class Heart:
    def __init__(self):
        self.HEART_COLOR = random.choice(mau_choices)
    
    def thay_doi_mau_lien_tuc(self, canvas, delay_ms=1000):
        self.HEART_COLOR = random.choice(mau_choices)
        canvas.config(bg=self.HEART_COLOR)
        canvas.after(delay_ms, self.thay_doi_mau_lien_tuc, canvas, delay_ms)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Thay đổi màu liên tục")

    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()

    heart = Heart()
    canvas.config(bg=heart.HEART_COLOR)
    heart.thay_doi_mau_lien_tuc(canvas)

    root.mainloop()
