from flask import current_app
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import validates
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime
# the db instance and mixins can be provided to any blueprint
from apps.shared.models import db, AppMixin

# auto-generated index names use the ix_table_column naming convention

# Example model

# class Example(db.Model, AppMixin):
#     """ An example model """
#     examplefield = db.Column(
#         db.String(),
#         nullable=False,
#         unique=True,
#         index=True)

#     def __init__(self, examplefield):
#         self.examplefield = examplefield
