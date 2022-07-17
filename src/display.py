import cv2
import matplotlib.pyplot as plt

#from file_selector import file_select 

#pic=file_select()
#image = cv2.imread(pic)
image = cv2.imread("src/generated_pic.jpg")
height, width = image.shape[:2]
resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

fig = plt.gcf()
fig.set_size_inches(18, 10)
plt.axis("off")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()