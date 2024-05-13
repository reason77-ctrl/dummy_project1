def format_data_for_display(data):
    formatted_data = []
    for person in data:
        formatted_person = "{} {}: {}".format(
            person["given_name"], person["family_name"], person["title"]
        )
        formatted_data.append(formatted_person)
    return formatted_data