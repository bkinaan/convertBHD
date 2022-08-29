print ("Welcome to the Binary, Hexidecimal, Decimal Converter!")
print ("What would you like to do?")
print("""
1. Convert binary to decimal
2. Convert decimal to binary
3. Convert hexidecimal to decimal
4. Convert decimal to hexidecimal\n""")

inputVal = input("Enter a value from 1-4: ")

if (inputVal == "4") {
	inputNum = input("Input the starting value: 0x")
	if (type(inputNum) == int):
		num = inputNum
		value = 0
		index = 0
		while (num != 0):
			temp = inputNum % 10
			value += temp * 16 ** index
}
