import os
import cv2


path="images1/"

images1=[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
    file_name = path+"/"+file
    
    print(file_name)

    images1.append(file_name)

print(len(images1))
count = len(images1)
frame=cv2.imread(images1[0])
width,height,channels=frame.shape
size=(width,height)
print(size)
out = cv2.VideoWriter('project1.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frame=cv2.imread(images1[i])
    out.write()
print("Done")

