people= [(1,'jo',0,19,'bangalore'),(2,'kakul',0,18,'rajasthan')]
print('%d %-15s %-7s %-3d %s '%('ID','NAME','GENDER','AGE','LOCATION'))
print('-' * 40)
gender=''

for person in people:
    if person[2]==0:
        gender='male'
    else:
        gender="female"
    print('%d %-15s %-7s %-3d %s' %(person[0],person[1],gender,person[3],person[4]))
  
