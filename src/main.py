from database.db_connection import execute_query

# execute_query("SELECT * FROM heroes")

def get_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query).fetchall()
    for item in returned_items:
        print(item[1])
    return returned_items

# def create_new_hero(name, about_me):
#     query = """
#         INSERT INTO heroes (name, about_me)
#         VALUES (%s, %s)
#         """
#     execute_query(query, (name, about_me))

get_heroes()

