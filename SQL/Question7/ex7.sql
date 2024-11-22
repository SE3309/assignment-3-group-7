USE `3309`;

-- Creating the ActiveManagers view
DROP VIEW IF EXISTS ActiveManagers;
CREATE VIEW ActiveManagers AS
SELECT staffEmail, fullName, stationLocation, dateOfHire
FROM adminstaff
WHERE employeeRole = 'Manager';

INSERT INTO ActiveManagers (staffEmail, fullName, stationLocation, dateOfHire)
VALUES ('jdoe@example.com', 'John Doe', 'Morrisonfurt', '2024-11-22');

SELECT * FROM ActiveManagers LIMIT 5;

-- Creating the StaffAtColemanview view
DROP VIEW IF EXISTS StaffAtColemanview;
CREATE VIEW StaffAtColemanview AS
SELECT staffEmail, fullName, employeeRole
FROM adminstaff
WHERE stationLocation = 'Colemanview';

SELECT * FROM StaffAtColemanview LIMIT 5;
