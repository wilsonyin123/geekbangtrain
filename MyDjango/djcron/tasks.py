from MyDjango.celery import app

 
@app.task()
def get_task():
  return 'test'

@app.task()
def get_task2():
  return 'test2'
