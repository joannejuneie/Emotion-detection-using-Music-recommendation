import cv2
with open("src/happy.txt",'r') as f:
    img = [line.strip() for line in f]
for image in img:
    loadedImage = cv2.imread("src/images/"+image)
    cv2.imwrite('src/data_set/happy/'+image,loadedImage)
print("done writing")