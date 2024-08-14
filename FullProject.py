import tkinter as tk
import mysql.connector
from tkinter import messagebox, Text, Scrollbar, VERTICAL
import frontend
import BackEnd
from datetime import date

def connect_to_db():
    try:
        con = mysql.connector.connect(
            host="Protiks-MacBook-Air.local",
            user="root",
            password="password",   
            database="Covid_19_database"
        )
        cursor = con.cursor()
        print("Connected successfully")
        return con, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None, None
    

def fetch_hospitals(cursor, city):
    query = f"""SELECT Upazilla as Hospitals, ContactNumber FROM `nearesthospitals` WHERE District = '{city}'"""
    cursor.execute(query)
    return cursor.fetchall()

def fetch_covid_stats(cursor, city):
    query = f"""SELECT `District name` as City, `Covid percentage2` as `Covid Percentage` FROM `main database` WHERE `District name` = "{city}";"""
    cursor.execute(query)
    return cursor.fetchall()

def insert_user_data(cursor, con, data, probability, time):
    query = f"""INSERT INTO User_database (Name, Age, Gender, NID, Address, Upozila, District, `Phone Number`, Email, `Posterior probability`, Date)
    VALUES ('{data['Name']}', {data['Age']}, '{data['Gender']}', '{data['NID']}', '{data['Address']}', '{data['Upozila']}', '{data['District']}', '{data['Phone Number']}', '{data['Email']}', {probability}, "{time}");"""
    cursor.execute(query)
    con.commit()


def create_ui(root, result_text, hospitals):
    root.title("COVID-19 Risk Assessment")
    root.geometry("600x600")

    header_label = tk.Label(root, text="COVID-19 Risk Assessment", font=("Helvetica", 16, "bold"))
    header_label.grid(row=0, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text=result_text, font=("Helvetica", 12))
    result_label.grid(row=1, column=0, columnspan=2, pady=10)

    hospital_frame = tk.Frame(root)
    hospital_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    hospital_label = tk.Label(hospital_frame, text="Nearest Hospitals", font=("Helvetica", 14, "bold"))
    hospital_label.pack(side=tk.TOP, pady=5)

    hospital_text_widget = Text(hospital_frame, height=15, width=80, wrap="word")
    hospital_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = Scrollbar(hospital_frame, orient=VERTICAL, command=hospital_text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    hospital_text_widget.config(yscrollcommand=scrollbar.set)

    hospital_text = "Hospitals\t\tContact Number\n\n"
    for hospital, contact in hospitals:
        hospital_text += f"{hospital}\t\t{contact}\n"
    
    hospital_text_widget.insert(tk.END, hospital_text)
    hospital_text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = frontend.Application(root)
    root.mainloop()

    con, cursor = connect_to_db()
    if not con or not cursor:
        exit(1)

    # l = ['Name: Mokabbir Protik', 'Age: 31', 'Gender: Male', 'NID: 402934893', 'Address: west brahmondi', 'Upozila: narsingdi sadar', 
    #      'District: Dhaka', 'Phone Number: 01911922242', 'Email Address: mzprotik88@gmail.com', 'Selected Symptoms:', "Fever or chills","Cough","Shortness of breath or difficulty breathing","Fatigue",
    #     "Muscle or body aches","Headache"," New loss of taste or smell","Sore throat","Congestion or runny nose","Nausea or vomiting","Diarrhea","Trouble Breathing","Persistent pain or pressure in the chest",
    #     "Joint pain", "Chest pain","Difficulty concentration", "Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone"]

    l = app.data
    city = l[6][10:]
    symptoms = l[10:]
    age = int(l[1][5:])

    hospitals = fetch_hospitals(cursor, city)
    covid_stats = fetch_covid_stats(cursor, city)
    posterior_probability = BackEnd.get_posterior_probability(city, age, symptoms)
    result_text = f"Posterior probability of having COVID-19 for age group {age} in {city}\n\n\n: {posterior_probability:.2f}"
    print(result_text)
    messagebox.showinfo("COVID-19 Risk Assessment", result_text)

    user_data = {
        "Name": l[0][l[0].index(":")+2:],
        "Age": int(l[1][l[1].index(":")+2:]),
        "Gender": l[2][l[2].index(":")+2:],
        "NID": l[3][l[3].index(":")+2:],
        "Address": l[4][l[4].index(":")+2:],
        "Upozila": l[5][l[5].index(":")+2:],
        "District": l[6][l[6].index(":")+2:],
        "Phone Number": l[7][l[7].index(":")+2:],
        "Email": l[8][l[8].index(":")+2:] 
    }

    time = date.today()
    insert_user_data(cursor, con, user_data, posterior_probability, time)

    create_ui(root, result_text, hospitals)

    root.mainloop()

    #have to see why lagging
