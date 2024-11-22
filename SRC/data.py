import os
import random
from faker import Faker
import mysql.connector

# Get the password from the environment variable
db_password = os.getenv('DB_PASSWORD')

fake = Faker()

# Establish connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=db_password,
    database='3309'
)

cursor = connection.cursor()

# Generate data for policeStation
def generate_police_station_data(num_records):
    for _ in range(num_records):
        while True:
            location = fake.city()
            cursor.execute("SELECT COUNT(*) FROM policeStation WHERE location = %s", (location,))
            if cursor.fetchone()[0] == 0:
                break
        station_name = fake.company()
        while True:
            contact_number = fake.unique.phone_number()[:10]
            cursor.execute("SELECT COUNT(*) FROM policeStation WHERE contactNumber = %s", (contact_number,))
            if cursor.fetchone()[0] == 0:
                break
        query = "INSERT INTO policeStation (location, stationName, contactNumber) VALUES (%s, %s, %s)"
        print(query % (location, station_name, contact_number))  # Print the query
        cursor.execute(query, (location, station_name, contact_number))
    connection.commit()

# Generate data for Suspect
def generate_suspect_data(num_records):
    for _ in range(num_records):
        while True:
            full_name = fake.name()
            dob = fake.date_of_birth(minimum_age=18, maximum_age=70)
            cursor.execute("SELECT COUNT(*) FROM Suspect WHERE fullName = %s AND dateOfBirth = %s", (full_name, dob))
            if cursor.fetchone()[0] == 0:
                break
        address = fake.address()
        criminal_record = random.choice([True, False])
        query = "INSERT INTO Suspect (fullName, dateOfBirth, Address, CriminalRecord) VALUES (%s, %s, %s, %s)"
        print(query % (full_name, dob, address, criminal_record))  # Print the query
        cursor.execute(query, (full_name, dob, address, criminal_record))
    connection.commit()

# Generate data for Incident
def generate_incident_data(num_records):
    for _ in range(num_records):
        incident_type = fake.word()
        incident_date = fake.date_this_decade()
        location = fake.city()
        incident_status = random.choice(['Open', 'Closed', 'Pending'])
        incident_desc = fake.sentence()
        query = "INSERT INTO Incident (incidentType, incidentDate, location, incidentStatus, incidentDesc) VALUES (%s, %s, %s, %s, %s)"
        print(query % (incident_type, incident_date, location, incident_status, incident_desc))  # Print the query
        cursor.execute(query, (incident_type, incident_date, location, incident_status, incident_desc))
    connection.commit()

# Generate data for policeOfficer
def generate_police_officer_data(num_records):
    cursor.execute("SELECT location FROM policeStation")
    stations = cursor.fetchall()
    for _ in range(num_records):
        full_name = fake.name()
        date_of_hire = fake.date_this_decade()
        date_of_birth = fake.date_of_birth(minimum_age=22, maximum_age=60)
        
        # Ensure unique staffEmail
        while True:
            staff_email = fake.unique.email()
            cursor.execute("SELECT COUNT(*) FROM policeOfficer WHERE staffEmail = %s", (staff_email,))
            if cursor.fetchone()[0] == 0:
                break
        
        while True:
            phone_number = fake.unique.phone_number()[:10]
            cursor.execute("SELECT COUNT(*) FROM policeOfficer WHERE phoneNumber = %s", (phone_number,))
            if cursor.fetchone()[0] == 0:
                break
        
        station_location = random.choice(stations)[0]
        query = "INSERT INTO policeOfficer (fullName, dateOfHire, dateOfBirth, staffEmail, phoneNumber, stationLocation) VALUES (%s, %s, %s, %s, %s, %s)"
        print(query % (full_name, date_of_hire, date_of_birth, staff_email, phone_number, station_location))  # Print the query
        cursor.execute(query, (full_name, date_of_hire, date_of_birth, staff_email, phone_number, station_location))
    connection.commit()

# Generate data for adminStaff
def generate_admin_staff_data(num_records):
    cursor.execute("SELECT location FROM policeStation")
    stations = cursor.fetchall()
    for _ in range(num_records):
        full_name = fake.name()
        date_of_hire = fake.date_this_decade()
        date_of_birth = fake.date_of_birth(minimum_age=22, maximum_age=60)
        
        # Ensure unique staffEmail
        while True:
            staff_email = fake.unique.email()
            cursor.execute("SELECT COUNT(*) FROM adminStaff WHERE staffEmail = %s", (staff_email,))
            if cursor.fetchone()[0] == 0:
                break
        
        while True:
            phone_number = fake.unique.phone_number()[:10]
            cursor.execute("SELECT COUNT(*) FROM adminStaff WHERE phoneNumber = %s", (phone_number,))
            if cursor.fetchone()[0] == 0:
                break
        
        station_location = random.choice(stations)[0]
        employee_role = random.choice(['Manager', 'Assistant', 'Coordinator'])
        query = "INSERT INTO adminStaff (staffEmail, fullName, dateOfHire, dateOfBirth, phoneNumber, stationLocation, employeeRole) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print(query % (staff_email, full_name, date_of_hire, date_of_birth, phone_number, station_location, employee_role))  # Print the query
        cursor.execute(query, (staff_email, full_name, date_of_hire, date_of_birth, phone_number, station_location, employee_role))
    connection.commit()

