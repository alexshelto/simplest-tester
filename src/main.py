
from test import Test
import sys





if __name__ == '__main__':
  if(len(sys.argv) < 2):
    print("Failed to pass build.txt & verify.txt to program")
    exit(1)

  tester = Test()          #creating Test object
  tester.build(str(sys.argv[1]))



  print("finished")
