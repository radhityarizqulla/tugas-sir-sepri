import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas koding aplikasi kuis")
        self.root.geometry("400x300")

        self.questions = [
            "Apa ibu kota Indonesia?",
            "Siapakah presiden Indonesia saat ini?",
            "Berapakah jumlah provinsi di Indonesia?"
        ]

        self.answers = [
            ["Jakarta", "Surabaya", "Bandung", "Semarang"],
            ["Joko Widodo", "Susilo Bambang Yudhoyono", "Megawati Soekarnoputri", "Soeharto"],
            ["34", "33", "35", "32"]
        ]

        self.correct_choices = [0, 0, 2] 

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Aplikasi kuis", font=("Arial", 20))
        self.label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)  

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(self.root, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio)
            radio.pack()

        self.next_button = tk.Button(self.root, text="Selanjutnya", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        self.question_label.config(text=self.questions[self.current_question])

        for i in range(4):
            self.radio_buttons[i].config(text=self.answers[self.current_question][i])

    def next_question(self):
        choice = self.radio_var.get()

        if choice == -1:
            messagebox.showerror("Error", "Pilih salah satu jawaban!")
            return

        if choice == self.correct_choices[self.current_question]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
            self.radio_var.set(-1)
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Skor Akhir", f"Skor Anda: {self.score}/{len(self.questions)}")
        self.root.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
