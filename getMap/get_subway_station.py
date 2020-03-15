import os
import glob
import cv2 as cv
import numpy as np
import com_tool

class Subway(object):
    def __init__(self, map_path, grayscale_path, circle_path):
        self.circle_center = []
        self.map_path = map_path
        self.grayscale_path = grayscale_path
        self.circle_path = circle_path

    def find_all_circles(self, img, x, y):
        src = img
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cimg = src.copy()

        edged = cv.Canny(img, 30, 150)
        circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 15, 0, 5)

        if(circles.any()):
            a, b, c = circles.shape
       
            for i in range(b):
                cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv.LINE_AA)
                cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv.LINE_AA)  # draw center of circle
                self.circle_center.append((circles[0][i][0] + 512 * int(y), circles[0][i][1] + 512 * int(x)))
   
        #cv.imshow("detected circles", cimg)
        cv.imwrite(self.circle_path + "/circles_{x}_{y}.png".format(x = x, y = y), cimg)

    def access_pixels_station(self, path):
        #print(image.shape)
        image = cv.imread(path)
        x = path.split('/')[4].split('_')[1]
        y = path.split('/')[4].split('_')[2].split('.')[0]
        print(x, y)
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2]
        #cv.imshow("aa.png", image)
        #cv.waitKey(0)
        #print("height : %s width : %s channels : %s"%(height, width, channels))
       
        for i  in range(height):
            for j in range(width):
                pv = image[i, j]
               
                if not com_tool.judge_color(pv, 170, 185):
                    image[i, j] = [255, 255, 255]
                else: 
                    #print(pv)
                    image[i, j] = [0, 0, 255]
                   
        #cv.imshow("a.png", image)
        #cv.waitKey(0)
        cv.imwrite(self.grayscale_path + "/Gs_{x}_{y}.png".format(x = x, y = y), image)
        self.find_all_circles(image, x, y)
     
    def get_subway_station(self):
        pic_list = sorted(glob.glob(os.path.join(self.map_path, 'map_*.png')), key = os.path.getmtime)
        com_tool.make_dir(self.grayscale_path)
        com_tool.make_dir(self.circle_path)
        for p in pic_list:
            print(p)
            self.access_pixels_station(p)
            
          
s = Subway("E:/MiniMetro/Picture/Beijing/Map", 
           "E:/MiniMetro/Picture/Beijing/Grayscale", "E:/MiniMetro/Picture/Beijing/Circle")

#s.get_subway_station()
#print(s.circle_center)
