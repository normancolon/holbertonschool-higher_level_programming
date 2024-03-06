-- Lists all cities in California from the database
SELECT 
    id, 
    name 
FROM 
    cities 
WHERE 
    state_id = (
        -- Retrieves the ID for the state named 'California'
        SELECT id FROM states WHERE name = 'California'
    );
