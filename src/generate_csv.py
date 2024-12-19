import csv
from random import randint, random
from datetime import datetime

fields = ["user_id", "name", "email", "signup_date"]
rows = []

names = [
    # Male names
    "Marco", "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", 
    "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", 
    "Jackson", "Sebastian", "Jack", "Aiden", "Owen", "Samuel", "Matthew", "Joseph", 
    "Levi", "David", "John", "Wyatt", "Carter", "Julian", "Luke", "Grayson", "Isaac", 
    "Jayden", "Theodore", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln", "Jaxon", 
    "Asher", "Christopher", "Andrew", "Thomas", "Joshua", "Ezra", "Hudson", "Charles",
    
    # Female names
    "Polina", "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", 
    "Evelyn", "Harper", "Luna", "Camila", "Gianna", "Elizabeth", "Ella", "Sofia", 
    "Emily", "Avery", "Mila", "Scarlett", "Eleanor", "Madison", "Layla", "Penelope", 
    "Aria", "Chloe", "Grace", "Ellie", "Nora", "Hazel", "Zoey", "Riley", "Victoria", 
    "Lily", "Aurora", "Violet", "Nova", "Hannah", "Emilia", "Stella", 
    "Everly", "Isla", "Leah", "Lillian", "Addison", "Willow", "Lucy", "Paisley", "Natalie"
]
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", 
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", 
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", 
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", 
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", 
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", 
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", 
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", 
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", 
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", 
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Shevchenko"
]
domains = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "aol.com",
    "icloud.com",
    "mail.com",
    "protonmail.com",
    "zoho.com",
    "gmx.com",
    "live.com",
    "fastmail.com",
    "qq.com",
    "126.com",
    "163.com",
    "inbox.com",
    "msn.com",
    "me.com",
    "example.com",
    "tutanota.com",
    "rediffmail.com",
    "rocketmail.com"
]
unique_email = set()

result = lambda x: "0" + str(x) if x < 10 else str(x)

def randomDomain():
    return domains[randint(0, len(domains)-1)] # example.com

def randomTimestamp():
    start_date = int(datetime(2022, 1, 1, 0, 0, 0).timestamp())
    end_date = int(datetime(2024, 12, 18, 0, 0, 0).timestamp())

    return str(datetime.fromtimestamp(randint(start_date, end_date))) # 2023-03-07 01:17:29

def randomEmail(name:str, surname:str):
    match randint(1, 7):
        case 1:
            return str(name.lower() + "_" + surname.lower() + "@" + randomDomain()) # john_geller@example.com
        case 2:
            return str(name.lower() + str(randint(100, 3000)) + "@" + randomDomain()) # john2999@example.com
        case 3:
            return str(surname.lower() + str(randint(100, 3000)) + "@" + randomDomain()) # geller800@example.com
        case 4:
            return str(name[0].lower() + surname.lower() + "@" + randomDomain()) # jgeller@example.com
        case 5:
            return str(name.lower() + result(randint(1, 12)) + result(randint(1, 12)) + "@" + randomDomain()) # john1203@example.com
        case 6:
            return str(name.lower() + str(result(randint(1, 12))) * 2 + "@" + randomDomain()) # john0707@example.com
        case 7:
            return str(surname.lower() + result(randint(1, 12)) + result(randint(1, 12)) + "@" + randomDomain()) # geller1212@example.com

def run(rowsToCreate):
    global id
    id = 1
    
    while len(rows) < rowsToCreate:
        name = str(names[randint(0, len(names)-1)])
        surname = str(surnames[randint(0, len(surnames)-1)])

        while True:
            email = randomEmail(name=name, surname=surname)
            if email not in unique_email:
                unique_email.add(email)
                break
        
        row = []
        row.append(id)
        row.append(name + " " + surname)
        row.append(email)
        row.append(randomTimestamp())

        id += 1
        rows.append(row)

    with open("./data/data.csv", "wt") as file:
        csvwrier = csv.writer(file)
        csvwrier.writerow(fields)
        csvwrier.writerows(rows)

    print("Data was generated successfully!")
