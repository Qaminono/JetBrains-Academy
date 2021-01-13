#  Description

It's very upsetting when the data about your to-do tasks disappear after the program is completed. To avoid this problem, you need to create a database where you can store all the necessary information about your tasks. We will use SQLite to create the database and SQLAlchemy to manage the database from Python.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM) that gives developers the full power and flexibility of SQL.

First, you need to create your database file. To create it, you should use the create_engine() method, where file_name is the database file name:

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///file_name?check_same_thread=False')
```

check_same_thread=False argument allows connecting to the database from another thread. It's required for the test purpose otherwise, you will get an exception.

Once you've created your database file, you need to create a table in it. First, create a model class that describes the table in the database. All model classes should inherit from the DeclarativeMeta class that is returned by declarative_base():

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field
```


All information about the table is described in its model class.

-    Table is the name of the model class. It is used to access data from the table it describes. The name of the class can be anything.
-    __tablename__ specifies the table name in the database.
-    id is an integer column of the table; primary_key=True says that this column is the primary key.
-    string_field is a string column; default='default_value' says that the default value of this column is 'default_value'.
-    date_field is a column that stores the date. SQLAlchemy automatically converts the SQL date into a Python datetime object.
-    __repr__ method returns a string representation of the class object. In the ORM concept, each row in the table is an object of a class.

After we've described our table, it's time to create it in our database. All we need is to call the create_all() method and pass engine to it:

```python
Base.metadata.create_all(engine)
```

This method creates a table in our database by generating SQL queries according to the models we described.

Now we can access the database and store data in it. To access the database, we need to create a session:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```


The session object is the only thing you need to manage the database. To create a row in our table, you need to create an object of the model class and pass it to the add() method:

```python
new_row = Table(string_field='This is string field!',
         date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()
```

To get all rows from the table, you can pass the model class to the query() method that selects all rows from the table represented by a model class:

```python
rows = session.query(Table).all()
```

The all() method returns all rows from the table as a Python list. Each element of this list is an object of the model class. You can access the row fields by their names:

```python
first_row = rows[0] # In case rows list is not empty

print(first_row.string_field) # Will print value of the string_field
print(first_row.id) # Will print the id of the row.
print(first_row) # Will print the string that was returned by __repr__ method
```
#  Objectives

Let's store the data about our tasks in the database. Here's what you need to do:

-    Create a database file. Its name should be todo.db.
-    Create a table in this database. The table name should be task.

The table task should have the following columns:

-    Integer column named id. It should be the primary key.
-    String column named task.
-    Date column named deadline. It should have the date when the task was created by default. You can use datetime.today() method.

Also, you need to implement a menu that will make your program more convenient. The menu should have the following items:

1.    Today's tasks. Prints all tasks for today.
2.    Add task. Asks for task description and saves it in the database.
3.    Exit.

#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Output:

    1) Today's tasks
    2) Add task
    0) Exit
    > 1
    
    Today:
    Nothing to do!
    
    1) Today's tasks
    2) Add task
    0) Exit
    > 2
    
    Enter task
    >Prepare presentation
    The task has been added!
    
    1) Today's tasks
    2) Add task
    0) Exit
    > 1
    
    Today:
    1. Prepare presentation
    
    1) Today's tasks
    2) Add task
    0) Exit
    > 0
    
    Bye!