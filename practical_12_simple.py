"""
Practical 12: Simple Student Performance Analyzer
A basic GUI to track and display student marks
"""

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: Tkinter not found!")
    exit()


class SimplePerformanceAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance Analyzer")
        self.root.geometry("500x400")
        
        self.students = []
        
        # Title
        title = tk.Label(root, text="STUDENT PERFORMANCE ANALYZER", 
                        font=("Arial", 14, "bold"), bg='lightblue')
        title.pack(pady=10)
        
        # Input frame
        frame = tk.Frame(root, bg='lightblue')
        frame.pack(padx=10, pady=10, fill=tk.X)
        
        # Student name
        tk.Label(frame, text="Student Name:", bg='lightblue').pack(anchor='w')
        self.name_entry = tk.Entry(frame, width=40)
        self.name_entry.pack(anchor='w', pady=5)
        
        # Marks
        tk.Label(frame, text="Marks (0-100):", bg='lightblue').pack(anchor='w')
        self.marks_entry = tk.Entry(frame, width=40)
        self.marks_entry.pack(anchor='w', pady=5)
        
        # Buttons
        btn_frame = tk.Frame(root, bg='lightblue')
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Student", command=self.add_student, 
                 width=12, bg='green', fg='white').pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="View All", command=self.view_all, 
                 width=12, bg='blue', fg='white').pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_student, 
                 width=12, bg='red', fg='white').pack(side=tk.LEFT, padx=5)
        
        # Display area
        tk.Label(root, text="Student Records:", bg='lightblue', 
                font=("Arial", 10, "bold")).pack(anchor='w', padx=10)
        
        self.text_area = tk.Text(root, height=10, width=60, font=("Courier", 9))
        self.text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.refresh_display()
    
    def add_student(self):
        """Add a new student"""
        name = self.name_entry.get().strip()
        marks_str = self.marks_entry.get().strip()
        
        if not name or not marks_str:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        try:
            marks = float(marks_str)
            if not (0 <= marks <= 100):
                messagebox.showerror("Error", "Marks must be 0-100!")
                return
            
            # Calculate grade
            if marks >= 90:
                grade = 'A+'
            elif marks >= 80:
                grade = 'A'
            elif marks >= 70:
                grade = 'B'
            elif marks >= 60:
                grade = 'C'
            elif marks >= 50:
                grade = 'D'
            else:
                grade = 'F'
            
            self.students.append({'name': name, 'marks': marks, 'grade': grade})
            messagebox.showinfo("Success", f"Added {name}!")
            self.name_entry.delete(0, tk.END)
            self.marks_entry.delete(0, tk.END)
            self.refresh_display()
        except:
            messagebox.showerror("Error", "Invalid marks!")
    
    def view_all(self):
        """View all students"""
        if not self.students:
            messagebox.showinfo("Info", "No students added yet!")
        else:
            total_marks = sum(s['marks'] for s in self.students)
            avg_marks = total_marks / len(self.students)
            messagebox.showinfo("Summary", 
                              f"Total: {len(self.students)} students\n"
                              f"Average: {avg_marks:.2f} marks")
    
    def delete_student(self):
        """Delete a student"""
        if not self.students:
            messagebox.showwarning("Warning", "No students to delete!")
            return
        
        name = self.name_entry.get().strip()
        for i, s in enumerate(self.students):
            if s['name'].lower() == name.lower():
                self.students.pop(i)
                messagebox.showinfo("Success", f"Deleted {name}!")
                self.name_entry.delete(0, tk.END)
                self.refresh_display()
                return
        
        messagebox.showerror("Error", "Student not found!")
    
    def refresh_display(self):
        """Refresh the display area"""
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        
        if not self.students:
            self.text_area.insert(tk.END, "No students yet.\n")
        else:
            self.text_area.insert(tk.END, f"{'Name':<20} {'Marks':<10} {'Grade':<10}\n")
            self.text_area.insert(tk.END, "-" * 50 + "\n")
            
            for s in self.students:
                line = f"{s['name']:<20} {s['marks']:<10.0f} {s['grade']:<10}\n"
                self.text_area.insert(tk.END, line)
        
        self.text_area.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = SimplePerformanceAnalyzer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
