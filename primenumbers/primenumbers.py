import unittest

def primeNumberFunction(input_value):
    while True:
        try:
            primeNumber=[]
            for i in range(input_value+1):
                li=[]
                if i>1:
                    for num in range(1,input_value):
                        if i%num==0:
                            li.append(num)
                            if len(li)==2:
                                if li[1]==i:
                                    primeNumber.append(i)
                                else:
                                    pass
            return primeNumber
        except (TypeError):
            return "The function only expects a number"
        except (AssertionError):
            return "The function only expects a number"
        except (AttributeError):
            return "The function only expects a number" 

class MyTestCases(unittest.TestCase):
    def testOne(self):
        result=primeNumberFunction(10)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5,7] ,msg="The function only expects a number")
    def testTwo(self):
        result=primeNumberFunction(20)
        print("prime numbers include", result)
        self.assertEqual(result, [2,3,5,7,11,13,17,19],msg="The function only expects a number")
    def testThree(self):
        result=primeNumberFunction(100)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] ,msg="The function only expects a number")
    def testFour(self):
        result=primeNumberFunction(4)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3] ,msg="Not a prime number")
    def testFive(self):
        result=primeNumberFunction(3)
        self.assertEqual(result, [2],msg="The function only expects a number")
    def testSix(self):
        result=primeNumberFunction(7)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5],msg="The function only expects a number")
    def testSeven(self):
        result= primeNumberFunction(5)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3],msg="The function only expects a number")
    def testEight(self):
        result=primeNumberFunction(9)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5,7] ,msg="The function only expects a number")
    def testNine(self):
        result=primeNumberFunction(25)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5,7,11,13,17,19,23], msg="The function only expects a number")
    def testTen(self):
        result=primeNumberFunction(13)
        print("prime numbers include", result)
        self.assertEqual(result,[2,3,5,7,11],msg="The function only expects a number")

if __name__ == '__main__':
    unittest.main()

      

    
  
    
  
    
                
      
    
                
              
                
              
            
            
          
        
      
     
    
    
    

