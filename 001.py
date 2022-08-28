def hello() :
      print(hello)
hello()
print("1+2", get_add_numbers(1,2))
print("12+2", get_add_numbers(12,2))    
def get_factorial(number) :
    result = 1
    while number > 0 :
      result *= number
      number -= 1
    return result
print("6!", get_factorial(6))
print("7!", get_factorial(7))
print("100!", get_factorial(100))
class Calculate：    
    def ——init——（self，number1，number2）        # 接收两个参数
        self.number1 = number1
        self.number2 = number2
    
    def he(self):
        print("和是 : %d " % (self.number1 + self.number2))    # 进行格式化输出
     
    def cha(self):
        print("差是 : %d " % (self.number1 - self.number2))




result = Calculate(5,5)        # 传递两个参数
result.he()
result.cha()            # 调用函数进行求值
