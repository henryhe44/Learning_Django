import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')

import django 
django.setup()

from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        fakeName = fakegen.name().split()
        fake_first_name = fakeName[0]
        fake_last_name = fakeName[1]
        fakeEmail = fakegen.email()

        # Make new entry
        user = User.objects.get_or_create(
            first_name = fake_first_name,
            last_name = fake_last_name,
            email = fakeEmail
        )[0]

if __name__ == '__main__':
    print("Populating...")
    populate(20)
    print("done!")