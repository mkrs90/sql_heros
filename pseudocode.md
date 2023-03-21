# Requirements
To complete the assignment, you must complete the following:

1. Create a Connection to a gitpod Database using Python 3 and view the database (using the vscode extension)

2. The supplied superheroes.sql database file (attached the Google Classroom assignment) contains CREATE TABLE and INSERT statements to get you started with seeded data. (Do not modify the SQL file directly unless you want to see the database differently) Use the VSCode extension to execute the file from top to bottom to get the appropriate tables/entries created.

3. Decide/Plan/Pseudocode on a minimum of four CRUD operations you wish to implement (at least one operation for Create, Read, Update, & Delete) - document these in your README.md

4. Interactive creation, update, delete of a hero in the terminal via Python script, with commands that are available for the README.md

### Additional Requirements

- This is completely a backend project. There will be no visual elements to it in a browser but will be interactive in the terminal.
- Your repo should be public so that others can see your code and comment on it. 	
    - Remember to push to GitHub!
    - Potential employers will view your GitHub profile, so activity is crucial!




User needs to be able to create heroes
User needs to be able to delete heroes
User needs to be able to read what heroes have been created
User needs to be able to update heroes

User needs to be able to update hero relationships
User needs to be able to update relationship types

be able to add abilities
be able to delete abilities
be able to update abilities


in the terminal
Display Name - SIDEKICKS
Display subtext - When they're not fighting crime, they're online
OPTIONS:
- Display heroes
- View Hero
- Add a hero
- Delete a hero
- Update a hero
- Update relationship
- Add Ability

**CRUD** - 
**CREATE | READ | UPDATE | DELETE**

Starting point

1. See Sidekicks
    - List of Heroes
2. Learn about Sidekick
    - Pick a sidekick
        - displays info about sidekick
3. Update Sidekick info
    - Update name
    - Update about_me
    - Update relationships
    - Update abilities
4. Delete a sidekick
    - Pick a sidekick to delete
5. Add a sidekick
    - Add name, about_me, ability, relationships
6. Add an ability
    - adds row to ability table


------------------------------------------------------------------

## See Sidekicks

User selects from list. User input = 1

SELECT * from heroes

def get_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(item[1])
    return returned_items

(also add about_me, abilities, and relationships)

## Learn about hero

User selects from list. User input = 2

SELECT * FROM HEROES



