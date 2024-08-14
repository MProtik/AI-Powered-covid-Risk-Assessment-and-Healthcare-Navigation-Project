import frontend

def bayesian_update(prior, likelihood, marginal_likelihood):
    return (likelihood / marginal_likelihood) + prior


def calculate_posterior(prior, likelihoods, marginal_likelihoods):
    new = zip(likelihoods, marginal_likelihoods) 
    percentage = prior
    for likelihood, marginal_likelihood in new:
        percentage = bayesian_update(percentage, likelihood, marginal_likelihood)
    return percentage

city_data = frontend.city_data


symptom_likelihoods = {
    "Fever or chills": 0.2, 
    "Cough": 0.6,
    "Shortness of breath or difficulty breathing": 0.3,
    "Fatigue": 0.05,
    "Muscle or body aches": 0.5,
    "Headache": 0.104,
    "New loss of taste or smell": 0.37,  #***
    "Sore throat": 0.05,
    "Congestion or runny nose": 0.048,
    "Nausea or vomiting": 0.10,
    "Diarrhea": 0.02,
    "Trouble Breathing": 0.34,
    "Persistent pain or pressure in the chest": 0.05,
    "Joint pain": 0.149,
    "Chest pain": 0.11,
    "Difficulty concentrating": 0.1,
    "Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone": 0.03
}

marginal_symptom_likelihoods = {
    "Fever or chills": 0.015,  #***
    "Cough": 0.0385, #***
    "Shortness of breath or difficulty breathing": 0.05, #**
    "Fatigue": 0.011, #**
    "Muscle or body aches": 0.2, #**
    "Headache": 0.01, #**
    "New loss of taste or smell": 0.04, #***
    "Sore throat": 0.049, #*
    "Congestion or runny nose": 0.047, #*
    "Nausea or vomiting": 0.099,#*
    "Diarrhea": 0.019, #*
    "Trouble Breathing": 0.06, #**
    "Persistent pain or pressure in the chest": 0.0495, #**
    "Joint pain": 0.0368, #**
    "Chest pain": 0.048, #**
    "Difficulty concentrating": 0.099, 
    "Pale, gray, or blue-colored skin, lips, or nail beds, depending on skin tone": 0.0298
}

# Data for different age groups and symptoms (example, replace with actual data)
age_groups_data = {
    "0-10": 0.005,
    "10-20": 0.30,
    "20-30": 0.57,
    "30-40": 0.40,
    "40-50": 0.56,
    "50-60": 0.43,
    "60-70": 0.32,
    "70-80": 0.25,
    "80+": 0.35
}

def get_posterior_probability(city, age, symptoms):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    if age <= 10:
        age_group = "0-10"
    elif age <= 20:
        age_group = "10-20"
    elif age <= 30:
        age_group = "20-30"
    elif age <= 40:
        age_group = "30-40"
    elif age <= 50:
        age_group = "40-50"
    elif age <= 60:
        age_group = "50-60"
    elif age <= 70:
        age_group = "60-70"
    elif age <= 80:
        age_group = "70-80"
    else:
        age_group = "80+"

    if city not in city_data:
        raise ValueError("City not found in database.")
    if age_group not in age_groups_data:
        raise ValueError("Age group not found in database.")
    
    prior = 0
    likelihoods = [symptom_likelihoods.get(symptom, 0) for symptom in symptoms]
    marginal_likelihoods = [marginal_symptom_likelihoods.get(symptom, 1) for symptom in symptoms]
    
    return calculate_posterior(prior, likelihoods, marginal_likelihoods)  + age_groups_data[age_group] + city_data[city]

# if __name__ == "__main__":
#     try:
#         #city = input("Enter the city you live in: ")
#         city = "Dhaka"
#         #age = int(input("Enter your age: "))
#         age = 40
#         #symptoms = input("Enter your symptoms (comma-separated): ").split(", ")
#         symptoms = "Fever or chills", "Shortness of breath or difficulty breathing"
#         posterior_probability = get_posterior_probability(city, age, symptoms)
#         print(f"Posterior probability of having COVID-19 for age {age} in {city} with symptoms {symptoms}: {posterior_probability:.2f}")
#     except ValueError as e:
#         print(e)
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
