import shutil

# 指定文件夹路径
source_folder = 'result'  # 原始 TIFF 文件所在文件夹
destination_folder = 'plus'  # 目标文件夹
import pandas as pd
import os  # 用于处理文件和目录

# 1. 读取Excel文件
# 1. 读取Excel文件
file_path = "C:/Users/r/Desktop/bayes/selection.csv"  # 替换为你的文件路径


data = pd.read_csv(file_path)

selected_features = [col for col in data.columns if col != 'RATIO']

for filename in os.listdir(source_folder):
    if filename.endswith('.tif') or filename.endswith('.tiff'):
        # 转换文件名为小写进行比较
        filename_lower = filename.lower()

        # 检查文件名是否与 selected_features 中的特征完全匹配（忽略大小写）
        for feature in selected_features:
            if filename_lower == feature.lower() + '.tif':  # 完全匹配文件名
                # 构造源文件和目标文件路径
                src_file = os.path.join(source_folder, filename)
                dest_file = os.path.join(destination_folder, filename)
                
                # 移动文件到目标文件夹
                shutil.move(src_file, dest_file)
                print(f"Moved: {filename} -> {destination_folder}")

