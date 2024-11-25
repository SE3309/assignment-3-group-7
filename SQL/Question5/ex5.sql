USE `Regional_Police_Department`;

-- Command 1: Close all incidents older than some interval (30 days here)
/* Step 1: Create a temporary table to store the incident numbers
 * This is done as safe update mode does not allow updates without 
 * providing a primary key, and accessing and modifying the table
 * is not allowed at the same time
 */
CREATE TEMPORARY TABLE TempIncident AS
SELECT incidentNumber
FROM Incident
WHERE incidentDate < CURDATE() - INTERVAL 30 DAY
  AND incidentStatus = 'Open';

-- Step 2: Update the rows using the temporary table
UPDATE Incident
SET incidentStatus = 'Closed'
WHERE incidentNumber IN (SELECT incidentNumber FROM TempIncident);

DROP TEMPORARY TABLE TempIncident;


-- Command 2: Delete outdated warrants
SET SQL_SAFE_UPDATES = 0; -- Disable safe updates instead of creating temp table

DELETE FROM Warrant
WHERE expirationDATE < CURDATE();

SET SQL_SAFE_UPDATES = 1;

-- Command 3: Inserting evidence for an incident
INSERT INTO Evidence (evidenceDesc, collectionDate, storedLocation, incident)
SELECT 'Fingerprint sample', CURDATE(), 'Evidence Room 1', incidentNumber
FROM Incident
WHERE incidentNumber = 23;




