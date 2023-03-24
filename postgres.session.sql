-- INSERT INTO abilities (hero_id, ability_type_id)
-- VALUES (19, 2);

-- SELECT *
-- FROM heroes;

-- SELECT
--     heroes.name as sidekick,
--     heroes.about_me as about,
--     heroes.biography as bio,
--     STRING_AGG(ability_types.name, ', ') as ability
-- FROM heroes
-- JOIN abilities
--     ON heroes.id = abilities.hero_id
-- JOIN ability_types
--     ON ability_types.id = abilities.ability_type_id
-- WHERE heroes.name = 'billy bob'
-- GROUP BY sidekick, about, bio;

-- INSERT INTO heroes (name, about_me, biography)
-- VALUES ('billy bob', 'Two first names and two fist, he is not afraid to show you both.', 'Billy of the bobs');


-- DELETE FROM heroes
-- WHERE id = 11;


