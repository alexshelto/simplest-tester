# simplest-tester
a simple not over-engineered solution for testing my algorithms hw outputs from various input file test cases all at once


#### TODO
- [ ] be able to work as executable from bin using cwd
- [ ] parse and check build.txt & verify.txt before testing output
- [ ] clean up code
- [ ] possibly extend to other langs depending on users / future classes and applications 
- [ ] nothing more since it should be simple

## Limitations
* Currently only made for C++
* executable must be named a.out 


## How to use
Create two files...
* build.txt
* verify.txt

### build.txt
build.txt will contain all the shell commands needed to build the project.  
can be as simple as: ```make```
or can be more expicit: ```g++ -Wall class.cpp main.cpp```

### verify.txt
This file will contain the name of your tests, the input file it will produce an output from, and the expected result.   
format for this file is **EXTREMELY** case sensitive
such a file can look like:    
```
NAME: Name of test 1 
FILE: inputFileName.extension 
VERIFY: "Hello\nWorld!" 

NAME: Name of test 2 
FILE: inputFileName.extension 
VERIFY: "2\nSecond Output" 
```
#### Rules for verify.txt
* It is important to remember to keep NAME, FILE, & VERIFY in caps.  
* Keep your entire *VERIFY* output in quotes, these quotes are to encapsulate the output to verify they wont be checked.  
* remember to end your program on a newline if its not already doing so -this shouldnt be an issue as its pretty standard-  
  * if your output matches the *VERIFY* and you're recieving a failure, its probably due to not having a newline after your last stdout.  

### Running
make sure main.py and test.py is in your project folder with your code and tests.  
execute main.py script and pass your build file first, then the verify file. 
``` python3 main.py build.txt verify.txt ```

### Demo output
<img src="https://raw.githubusercontent.com/alexshelto/simplest-tester/main/screenshot/output.png"/>

