import os
import glob
import requests
import numpy as np
import com_tool

from PIL import Image


class Map(object):
    def __init__(self, place, xidx, yidx, z, path):
        self.place = place
        self.xidx = xidx
        self.yidx = yidx
        self.z = z
        self.path = path

    def save_picture(self, url, x, y):
        r = requests.get(url)
        
        sname = self.path + "/map_{y}_{x}.png".format(x = x, y = y)
        
        with open(sname, 'ab') as pngf:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    pngf.write(chunk)
                    pngf.flush()

    def get_picture(self):
        cntx = 0
        cnty = 0
        for y in reversed(self.yidx):
            for x in self.xidx:
                url = "https://maponline3.bdimg.com/tile/?qt=vtile&x={x}&y={y}&z={z}&styles=pl" \
                    "&scaler=2&udt=20200304".format(x=x, y=y, z=self.z)   
                self.save_picture(url, cntx, cnty)
                cntx= cntx + 1
            cnty = cnty + 1
            cntx = 0

    def connect_picture_by_x(self):
        #命名规则：cd_x_y.png 左下坐标系
        #同一个x 同1列，y增加，图片在上面
        #假设输入排好序了

        plst = sorted(glob.glob(os.path.join(self.path, '*.png')), key = os.path.getmtime)
        print(plst)

        xmin = ((plst[0].split("\\")[1]).split(".")[0]).split('_')[1]
        print(xmin)

        alst = [] #3维   每行是在一列的图片 即x坐标相同的
        qlst = []
        for f in plst:
            w = ((f.split("\\")[1]).split(".")[0]).split('_') #['cd', '22568', '6898']
            w[0] = f
            print(w)
            if w[1] == xmin:
                qlst.append(w.copy())
            else:
                alst.append(qlst.copy())
                xmin = w[1]
                qlst = []
                qlst.append(w.copy())
        alst.append(qlst.copy())
   
        print(alst)
        print(len(alst[0]), len(alst))
        m2 = [512 * len(alst[0]), 512 * len(alst)] #计算有多少行， 多少列
        #im2=Image.new('RGBA', (m2[0], m2[1]))
        print(m2)
        iw = 0
        for k in alst:#k里面装的是x相同的值，y应该递增
            plen = len(k)   #行的个数
            #print(k[0])
            msize = [512 * plen, 512]
            print(msize)
            toImage = Image.new('RGBA', (msize[0], msize[1]))
            for i in range(plen):
                fromImage = Image.open(k[i][0])
                toImage.paste(fromImage, (i * msize[1], 0 * msize[1]))
                print(k[i][0])

            #print(k[0])
            sname = "/m_{x}.png".format(x = k[0][1])
            iw += 1
            #im2.paste(toImage)
            toImage.save(self.path + sname)

    def connect_picture_by_y(self):
        #命名规则：cd_x_y.png 左下坐标系
        #同一个x 同1列，y增加，图片在上面
        #假设输入排好序了

        plst = sorted(glob.glob(os.path.join(self.path, 'm_*.png')), key = os.path.getmtime)

        for i in plst:
            print(i)

        xmin = ((plst[0].split("\\")[1]).split(".")[0]).split('_')[1] #817
        ima21 = Image.open(plst[0]) #817
        w = np.array(ima21).shape
        print(ima21, plst[0]) 
        print(w) #(512, 2560, 4)
       
        plen = len(plst)
        msize = [w[1], w[0]*plen] #
        print(msize)
        toImage = Image.new('RGBA', (int(msize[0]), int(msize[1])))
        for i in range(plen):
            print(i)
            fromImage = Image.open(plst[i])
            fromImage = fromImage.resize((int(msize[0]), int(512)), Image.ANTIALIAS) #
            toImage.paste(fromImage, (0, int(i * 512))) #

        #print(k[0])
        sname = "/" + self.place + ".png"

        toImage.save(self.path + sname)
     
    def get_map(self):
        com_tool.make_dir(self.path)
        self.get_picture()
        self.connect_picture_by_x()
        self.connect_picture_by_y()
  


#beijing = Map([3162, 3163, 3164, 3165], [1177, 1178, 1179], 14, 
#             "E:/MiniMetro/Picture/Beijing/Map")
#beijing.get_map()
