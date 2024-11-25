-- Query 1: Retrieve all incidents with the status closed.
SELECT incidentNumber, incidentType, incidentDate, location, incidentDesc
FROM Incident
WHERE incidentStatus = 'Closed';

-- Query 2: List down all the police officers and their assigned stations including station contact numbers.
SELECT po.fullName AS officerName, po.staffEmail, ps.stationName, ps.contactNumber
FROM policeOfficer po
JOIN policeStation ps ON po.stationLocation = ps.location;

-- Query 3: retrieve all the suspects who have a warrant issued against them.
SELECT fullName, dateOfBirth, Address
FROM Suspect
WHERE (fullName, dateOfBirth) IN (
    SELECT suspectName, suspectDOB
    FROM Warrant
);

-- Query 4: Count the total number of incidents by status.
SELECT incidentStatus, COUNT(*) AS totalIncidents
FROM Incident
GROUP BY incidentStatus;

-- Query 5: Get all the police officers who are assigned to at least one incident.
SELECT fullName, staffEmail
FROM policeOfficer po
WHERE EXISTS (
    SELECT 1
    FROM policeOfficer_Incident poi
    WHERE poi.staffEmail = po.staffEmail
);

-- Query 6: retrieve details of incidents involving suspects, along with the assigned officer's information (this is limited to 5 results).
SELECT i.incidentNumber, i.incidentType, i.incidentDate, i.location, po.fullName AS officerName
FROM Incident i
JOIN suspect_incident si ON i.incidentNumber = si.incidentNumber
JOIN policeOfficer_Incident poi ON i.incidentNumber = poi.incidentNumber
JOIN policeOfficer po ON poi.staffEmail = po.staffEmail
LIMIT 5;

-- Query 7: Get the top 3 most recently issued warrants.
SELECT warrantID, issuedDate, expirationDATE, warrantStatus, suspectName
FROM Warrant
ORDER BY issuedDate DESC
LIMIT 3;