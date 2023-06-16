
# firstname = input("input first name here: ")
# last_name = input ("Enter last name here: ")
# matricnum = input ("Enter Matric number here: ")
# print ("Hello",firstname )



def StdID_function():
      fst_name = input("input your first name:- ") 
      scd_name = input("Enter your last name:- ")
      mtr_num = input("Enter your matric Number:- ")
      std_info_list = {fst_name,scd_name,mtr_num}

      print (list(std_info_list))
      
StdID_function()     
input("press ENTER to continue.")