#
#
#
#
#
import os
import subprocess
from colorama import Fore, Back, Style


class Test:
  def __init__(self, build_file: str, verify_file: str):
    self.build_file = build_file
    self.verify_file = verify_file
    self.passed = 0
    self.failed = 0

  '''
  build(): responsible for executing all commands inside of build.txt file
  '''
  def build(self) -> None:
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





  def verify(self):
    try:
      file = open(self.verify_file, 'r')
    except:
      print("trouble opening verify file")
      exit(1)
    

    #reading verify file, running correct code file and comparing outputs
    while True:
      test_name = file.readline().partition("NAME:")[2].strip()
      file_name = file.readline().partition("FILE:")[2].strip()
      expected_output = file.readline().partition("VERIFY:")[2].replace('"', '').strip()
      file.readline() #ignore newline

      if not test_name or not file_name or not expected_output:
        file.close()
        break
      
      #running file and grabbing stdout 
      output = ''
      exe = subprocess.Popen(['./a.out ../test-cases/'+str(file_name)],stdout=subprocess.PIPE, shell=True)
      for line in exe.stdout:
        output += line.decode('utf-8').replace('\n', '\\n')
      output = output[:-2] #removes final new line

      self.display_test(test_name, file_name, expected_output, output)



    

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
    print('Expecting: {}'.format(expected))
    print('Output: {}'.format(output))
    print('=' * 50 + '\n')


  def summary(self):
    print(Fore.GREEN + str(self.passed) + ' passed ' + Fore.RED + str(self.failed) + ' failed' + Style.RESET_ALL)


  
    
