import tkinter as tk
from tkinter import messagebox
from typing import List
import csv
from Project1_logic import StudentGrader

class StudentGraderGUI:
    """Class to create a GUI for student grading."""

    def __init__(self, master: tk.Tk) -> None:
        """Initialize the GUI."""
        self.master = master
        self.master.title("Student Grader")

        self.label1 = tk.Label(master, text="Total number of students:")
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Enter scores (space-separated):")
        self.label2.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        self.button = tk.Button(master, text="Calculate Grades", command=self.calculate_grades)
        self.button.pack()

    def calculate_grades(self) -> None:
        """Calculate grades based on user input."""
        try:
            total_students = int(self.entry1.get())
            scores = list(map(int, self.entry2.get().split()))

            if len(scores) != total_students:
                messagebox.showerror("Error", f"Please enter exactly {total_students} scores.")
                return

            grader = StudentGrader()
            grades = grader.calculate_grades(scores)
            self.display_grades(total_students, scores, grades)

            # Save data to CSV file
            self.save_to_csv(total_students, scores, grades)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter integers only.")

    def display_grades(self, total_students: int, scores: List[int], grades: List[str]) -> None:
        """Display grades in a new window."""
        result_window = tk.Toplevel(self.master)
        result_window.title("Grading Report")

        result_label = tk.Label(result_window, text="Grading Report:")
        result_label.pack()

        for i, grade in enumerate(grades):
            result_text = f"Student {i + 1} score is {scores[i]} and grade is {grade}"
            result_label = tk.Label(result_window, text=result_text)
            result_label.pack()

    def save_to_csv(self, total_students: int, scores: List[int], grades: List[str]) -> None:
        """Save grades to a CSV file."""
        with open('grades.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student", "Score", "Grade"])
            for i in range(total_students):
                writer.writerow([i + 1, scores[i], grades[i]])

    def load_from_csv(self) -> None:
        """Load grades from a CSV file."""
        try:
            with open('grading_results.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                data = [row for row in reader]
                if data:
                    total_students = len(data)
                    scores = [int(row[1]) for row in data]
                    grades = [row[2] for row in data]
                    self.display_grades(total_students, scores, grades)
                else:
                    messagebox.showinfo("Info", "No data available in the CSV file.")
        except FileNotFoundError:
            messagebox.showinfo("Info", "No data available in the CSV file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGraderGUI(root)
    root.mainloop()
