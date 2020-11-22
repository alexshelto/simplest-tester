#
#
#
#
#

import os



class Test:
  def __init__(self):
    self.executable_name = None

  '''
  build(): responsible for executing all commands inside of build.txt file
  '''
  def build(self, file_name: str) -> None:
    try:
      file = open(file_name, 'r')
    except:
      print("trouble opening build file")
      exit(1)
    #executing each command in build.txt file
    for command in file:
      os.system(command)




  def execute(self):
    pass

  def ls(self):
    os.system('ls -l')
    
    
