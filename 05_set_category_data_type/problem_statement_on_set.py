# Questions:
# ------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Find the Names of those Learners who are learning all the Courses in an organization
# 2. Find the Names of those Learners who are learning Both 'Python' and 'Java'.
# 3. Find the Names of those Learners who are learning Only 'Python' But Not 'Java'
# 4. Find the Names of those Learners who are learning Only 'Java' But Not 'Python'
# 5. Find the Names of those Learners who are learning  Exclusively 'Python'  and  'Java'
# ---------------------------------------------------------------------------------------------------------------
# Set of Python Learners={"Rossum","Travis","Dennis"}
# Set of Java Learners={"Gosling","James","Dennis"}
from statistics import pvariance

#Question 1.
pylrnr= {"Rossum","Travis","Dennis"}
jvlrnr= {"Gosling","James","Dennis"}
un= pylrnr.union(jvlrnr)
print(un)

#Question 2.
pylrnr= {"Rossum","Travis","Dennis"}
jvlrnr= {"Gosling","James","Dennis"}
un1 = pylrnr.intersection(jvlrnr)
print(un1)

#Question 3.
pylrnr= {"Rossum","Travis","Dennis"}
jvlrnr= {"Gosling","James","Dennis"}
un2= pylrnr.difference(jvlrnr)
print(un2)

#Question 4.
pylrnr= {"Rossum","Travis","Dennis"}
jvlrnr= {"Gosling","James","Dennis"}
un3=jvlrnr.difference(pylrnr)
print(un3)

#Question 5.
pylrnr= {"Rossum","Travis","Dennis"}
jvlrnr= {"Gosling","James","Dennis"}
un4= pylrnr.symmetric_difference(jvlrnr)
print(un4)