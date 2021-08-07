from database import run_query, run_query_executemany


def insertStudent():
    studentList = []
    flag = True
    while flag:
        try:
            id_student = int(input("请输入学生学号："))
        except ValueError as e:
            print(e, "请重新输入有效的学生学号信息！")
            continue
        if not id:
            break
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            pythonScore = int(input("请输入python成绩："))
            englishScore = int(input("请输入english成绩："))
            mathScore = int(input("请输入math成绩："))
        except ValueError as e:
            print(e, "输入的成绩无效，请输入正确的数值....开始重新录入信息")
            continue

        # 将输入的学生信息保存到字典
        student = (id_student, name, pythonScore, englishScore, mathScore)
        studentList.append(student)

        input_mark = input("请问是否继续添加学生信息？y/n")
        if input_mark.lower() == "y":
            flag = True
        else:
            flag = False

    query = "INSERT INTO sys.student (id, studentName, pythonScore, englishScore, mathScore) " \
            "VALUES (%s, %s, %s, %s, %s)"
    run_query_executemany(query, studentList)
    print("学生信息录入数据库完毕！")


def deleteStudent():
    flag = True
    while flag:
        deleteOption = input("请选择按 1 (学生ID)或 2 (学生姓名)删除: ")
        if deleteOption == "1":
            deleteID = input("请输入删除学生的ID:")
            confirmDelete = input("将要删除的学生ID为: " + deleteID + ", 确认请按'y'!")
            if confirmDelete == 'y':
                deleteQuery = "DELETE FROM sys.student WHERE id = '" + deleteID + "'"
                run_query(deleteQuery)
                print("学生ID " + deleteID + " 已被成功删除")
            else:
                print("输入有误，请重新输入！")
                continue
            continueDelete = input("是否继续删除? (y/n): ")
            if continueDelete == 'y':
                continue
            else:
                break
                flag = False

        elif deleteOption == "2":
            ''' 模块待完善'''
            print("模块功能尚未完成！")
            continue
        else:
            print("输入的删除选择有误，请重新输入数字 1 或 2 !")
            continue
