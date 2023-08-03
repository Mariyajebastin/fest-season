# import pandas
# from pandas import DataFrame, ExcelWriter
# def export_excel(n):
# 	d= DataFrame(data=[["Mariya jebastin","19","5","24"],["Abhijith","15","9","24"],[],[],["Mariya jebastin","16","6","22"],["Abhijith","10","0","10"]],columns=["Name","Present days","Absent days","Total days"])
# 	count =0
# 	for x in range(1):
# 		excel_writer = ExcelWriter("uuk_attendance.xlsx")
# 		d.to_excel(excel_writer)
# 		excel_writer.save()
# 		count+=1
# export_excel(1)
#
#
#
#
#
#
# data =pandas.read_csv("aids.csv")
# d = DataFrame(data=[["mariyajebastin","12","kelambakkam","mariyajebastin777@gmail.com"],\
#                     ["kumar","27","kelambakkam","kumar7@gmail.com",],["angel","23","kelambakkam","angel7@gmail.com"],\
#                     ],columns=["name","age","address","email"])
# print(d)
#
#
#
# print(data[["Guinea"]][data["Data.New HIV Infections.Adults"]>0])
# print(data[["Date_reported","Country","New_cases","New_deaths"]])
# print(data['New_deaths'].min())
# for value in data.values:
#
#
# 	print(value)
# print()
# print(data.shape)
# print(data[["Country"]][data["New_deaths"]>6000])
#
# for value in data[data["New_deaths"]<5000].values:
# 	print(value)
#
# data=pandas.read_csv("art_coverage_by_country_clean.csv")
# print(data[])
# # class Queue:
# 	def __init__(self,limit=5):
# 		self.que=[]
# 		self.limit=limit
# 		self.front=None
# 		self.rear=None
# 		self.size=0
# 	def is_empty(self):
# 		return self.size<=0
# 	def en_queue(self,item):
# 		if self.size>= self.limit:
# 			print("Queue Overflow")
# 			return
# 		else:
# 			self.que.append(item)
# 		if self.front is None:
# 			self.front=self.rear=0
# 		else:
# 			self.rear=self.size
# 		self.size+=1
# 	print("Queue after en_queue",self.que)
# 	def de_queue(self):
# 		if self.size<=0:
# 			print("Queue Underflow")
# 			return 0
# 		else:
# 			self.que.pop(0)
# 			self.size-=1
# 			if self.size==0:
# 				self.front=self.rear=None
# 			else:
# 				self.rear=self.size-1
# 				print("Queue after de_queue",self.que)
# 	def queue_rear(self):
# 		if self.rear is None:
# 			print("Sorry,the queue is empty")
# 			raise IndexError
# 		return self.que[self.rear]
# 	def queue_front(self):
# 		if self.front is None:
# 			print("Sorry,the queue is empty!")
# 			raise IndexError
# 		return self.que[self.front]
# 	def size(self):
# 		return self.size
#
# que=Queue()
# que.en_queue("first")
# print("Front:"+que.queue_front())
# print("Rear:"+que.queue_rear())
# que.en_queue("second")
# print("Front:"+que.queue_front())
# print("Rear:"+que.queue_rear())
# que.en_queue("third")
# print("Front:"+que.queue_front())
# print("Rear:"+que.queue_rear())
# que.de_queue()
# print("Front:"+que.queue_front())
# print("Rear:"+que.queue_rear())
# que.de_queue()
# print("Front:"+que.queue_front())
# print("Rear:"+que.queue_rear())

# def delete_last_rode_from_CLL(self):
# 	temp=self.head
# 	current=self.head
# 	if self.head==None;
# 	print("List Empty")
# 	return
# 	while current.get_next()!=self.head:
# 		temp=current;
# 		current=current.get_next()
# 	temp.set_next(current.get_next())
# 	return
	

# class queue:
	# def print_circular_list(self):
	# 	currentNode=self.head
	# 	if currentNode==None:
	# 		return 0
	# 	print(current.get_data())
	# 	currentNode=currentNode.get_next()
	# 	while currentNode != self.head:
	# 		currentNode=current.get_next()
	# 		print(curren.get_data())
	



# def print_num(n):
# 	if n > 0:
# 		print_num(n-1)
# 		print(n,end="")
#
# print("numbers from 1 to 10")
# print_num(10)
# def remove_duplicate_space(data):
# 	data = ' '.join( data.split() )
# 	return data
#
# print(remove_duplicate_space("kumar isravel "))
# def value_find(x,y):
# 	if y in x:
# 		return True
# 	return False
# print(value_find([1,2,3,4,4],10))
# def count_string(value1,value2):
# 	count=0
# 	for value in value2:
# 		if value==value1:
# 			count+=1
# 	print(count)
# count_string("a","jebastin")
#
# def reverse(s):
# 	x = ""
# 	for i in s:
# 		x =  x+i
# 	return x
# s = "jebstin"
# print(reverse(s))
#
# def identify(data):
# 	a1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# 	a2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 	a3=["!","@","#","$","%","^","&","*","(",")","-",":",";","'",">","<","."]
# 	a4=["0","1","2","3","4","5","6","7","8","9"]
# 	for value in data:
# 		if not value in a1:
# 			if not value in a2:
# 				if not value in a3:
# 					if not value in a4:
# 						return False
#
# 	return True
# value="Mariyajebastin123@"
# print(identify(value))

# def remove_symbols(data):
# 	a=["!","@","#","$","%","^","&","*","(",")","?",".","/",">","<",]
# 	for value in data:
# 		if not value in a:
# 			print(value,end="")
# 		else:
# 			pass
# value="jebastin@123!@#"
# remove_symbols(value)
		
# def num_check(data):
# 	if len(data) == 10:
# 		for value in data:
# 			if not value.isdigit():
# 				return False
# 		return True
# 	return False
# value="0176731375"
# print(num_check(value))


		
		
		
		
	

		


	
