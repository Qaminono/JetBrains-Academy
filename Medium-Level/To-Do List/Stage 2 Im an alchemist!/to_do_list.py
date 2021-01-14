from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class ToDo(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Noting to do!')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

while True:
    user_input = input("1) Today's tasks\n2) Add task\n0) Exit\n")
    if user_input == "0":
        print("Bye!")
        break
    if user_input == "1":
        rows = session.query(ToDo).all()
        print("Today:")
        if rows:
            [print(row) for row in rows]
        else:
            print("Nothing to do")
    if user_input == "2":
        user_task = input("Enter task\n")
        new_row = ToDo(task=user_task)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
