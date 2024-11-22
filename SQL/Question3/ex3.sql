INSERT INTO policestation (location, stationName, contactNumber)
VALUE ('12 Downs St', 'Downtown Police Station', '1239839394');

INSERT INTO policeofficer (fullName, dateOfBirth, dateOfHire, staffEmail, phoneNumber, stationLocation)
SELECT 'John Doe','2022-06-15', '1990-04-23', 'JohnDoe@gmail.com', '902823489', location 
FROM policestation 
WHERE stationName = 'Downtown Police Station';

INSERT INTO policeequipment (serialNumber, equipmentName, equipmentType, purchaseDate, equipmentStatus, badgeNumber, location)
SELECT 'ETRFJ32RJ2J3', 'Body Cam', 'Surveillance', '2024-01-15', 'In-Field', po.badgeNumber, ps.location
FROM policeofficer po 
JOIN policestation ps ON po.stationLocation = ps.location
WHERE ps.stationName = 'Downtown Police Station' AND po.fullName = 'John Doe';