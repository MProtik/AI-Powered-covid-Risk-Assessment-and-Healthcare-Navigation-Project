import tkinter as tk
from tkinter import ttk, messagebox
from spinningwheel import SpinningWheelApp
import mysql.connector

try:
    con = mysql.connector.connect(host="Protiks-MacBook-Air.local", user="root", password="password", database="Covid_19_database")
except:
    print("Connection Problem")
else:
    cursor = con.cursor()
    print("Connected successfully")

query = "SELECT `District name`, `Covid percentage2` AS CovidPercentage FROM `main database`;"
cursor.execute(query)
record = cursor.fetchall()
record = list(record)

# Making hashmap
city_data = dict()
for i in range(len(record)):
    city_data[record[i][0]] = record[i][1]

cities = list(city_data.keys())


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Powered COVID Risk Assessment and Healthcare Navigation")
        self.root.geometry("800x600")  # Set initial window size
        
        self.data = []
        
        self.create_front_page()

    def create_front_page(self):
        self.clear_frame()
        
        # Create Register button
        register_button = ttk.Button(self.root, text="Register", command=self.create_info_page)
        register_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Create See Your Data button
        see_data_button = ttk.Button(self.root, text="See Your Data", command=self.prompt_for_data)
        see_data_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def create_info_page(self):
        self.clear_frame()
        
        # Create labels and entry fields
        tk.Label(self.root, text="Name:").grid(row=1, column=0, pady=5)  # name form
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, columnspan=2, pady=5) 
        
        tk.Label(self.root, text="Age:").grid(row=2, column=0, pady=5)  # age form
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Gender:").grid(row=3, column=0, pady=5)  # gender form
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.root, textvariable=self.gender_var)
        self.gender_combobox['values'] = ['Male', 'Female', 'Trans']
        self.gender_combobox.grid(row=3, column=1, columnspan=2, pady=5)
        self.gender_combobox.current(0)  # Set default value

        tk.Label(self.root, text="NID:").grid(row=4, column=0, pady=5)  # NID form
        self.nid_entry = tk.Entry(self.root) 
        self.nid_entry.grid(row=4, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Address:").grid(row=5, column=0, pady=5)  # address form
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=5, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Upozila:").grid(row=6, column=0, pady=5)  # upozila form
        self.upozila_entry = tk.Entry(self.root)
        self.upozila_entry.grid(row=6, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="District:").grid(row=7, column=0, pady=5)  # district form
        self.district_var = tk.StringVar()
        self.district_combobox = ttk.Combobox(self.root, textvariable=self.district_var)
        self.district_combobox['values'] = cities
        self.district_combobox.grid(row=7, column=1, columnspan=2, pady=5)
        self.district_combobox.current(0)  # Set default value

        tk.Label(self.root, text="Phone Number:").grid(row=8, column=0, pady=5)  # phone number form
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.grid(row=8, column=1, columnspan=2, pady=5)

        tk.Label(self.root, text="Email Address:").grid(row=9, column=0, pady=5)  # email address form
        self.email_address_entry = tk.Entry(self.root)
        self.email_address_entry.grid(row=9, column=1, columnspan=2, pady=5)

        # Create a button to submit the data
        submit_button = tk.Button(self.root, text="Next", command=self.submit_info)
        submit_button.grid(row=10, column=1, pady=10)

        # Button to choose a disease
        self.choose_disease_button = tk.Button(self.root, text="Choose a Disease", command=self.choose_disease)
        self.choose_disease_button.grid(row=0, column=2, sticky="ne", padx=10, pady=10)  # Grid positioning

    def submit_info(self):
        self.name = self.name_entry.get().strip()
        self.age = self.age_entry.get().strip()
        self.gender = self.gender_var.get().strip()
        self.nid = self.nid_entry.get().strip()
        self.address = self.address_entry.get().strip()
        self.upozila = self.upozila_entry.get().strip()
        self.district = self.district_var.get().strip()
        self.phone_number = self.phone_number_entry.get().strip()
        self.email_address = self.email_address_entry.get().strip()

        # Check if any field is empty
        if not self.name or not self.age or not self.gender or not self.nid or not self.address or not self.upozila or not self.district or not self.phone_number or not self.email_address:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        # Check if age is a number
        if not self.age.isdigit():
            messagebox.showerror("Error", "Age must be a number!")
            return

        self.data.extend([
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Gender: {self.gender}",
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
            "Trouble Breathing", "Persistent pain or pressure in the chest", "Joint pain",
            "Chest pain", "Difficulty concentrating", "Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone"
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
        long_covid_frame = ttk.LabelFrame(self.root, text="Emergency Warning signs")
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
        
        self.root.quit()

    def prompt_for_data(self):
        self.clear_frame()
        
        # Create labels and entry fields for name and phone number
        tk.Label(self.root, text="Name:").grid(row=0, column=0, pady=5)
        self.search_name_entry = tk.Entry(self.root)
        self.search_name_entry.grid(row=0, column=1, columnspan=2, pady=5)
        
        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0, pady=5)
        self.search_phone_entry = tk.Entry(self.root)
        self.search_phone_entry.grid(row=1, column=1, columnspan=2, pady=5)
        
        # Create a button to submit the data
        submit_button = ttk.Button(self.root, text="Submit", command=self.print_user_data)
        submit_button.grid(row=2, column=1, pady=10)

    def print_user_data(self):
        search_name = self.search_name_entry.get().strip()
        search_phone = self.search_phone_entry.get().strip()

        if not search_name or not search_phone:
            messagebox.showerror("Error", "Both fields must be filled!")
            return

        print(f"Name: {search_name}, Phone Number: {search_phone}")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
