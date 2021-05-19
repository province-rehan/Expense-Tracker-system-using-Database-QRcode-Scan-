import cv2
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

camera = True
global data11
while camera == True:
   success, frame = cap.read()

   for code in decode(frame):
       a = code.data.decode('utf-8')
       data11 = int(a)
       print(data11)

   cv2.imshow('no', frame)
   cv2.waitKey(1)





# Append vs write mode
file1 = open("myfile1.txt", "w")
file1.close()

# Write-Overwrites
file1 = open("myfile1.txt", "w")  # write mode
file1.write(str(data11))
file1.close()

file1 = open("myfile1.txt", "r")
print(
"Output of Readlines after writing")
print(
file1.readlines())
print(
file1.close())
