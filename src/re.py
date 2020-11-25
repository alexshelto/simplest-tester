


s = '''NAME: Test1
FILE: test1.txt
VERIFY:<output>
2
wazfee
</output>
'''



start = s.find("NAME:") + len("NAME:")
end = s.find('\n')
test_name = s[start:end].strip()
print('test name: {}'.format(test_name))


start = s.find("FILE:") + len("FILE:")
end = s.find("VERIFY:") 
file = s[start:end].strip()

print("File name: {}".format(file))

start = s.find("<output>") + len("<output>")
end = s.find("</output>")
expected_output = s[start:end].strip()
print("Expected output: {}".format(expected_output))
