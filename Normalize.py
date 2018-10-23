class Normalize:

	def show(self):

		# ADD THE INPUT MODULE INSTEAD OF THIS HARD CODE STRING VALUE
		a = "2+4*9/3"

		order1=['/','*','+','-']
		nString = ""

		if (')' not in a):
			for i in range(len(order1)):
				for j in range(len(a)):
					if (order1[i] == a[j] and nString == ""):
						if (order1[i] == "/"):
							nString = nString + a[j-1] + " " + a[j+1] + " " + "/"
						if (order1[i] == "*"):
							nString = nString + a[j-1] + " " + a[j+1] + " " + "*"
						if (order1[i] == "+"):
							nString = nString + a[j-1] + " " + a[j+1] + " " + "+"
						if (order1[i] == "-"):
							nString = nString + a[j-1] + " " + a[j+1] + " " + "-"	
					elif (order1[i] == a[j] and nString != ""):
						if (order1[i] == "*"):
							nString = nString + " " + a[j-1] + " " + "*"
						if (order1[i] == "+"):
							nString = nString + " " + a[j-1] + " " + "+"
						if (order1[i] == "-"):
							nString = nString + " " + a[j-1] + " " + "-"
						if (order1[i] == "/"):
			 				nString = nString + " " + a[j-1] + " " + "/"	
		elif (")" in a and "(-" not in a):
			for j in range(len(a)):
				if (a[j] == ")"):
					nString = nString + " " + a[j-3] + " " + a[j-1] + " " + a[j-2]
				elif (a[j] == "*" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "*"
				elif (a[j] == "+" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "+"
				elif (a[j] == "/" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "/"
				elif (a[j] == "-" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "-"				
		elif ("(-" in a):
			for j in range(len(a)):
				if (a[j] == ")" and a[j-2] != "-"):
					nString = nString + " " + a[j-3] + " " + a[j-1] + " " + a[j-2]
				elif (a[j] == "*"  and a[j+2] != "-" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "*"
				elif (a[j] == "+" and a[j+2] != "-" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "+"
				try:
					if ((a[j] == "/"  and a[j+2] != "-" and nString != "")  or (a[j] == "/" and nString != "")):
						nString = nString +  " " + a[j+1] + " " + "/"
				except:
					nString = nString +  " " + a[j+1] + " " + "/"
				if (a[j] == "-"  and a[j+2] != "-" and a[j-1] != "(" and nString != ""):
					nString = nString +  " " + a[j+1] + " " + "-"
				if (a[j] == "(" and a[j+1] == "-"):
					nString = nString + " " + a[j]+a[j+1] + a[j+2]+a[j+3] + " " + a[j-1]

		print "Normalized Form : " + nString	
		print  "Result : ", eval(a)

norm = Normalize()
norm.show()