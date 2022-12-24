from second_realize import get_data


def merge_data(data: dict):
    gifts = data['gifts']
    moves = data['children']
    gifts_id = (_id['id'] for _id in gifts)
    return zip(moves, gifts_id)


print(list(merge_data(get_data())))