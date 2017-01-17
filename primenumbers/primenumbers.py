import unittest

def primeNumberFunction(x): 
    return x

print(primeNumberFunction(5))

class MyTestCases(unittest.TestCase):
    def testOne(self):
        self.assertEqual(primeNumberFunction("A"), "The function only expects a number")
    def testTwo(self):
        self.assertEqual(primeNumberFunction(20), [1,2,3,5,7,11,13,17])
    def testThree(self):
        self.assertEqual(primeNumberFunction(-5), "There are no negative pime numbers")
    def testFour(self):
        self.assertEqual(primeNumberFunction(0), "Not a prime number")
    def testFive(self):
        self.assertEqual(primeNumberFunction(1), 1)
    def testSix(self):
        self.assertEqual(primeNumberFunction([1,2,3]), "Not a number")
    def testSeven(self):
        self.assertEqual(primeNumberFunction(5), [1,2,3,5])
    def testEight(self):
        self.assertEqual(primeNumberFunction(1.3), "Only accept integers")
    def testNine(self):
        self.assertEqual(primeNumberFunction(0.7), "Only accept integers")
    def testTen(self):
        stuff = {'string': 'name', 'int': 25}
        self.assertEqual(primeNumberFunction(stuff), "Only accept integers")

if __name__ == '__main__':
    unittest.main()

      
def primeNumberFunction(input_value):
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
    raise ValueError('')
  except (AttributeError):
    raise ValueError('The provided input is not a dictionary')
  except (AttributeError):
    raise ValueError('The provided input is not a dictionary')
    
l=primeNumberFunction(1.3)
print l
