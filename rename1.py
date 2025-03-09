import os
import shutil
# 指定文件夹路径
source_folder = 'cropped'  # 原始 TIFF 文件所在文件夹
destination_folder = 'result'  # 目标文件夹

os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹及其所有子文件夹
for root, dirs, files in os.walk(source_folder, topdown=False):  


    for filename in files:
        if filename.endswith('.tif') or filename.endswith('.tiff'):
            # 构造源文件和目标文件路径
            src_file = os.path.join(root, filename)
            dest_file = os.path.join(destination_folder, filename)
            
            # 移动文件到目标文件夹
            shutil.copy(src_file, dest_file)

    if not os.listdir(root):  # 如果子文件夹为空
        
        os.rmdir(root)  
folder_path = 'result'

# 遍历文件夹中的所有 TIFF 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.tif') or filename.endswith('.tiff'):


        if filename.startswith('cropped_wc2.1_5m_'):
            new_filename = filename.replace('cropped_wc2.1_5m_', '')

            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            shutil.copy(old_file_path, new_file_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.tif') or filename.endswith('.tiff'):

        if filename.startswith('cropped_'):

            new_filename = filename.replace('cropped_', '')

            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            if old_file_path != new_file_path:  

                if os.path.exists(new_file_path): 
                    
                    print(f"File already exists, skipping rename: {new_file_path}")
                else:
                    os.rename(old_file_path, new_file_path)  # 重命名文件

for filename in os.listdir(folder_path):
    if filename.endswith('.tif') or filename.endswith('.tiff'):
        if 'resampled' in filename:
            new_filename = filename.replace('_resampled', '')

            old_file_path = os.path.join(folder_path, filename)

            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(old_file_path, new_file_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.tif') or filename.endswith('.tiff'):
        name_without_extension, extension = os.path.splitext(filename)
        
        if '_' in name_without_extension:

            parts = name_without_extension.split('_')  

            new_filename = ""

            if len(parts) > 1 and parts[0] == parts[-1]:  
                new_filename = '_'.join(parts[:1])  
            elif len(parts) > 2 and parts[1] == parts[-1]:  
                new_filename = '_'.join(parts[:2])  
            elif len(parts) > 3 and parts[2] == parts[-1]:  
                new_filename = '_'.join(parts[:3])  
            else:
                new_filename = name_without_extension 

            # 重新构造完整的文件名
            new_filename += extension
            

            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(destination_folder, new_filename)
            
            # 重命名文件
            if old_file_path != new_file_path:  

                shutil.move(old_file_path, new_file_path)
            
            if old_file_path != new_file_path:  
            
                if os.path.exists(new_file_path): 
            
                    print(f"File already exists, skipping rename: {new_file_path}")
            
                else:
            
                    os.rename(old_file_path, new_file_path)  
            
            print(f'Renamed: {filename} -> {new_file_path}')
