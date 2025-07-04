# list of students with their grades 
students = [
    {"name": "ali" , "grades":(80, 90 , 95)},
    {" name": "essam" ,"grades":(80 , 70 , 75)},
    {" name ": "oney" , "grades":( 90 ,85, 95)}
]
# print average grades for S in stundes:
for s in students :
  total = sum(s("grades"))
  average = total / 3 
  print(s("name"), "avrage:", average)
