#
#
#
#
#
import os
import subprocess
from colorama import Fore, Back, Style




def parseTestCaseDetails(test_str: str)->str:
  start = test_str.find("NAME:") + len("NAME:")
  end = test_str.find('FILE:')
  test_name = test_str[start:end].strip()

  start = test_str.find("FILE:") + len("FILE:")
  end = test_str.find("VERIFY:") 
  file_name = test_str[start:end].strip()

  start = test_str.find("<output>") + len("<output>")
  end = test_str.find("</output>")
  expected_output = test_str[start:end].strip()

  return test_name, file_name, expected_output


class Test:
  def __init__(self, build_file: str, verify_file: str):
    self.build_file = build_file
    self.verify_file = verify_file
    self.passed = 0
    self.failed = 0


  def build(self) -> None:
    """build(): responsible for executing all commands inside of build.txt file""" 
    try:
      file = open(self.build_file, 'r')
    except:
      print("trouble opening build file")
      exit(1)
    
    self.file_type = file.readline()  #grabbing file type to know how to build

    #executing command from file
    for command in file:
      print('>> {}'.format(command))
      os.system(command)

    file.close() #closing file stream


  def read(self):
    try:
      with open(self.verify_file, 'r') as myFile:
        text = myFile.read()
        myFile.close()
    except:
      print("trouble opening verify file")
      exit(1)

    seperator = '@case'             #string to split verify.txt into array indexes of each cae
    tests = text.split(seperator)[1:]  #split into list by '@case', empty first index so remove

    #loop through list to build each test case info
    for test in tests:
      test_name, file_name, expected_output = parseTestCaseDetails(test)
      print("File name: {}".format(file_name))
      print('test name: {}'.format(test_name))
      print("Expected output: {}".format(expected_output))



  def verify(self):
    """
    Verify opens the verify file, seperates all test cases by '@case' identifier
    Loops through each case, grabs test name, file name, and expected output
    Procedes to run the program with the given file name, compares output to expected output
    """
    try:
      with open(self.verify_file, 'r') as myFile:
        text = myFile.read()
        myFile.close()
    except:
      print("trouble opening verify file")
      exit(1)

    seperator = '@case'             #string to split verify.txt into array indexes of each cae
    tests = text.split(seperator)[1:]  #split into list by '@case', empty first index so remove

    #loop through list to build each test case info
    for test in tests:
      test_name, file_name, expected_output = parseTestCaseDetails(test)

      #running file and grabbing stdout 
      output = ''
      exe = subprocess.Popen(['./a.out ../test-cases/'+str(file_name)],stdout=subprocess.PIPE, shell=True)
      for line in exe.stdout:
        output += line.decode('utf-8')
      
      self.display_test(test_name, file_name, expected_output.strip(), output.strip())



    

  def display_test(self, name: str, file: str, expected: str, output: str) -> None:
    passed = True if output == expected else False  #does output and expected output match?
    if passed:
      self.passed += 1
    else:
      self.failed += 1

    print('=' * 50)
    print(Fore.GREEN + 'Passed!') if passed else print(Fore.RED + 'Failed!')
    print(Style.RESET_ALL)
    print('Test Name: {}'.format(name))
    print('Input File: {}\n'.format(file))
    print('Expecting: {}\n'.format(expected))
    print('Output: {}'.format(output))
    print('=' * 50 + '\n') 


  def summary(self):
    print(Fore.GREEN + str(self.passed) + ' passed ' + Fore.RED + str(self.failed) + ' failed' + Style.RESET_ALL)


  
    
