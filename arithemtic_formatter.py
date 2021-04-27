def arithmetic_arranger(prob,show_ans=False):
	if len(prob)>4:
		return "Error: Too many problems."
	val1 = ""
	val2 = ""
	div_line = ""
	ans_out = ""
	output=""
	for i in prob:
		problem = i.split(" ")
		if problem[0].isnumeric() == False or problem[2].isnumeric()== False : 
			return "Error: Numbers must only contain digits."
		if problem[1] == "+":
			solution = str(int(problem[0])+int(problem[2]))
		elif problem[1] == "-":
			solution = str(int(problem[0])-int(problem[2]))
		else:
			return "Error: Operator must be '+' or '-'."
		if(len(problem[0])>=5 or len(problem[2])>=5):
			return "Error: Numbers cannot be more than four digits."
		num1 = problem[0]
		num2 = problem[2]
		op = problem[1]
		l = max(len(num1),len(num2))+2
		fisrtline = str(num1).rjust(l)
		secondline = op + str(num2.rjust(l - 1))
		ans = str(solution).rjust(l)
		
		dashline = ""
		for dash in range(l):
			  dashline += "-"
		
		if i != prob[-1]: 
			val1 += fisrtline + '    '
			val2 += secondline + '    '
			div_line += dashline + '    '
			ans_out += ans + '    '
		else: 
			val1 += fisrtline
			val2 += secondline 
			div_line += dashline 
			ans_out += ans  

	if show_ans: 
		output = val1 + "\n" + val2 + "\n" + div_line + "\n" + ans_out
	else:
		output = val1 + "\n" + val2 + "\n" + div_line  
	return output


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
    



