# # # # s = "sudh"
# # # # for i in s :
# # # #     print(i)
# # # # print(type(s))
# # # # s1 = iter(s)
# # # # print(type(s1))
# # # # print(next(s1))
# # # # def count_test(n):
# # # #     count = 1
# # # #     while count<= n:
# # # #         yield count
# # # #         count = count + 1 
# # # # c = count_test(5);
# # # # for i in c:
# # # #     print(i)


# # # # def count_test(n):
# # # #     count = 1
# # # #     while count<= n:
# # # #         yield count
# # # #         count = count*3 + 1 
# # # # c = count_test(15);
# # # # for i in c:
# # # #     print(i)

# # # #-------------------------------------------lambda function-----------------------------------------------------------



# # # # n = 3
# # # # p = 2
# # # # def test(n,p):
# # # #      return n**p
# # # # print(test(3,2))

# # # # a = lambda n , p : n**p

# # # # print(a(3,5))

# # # # add = lambda x,y : x + y
# # # # print(add(3,5))

# # # # c_to_f =lambda c : (9/5)*c + 32
# # # # print(c_to_f(45))

# # # # f_to_c = lambda f : (f-32)*(5/9)
# # # # print(f_to_c(113))

# # # # finding_max = lambda x,y : x if x>y else y
# # # # print(finding_max(12,23))

# # # # s = "skills"
# # # # find_len = lambda s : len(s)
# # # # print(find_len(s))

# # # # finding_min = lambda x,y,z: x if x<y and x<z else y  if y<x and y<z else z if z<x and z<y else invalid 

# # # # print(finding_min(3,5,2))
# # # # print(finding_min(3,2,5))
# # # # print(finding_min(2,3,5))


# # # #l =[2,3,4,5,6]
# # # # def sq(x):
# # # #     return x**2
# # # # print(list(map(sq,l)))

# # # # print(list(map(lambda x : x**2 , l)))  #using lambda

# # # # def test(l):
# # # #     l1 = []
# # # #     for i in l :
# # # #         l1.append(i**2)
# # # #     return l1

# # # # l1 = [1,2,3,4,5]
# # # # l2 = [6,7,8,9,10]
# # # # print(list(map(lambda x , y : x + y , l1 , l2)))

# # # # def add(x,y):
# # # #     return x + y
# # # # print(list(map(add,l1,l2)))

# # # # s = "skils"
# # # # print(list(map(lambda s :s.upper() , s)))

# # # # from functools import reduce 

# # # # l = [1,2,3,4,5]
# # # # # result = reduce (lambda x,y : x+y , l)
# # # # # print(result)

# # # # # g = reduce(lambda x , y : x*y , l)
# # # # # print(g)

# # # # filter = list(filter(lambda x : x%2 == 0 , l))
# # # # print(filter)

# # # # a = 1 
# # # # print(type(a))

# # # # print(type("skills"))
# # # # class test:

# # # # def test():
# # # #     return "Hello"

# # # # a = test()
# # # # print(type(a))

# # # # class Skills:
# # # #     def welcome_msg(self):
# # # #         print("Welcome to Skills")

# # # # rohan = Skills()      

# # # # print(type(rohan))

# # # # rohan.welcome_msg()

# # # class skills1:
# # #     def __init__(self,phone_number, email_id, student_id):
# # #         self.phone_number = phone_number
# # #         self.email_id = email_id
# # #         self.student_id = student_id

# # #     def return_student_details(self):
# # #         return self.student_id , self.email_id , self.phone_number
    
# # # rohan = skills1(29893444,"dudhdhu@gmail.com",121)

# # # print(rohan.return_student_details())
# # # print(rohan.email_id)

# # # ron = skills1(298944,"dudhu@gmail.com",123)

# # # print(ron.return_student_details())
# # # print(ron.email_id)

# # class skills2:
# #     def __init__(self,phone_number, email_id, student_id):
# #         self.phone_number1 = phone_number
# #         self.email_id1 = email_id
# #         self.student_id1 = student_id

# #     def return_student_details(self):
# #         return self.student_id1 , self.email_id1 , self.phone_number1

# # sudha = skills2(2394839489, "aajb@gmail.com",124)

# # print(sudha.return_student_details())

# # class UPI:

# #     def pay(self):
# #         print("payment through UPI")

# # class card:
# #     def pay(self):
# #         print("payment thorugh card")

# # for payment in [UPI(),card()]:
# #     payment.pay()


# # username1 = "anmol"
# # pin1 = 1234

# # username2 = "ankit"
# # pin2 = 5678

# # username3 = "alok"
# # pin3 = 9101

# # entered_username = (input("Enter your username :"))
# # entered_pin = int(input("enter your pin:"))

# # if entered_username == username1 and entered_pin == pin1 :
# #    print("name : Anmol Nigam")
# #    print("account id : 123654")
# #    print("balance : $1000000000000000000000000000000000")

# # elif entered_username == username2 and entered_pin == pin2 :
# #        print("name : Ankit kumar prajapti")
# #        print("account id : 456987")
# #        print("balance : $1000000000000000000000000000000000")


# # elif entered_username == username3 and entered_pin == pin3 :
# #        print("name : Anmol Nigam")
# #        print("account id : 123987")
# #        print("balance : $1000000000000000000000000000000000")


# # else:
# #    print("invalid username or incorect pin")


# class BankAccount:
#     def __init__(self, username, pin, name, account_id, balance):
#         self.username = username
#         self.pin = pin
#         self.name = name
#         self.account_id = account_id
#         self.balance = balance

#     def display_details(self):
#         print("\n----- Account Details -----")
#         print("Name :", self.name)
#         print("Account ID :", self.account_id)
#         print("Balance : $", self.balance)




  