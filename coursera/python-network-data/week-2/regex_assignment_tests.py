import re,sys

def main(file_name):
    print sum([int(i) for i in re.findall('[0-9]+', open(file_name).read())])

"""
def findNumbers(text):
    numbers_as_strings = re.findall('[0-9]+',text);
    return [int(i) for i in numbers_as_strings]

text = open('test_file.txt')
numbers = findNumbers(text)
print sum(numbers)
"""

if __name__ == "__main__":
    main(sys.argv[1])
