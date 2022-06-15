Side_1=float(input('Side 1:'))
Side_2=float(input('Side 2:'))
Side_3=float(input('Side 3:'))
#Conditions in which Triangles cannot exist
bool_1= Side_1+Side_2>Side_3
bool_2= Side_1+Side_3>Side_2
bool_3= Side_2+Side_3>Side_1

if(bool_1):
  if(bool_2):
    if(bool_3):
      semi_perimeter=(Side_1+Side_2+Side_3)/2
      Area=(semi_perimeter*(semi_perimeter-Side_1)*(semi_perimeter-Side_2)*(semi_perimeter-Side_3))**0.5
      print(Area)
