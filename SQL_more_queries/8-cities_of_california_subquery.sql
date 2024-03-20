-- Sélectionner toutes les villes de Californie en utilisant une sous-requête
SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;