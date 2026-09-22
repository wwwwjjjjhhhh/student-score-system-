def show_student():
   name = input("请输入学生姓名：")
   gender = input("请输入学生性别：")
   score = float(input("请输入学生成绩："))

   print(f"学生姓名：{name}")
   print(f"学生性别：{gender}")
   print(f"学生成绩：{score}")


if __name__ == "__main__":
    show_student()
