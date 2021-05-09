class student:
  n=0  
  age=0 
    
  def __init__(self,name,age):
    self.name=name
    self.age=age
    student.n+=1
    student.age+=age
  
  def detail():
    print(student.age,student.n)
  
  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  
  def change_name(self,name):
    self.name=name
  
  def change_age(self,age):
    self.age=age
  
  def total_student():
    print(student.n)
  
  def avg_age():
    print("average age of ",student.n,"student is " , (student.age/student.n))

  # def set_student(self,name,age):
  #   self.name=name
  #   self.age=age

a=student("ama",45)
d=student("ama",45)
c=student("ama",45)
b=student("ama",45)

student.detail()
student.avg_age()

