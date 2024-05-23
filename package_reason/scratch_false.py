import json
import requests

"""
    Json file of all completed False Data

"""

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


user_todos = {}
for todo in todos:
    if todo["completed"]==False:
        try:
            user_todos[todo["userId"]] += 1
        except KeyError:
            user_todos[todo["userId"]] = 1

top_users = sorted(user_todos.items(), 
                   key=lambda x: x[1], reverse=True)


max_not_completed = top_users[0][1]


users = []
for user, num_not_completed in top_users:
    if num_not_completed <= max_not_completed:
        users.append(str(user))



def keep(todo):
    is_complete_false = todo["completed"] == False
    has_count = str(todo["userId"]) in users
    return is_complete_false and has_count

with open("filtered_data_file_false.json", "w") as data_file:
    filtered_todos = list(filter(keep,todos))
    json.dump(filtered_todos,data_file,indent=2)