#team name-{pycharmers}
def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    """
    Create a frequency dictionary from a list of fruits.
    """
    inventory = {}
    for fruit in fruit_list:
        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1
    return inventory
