import tkinter as tk
import random

class SpinningWheel:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Wheel")
        self.canvas = tk.Canvas(root, width=400, height=450)
        self.canvas.pack()

        # Initialize wheel properties
        self.radius = 150
        self.center_x = 200
        self.center_y = 200
        self.segments = 8
        self.angle = 0
        self.is_spinning = False

        # Draw the wheel and arrow
        self.draw_wheel()
        self.draw_arrow()

        # Create a button to start the spin
        self.start_button = tk.Button(root, text="Spin", command=self.start_spin)
        self.start_button.pack()

    def draw_wheel(self):
        self.canvas.delete("wheel")
        for i in range(self.segments):
            start_angle = i * (360 / self.segments) + self.angle
            end_angle = start_angle + (360 / self.segments)
            color = "red" if i % 2 == 0 else "blue"
            self.canvas.create_arc(
                self.center_x - self.radius, self.center_y - self.radius,
                self.center_x + self.radius, self.center_y + self.radius,
                start=start_angle, extent=360 / self.segments,
                fill=color, outline="black", tags="wheel"
            )

    def draw_arrow(self):
        self.canvas.delete("arrow")
        points = [self.center_x, self.center_y - self.radius - 10,
                  self.center_x - 10, self.center_y - self.radius + 10,
                  self.center_x + 10, self.center_y - self.radius + 10]
        self.canvas.create_polygon(points, fill="black", tags="arrow")

    def start_spin(self):
        if not self.is_spinning:
            self.is_spinning = True
            self.spin_speed = 20  # initial speed
            self.deceleration = 0.99  # deceleration factor
            self.min_spin_speed = 0.1  # minimum speed to stop
            self.target_segment = random.randint(0, self.segments - 1)
            self.target_angle = self.target_segment * (360 / self.segments)
            self.spin_duration = 3000  # spin duration in milliseconds
            self.start_time = self.root.after(0, self.spin_wheel)

    def spin_wheel(self):
        self.angle += self.spin_speed
        self.draw_wheel()
        
        # Spin for a fixed duration before slowing down
        if self.spin_duration > 0:
            self.spin_duration -= 50
            self.root.after(50, self.spin_wheel)
        else:
            if self.spin_speed > self.min_spin_speed:
                self.spin_speed *= self.deceleration
                self.root.after(50, self.spin_wheel)
            else:
                # Correct the final position to align exactly with the target segment
                self.angle = self.target_angle
                self.draw_wheel()
                self.is_spinning = False
                self.root.after(1000, self.stop_spin)  # Wait for 1 second before stopping

    def stop_spin(self):
        self.is_spinning = False

if __name__ == "__main__":
    root = tk.Tk()
    wheel = SpinningWheel(root)
    root.mainloop()
