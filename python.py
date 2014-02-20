import math;
def calculate(): 
 # alternate solution is using eval() maybe the easiest way to do this, but can also raise security issues
	
	calc = SimpleCalculator();
	v =  "Calculator currently supports : ";
	for key, value in calc.options.items():
		v += key + " ";
	print v;
	a  = raw_input('Type your calculation e.g. 1+3 ?  ');
	
	
	#return calc.calculate(a);
	print calc.calculate(a);
	b = raw_input('New Calculation Y/n? ');
	if( b is "Y" or b is "y"):
		calculate();

class SimpleCalculator:
	#BIDMAS - Brackets, Indices,Divide,Multiply,Add,Subtract

	def calculate(self,a):
		a.replace(" ","");
		try:
			return self.getvalue(a);
		except ValueError:
			return "E";


	# for additional support update the process
	# allows future additions by modifying one  method.
	def calculator_evaluator(self,a,operator):
		if(operator  in s for s in self.options):
			vals = a.split(operator,1);
			return self.options[operator](self,vals[0],vals[1]);
		else:
			return a;
			
			
	# check if the current figure contains operators
	# check if the value is integer or float
	def getvalue(self,a):
		for key, value in self.options.items():
			if(key in a):
				return self.calculator_evaluator(a,key);
		if(self.is_int(a)):
			return int(a);
		else:
			return float(a);
	
	#simple check if the value is an integer
	def is_int(self,s):
		try: 
			int(s)
			return True;
		except ValueError:
			return False;

	# add 2 values
	def add(self,a,b):
		return self.getvalue(a) + self.getvalue(b);

	# subtract values
	def subtract(self,a,b):
		return self.getvalue(a) - self.getvalue(b);

	# multiply values
	def multiply(self,a,b):
		return self.getvalue(a) * self.getvalue(b);

	#divide values
	def divide(self,a,b):
		return self.getvalue(a) / self.getvalue(b);
		
	# brackets for calculating  information in brackets
	def brackets(self,a,b):
		openbackets = 0
		for char in b:
			if(char == ")"):
				break;
			elif(char == "("):
				openbackets +=1;

		rst = b.split(")",1+openbackets);
		#print "result="+  str(len(rst));	
		vals2 = ["",""];
		if(openbackets > 1):
			for  x in range(0,openbackets):
				vals2[0] += rst[x] + ")";
			vals2[1] = rst[-1];
		elif(openbackets == 1):
			vals2[0] = rst[0] + ")";
			vals2[1] = rst[-1];
		else:
			vals2 = rst;
		
		print vals2;
	
		inbrackets = self.getvalue(vals2[0]);
		if(len(a) > 0 and self.is_int(a[-1]) == True):
			out = str(a) + str("*") +  str(inbrackets) + str(vals2 [1]);
		else:
			out = str(a) + str(inbrackets) + str(vals2 [1]);
		return self.getvalue(out);

	# add method and identifier
	options  = {
				"(":brackets,
				"/":divide,
				"*":multiply,
				"+":add,
				"-":subtract		
				};
