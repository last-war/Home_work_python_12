def Error_Handler(func):
	def Inner_Function(*args, **kwargs):
		try:
			func(*args, **kwargs)
		except TypeError:
			print(f"{func.__name__} wrong data types. enter numeric")
	return Inner_Function

@Error_Handler
def Mean(a,b):
		print((a+b)/2)

