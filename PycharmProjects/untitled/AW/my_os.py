# _*_ coding:utf-8 _*_
import os


def get_child_items():
    """
    获取当前目录下的文件和目录
    :return: None
    """
    # 获取当前目录下的文件和目录
    items = os.listdir()
    file_list = list()
    dir_list = list()

    # 将文件和目录分别放到文件列表和目录列表
    for item in items:
        if os.path.isfile(item):
            file_list.append(item)
        else:
            dir_list.append(item)

    # 将文件列表转换为string
    file_str = "---- total {0} files----".format(len(file_list)) + "\n"
    for index in range(len(file_list)):
        file_str = file_str + str(index).rjust(6) + " : " + file_list[index] +"\n"

    # 将目录列表转换为string
    dir_str = "---- total {0} directories----".format(len(dir_list)) + "\n"
    for index in range(len(dir_list)):
        dir_str = dir_str + str(index).rjust(6) + " : " + dir_list[index] + "\n"

    # 合并文件string和目录string
    rst = (file_str + dir_str, dir_list, file_list)

    return rst


def file_explorer():
    """
    资源管理器
    :return: None
    """
    # 默认打开目录d:\
    var_path = "d:\\"
    os.chdir(var_path)
    items = get_child_items()
    tips = "Keyboard index to enter a directory\nKeyboard Q/q to quit\nKeyboard B/b to back\n"
    while True:
        os.chdir(var_path)
        items = get_child_items()
        print("Current directory: {0}".format(os.getcwd()))
        print(items[0])
        choice = input(tips)
        if choice.isalpha() and (choice.upper() == "Q"):
            break
        elif choice.isalpha() and (choice.upper() == "B"):
            os.chdir("..")
            if os.getcwd().endswith("\\"):
                print("已经是根目录了，不能再后退了")
            var_path = os.getcwd()
        elif choice.isnumeric() and (int(choice) in range(len(items[1]))):
            var_path = os.path.join(var_path, items[1][int(choice)])


if __name__ == "__main__":
    var_path = r"d:\temp"
    file_explorer()



