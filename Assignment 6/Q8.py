

def findTriplets(arr, n):
  
    found = False
    for i in range(0, 1):
      
        for j in range(i+1, 2):
          
            for k in range(j+1, 3):
              
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    if (found == False):
        print(" NONE ")
  

arr = [-25, -10, -7, -3, 2, 4, 8, 10]

findTriplets(arr, n)