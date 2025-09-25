from faker import Faker

faker = Faker()

def fake_user():
    return {
            "name": faker.name(),
            "email": faker.email(),
            "address": faker.address()
            }
