# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# import math


# img1 = cv2.imread("img1.jpg")
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# img2 = cv2.imread("img2.jpg")
# img2 = cv2.resize(
#     img2, (img1.shape[1], math.floor(img1.shape[1] / img2.shape[1] * img2.shape[0]))
# )
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# sum_img = np.concatenate([img1, img2])

# sum_img = np.rot90(sum_img)

# plt.imshow(sum_img)
# plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")
# import cv2

# def rotate_image(image_path, angle):
#     img = cv2.imread(image_path)
#     (h, w) = img.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated = cv2.warpAffine(img, M, (w, h))
#     return rotated

# def uniform_resize(image_path, scale_factor):
#     img = cv2.imread(image_path)
#     (h, w) = img.shape[:2]
#     new_size = (int(w * scale_factor), int(h * scale_factor))
#     resized = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)
#     return resized

# def nonuniform_resize(image_path, width_factor, height_factor):
#     img = cv2.imread(image_path)
#     (h, w) = img.shape[:2]
#     new_size = (int(w * width_factor), int(h * height_factor))
#     resized = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)
#     return resized

# def main():
#     res = rotate_image('./square_plot.png', 180)
#     show_image(res, 'Изображение повернуто')

#     res = uniform_resize('./square_plot.png', 0.5)
#     show_image(res, 'Равномерно сжатое изображение')

#     res = nonuniform_resize('./square_plot.png', 0.8, 0.3)
#     show_image(res, 'Неравномерно сжатое изображение')

# if __name__ == '__main__':
#     main()
# def create_collage(image_paths, target_size=(1000, 1000)):
#     images = [cv2.imread(path) for path in image_paths]
#     if any(img is None for img in images):
#         print("Error: Could not load one or more images.")
#         return None

#     resized_images = [cv2.resize(img, target_size, interpolation=cv2.INTER_AREA) for img in images]
#     h, w = target_size
#     num_images = len(resized_images)
#     cols = int(np.sqrt(num_images))
#     rows = (num_images + cols - 1) // cols

#     collage = np.zeros((rows * h, cols * w, 3), dtype=np.uint8)
#     for i, img in enumerate(resized_images):
#         row = i // cols
#         col = i % cols
#         collage[row * h:(row + 1) * h, col * w:(col + 1) * w] = img
#     return collage


# def show_image(img, title='Image'):
#     plt.figure(figsize=(7,7))
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     plt.title(title)
#     plt.axis('off')
#     plt.show()

# def main():
#     res = create_collage(['./linear_plot.png', './square_plot.png', './sin_plot.png'])
#     show_image(res, 'Коллаж')

# if __name__ == '__main__':
#     main()


# 3d график по cars.csv
# import pandas as pd
# import plotly
# import plotly.graph_objs as go


# #Read cars data from csv
# data = pd.read_csv("cars.csv")


# #Make Plotly figure
# fig1 = go.Scatter3d(x=data['curb-weight'],
#                     y=data['horsepower'],
#                     z=data['price'],
#                     marker=dict(opacity=0.9,
#                                 reversescale=True,
#                                 colorscale='Blues',
#                                 size=5),
#                     line=dict (width=0.02),
#                     mode='markers')

# #Make Plot.ly Layout
# mylayout = go.Layout(scene=dict(xaxis=dict( title="curb-weight"),
#                                 yaxis=dict( title="horsepower"),
#                                 zaxis=dict(title="price")),)

# #Plot and save html
# plotly.offline.plot({"data": [fig1],
#                      "layout": mylayout},
#                      auto_open=True,
#                      filename=("3DPlot.html"))
print ("Hello world")
