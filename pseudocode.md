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

1. Function first gives you a list of sidekicks.
2. User selects sidekick they want to view.
3. Information is given on the sidekick
    - Name, about, bio, ability, and relationships
4. User clicks enter to return to "home menu"

The following code will return sidekick name and their ability.

'''
    def get_sidekicks_abilities():
        query = """
            SELECT 
                heroes.name as sidekick,
                ability_types.name as ability
            FROM heroes
            JOIN abilities
                ON heroes.id = abilities.hero_id
            JOIN ability_types
                ON ability_types.id = abilities.ability_type_id;
        """
        returned_items = execute_query(query).fetchall()
        for item in returned_items:
            print(item[1])
        return returned_items
'''

(also add about_me, abilities, and relationships)

## Learn about hero

User selects from list. User input = 2

SELECT * FROM HEROES

heroes are listed by number

user inputs number associated with hero

Hero information - about_me, abilities, and relationships is shown

def select_hero():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(item[1])
    return returned_items

def learn_about_hero(hero):
    query = """

    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(item[1])
    return returned_items

## Update Hero

User select from menu list. User selects 3.

Q: What hero would you like to update?
Q: What would you like to update?
    - Name
    - Ability
    - About
    - Relationship

def update_hero():
    query = """

    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(item[1])
    return returned_items

## Delete a hero

User selects from menu list. User selects 4.

Q: Which here would you like to delete?

User selects hero

def delete_hero():
    query = """

    """
    returned_items = execute_query(query).fetchall()
    for item in returned_item:
        print(item[1])
    return returned_items

## Add hero

## Add ability




--------------------------

Adding new hero

INSERT INTO heroes (param1, param2)
VALUES (input1, input2)

user will need to supply the inputs and the def will need to take them as params?

To input values with python:

hero_name = input("Who is the hero?")
to test it print("Hero name: " + hero_name)

hero_about = input("Tell me about " + hero_name + "?")
to test it print("Hero about: " + hero_about)


so VALUES will be:
VALUES(hero_name, hero_about)


to get these values you must first have user select that they want to add a hero from a
menu list. This must be displayed first. upon selection of adding a character user will be prompted with inputs. Once they hit enter the above code will run thus updating the heroes table. 

