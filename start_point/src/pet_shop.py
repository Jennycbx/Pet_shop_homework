# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(store):
    return store["name"]


def get_total_cash(store):
    return store["admin"]["total_cash"]


def add_or_remove_cash(store, cash):
    store["admin"]["total_cash"] = store["admin"]["total_cash"] + cash


def get_pets_sold(store):
    return store["admin"]["pets_sold"]


def increase_pets_sold(store, sold):
    store["admin"]["pets_sold"] += sold


def get_stock_count(store):
    return len(store["pets"])


def get_pets_by_breed(store, breed):
    dogs = []
    for dog in store["pets"]:
        if dog["breed"] == breed:
            dogs.append(1)
    return dogs

    



    