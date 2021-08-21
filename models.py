# importing db for access to actual peewee database and db_wrapper to access Model

from enum import unique
from flask_login.mixins import UserMixin
from app import db_wrapper, db, app
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from peewee import (
    BlobField,
    CharField,
    Check,
    DecimalField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    DateTimeField,
)


class BaseModel(db_wrapper.Model):
    class Meta:
        database = db


class User(BaseModel, UserMixin):
    first_name = CharField(index=True, max_length=30, null=True, default="")
    last_name = CharField(max_length=120, null=True, default="")
    address = CharField(max_length=200, null=True, default="")
    city = CharField(max_length=50, null=True, default="")
    country = CharField(max_length=50, null=True)
    cc_number = IntegerField(null=True, default="")
    username = CharField(index=True, max_length=30, unique=True)
    email = CharField(index=True, max_length=50, unique=True)
    password = CharField(max_length=20)
    profile_pic = CharField(null=True, default="default_user.jpg")

    def get_reset_token(self, expires_seconds=900):
        s = Serializer(app.secret_key, expires_seconds)
        token = s.dumps({"user_id": self.id}).decode("utf-8")
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.secret_key)
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.get(user_id)


class Product(BaseModel):
    name = CharField(max_length=50)
    description = TextField(null=True)
    price_per_unit = DecimalField(
        constraints=[Check("price_per_unit >= 0")],
        decimal_places=2,
        max_digits=10,
        auto_round=True,
    )
    stock = IntegerField(default=1)
    owner = ForeignKeyField(User, backref="products")
    product_pic = CharField(null=True, default="default_product.jpg")
    date_posted = DateTimeField(formats="%Y-%m-%d %H:%M", default=datetime.now())


Product.add_index(Product.name, Product.description)


class Tag(BaseModel):
    name = CharField(unique=True, max_length=30)


class ProductTag(BaseModel):
    product = ForeignKeyField(Product, index=True, backref="tags")
    tag = ForeignKeyField(Tag, index=True, backref="products")


class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref="transactions", index=True)
    product_bought = ForeignKeyField(Product, index=True)
    amount_bought = IntegerField()
    transaction_date = DateTimeField(
        formats="%Y-%m-%d %H:%M", default=datetime.utcnow()
    )


# db.connect()
# db.create_tables([User, Product, Tag, ProductTags, Transaction])
