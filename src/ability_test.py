from database.db_connection import execute_query

def view_abilities():
    query = f"""
        SELECT *
        FROM ability_types
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(f"{item[0]}.  {item[1]}")

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
    print(ability, num)
    # query = f"""
    #     INSERT INTO abilities (hero_id, ability_type_id)
    #     VALUES ({int(num)}, {int(ability)});
    # """
    # execute_query(query)
    # get_heroes_list()


get_sidekick_ability("billy bob")