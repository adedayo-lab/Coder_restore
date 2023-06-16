# class MyClass:
#       x = "Dedayo"

# pi = MyClass()
# print (pi.x)


class studentID:
      #creating containers
      def __init__(self,sur_name,fst_name,scd_name,mtr_num):
            self.sur_name = sur_name
            self.fst_name = fst_name
            self.scd_name = scd_name
            self.mtr_num = mtr_num
            

#Entering the values for each container above
std_info_list = studentID("Aderibigbe","Adedayo","Ayobami","2016232070019")

# to choose the specific output


print(std_info_list.sur_name)
print(std_info_list.fst_name)
print(std_info_list.scd_name)
print(std_info_list.mtr_num)


input("press ENTER to continue.")