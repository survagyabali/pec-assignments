#Taking side inputs
Side_1=float(input('Side 1:'))
Side_2=float(input('Side 2:'))
Side_3=float(input('Side 3:'))
#Conditions in which Triangles cannot exist
bool_1= Side_1+Side_2<Side_3
bool_2= Side_1+Side_3<Side_2
bool_3= Side_2+Side_3<Side_1


match bool_1,bool_2,bool_3:
    case True,False,False:
        print('NO')
    case False,True,False:
        print('NO')
    case False,False,True:
        print('NO')
    case False,False,False:
        print('YES')
