cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    for key, value in cars.items():
        if key == "Jeep":
            print(value)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    car_list = []
    for key, value in cars.items():
        car_list.append(value[0])
    pass


def get_all_matching_models(cars=cars, grep='Trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    car_list = []
    for key, value in cars.items():
        for item in value:
            if grep in item:
                car_list.append(item)
    car_list.sort()


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return sorted(cars.values())


