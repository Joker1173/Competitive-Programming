
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr1=[]
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr1.append("FizzBuzz")
            elif i %3 == 0:
                arr1.append("Fizz")
            elif i %5 == 0:
                arr1.append("Buzz")
            else:
                arr1.append(str(i))
            i += 1
        return arr1

        
       
