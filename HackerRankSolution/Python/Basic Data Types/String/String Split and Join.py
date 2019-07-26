#String Split and Join
'''


Sample Input
			this is a string   
Sample Output
	this-is-a-string
'''
def split_and_join(line):
    input_string = line
    input_string = input_string.split(" ")
    input_string = "-".join(input_string)
    return input_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)