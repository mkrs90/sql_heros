SELECT 
    heroes.name as sidekick,
    ability_types.name as ability
FROM heroes
JOIN abilities
    ON heroes.id = abilities.hero_id
JOIN ability_types
    ON ability_types.id = abilities.ability_type_id
WHERE heroes.id = 1;

