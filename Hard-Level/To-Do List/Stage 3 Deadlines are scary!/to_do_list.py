from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
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
    user_input = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n")
    if user_input == "0":
        print("Bye!")
        break
    if user_input == "1":
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        print(f"Today {today.day} {today.strftime('%b')}:")
        if rows:
            [print(f"{num + 1}. {row}") for num, row in enumerate(rows)]
        else:
            print("Nothing to do")
    if user_input == "2":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        today = datetime.today()
        for _ in range(7):
            rows = session.query(Table).filter(Table.deadline == today.date()).all()
            print(f"\n{days[today.weekday()]} {today.day} {today.strftime('%b')}:")
            if rows:
                [print(f"{num + 1}. {row}") for num, row in enumerate(rows)]
                print()
            else:
                print("Nothing to do")
            today += timedelta(days=1)
    if user_input == "3":
        rows = session.query(Table).order_by(Table.deadline).all()
        print("All tasks:")
        if rows:
            [print(f"{num + 1}. {row}. {row.deadline.day} {row.deadline.strftime('%b')}") for num, row in enumerate(rows)]
        else:
            print("Nothing to do")
    if user_input == "4":
        user_task = input("Enter task\n")
        task_deadline = datetime.strptime(input("Enter a deadline\n"), '%Y-%m-%d')
        new_row = Table(task=user_task, deadline=task_deadline)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
