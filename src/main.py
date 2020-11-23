
from test import Test
import sys





if __name__ == '__main__':
  if(len(sys.argv) < 2):
    print("Failed to pass build.txt & verify.txt to program")
    exit(1)

  build_file = sys.argv[1]
  verify_file = sys.argv[2]

  # 
  # run tests on file before proceding to build and verify
  #

  tester = Test(build_file, verify_file)                 #creating Test object
  tester.build()  #building with input file build
  tester.verify()



  print("finished")
