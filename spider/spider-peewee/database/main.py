from peewee import *

db = MySQLDatabase("kf_spider", host="127.0.0.1", port=3306, user="root", password="123456")


class Person(Model):
    name = CharField(max_length=20, null=True)
    birthday = DateField()

    class Meta:
        database = db
        table_name = "users"


def crud():
    from datetime import date
    uncle_bob = Person(name='kf', birthday=date(1994, 10, 9))
    uncle_bob.save()

    kf = Person.select().where(Person.name == 'kf').get()

    print(kf)


if __name__ == "__main__":
    # db.create_tables([Person])
    crud()
