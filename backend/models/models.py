from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, Integer, ForeignKey, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()


class Role(Base):
    __tablename__ = 'Roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    permission = Column(JSON)


class User(Base):
    __tablename__ = 'User'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    role_id = Column(ForeignKey(Role.id))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False, unique=True)


class Brand(Base):
    __tablename__ = 'Brand'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String, nullable=False, unique=True)


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(ForeignKey(Category.id))
    brand_id = Column(ForeignKey(Brand.id))
    cost = Column(Integer, nullable=False)


class Basket(Base):
    __tablename__ = 'Basket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)


class FollowProducts(Base):
    __tablename__ = 'FollowProducts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)


class PurchaseHistory(Base):
    __tablename__ = 'PurchaseHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)
    sold_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
