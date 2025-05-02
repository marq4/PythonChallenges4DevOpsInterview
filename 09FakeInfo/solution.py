
import pandas
from faker import Faker

TARGET = 3

fake = Faker()

data_frame = pandas.DataFrame({
    'Date': [fake.date() for d in range(TARGET)],
    'Name': [fake.name() for n in range(TARGET)],
    'Email': [fake.email() for e in range(TARGET)]
})

print(data_frame)

