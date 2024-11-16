class employee:
    def __init__(self):
        print("I am an employee at Codingal")
    def __del__(self):
        print("Removed")
obj=employee()
del obj