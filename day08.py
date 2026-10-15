class student:
    age = None
    name = None
    def student1(self):
        print(f"大家好，我叫{self.name},今年{self.age},会发出奇怪声音")
    def wing(self):
        import winsound
        winsound.Beep(2000,2000)  
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height       
stu1 = student("王","20","165cm")
stu_zhu = student("竹","19","175cm")
print(stu1.name,stu1.age)
stu1.student1()
stu1.wing()
print(stu_zhu.height)
class bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
 #这里的account仅作表示自变量用，具体的值为num引入            
    def deposit(self,account):
        self.balance += account 
        print(f"剩余{self.balance}元")
        return True
    def withdraw(self,account):
        if self.balance >= account: 
            self.balance -= account
            print(f"剩余{self.balance}元")
        else:
            print("余额不足")
        return True
account = bank("竹",10000)    
while True:
    choose = int(input("""欢迎您来到银行
      取款：【输入1】
      存款：【输入2】
      退出：【输入3】
      请输入你的选择:"""))
    if choose == 1:
       num = float(input("需要存入："))
#注意前缀，指明对象！
       account.deposit(num)
    elif choose == 2:
       num = float(input("需要取出："))
       account.withdraw(num)
    elif choose == 3:
        break
    else:
        print("输入无效")    
           
                  
