import tkinter as tk
from tkinter import ttk
from spinningwheel import SpinningWheelApp

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Collection and Symptoms Checklist")
        self.root.geometry("800x600")  # Set initial window size
        
        self.data = []
        
        self.create_info_page()

        # Button to choose a disease
        self.choose_disease_button = tk.Button(self.root, text="Choose a Disease", command=self.choose_disease)
        self.choose_disease_button.grid(row=0, column=2, sticky="ne", padx=10, pady=10)  # Grid positioning

    def create_info_page(self):
        self.clear_frame()
        
        # Create labels and entry fields
        tk.Label(self.root, text="Name:").grid(row=1, column=0, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="NID:").grid(row=2, column=0, pady=5)
        self.nid_entry = tk.Entry(self.root)
        self.nid_entry.grid(row=2, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Upozila:").grid(row=4, column=0, pady=5)
        self.upozila_entry = tk.Entry(self.root)
        self.upozila_entry.grid(row=4, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="District:").grid(row=5, column=0, pady=5)
        self.district_entry = tk.Entry(self.root)
        self.district_entry.grid(row=5, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Phone Number:").grid(row=6, column=0, pady=5)
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.grid(row=6, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Email Address:").grid(row=7, column=0, pady=5)
        self.email_address_entry = tk.Entry(self.root)
        self.email_address_entry.grid(row=7, column=1, columnspan=2, pady=5)

        # Create a button to submit the data
        submit_button = tk.Button(self.root, text="Next", command=self.submit_info)
        submit_button.grid(row=8, column=1, pady=10)

    def submit_info(self):
        self.name = self.name_entry.get()
        self.nid = self.nid_entry.get()
        self.address = self.address_entry.get()
        self.upozila = self.upozila_entry.get()
        self.district = self.district_entry.get()
        self.phone_number = self.phone_number_entry.get()
        self.email_address = self.email_address_entry.get()

        self.data.extend([
            f"Name: {self.name}",
            f"NID: {self.nid}",
            f"Address: {self.address}",
            f"Upozila: {self.upozila}",
            f"District: {self.district}",
            f"Phone Number: {self.phone_number}",
            f"Email Address: {self.email_address}"
        ])

        self.create_symptoms_page()

    def create_symptoms_page(self):
        self.clear_frame()

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
        common_frame.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")  # Grid positioning

        # Add checkboxes for common symptoms
        for index, symptom in enumerate(self.common_symptoms):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(common_frame, text=symptom, variable=var)
            chk.grid(row=index // 2, column=index % 2, sticky="w")
            self.symptom_vars[symptom] = var

        # Create a frame for long COVID symptoms
        long_covid_frame = ttk.LabelFrame(self.root, text="Long COVID Symptoms")
        long_covid_frame.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")  # Grid positioning

        # Add checkboxes for long COVID symptoms
        for index, symptom in enumerate(self.long_covid_symptoms):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(long_covid_frame, text=symptom, variable=var)
            chk.grid(row=index // 2, column=index % 2, sticky="w")
            self.symptom_vars[symptom] = var

        # Add a button to print selected symptoms
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_symptoms)
        submit_button.grid(row=3, column=2, pady=10)

    def choose_disease(self):
        root = tk.Tk()
        app = SpinningWheelApp(root)
        root.mainloop()

    def submit_symptoms(self):
        selected_symptoms = [symptom for symptom, var in self.symptom_vars.items() if var.get()]
        
        self.data.append("Selected Symptoms:")
        self.data.extend(selected_symptoms)
        
        for item in self.data:
            print(item)
        
        self.root.quit()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
