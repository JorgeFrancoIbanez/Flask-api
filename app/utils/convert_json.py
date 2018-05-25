def data_to_json(data_in):
    elements = []
    for item in data_in:
        item.timestamp = str(item.timestamp)
        item._sa_instance_state = str(item._sa_instance_state)
        elements.append(item.__dict__)
    new_dict = elements
    return new_dict
