-- Lists all cities along with their corresponding state names
SELECT 
    cities.id, 
    cities.name AS city_name, 
    states.name AS state_name
FROM 
    cities
INNER JOIN 
    states ON cities.state_id = states.id
ORDER BY 
    cities.id ASC;
