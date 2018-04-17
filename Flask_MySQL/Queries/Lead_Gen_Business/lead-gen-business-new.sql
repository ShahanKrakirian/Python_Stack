-- 1. What query would you run to get the total revenue for March of 2012?

SELECT MONTHNAME(charged_datetime) AS month, SUM(amount) AS total
FROM billing 
WHERE charged_datetime BETWEEN '2012-03-01 00:00:00' AND '2012-04-01 00:00:00';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?

SELECT clients.client_id AS Client_2, SUM(amount) AS Total
FROM billing 
LEFT JOIN clients ON clients.client_id = billing.client_id
WHERE clients.client_id = 2
GROUP BY clients.client_id;

-- 3. What query would you run to get all the sites that client=10 owns?

SELECT sites.domain_name AS Websites, clients.client_id AS Owner
FROM sites
LEFT JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

SELECT clients.client_id AS Client, COUNT(sites.created_datetime) AS Number_of_Sites, DATE_FORMAT(sites.created_datetime, '%M') AS Month, DATE_FORMAT(sites.created_datetime, '%Y') AS Year 
FROM sites
LEFT JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 1
GROUP BY DATE_FORMAT(sites.created_datetime, '%M %Y');

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?

SELECT sites.domain_name AS Site, COUNT(leads.leads_id) AS Total_Leads, DATE_FORMAT(leads.registered_datetime, '%D %M %Y') AS Date_Created
FROM leads
LEFT JOIN sites ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:00' AND '2011-02-15 00:00:00'
GROUP BY sites.domain_name;

-- 6. What query would you run to get a list of client names and the total # of leads we've 
-- generated for each of our clients between January 1, 2011 to December 31, 2011?

SELECT clients.first_name AS First, clients.last_name AS Last, COUNT(leads.registered_datetime) AS Number_of_Leads, DATE_FORMAT(leads.registered_datetime, '%D, %M, %Y') AS Date_Generated
FROM leads 
LEFT JOIN sites ON leads.site_id = sites.site_id 
LEFT JOIN clients ON sites.client_id = clients.client_id 
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:00' AND '2011-12-31 00:00:00' 
GROUP BY First, Last;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated 
-- for each client each month between months 1 - 6 of Year 2011?

SELECT clients.first_name AS First, clients.last_name AS Last, COUNT(leads.registered_datetime) AS Number_of_Leads, DATE_FORMAT(leads.registered_datetime, '%M') AS Month
FROM leads 
LEFT JOIN sites ON leads.site_id = sites.site_id 
LEFT JOIN clients ON sites.client_id = clients.client_id 
WHERE YEAR(leads.registered_datetime)=2011 AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6
GROUP BY sites.domain_name;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our 
-- clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second 
-- query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

SELECT clients.first_name AS First, clients.last_name AS Last, COUNT(leads.registered_datetime) AS Number_of_Leads, DATE_FORMAT(leads.registered_datetime, '%M') AS Month
FROM leads 
LEFT JOIN sites ON leads.site_id = sites.site_id 
LEFT JOIN clients ON sites.client_id = clients.client_id 
WHERE leads.registered_datetime BETWEEN '2011-01-01 00:00:00' AND '2011-12-31 00:00:00' 
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS Client, sites.domain_name AS Domain_Name, COUNT(leads.leads_id) AS Number_of_Leads, DATE_FORMAT(leads.registered_datetime, '%D %M %Y') AS Date
FROM leads
LEFT JOIN sites ON leads.site_id = sites.site_id 
LEFT JOIN clients ON sites.client_id = clients.client_id 
GROUP BY clients.client_id, sites.site_id
ORDER BY Client;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS Client, SUM(billing.amount) AS Total, DATE_FORMAT(billing.charged_datetime, '%M') AS Month, DATE_FORMAT(billing.charged_datetime, '%Y') AS Year
FROM billing 
LEFT JOIN clients ON billing.client_id = clients.client_id 
GROUP BY Client, Month
ORDER BY clients.client_id;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. 
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS Client_Name, GROUP_CONCAT(' / ', sites.domain_name) AS Sites_Owned
FROM sites 
LEFT JOIN clients ON clients.client_id = sites.client_id 
GROUP BY Client_Name;





