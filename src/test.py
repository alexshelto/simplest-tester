#
#
#
#
#

import os



class Test:
  def __init__(self, build_file: str, verify_file: str):
    self.build_file = build_file
    self.verify_file = verify_file
    self.executable_name = None
    self.file_type = None

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




  def verify(self):
    try:
      file = openn(self.verify_file, 'r')
    except:
      print("trouble opening verify file")
      exit(1)
    pass
    

  def ls(self):
    os.system('ls -l')
    
    
