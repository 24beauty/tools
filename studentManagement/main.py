import function as f


def main():
    flag = True    # Decide if exit the system
    while flag:
        menu()
        option = input("请输入选项前的数字编号：")
        if option in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option)
            if option_int == 0:
                print("您已选择退出学生信息管理系统！！！")
                flag = False
            elif option_int == 1:
                f.insertStudent()
            elif option_int == 2:
                f.deleteStudent()
            """elif option_int == 3:
                editStudent()
            elif option_int == 4:
                searchStudent()
            elif option_int == 5:
                sortStudent()
            elif option_int == 6:
                totalStudent()
            elif option_int == 7:
                showStudent()
"""

def menu():
    print('''
    ╔*******************学生信息管理系统******************╗
    |                                                  |
    |    ==================功能菜单==================   |
    |    1. 录入学生信息                                 |
    |    2. 删除学生信息                                 |
    |    3. 修改学生信息                                 |
    |    4. 查询学生信息                                 |
    |    5. 排序学生信息                                 |
    |    6. 求和学生信息                                 |
    |    7. 显示所有学生                                 |
    |    0. 退出管理系统                                 |
    |    ===========================================  |
    |    说明：通过输入选项数字或↑↓方向键选择菜单选项          |
    ╚**************************************************╝
    ''')


if __name__ == "__main__":
    main()
