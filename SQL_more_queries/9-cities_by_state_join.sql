-- Lists all cities with their corresponding state names
SELECT 
    cities.id, 
    cities.name AS CityName, 
    states.name AS StateName
FROM 
    cities
JOIN 
    states ON cities.state_id = states.id
ORDER BY 
    cities.id;
