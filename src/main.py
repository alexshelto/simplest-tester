
from test import Test
#from utils import VerifyParse
import sys





if __name__ == '__main__':
  if(len(sys.argv) < 3):
    print("Failed to pass build.txt & verify.txt to program")
    exit(1)

  build_file = sys.argv[1]
  verify_file = sys.argv[2]

  print(build_file)
  print(verify_file)

  # 
  # run tests on file before proceding to build and verify
  #

  tester = Test(build_file, verify_file)                 #creating Test object
  # tester.build()  #building with input file build
  # tester.verify()
  # tester.summary()
  tester.read()
  exit(0)

