import rasterio
import numpy as np
import os

def process_tif_files(folder_path, output_file_path, prefix, operation="sum"):
    # 获取符合前缀条件的 TIFF 文件
    tif_files = [f for f in os.listdir(folder_path) if f.endswith(('.tif', '.tiff')) and f.startswith(prefix)]
    
    if not tif_files:
        print(f"No TIFF files with the prefix '{prefix}' found.")
        return
    
    # 读取第一个 TIFF 文件，作为参考
    first_tif_path = os.path.join(folder_path, tif_files[0])
    with rasterio.open(first_tif_path) as src:
        meta = src.meta
        # 使用 float64 类型进行累加
        result_array = src.read(1).astype(np.float64)
    
    # 对剩下的 TIFF 文件进行操作
    for tif in tif_files[1:]:
        tif_path = os.path.join(folder_path, tif)
        with rasterio.open(tif_path) as src:
            data = src.read(1).astype(np.float64)
            result_array += data  # 累加操作
    
    # 如果操作是求平均
    if operation == "mean":
        result_array /= len(tif_files)
    
    # 累加完成后，将结果转换为 float32
    result_array = result_array.astype(np.float32)
    
    # 更新元数据
    meta.update(dtype=rasterio.float32, count=1)
    
    # 确保目标文件夹存在，如果不存在则创建
    output_folder = os.path.dirname(output_file_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 保存结果为新的 TIFF 文件
    with rasterio.open(output_file_path, 'w', **meta) as dst:
        dst.write(result_array, 1)
    
    print(f"Result saved as: {output_file_path}")

# 调用函数处理不同变量
process_tif_files('result', 'plus/MAP.tif', 'prec', operation="sum")
process_tif_files('result', 'plus/TMAX.tif', 'tmax', operation="mean")
process_tif_files('result', 'plus/TMIN.tif', 'tmin', operation="mean")
process_tif_files('result', 'plus/TAVG.tif', 'tavg', operation="mean")
process_tif_files('result', 'plus/SRAD.tif', 'srad', operation="mean")
process_tif_files('result', 'plus/WIND.tif', 'wind', operation="mean")
process_tif_files('result', 'plus/VAPR.tif', 'vapr', operation="mean")
