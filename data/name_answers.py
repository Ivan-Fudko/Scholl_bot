import sqlalchemy
from data.db_session import SqlAlchemyBase



class Answers(SqlAlchemyBase):
    __tablename__ = 'answers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, unique=True)
    answer = sqlalchemy.Column(sqlalchemy.String, default=False, nullable=True)

