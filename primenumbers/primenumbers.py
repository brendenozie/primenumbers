import unittest

def primeNumberFunction(x): 
    return x

print(primeNumberFunction(5))

class MyTestCases(unittest.TestCase):
    def testOne(self):
        self.assertEqual(primeNumberFunction("A"), "The function only expects a number")
    def testTwo(self):
        self.assertEqual(primeNumberFunction(20), [1,2,3,5,7,11,13,17])
    

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
