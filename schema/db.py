from schema.models import db

# getall values
def getAll(model):
  data = model.query.all()
  return data

def add_instance(model ,**kwargs):
  instance = model(**kwargs)
  db.session.add(instance)
  commit_changes()

# delete instance
def delete_instance(model,id):
  model.query.filter_by(id =id).delete()
  commit_changes

# edit instance
def edit_instance(model, id,**kwargs):
  instance = model.query.filter_by(id =id).all()[0]
  for attr, new_value in kwargs:
    setattr(instance,attr,new_value)
    commit_changes

def commit_changes():
  db.session.commit()

