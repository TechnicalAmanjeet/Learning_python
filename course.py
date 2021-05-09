class course:
  n=0 #n=no. of subject in this course
  
  def __init__(self,name):
    self.name=name
    course.n+=1
  
  def get_name(self):
    print(self.name)
    
c=course("eee")
c.get_name()