# Generate data for Warrant
def generate_warrant_data(num_records):
    cursor.execute("SELECT fullName, dateOfBirth FROM Suspect")
    suspects = cursor.fetchall()
    for _ in range(num_records):
        issued_date = fake.date_this_decade()
        expiration_date = fake.date_this_decade()
        warrant_status = random.choice(['Active', 'Expired'])
        suspect_name, suspect_dob = random.choice(suspects)
        query = "INSERT INTO Warrant (issuedDate, expirationDATE, warrantStatus, suspectName, suspectDOB) VALUES (%s, %s, %s, %s, %s)"
        print(query % (issued_date, expiration_date, warrant_status, suspect_name, suspect_dob))  # Print the query
        cursor.execute(query, (issued_date, expiration_date, warrant_status, suspect_name, suspect_dob))
    connection.commit()

# Generate data for Evidence
def generate_evidence_data(num_records):
    cursor.execute("SELECT incidentNumber FROM Incident")
    incidents = cursor.fetchall()
    for _ in range(num_records):
        evidence_desc = fake.sentence()
        collection_date = fake.date_this_decade()
        stored_location = fake.city()
        incident_number = random.choice(incidents)[0]
        query = "INSERT INTO Evidence (evidenceDesc, collectionDate, storedLocation, incident) VALUES (%s, %s, %s, %s)"
        print(query % (evidence_desc, collection_date, stored_location, incident_number))  # Print the query
        cursor.execute(query, (evidence_desc, collection_date, stored_location, incident_number))
    connection.commit()

# Generate data for policeEquipment
def generate_police_equipment_data(num_records):
    cursor.execute("SELECT badgeNumber FROM policeOfficer")
    officers = cursor.fetchall()
    cursor.execute("SELECT location FROM policeStation")
    stations = cursor.fetchall()
    
    equipment_mapping = {
        'Handcuffs': 'Tool',
        'Radio': 'Tool',
        'Taser': 'Weapon',
        'Body Camera': 'Tool',
        'Flashlight': 'Tool',
        'Baton': 'Weapon',
        'Pepper Spray': 'Weapon',
        'Riot Shield': 'Tool',
        'Bulletproof Vest': 'Tool',
        'Patrol Car': 'Vehicle'
    }
    
    for _ in range(num_records):
        while True:
            serial_number = fake.uuid4()[:12]
            cursor.execute("SELECT COUNT(*) FROM policeEquipment WHERE serialNumber = %s", (serial_number,))
            if cursor.fetchone()[0] == 0:
                break
        
        equipment_name = random.choice(list(equipment_mapping.keys()))
        equipment_type = equipment_mapping[equipment_name]
        purchase_date = fake.date_this_decade()
        equipment_status = random.choice(['Available', 'In Use', 'Damaged'])
        badge_number = random.choice(officers)[0]
        location = random.choice(stations)[0]
        query = "INSERT INTO policeEquipment (serialNumber, equipmentName, equipmentType, purchaseDate, equipmentStatus, badgeNumber, location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print(query % (serial_number, equipment_name, equipment_type, purchase_date, equipment_status, badge_number, location))  # Print the query
        cursor.execute(query, (serial_number, equipment_name, equipment_type, purchase_date, equipment_status, badge_number, location))
    connection.commit()

# Generate data for policeOfficer_Incident
def generate_police_officer_incident_data(num_records):
    cursor.execute("SELECT incidentNumber FROM Incident")
    incidents = cursor.fetchall()
    cursor.execute("SELECT staffEmail FROM policeOfficer")
    officers = cursor.fetchall()
    for _ in range(num_records):
        incident_number = random.choice(incidents)[0]
        staff_email = random.choice(officers)[0]
        assignment_date = fake.date_this_decade()
        assignment_role = random.choice(['Lead', 'Support', 'Investigator'])
        query = "INSERT INTO policeOfficer_Incident (incidentNumber, staffEmail, assignmentDate, assignmentRole) VALUES (%s, %s, %s, %s)"
        print(query % (incident_number, staff_email, assignment_date, assignment_role))  # Print the query
        cursor.execute(query, (incident_number, staff_email, assignment_date, assignment_role))
    connection.commit()

def generate_suspect_incident_data(num_records):
    cursor.execute("SELECT incidentNumber FROM Incident")
    incidents = cursor.fetchall()
    cursor.execute("SELECT suspectID FROM Suspect")
    suspects = cursor.fetchall()
    for _ in range(num_records):
        while True:
            incident_number = random.choice(incidents)[0]
            suspect_id = random.choice(suspects)[0]
            cursor.execute("SELECT COUNT(*) FROM suspect_incident WHERE incidentNumber = %s AND suspectID = %s", (incident_number, suspect_id))
            if cursor.fetchone()[0] == 0:
                break
        involvement_type = random.choice(['Witness', 'Accused', 'Victim'])
        query = "INSERT INTO suspect_incident (incidentNumber, suspectID, involvementType) VALUES (%s, %s, %s)"
        print(query % (incident_number, suspect_id, involvement_type))  # Print the query
        cursor.execute(query, (incident_number, suspect_id, involvement_type))
    connection.commit()

# Generate data for all tables
def generate_all_data():
    generate_police_station_data(10)
    generate_suspect_data(2000)
    generate_incident_data(1000)
    generate_police_officer_data(500)
    generate_admin_staff_data(200)
    generate_warrant_data(500)
    generate_evidence_data(1000)
    generate_police_equipment_data(1000)
    generate_police_officer_incident_data(200)
    generate_suspect_incident_data(2000)

# Function to truncate all tables
def truncate_all_tables():
    tables = [
        'policeOfficer_Incident', 'suspect_incident', 'policeEquipment', 'Evidence', 'Warrant',
        'adminStaff', 'policeOfficer', 'Incident', 'Suspect', 'policeStation'
    ]
    
    # Disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    
    for table in tables:
        cursor.execute(f"TRUNCATE TABLE {table}")
    
    # Re-enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    
    connection.commit()

# Start generating data
truncate_all_tables()
generate_all_data()

# Close the connection
cursor.close()
connection.close()

print("Data generation complete.")