import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)



user_todos = {}
for todo in todos:
    if todo["completed"]:
        print(todo["completed"])
        try:
            user_todos[todo["userId"]] += 1
        except KeyError:
            user_todos[todo["userId"]] = 1

# top_users = sorted(user_todos.items(), 
#                    key=lambda x: x[1], reverse=True)
# print(top_users)

# users = []
# for user in top_users:
#     users.append(str(user))
# print(users)

# def keep(todo):
#     is_complete_false = todo["completed"]
#     has_count = str(todo["userId"]) in users
#     return is_complete_false and has_count

# with open("filtered_data_file_false.json", "w") as data_file:
#     filtered_todos = list(filter(keep,todos))
#     json.dump(filtered_todos,data_file,indent=2)