import tkinter as tk
from tkinter import ttk

class CovidSymptomsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Symptoms Checklist")
        
        # Common Symptoms
        self.common_symptoms = [
            "Fever or chills", "Cough", "Shortness of breath or difficulty breathing",
            "Fatigue", "Muscle or body aches", "Headache",
            "New loss of taste or smell", "Sore throat",
            "Congestion or runny nose", "Nausea or vomiting", "Diarrhea"
        ]
        
        # Long COVID Symptoms
        self.long_covid_symptoms = [
            "Fatigue", "Brain fog", "Joint pain",
            "Chest pain", "Difficulty concentrating", "Sleep problems"
        ]

        self.symptom_vars = {}

        # Create a frame for common symptoms
        common_frame = ttk.LabelFrame(self.root, text="Common Symptoms")
        common_frame.pack(padx=10, pady=5, fill="x")

        # Add checkboxes for common symptoms
        for symptom in self.common_symptoms:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(common_frame, text=symptom, variable=var)
            chk.pack(anchor="w")
            self.symptom_vars[symptom] = var

        # Create a frame for long COVID symptoms
        long_covid_frame = ttk.LabelFrame(self.root, text="Long COVID Symptoms")
        long_covid_frame.pack(padx=10, pady=5, fill="x")

        # Add checkboxes for long COVID symptoms
        for symptom in self.long_covid_symptoms:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(long_covid_frame, text=symptom, variable=var)
            chk.pack(anchor="w")
            self.symptom_vars[symptom] = var

        # Add a button to print selected symptoms
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack(pady=10)

    def submit(self):
        selected_symptoms = [symptom for symptom, var in self.symptom_vars.items() if var.get()]
        print("Selected Symptoms:")
        for symptom in selected_symptoms:
            print(symptom)

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidSymptomsApp(root)
    root.mainloop()
