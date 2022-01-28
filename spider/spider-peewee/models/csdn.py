from peewee import *

db = MySQLDatabase("kf_spider", host="127.0.0.1", port=3306, user="root", password="123456")


class BaseModel(Model):
    class Meta:
        database = db


"""
1. char类型，设置最大长度，无法确定使用text
2. 采集到数据先格式化处理
3. default & null = True时可以不设置（默认为True）
"""


class Topic(BaseModel):
    title = CharField()
    content = TextField()
    id = IntegerField(primary_key=True)
    author = CharField()
    create_time = DateTimeField()
    answer_nums = IntegerField(default=0)
    click_nums = IntegerField(default=0)
    parised_nums = IntegerField(default=0)
    jtl = FloatField(default=0.0)
    score = IntegerField(default=0)
    status = CharField()


class Answer(BaseModel):
    topic_id = IntegerField()
    author = CharField()
    content = TextField(default="")
    create_time = DateTimeField()
    parised_nums = IntegerField(default=0)  # 点赞数


class Author(BaseModel):
    name = CharField()
    id = CharField(primary_key=True)
    click_nums = IntegerField(default=0)
    original_nums = IntegerField(default=0)  # 原创数
    forward_nums = IntegerField(default=0)
    rate = IntegerField(default=-1)
    answer_nums = IntegerField(default=0)  # 评论数
    parised_nums = IntegerField(default=0)  # 点赞数
    desc = TextField(null=True)
    industry = CharField(null=True)
    location = CharField(null=True)
    follower_nums = IntegerField(default=0)  # 粉丝数
    following_nums = IntegerField(default=0)  # 关注数


if __name__ == "__main__":
    db.create_tables([Topic, Answer, Author])
