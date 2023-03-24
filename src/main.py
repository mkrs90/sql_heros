from database.db_connection import execute_query
import os


################### VIEW HERO ##########################

def get_heroes_list():
    os.system('clear')
    app_header()
    view_heroes()
    hero_number = input("Which sidekick do you want to view? ")
    get_hero(hero_number)

def get_hero(num):
    query = f"""
        SELECT
            heroes.name as sidekick,
            heroes.about_me as about,
            heroes.biography as bio,
            STRING_AGG(ability_types.name, ', ') as ability
        FROM heroes
        JOIN abilities
            ON heroes.id = abilities.hero_id
        JOIN ability_types
            ON ability_types.id = abilities.ability_type_id
        WHERE heroes.id = '{num}'
        GROUP BY sidekick, about, bio;
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"""
        name: {item[0]}
        About: {item[1]}
        Bio: {item[2]}
        Ability: {item[3]}
        """)
    view_another_hero()

def view_another_hero():
    view_another = input("Would you like to view another sidekick? y/n ")
    if view_another == "y":
        get_heroes_list()
    elif view_another == "n":
        main_menu()
    else:
        print("Please enter valid response.")

################### ADD HERO ##########################        

def get_sidekick_info():
    os.system('clear')
    app_header()
    sidekick_name = input("What's the sidekicks name? ")
    sidekick_about = input(f"What's something interesting about {sidekick_name}?")
    sidekick_bio = input(f"What's {sidekick_name}'s story?")
    add_hero(sidekick_name, sidekick_about, sidekick_bio)

def add_hero(name, about, bio):
    query = f"""
        INSERT INTO heroes (name, about_me, biography)
        VALUES ('{name}', '{about}', '{bio}')
    """
    execute_query(query)
    get_sidekick_ability(name)

def get_sidekick_ability(name):
    view_abilities()    
    query = f""" 
        SELECT id
        FROM heroes
        WHERE name = '{name}';
    """
    hero_num = execute_query(query).fetchone()
    abil = input(f"What's {name}'s ability? #")
    add_hero_ability(abil, hero_num[0])

def add_hero_ability(ability, num):
    query = f"""
        INSERT INTO abilities (hero_id, ability_type_id)
        VALUES ({int(num)}, {int(ability)});
    """
    execute_query(query)
    get_heroes_list()
    
################### UPDATE HERO ##########################

def pick_hero_to_update():
    os.system('clear')
    app_header()
    view_heroes()
    hero_to_update = input("Which sidekick would you like to update? #")
    items_to_update()
    what_to_update = input("What would you like to update? #")
    if what_to_update == '1':
        new_name = input("Enter new name: ")
        update_hero('heroes', 'name', new_name, hero_to_update, 'id')
    elif what_to_update == '2':
        new_about = input("Enter new about: ")
        update_hero('heroes', 'about_me', new_about, hero_to_update, 'id')
    elif what_to_update == '3':
        new_bio = input("Enter new bio: ")
        update_hero('heroes', 'biography', new_bio, hero_to_update, 'id')
    elif what_to_update == '4':
        view_abilities()
        new_ability = input("Enter new ability #")
        update_hero('abilities', 'ability_type_id', new_ability, hero_to_update, 'hero_id')
    elif what_to_update == '5':
        main_menu()
    else:
        print("Please enter valid number")
        


def update_hero(table, column, value, conditional, where):
    query = f""" 
        UPDATE {table}
        SET {column} = '{value}'
        WHERE {where} = {conditional};
    """
    execute_query(query)
    pick_hero_to_update()


def items_to_update():
    print("""
    1. Name
    2. About Me
    3. Biography
    4. Ability
    5. Return to Main Menu
    """)


################### DELETE HERO ##########################
def delete_hero():
    os.system('clear')
    app_header()
    view_heroes()
    hero_to_delete = input("Which sidekick would you like to delete? #")
    query = f"""
        DELETE FROM heroes
        WHERE id = {hero_to_delete};
    """    
    execute_query(query)
    print("""
    )      )   (        )          (     
 ( /(   ( /(   )\ )  ( /(   (      )\ )  
 )\())  )\()) (()/(  )\())  )\    (()/(  
((_)\  ((_)\   /(_))((_)\((((_)(   /(_)) 
  ((_)  _((_) (_))   _((_))\ _ )\ (_))   
 / _ \ | || | / __| | \| |(_)_\(_)| _ \  
| (_) || __ | \__ \ | .` | / _ \  |  _/  
 \___/ |_||_| |___/ |_|\_|/_/ \_\ |_|    
      Sidekick has been deleted.
    """)
    return_to_menu = input("Would you like to return to the main menu? y/n ")
    if return_to_menu == 'y':
        main_menu()
    elif return_to_menu == 'n':
        view_heroes()
    else:
        print("Please start over...")
        main_menu()

################### CREATE ABILITY ##########################

def input_ability():
    os.system('clear')
    app_header()
    view_abilities()
    new_ability = input("What ability would you like to add? ")
    sure = input(f"Are you sure you want to add {new_ability} to the list of abilities? y/n")
    if sure == 'y':
        add_ability(new_ability)
    else:
        main_menu()


def add_ability(value):
    query = f"""
        INSERT INTO ability_types (name)
        VALUES ('{value}');
    """
    execute_query(query)
    print("Ability has been added.")
    main_menu()

################### GENERAL ##########################

def view_heroes():
    query = """
        SELECT *
        FROM heroes
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"{item[0]}.  {item[1]}")

def view_abilities():
    query = f"""
        SELECT *
        FROM ability_types
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"{item[0]}.  {item[1]}")

def main_menu():
    os.system('clear')
    app_header()
    print("""
        What would you like to do?
        1. View a sidekick
        2. Add a sidekick
        3. Update sidekick info
        4. Delete a sidekick
        5. Add an ability
        6. View an ability
    """)
    menu_answer = input("Enter number: ")
    if menu_answer == "1":
        get_heroes_list()
    elif menu_answer == "2":
        get_sidekick_info()
    elif menu_answer == "3":
        pick_hero_to_update()
    elif menu_answer == "4":
        delete_hero()
    elif menu_answer == "5":
        input_ability()
    elif menu_answer == "6":
        view_abilities()
    else:
        print("Please enter valid number")

def app_header():
    print("""
 ______     __     _____     ______     __  __     __     ______     __  __     ______    
/\  ___\   /\ \   /\  __-.  /\  ___\   /\ \/ /    /\ \   /\  ___\   /\ \/ /    /\  ___\   
\ \___  \  \ \ \  \ \ \/\ \ \ \  __\   \ \  _"-.  \ \ \  \ \ \____  \ \  _"-.  \ \___  \  
 \/\_____\  \ \_\  \ \____-  \ \_____\  \ \_\ \_\  \ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_____/   \/_/   \/____/   \/_____/   \/_/\/_/   \/_/   \/_____/   \/_/\/_/   \/_____/          
  
            When they're not out fighting crime, they are probably online.
    """)

def start_it():
    os.system('clear')
    app_header()
    start = input("Press enter to get started!")
    if start == "":
        main_menu() 

start_it()



