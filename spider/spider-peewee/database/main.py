from peewee import *

db = MySQLDatabase("kf_spider", host="127.0.0.1", port=3306, user="root", password="123456")


class Person(Model):
    name = CharField(max_length=20, null=True)
    birthday = DateField()

    class Meta:
        database = db
        table_name = "users"


if __name__ == "__main__":
    db.create_tables([Person])
