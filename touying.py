import salem
from salem import get_demo_file

# 加载 GeoTIFF 文件
tif_file = "your_file.tif"  # 替换为你的文件路径
# 如果没有文件，可以使用 salem 示例文件
# tif_file = get_demo_file('himalaya.tif')

# 打开并可视化
smap = salem.Map(tif_file)
smap.visualize(cmap='terrain')  # 自定义颜色映射
