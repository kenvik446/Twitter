from pytwitter import Api
from cryptography.x509 import load_pem_x509_certificate
import pandas as pd
import sqlalchemy as db
Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAExweQEAAAAAcHYwAIXpI8VrhLNpc6ELBT"
Bearer_Token += "%2BOUX0%3DjMNh7b7NgR4e6FPB7LK03O3qHiqeSZ2jtDaylQXvizysxYtnzr"
api=Api(bearer_token=BA)
# Getting user ID By username
name= input("Enter username: ")
s=(api.get_user(username=name))
# to get just id
ID=(s.data.id)


# This should return a dictionary of the following
# The parameters should all be of type list([])
def get_dict(ids, names, usernames):
    dict = {
        'ids': ids,
        'names': names,
        'usernames': usernames
        }
    return dict


# This should return a dictionary by calling the get_dict
# The id must be a of type string and max_users should be of type int
def get_users_followers(id, max_users):
    response = api.get_followers(user_id=id, max_results=max_users)
    ids = []
    names = []
    usernames = []

    for data in response.data:
        ids.append(data.id)
        names.append(data.name)
        usernames.append(data.username)

    return get_dict(ids, names, usernames)


# The info must be a dictionary to add to the database, d
# b_name, and table_name should be of type string
def create_database(info, db_name, table_name):

    data = pd.DataFrame.from_dict(users_followers)
    engine = db.create_engine('sqlite:///' + db_name + '.db')

    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
    query_result= engine.execute("SELECT * FROM" + table_name + ";").fetchall()
    print(pd.DataFrame(query_result), "\n")


# Getting users followers by ID
max = input("Enter number of followers you would like to see: ")
users_followers = get_users_followers(ID, int(max))
print(users_followers)
create_database(users_followers, "Twitter", "users_followers")
