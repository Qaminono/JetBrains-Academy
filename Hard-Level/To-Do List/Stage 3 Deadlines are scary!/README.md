#  Description

Everyday, we’re surrounded by thousands of small distractions, facts, and bits of odd information. When you’re on a deadline, you don’t have time for all this fluff. You need to focus on the task at hand, so you can’t afford to spend hours on Pinterest, chatting at the water cooler with your coworkers, or watching re-runs on TV. At this point in time, the deadline takes precedence.

So let's add the ability to set deadlines to our tasks. Python datetime module will help us to work with dates.

Here are some methods that might help you:

```python
from datetime import datetime, timedelta

datetime.today() # return current date and time.
datetime.today().date() # current date without time
datetime.today().time() # current time without date

datetime.strptime(date_string, format) # return a datetime corresponding to date_string, parsed according to format.
# Format example: '%Y-%m-%d' - '2020-04-24'

today = datetime.today()
today.day # the day of a current month.
today.strftime('%b') # the short name of the current month. I.e 'Apr'
today.weekday() # return the day of the week as an integer, where Monday is 0 and Sunday is 6.

yesterday = today - timedelta(days=1) # a timedelta object represents a duration, the difference between two dates or times.
day_after_tomorrow = today + timedelta(days=2)
```

To select rows from the table with some condition, you can use filter() method that accepts the condition by which to select rows:

```python
from datetime import datetime

today = datetime.today()
rows = session.query(Table).filter(Table.date == today.date()).all()
```

In the code snippet above, we selected all rows from Table where the date column equals today's date.

To sort selected data, you can use order_by() that accepts a column by which you need to sort data:

```python
# select all rows ordered by the date column
session.query(Table).order_by(Table.date).all()

# select all rows where string_fields starts with 'L'. The result is ordered by date column
session.query(Table).filter(Table.string_field.startswith('L'))).order_by(Table.date).all()
```

#  Objectives

Add the following items to your menu:

-    Week's tasks: prints all tasks for 7 days from today.
-    All tasks: prints all tasks sorted by deadline.

Now Add task item should ask for the deadline of the task. Users should input the deadline in this format: YYYY-MM-DD.

Also, Today's tasks item should print today's date.

See the format of the output in the example.
#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    Output:
    
    1) Today's tasks
    2) Week's tasks
    3) All tasks
    4) Add task
    0) Exit
    > 1
    
    Today 26 Apr:
    Nothing to do!
    
    1) Today's tasks
    2) Week's tasks
    3) All tasks
    4) Add task
    0) Exit
    > 4
    
    Enter task
    >Meet my friends
    Enter deadline
    >2020-04-28
    The task has been added!
    
    1) Today's tasks
    2) Week's tasks
    3) All tasks
    4) Add task
    0) Exit
    > 2
    
    Sunday 26 Apr:
    Nothing to do!
    
    Monday 27 Apr:
    Nothing to do!
    
    Tuesday 28 Apr:
    1. Meet my friends
    
    Wednesday 29 Apr:
    Nothing to do!
    
    Thursday 30 Apr:
    1. Math homework
    2. Call my mom
    
    Friday 1 May:
    1. Order a new keyboard 
    
    Saturday 2 May:
    Nothing to do!
    >3
    
    All tasks:
    1. Meet my friends. 28 Apr
    2. Math homework. 30 Apr
    3. Call my mom. 30 Apr
    4. Order a new keyboard. 1 May
    
    1) Today's tasks
    2) Week's tasks
    3) All tasks
    4) Add task
    0) Exit
    > 0
    
    Bye!