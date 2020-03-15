import os

def make_dir(path):
    path = path.strip()
    path = path.rstrip()

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path + "创建成功")
    else: 
        print(path + "目录已存在")

def judge_color(pv, l, r):
        if(l <= pv[0] <= r and l <= pv[1] <= r and l <= pv[2] <= r):
            return True
        return False