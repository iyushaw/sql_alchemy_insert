from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ssasa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    geo = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    city = db.relationship("City", backref='country', lazy=True, uselist=False)

    def __repr__(self):
        return f'Country Name: {self.id}, {self.name}, {self.geo}, {self.population}'


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mayor = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.mayor}'

# This is the error I get when I try to test the data entry

# sqlalchemy_table]$ python
# Python 3.9.5 (default, May 24 2021, 12:50:35) 
# [GCC 11.1.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from app import db, City, Country
# >>> db.create_all()
# >>> country = Country(name='ismail',geo='west africa', population = 32)
# >>> city = City(name='Accra', mayor='John Smith')
# >>> db.session.add(country)
# >>> db.session.add(city)
# >>> db.session.commit()
# Traceback (most recent call last):
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
#     self.dialect.do_execute(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
#     cursor.execute(statement, parameters)
# sqlite3.IntegrityError: NOT NULL constraint failed: city.country_id

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 2, in commit
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1428, in commit
#     self._transaction.commit(_to_root=self.future)
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 829, in commit
#     self._prepare_impl()
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 808, in _prepare_impl
#     self.session.flush()
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 3298, in flush
#     self._flush(objects)
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 3438, in _flush
#     transaction.rollback(_capture_exception=True)
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 70, in __exit__
#     compat.raise_(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
#     raise exception
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 3398, in _flush
#     flush_context.execute()
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/unitofwork.py", line 456, in execute
#     rec.execute(self)
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/unitofwork.py", line 630, in execute
#     util.preloaded.orm_persistence.save_obj(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/persistence.py", line 242, in save_obj
#     _emit_insert_statements(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/orm/persistence.py", line 1219, in _emit_insert_statements
#     result = connection._execute_20(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
#     return meth(self, args_10style, kwargs_10style, execution_options)
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 323, in _execute_on_connection
#     return connection._execute_clauseelement(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
#     ret = self._execute_context(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
#     self._handle_dbapi_exception(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1994, in _handle_dbapi_exception
#     util.raise_(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
#     raise exception
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
#     self.dialect.do_execute(
#   File "/home/pipi/Desktop/sqlalchemy_table/venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
#     cursor.execute(statement, parameters)
# sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: city.country_id
# [SQL: INSERT INTO city (name, mayor, country_id) VALUES (?, ?, ?)]
# [parameters: ('Accra', 'John Smith', None)]
# (Background on this error at: http://sqlalche.me/e/14/gkpj)

if __name__ == "__main__":
    app.run(debug=True)