'''
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''



def is_triangle(a, b, c):
    if(a != 0 and b != 0 and c != 0):
        arm = [a,b,c]
        arm.sort()
        
        if(arm[0]+arm[1]>arm[2]):
            return True
        else:
            return False 
    else:
        return False
    
