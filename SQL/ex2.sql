-- Define the policeStation table first, as it's referenced by others.
CREATE TABLE policeStation (
    location VARCHAR(255) NOT NULL PRIMARY KEY,
    stationName VARCHAR(255) NOT NULL,
    contactNumber VARCHAR(10) NOT NULL,
    UNIQUE (contactNumber)
);

-- Define the Suspect table, as it is referenced by Warrant and suspect_incident.
CREATE TABLE Suspect (
    suspectID INT AUTO_INCREMENT PRIMARY KEY, 
    fullName VARCHAR(255) NOT NULL,
    dateOfBirth DATE NOT NULL,
    Address VARCHAR(255),
    CriminalRecord BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (fullName, dateOfBirth)
);

-- Define the Incident table, as it's referenced by other tables.
CREATE TABLE Incident (
    incidentNumber INT AUTO_INCREMENT PRIMARY KEY, 
    incidentType VARCHAR(255) NOT NULL, 
    incidentDate DATE NOT NULL,
    location VARCHAR(255) NOT NULL,
    incidentStatus VARCHAR(255) NOT NULL,
    incidentDesc VARCHAR(255) NOT NULL
);

-- Define the policeOfficer table, as it's referenced by policeEquipment and policeOfficer_Incident.
CREATE TABLE policeOfficer (
    badgeNumber INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(255) NOT NULL,
    dateOfHire DATE NOT NULL,
    dateOfBirth DATE NOT NULL,
    staffEmail VARCHAR(255) NOT NULL UNIQUE,
    phoneNumber VARCHAR(10) NOT NULL, 
    stationLocation VARCHAR(255) NOT NULL,
    FOREIGN KEY (stationLocation) REFERENCES policeStation(location)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define adminStaff, as it references policeStation.
CREATE TABLE adminStaff (
    staffEmail VARCHAR(255) NOT NULL PRIMARY KEY,
    fullName VARCHAR(255) NOT NULL,
    dateOfHire DATE NOT NULL,
    dateOfBirth DATE NOT NULL,
    phoneNumber VARCHAR(10) NOT NULL, 
    stationLocation VARCHAR(255) NOT NULL, 
    employeeRole VARCHAR(255), 
    FOREIGN KEY (stationLocation) REFERENCES policeStation(location)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define Warrant, referencing Suspect.
CREATE TABLE Warrant (
    warrantID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    issuedDate DATE NOT NULL, 
    expirationDATE DATE NOT NULL,
    warrantStatus VARCHAR(255) NOT NULL,
    suspectName VARCHAR(255) NOT NULL,
    suspectDOB DATE NOT NULL,    
    FOREIGN KEY (suspectName, suspectDOB) REFERENCES Suspect(fullName, dateOfBirth)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define Evidence, referencing Incident.
CREATE TABLE Evidence (
    evidenceID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    evidenceDesc VARCHAR(255) NOT NULL,
    collectionDate DATE NOT NULL,
    storedLocation VARCHAR(255),
    incident INT NOT NULL,
    FOREIGN KEY (incident) REFERENCES Incident(incidentNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define policeEquipment, referencing policeStation and policeOfficer.
CREATE TABLE policeEquipment (
    serialNumber VARCHAR(12) PRIMARY KEY,
    equipmentName VARCHAR(25) NOT NULL,
    equipmentType VARCHAR(255) NOT NULL,
    purchaseDate DATE NOT NULL,
    equipmentStatus VARCHAR(255) NOT NULL,
    badgeNumber INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    FOREIGN KEY (location) REFERENCES policeStation(location)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (badgeNumber) REFERENCES policeOfficer(badgeNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define policeOfficer_Incident, referencing policeOfficer and Incident.
CREATE TABLE policeOfficer_Incident (
    incidentNumber INT NOT NULL,
    staffEmail VARCHAR(255) NOT NULL,
    assignmentDate DATE NOT NULL,
    assignmentRole VARCHAR(255) NOT NULL,
    PRIMARY KEY (incidentNumber, staffEmail),
    FOREIGN KEY (incidentNumber) REFERENCES Incident(incidentNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (staffEmail) REFERENCES policeOfficer(staffEmail)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Define suspect_incident, referencing Incident and Suspect.
CREATE TABLE suspect_incident (
    incidentNumber INT NOT NULL,
    suspectID INT NOT NULL,
    involvementType VARCHAR(255) NOT NULL,
    PRIMARY KEY (incidentNumber, suspectID),
    FOREIGN KEY (incidentNumber) REFERENCES Incident(incidentNumber)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (suspectID) REFERENCES Suspect(suspectID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);