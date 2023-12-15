#1.შექმენით Rectangle კლასი სურათის მიხედვით. დაამატეთ კლასის კონსტრუქტორი შესაბამისი ატრიბუტებით. 
# დაამატეთ მართკუხედის ფართობის და პერიმეტრის გამოსათვლელი ფუნქციები. კლასის გარეთ შემოიღეთ ობიექტები.
#  გამოთვალეთ obj1 ობიექტის ფართობი და დაბეჭდეთ მიღებული შედეგი.

# class Rectangle:

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def perimeter(self):
#         return 2*(self.length+self.width)
    
#     def area(self):
#         return (self.width*self.length)
    
# obj1 = Rectangle(3, 7)
# print(obj1.perimeter(),obj1.area())

    
# 2.აღწერეთ კლასი Car ქვემოთ მითითებული ატრიბუტების მიხედვით. შემოიღეთ 3 ობიექტი. 
# კლასში დაამატეთ მეთოდები სურვილისამებრ, რომელიც დაბეჭდავს შესაბამის ტექსტს.

# class car:
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.year = year
#         self.color = color
    
#     def sell(self):
#         return (self.brand,self.color,self.year,  "this vehicles price is $1000")
#     def buy(self):
#         return (self.brand,  self.color, self.year,  " this vehicle costs $500")
    

# obj1 = car("lada", "red", "1997")
# obj2 = car("mercedes", "blue", '2007')
# obj3 = car("toyota", "white" , "2018")

# print(obj2.sell())

# 3. აღწერეთ კლასი Dog ატრიბუტებით breed, size, age, color. შექმენით 3 ახალი ობიექტი შემდეგი მონაცემების მიხედვით.
# class dog:
#     def __init__(self,breed,size,age,color):
#         self.age = age
#         self.color = color
#         self.breed = breed
#         self.size = size
#     def dogs(self):
#         return (self.breed,self.size,self.age,self.color)
    
# obj1 = dog("pitbull", "31 meter", " 9 years old","white")
# obj2 = dog("chichuaua", "30 cms", "5 years old","black")
# obj3 = dog("mastiff", "1,90 meters", "7 years old","brown")

# print(obj3.dogs())
        
#  4. აღწერეთ კლასი Calculator მეთოდებით add, divide, subtract, multiply.

# class calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         return (self.num1 + self.num2)
#     def divide(self):
#         return (self.num1/self.num2)
#     def subtract(self):
#         return (self.num1 - self.num2)
#     def multiply(self):
#         return (self.num1*self.num2)
# nums = calculator(11,18)
# print(nums.multiply())
# print(nums.add())

# 5. აღწერეთ კლასი People, Student, Lecturer-შემდეგი სქემის მიხედვით (გამოიყენეთ მემკვიდრეობითობა).
# შვილობილი კლასის ინიციალიზაციაში გამოიძახეთ მშობელი კლასის ინიციალიზაცია. სურვილისამებრ შეგიძლიათ დაამატოთ სხვა ფუნქციონალი.
# კლასების აღწერის შემდეგ შემოიღეთ სხვადასხვა ობიექტები და გააკეთეთ მათზე მანიპულაციები.
# class people:
#     def __init__(self,mom,dad):
#         self.mom = mom
#         self.dad = dad

# class student:
#     def __init__(self,name,last):
#         self.name = name
#         self.lastname = last

# class lecturer:
#     def __init__(self,name2,last2):
#         self.name2 = name2
#         self.last2 = last2
#mas es ver gavige da iqneb klashi agvixsnat

#BONUS
#შექმენით კლასი Bank_Account, რომელიც შეიცავს დაფარულ (private) ატრიბუტებს account_name და balance. account_name არის
# მომხარებლის სახელი, ხოლო balance-ის მნიშვნელობაა თანხა, რომელიც მომხარებლს აქვს საბანკო ანგარიშზე. აღწერეთ კლასის
# ატრიბუტები კონსტრუქტორის მეშვეობით (ინიციალიზაცია). კონსტრუქტორში balance ატრიბუტს გაჩუმებით (default value)
# მიანიჭეთ 0.
# დამატებით შექმენით შემდეგი მეთოდები კლასში:
# 1. Account_name-სთვის დაწერეთ getter და setter მეთოდები.
# 2. დაამატეთ deposit() მეთოდი, რომელიც ასრულებს ანგარიშზე თანხის შეტანას. მას გადაეცემა ერთი პარამეტრი. პარამეტრად
# გადაცემული მნიშვნელობა ემატება საბანკო ანგარიშზე არსებულ თანხას. ფუნქცია ასევე ბეჭდავს ანგარიშზე არსებულ თანხას. მაგ:
# “თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ 120 ლარი”
# 3. დაამატეთ withdraw() მეთოდი, რომელიც ასრულებს ანგარიშიდან თანხის გამოტანას. გადაეცემა ერთი პარამეტრი. პარამეტრად
# გადაცემული მნიშვნელობა აკლდება საბანკო ანგარიშზე არსებულ თანხას. ფუნქცია ასევე ბეჭდავს ანგარიშზე არსებულ თანხას. მაგ:
# “თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ 120 ლარი”
# კლასის გარეთ შემოიტანეთ Bank_Account-ის ობიექტი. იხილეთ სურათი, თუ როგორ ხდება ოპერაციების შესრულება და დაწერეთ
# შესაბამისი კოდი.

# class bank_account:
#     def __init__(self,account_name,balance=0):
#         self.account_name = account_name 
#         self._balance = balance

#     def get_deposit(self):
#          return self._balance
#     def set_deposit(self):
        
# money = bank_account(0) 
# money.set_deposit(120)
# print(money.set_deposit)
# print(money.get_deposit)


