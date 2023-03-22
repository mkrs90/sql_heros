from database.db_connection import execute_query



def get_heroes_list():
    query = """
        SELECT *
        FROM heroes
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"{item[0]}.  {item[1]}")
    hero_number = input("Which hero do you want to view? ")
    get_hero(hero_number)

def get_hero(num):
    query = f"""
        SELECT
            heroes.name as sidekick,
            heroes.about_me as about,
            heroes.biography as bio,
            ability_types.name as ability
        FROM heroes
        JOIN abilities
            ON heroes.id = abilities.hero_id
        JOIN ability_types
            ON ability_types.id = abilities.ability_type_id
        WHERE heroes.id = {num};
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"""
        name: {item[0]}
        About: {item[1]}
        Bio: {item[2]}
        Ability: {item[3]}
        """)
    return returned_items

def main_menu():
    app_header()
    print("""
        What would you like to do?
        1. View a sidekick
        2. Add a sidekick
        3. Update sidekick info
        4. Delete a sidekick
        5. Add an ability
    """)
    menu_answer = input("Enter number: ")
    if menu_answer == "1":
        get_heroes_list()
    elif menu_answer == "2":
        add_sidekick()
    elif menu_answer == "3":
        update_sidekick_menu()
    elif menu_answer == "4":
        delete_sidekick()
    elif menu_answer == "5":
        add_ability()
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
    app_header()
    start = input("Press enter to get started!")
    if start == "":
        main_menu() 



# def create_new_hero(name, about_me):
#     query = """
#         INSERT INTO heroes (name, about_me)
#         VALUES (%s, %s)
#         """
#     execute_query(query, (name, about_me))

start_it()



