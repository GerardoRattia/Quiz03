#Problem 1
def dot(vector01, vector02):
    """
    This function takes two vectors as its arguments. It multiplies
    each element of each vector before adding them, and returning the dot product of two 
    vectors as a scalar, If the vector are not of equal 
    length, the function will print Error and an empty list.
    """
    
    if(len(vector01) == len(vector02)): 
        #if  vectors are of equal lengths
        dotProduct = 0; 
        #initialize dot product
        for i in range(0, len(vector01)): 
            #iterate over range
            dotProduct +=(vector01[i] * vector02[i]);
            #compute the sumation product to get the dot product.
        return dotProduct;
    
    else: #lengths are not equal.
        print("ERROR: Vectors have different lengths.");
        return [];

#dot product Test
#Test#1 dot product 
vector01 = [4,2,3,4];
vector02 = [4,2,3,4];
print(dot(vector01, vector02));

#Test#2 Empty Lists
vector01 = [];
vector02 = [];
print(dot(vector01, vector02));

#Test#3 different length vectors
vector01 = [7,1,2];
vector02 = [9];
print(dot(vector01, vector02));

#Test#4 Vector and Scalar"""
#vector01 = [1,2,3];
#scalar = 45;
#print(dot(vector01, scalar));



#Problem 2 
def vectSubtract(vector01, vector02):
    """
    This function takes two vectors as its arguments, then it updates
    each of the elements inside the vector by subtracting them, returning
    a new updated vector. If the vectors are not of 
    equal length, the program will stop, and return an Error.

    """
    
    if(len(vector01) == len(vector02)): 
        #if lengths are equal
        vectSubtract = [];
        #initialize subtraction vector
        for i in range(0, len(vector01)):
            #iterate over range
            vectSubtract.append(vector01[i] - vector02[i]); 
            #compute and append vector elements to end of subtraction vector.
        return vectSubtract;
    
    else: 
        #lengths are not equal.
        print("ERROR: Vectors have different length.");
        return [];

#TEST 1 Empty Lists
vector01 = [];
vector02 = [];
print(vectSubtract(vector01,vector02));


#TEST 2 Vectors of Unequal Lengths
vector01 = [1,1,1];
vector02 = [7,2];
print(vectSubtract(vector01,vector02));
#return = ERROR: Vectors are not of equal length.


#TEST 3 Vectors of Equal Lengths
vector01 = [5,3,1];
vector02 = [8,5,3];
print(vectSubtract(vector01,vector02));



#TEST 4 Vector and a Scalar
#vector01 = [5,3,2,1];
#scalar = 5;
#print(vectSubtract(vector01,scalar));



#Problem 3
def scalarVecMulti(scalar, vector):
    """
    This function takes a vector an a scalar as it’s arguments, 
    and then it multiplies each element of the vector by
    the scalar, updating each element of the vector. 
    If else print Error
    """
    
    for i in range(0,len(vector)):
        #iterate over range [0,length-1]
        vector[i] *= scalar; 
        #scalar * vector multiplication
    return vector;

#Test 1 Scalar and Vector
scalar = 17;
vector = [5,7,1];
print(scalarVecMulti(scalar,vector));



#Test 2 Vector and Scalar <two ways with code>
#vector = [5,5,2];
#scalar = 3;
#print(scalarVecMulti(scalar,vector));
#print(scalarVecMulti(vector,scalar));


#problem 4
def infNorm(vector):
    
    """
    This function initialize Max(variable) to the absolute value of the first element
    in the vector, if the absolute value is greater than Max, assign the element to Max.
    If the vector is empty, print error and return a null space.
    """
    #Max is used as a variable in this problem NOT as a function!
    
    if(len(vector) == 0) : 
        #checks for empty vector, if there is any Print(Error: Empty Vector)
        print("ERROR: Empty Vector");
        return []; 
        
    else :
        Max = abs(vector[0]);
            #initialize our output
        
        for i in range(1,len(vector)):
            if(abs(vector[i]) > Max): 
                #iteration
                Max = abs(vector[i]);
    
        return Max 
        #finalize output
    


#TEST 1 Non-Empty Vector
vector = [-72,3,7,-19,23,20,-13,-50,1]
print(infNorm(vector));
#infNorm(vector) = 24

#TEST 2 Empty Vector
vector = [];
print(infNorm(vector));



#problem 5
def normalize(vector) :
  """
  This function takes the infinity norm and uses it to normalize a
  vector, Returning a normalize vector with respect 
  to the infinity norm.
  """
    
  if (len(vector) == 0): 
    #Empty Vector Check
    print("ERROR: Empty Vector");
    return [];
  else:
        #We have the values for the infnorm
    currentMax = infNorm(vector)
    normalizer=[]
    #Store the values in the normalizer vector
    for i in range(len(vector)):
      normalizer.append((1/currentMax)*vector[i]) 
    #remember parentheses
    return normalizer 

#Test 1 non-empty vector
vector = [5,10,15];
print(normalize(vector))


#Test 2 Empty Vector
vector = []
print(normalize(vector))
