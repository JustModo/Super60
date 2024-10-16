from training import Training
from trainer import Trainer
from trainee import Trainee
from organization import Organization
from course import Course
from module import Module
from unit import Unit
from topic import Topic

org1 = Organization("TSC")
print(org1.get_name())


tr1 = Trainer("Bob", org1)

s1 = Trainee("Yash")
s2 = Trainee("Alice")
s3 = Trainee("Tom")

tr1.add_trainee(s1, s2, s3)

training = Training("Main Training")

training.add_trainers(tr1)

print(training.get_trainees())

t1 = Topic("Topic 1")
t2 = Topic("Topic 2")
t3 = Topic("Topic 3")

t4 = Topic("Topic 4")
t5 = Topic("Topic 5")

u1 = Unit("Unit 1", 5, t1, t2, t3)
u2 = Unit("Unit 2", 2, t4)
u3 = Unit("Unit 3", 3, t5)

m1 = Module("Module 1", u1, u2)
m2 = Module("Module 2", u3)

c1 = Course("Course 1", m1)
c2 = Course("Course 2", m2)

training.add_courses(c1, c2)

print(training.get_training_duration_in_hrs())
