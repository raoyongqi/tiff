import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import rasterio
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeatur
import os
from matplotlib.colors import LinearSegmentedColormap


# 配置字体
config = {
    "font.family": 'Arial',
    'font.size': 24,
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
    'font.weight': 'bold'
}
mpl.rcParams.update(config)
mpl.rcParams['axes.unicode_minus'] = False

# 读取 SHP 作为底图
bound_file = gpd.read_file('GS(2020)4619/GS(2020)4619.shp')
import geopandas as gpd

# 使用 geopandas 直接读取 shapefile 文件
map_china_path = r'GS(2020)4619\\GS(2020)4619_4326_map.shp'
map_china_gdf = gpd.read_file(map_china_path)

# 打印出 GeoDataFrame 的前几行
print(map_china_gdf.head())

def point_plot(pre_title: str, tif_file: str):
    fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([73.2, 135, 17, 55], crs=ccrs.PlateCarree())  # 设置地图范围

    # 添加背景要素
    ax.add_feature(cfeatur.OCEAN.with_scale('10m'), zorder=2)
    ax.add_feature(cfeatur.LAKES.with_scale('10m'), zorder=2)

    # 绘制 SHP 边界
    bound_file.to_crs("EPSG:4326").plot(ax=ax, color='none', edgecolor='black', linewidth=0.8)

    # 绘制 map_china 的边界
    if map_china_gdf is not None:
        map_china_gdf.to_crs("EPSG:4326").plot(ax=ax, color='none', edgecolor='blue', linewidth=1)

    # 读取 TIFF 文件并绘制
    with rasterio.open(tif_file) as src:
        data = src.read(1)
        no_data_value = src.nodata

        # 处理无效值
        if no_data_value is not None:
            data = np.where(data == no_data_value, np.nan, data)

        # 计算 TIFF 的范围
        transform = src.transform
        bounds = [transform * (0, 0), transform * (src.width, src.height)]
        extent = [bounds[0][0], bounds[1][0], bounds[1][1], bounds[0][1]]

        # 获取颜色范围
        vmin, vmax = np.nanmin(data), np.nanmax(data)
        print(f"TIFF 文件 {tif_file} 的最小值: {vmin}, 最大值: {vmax}")

        # 颜色映射
        clist = ['blue', 'limegreen', 'orange', 'red']
        newcmap = LinearSegmentedColormap.from_list('mycolmap', clist, N=1024)

        # 使用自定义颜色映射绘制栅格数据
        im = ax.imshow(data, cmap=newcmap, interpolation='none', extent=extent, transform=ccrs.PlateCarree(), alpha=1)
        cax = fig.add_axes([ax.get_position().x0, ax.get_position().y0-0.07, ax.get_position().width, 0.02]) # Set the length, width, height and position of the color bar
        plt.colorbar(im, cax=cax, orientation = 'horizontal')
        # 添加颜色条

    # 添加南海区域
    ax2 = fig.add_axes([0.805, 0.274, 0.1, 0.15], projection=ccrs.PlateCarree())
    ax2.set_extent([104.5, 124, 0, 26], crs=ccrs.PlateCarree())
    ax2.add_feature(cfeatur.OCEAN.with_scale('10m'), zorder=2)
    bound_file.to_crs("EPSG:4326").plot(ax=ax2, color='none', edgecolor='black', linewidth=0.8)
    if map_china_gdf is not None:
        map_china_gdf.to_crs("EPSG:4326").plot(ax=ax2, color='none', edgecolor='blue', linewidth=0.8)
    ax2.gridlines(draw_labels=False, linestyle='--', lw=0.3)

    # 保存图片
    output_file = f'photo/{pre_title}1.png'
    plt.savefig(output_file, dpi=2800, bbox_inches='tight')
    plt.show()

# 测试调用
tif_file_path = 'cropped_result/tiff/cropped_predicted_rf.tif'
point_plot('China_TIFF', tif_file_path)
