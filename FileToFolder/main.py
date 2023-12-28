import os
import shutil


def file_to_folder(input_path):
    # 获取输入路径的绝对路径
    abs_path = os.path.abspath(input_path)

    if os.path.isfile(abs_path):
        # 如果是文件，提取文件名（不包含后缀）
        file_name, _ = os.path.splitext(os.path.basename(abs_path))

        # 获取上一级文件夹名
        parent_folder = os.path.basename(os.path.dirname(abs_path))

        # 如果上一级文件夹名和文件名已经一样，则不处理
        if file_name != parent_folder:
            # 构建目标文件夹路径
            target_folder = os.path.join(os.path.dirname(abs_path), file_name)

            # 创建目标文件夹
            os.makedirs(target_folder, exist_ok=True)

            # 移动文件到目标文件夹
            shutil.move(abs_path, os.path.join(target_folder, os.path.basename(abs_path)))

    elif os.path.isdir(abs_path):
        # 如果是文件夹，遍历文件夹下的所有文件和子文件夹
        for root, _, files in os.walk(abs_path):
            for file in files:
                # 提取文件名（不包含后缀）
                file_name, _ = os.path.splitext(file)

                # 获取上一级文件夹名
                parent_folder = os.path.basename(root)

                # 如果上一级文件夹名和文件名已经一样，则不处理
                if file_name != parent_folder:
                    # 构建目标文件夹路径
                    target_folder = os.path.join(root, file_name)

                    # 创建目标文件夹
                    os.makedirs(target_folder, exist_ok=True)

                    # 移动文件到目标文件夹
                    file_path = os.path.join(root, file)
                    shutil.move(file_path, os.path.join(target_folder, file))


if __name__ == "__main__":
    # 通过用户输入获取文件或文件夹路径
    input_path = input("请输入文件或文件夹路径: ")

    # 调用函数进行处理
    file_to_folder(input_path)

    print("文件转移到文件夹完成。")
