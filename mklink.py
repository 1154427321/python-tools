import os
# 批量创建软连接 输入源目录
# 输入指定目录，会在指定目录创建源目录下所有文件的软连接
def create_symlinks(source_dir, target_dir):
    # 确保源目录存在
    if not os.path.isdir(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    # 创建目标目录如果它不存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源目录中的所有文件
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)

        # 检查是否是文件，忽略目录
        if os.path.isfile(source_item):
            # 如果目标已存在，跳过
            if os.path.exists(target_item):
                print(f"Target already exists: {target_item}")
                continue

            try:
                # 创建软链接
                os.symlink(source_item, target_item)
                print(f"Created symlink: {target_item} -> {source_item}")
            except OSError as e:
                print(f"Could not create symlink due to: {e.strerror}")
        else:
            print(f"Skipping directory: {source_item}")

if __name__ == "__main__":
    # 用户输入源目录和目标目录
    source_dir = input("Enter the source directory: ").strip()
    target_dir = input("Enter the target directory: ").strip()
    create_symlinks(source_dir, target_dir)
