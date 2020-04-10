#fibonacci numbers within a range
# def find_previous(max,min):
#     prev_val=0
#     curr_val=1
#     next_val=1
#     while(next_val<num):
#        curr_val=curr_val+prev_val
#        next_val=curr_val
#     return curr_val

user_input_min=int(input("Enter the lower range :"))
user_input_max=int(input("Enter the upper range :"))

num1=0 #0 1 1 2 3
num2=1
num3=1
while(num1<=user_input_max):
    if(num1>=user_input_min):
       print(num1)
    num1=num2   #0
    num2=num3
    num3=num1+num2
   # print(num1)   #0if num1# 1123580




