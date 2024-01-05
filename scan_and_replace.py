import os
# 用于扫描一个目录下所有指定文件，并替换字符串
# 无法恢复，谨慎使用
# 处理所有build.gradle
def scan_and_replace(directory, target_string, replacement):
    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(directory):
        if exclude_directory in dirs:
            dirs.remove(exclude_directory)
        for file in files:
            # 只处理gradle文件，你可以根据需要修改文件扩展名
            if file.endswith(".gradle"):
                file_path = os.path.join(root, file)
                print(file_path)
                # # 打开文件并读取内容
                # with open(file_path, 'r', encoding='utf-8') as f:
                #     content = f.read()
                #     # 判断文件中是否存在目标字符串
                #     if target_string in content:
                #         # 替换目标字符串
                #         new_content = content.replace(target_string, replacement)
                #
                #         # 写回文件
                #         with open(file_path, 'w', encoding='utf-8') as f:
                #             f.write(new_content)
                #
                #         # 打印日志
                #         print(f"Replaced in file: {file_path}")



# 指定要扫描和替换的目录、目标字符串和替换字符串
directory_to_scan = "D:\\Luink\\project\\iames-alps-abnormal"
target_string = ':mode-lib'
replacement = ''
exclude_directory = "build-logic"

# 执行扫描和替换操作
scan_and_replace(directory_to_scan, target_string, replacement)