import faker


def generate_date():

    day_1 = '2024-09-30'
    day_2 = '2024-09-29'
    return day_1, day_2

def get_user_data():
    fake = faker.Faker("ru_RU")
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_name()
    phone = fake.msisdn()
    return first_name, last_name, address, phone






