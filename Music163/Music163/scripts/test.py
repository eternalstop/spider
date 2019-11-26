class TestClass:
	# def __init__(self):
	# 	print("测试类")

	def method1(self):
		return "method1"

	def method2(self):
		return "method2"

	def method3(self):
		return "method3"


instance_class = TestClass()

for test_method in ['method1', 'method2', 'method3']:
	# print(test_method)
	# print(getattr(instance_class, test_method))
	print(instance_class.__dict__.get(test_method))