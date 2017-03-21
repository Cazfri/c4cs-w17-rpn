import operator
from colorama import init, Fore, Back, Style
init()
import logging
logging.basicConfig(filename='rpn.log', level=logging.INFO)

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			logging.info(str(operand) + ' operator used')
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			stack.append(result)
	return stack.pop()

def something():
	print("This function doesn't do anything, no need to test for it!")

def main():
	while True:
		userinput = input('rpn calc> ')
		for word in userinput.split():
			if word.isdigit():
				print(Fore.GREEN + word, end=' ')
			elif word in OPERATORS.keys():
				print(Fore.RED + word, end=' ')
			else:
				print(word, end=' ')
		print()
		result = calculate(userinput)
		print('=\t'+ Fore.BLUE + str(result))
		print(Style.RESET_ALL, end='')
		

if __name__ == '__main__':
	main()