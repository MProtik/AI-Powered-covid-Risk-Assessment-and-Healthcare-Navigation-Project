import tkinter as tk
from tkinter import messagebox
import random
import math

# List of symptoms
symptoms = [
"Dengue Fever", "Cholera","Malaria","Tuberculosis","Hepatitis A and E","Diarrheal Diseases",
"Typhoid Fever","Japanese Encephalitis","Leptospirosis","Rabies","Pneumonia","Leprosy",
"Kala-Azar (Visceral Leishmaniasis)","Filariasis","HIV/AIDS","Diabetes","Hypertension","Asthma","Chronic Obstructive Pulmonary Disease (COPD)",
"Stroke"
]

class SpinningWheelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symptom Spinning Wheel")
        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()
        self.angle = 0
        self.sectors = len(symptoms)
        self.radius = 250
        self.center = 300
        self.create_wheel()
        self.button = tk.Button(root, text="Spin", command=self.spin_wheel)
        self.button.pack(pady=20)

    def create_wheel(self):
        self.canvas.delete("all")
        colors = ["#FF9999", "#FFCC99", "#FFFF99", "#CCFF99", "#99FF99",
                  "#99FFCC", "#99FFFF", "#99CCFF", "#9999FF", "#CC99FF",
                  "#FF99FF", "#FF99CC", "#FF6699", "#FF6666", "#FF9966",
                  "#FFCC66", "#FFFF66", "#CCFF66"]
        for i in range(self.sectors):
            start_angle = i * (360 / self.sectors)
            end_angle = start_angle + (360 / self.sectors)
            self.canvas.create_arc((self.center - self.radius, self.center - self.radius, 
                                    self.center + self.radius, self.center + self.radius),
                                   start=start_angle, extent=(360 / self.sectors),
                                   fill=colors[i % len(colors)], outline="black")
            mid_angle = (start_angle + end_angle) / 2
            x = self.center + (self.radius - 30) * math.cos(mid_angle * math.pi / 180)
            y = self.center - (self.radius - 30) * math.sin(mid_angle * math.pi / 180)
            self.canvas.create_text(x, y, text=symptoms[i], angle=mid_angle, font=("Helvetica", 10, "bold"))

    def spin_wheel(self):
        # Pick a random symptom
        target_index = random.randint(0, self.sectors - 1)
        target_angle = target_index * (360 / self.sectors)

        # Animate the spin
        spins = random.randint(5, 10)
        current_angle = self.angle

        for _ in range(spins):
            for _ in range(360 // 10):
                current_angle = (current_angle + 10) % 360
                self.update_arrow(current_angle)
                self.root.update()
                self.root.after(10)

        # Slow down to the final angle
        while abs(current_angle - target_angle) > 10:
            current_angle = (current_angle + 10) % 360
            self.update_arrow(current_angle)
            self.root.update()
            self.root.after(10)
        
        self.update_arrow(target_angle)
        self.angle = target_angle

        result = symptoms[target_index]
        messagebox.showinfo("Congratulations!", f"Congratulations! You have {result}.")

    def update_arrow(self, angle):
        self.canvas.delete("arrow")
        self.canvas.create_line(self.center, self.center, 
                                self.center + self.radius * math.cos(angle * math.pi / 180),
                                self.center - self.radius * math.sin(angle * math.pi / 180), 
                                fill="red", width=3, arrow=tk.LAST, tag="arrow")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
