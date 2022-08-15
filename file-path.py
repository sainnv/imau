### 如果只有一个层级需要遍历，那使用os.listdir(“路径”)就挺好用。我们大多数情况下只需要使用这个就行了。

url = r"D:\myproject\test"
files = os.listdir(url)
for file in files:
    print(os.path.join(url, file))

### 如果你需要遍历多个层级，那使用os.walk("路径")会更方便些。
url = r"D:\myproject\test"
for root, dirs, files in os.walk(url):
    print(root)
    for d in dirs:
        print(os.path.join(root, d))
    for file in files:
        print(os.path.join(root, file))

### 1.使用os模块os模块中的os.path.exists()方法用于检验文件是否存在, 全部路径。
os.path.exists('/test_file.txt')
# 通过这个方法，如果文件”test-data”不存在将返回False，反之返回True。
os.path.isfile("/test-data")

###3. 使用pathlib模块 pathlib模块在Python3版本中是内建模块，但是在Python2中是需要单独安装三方模块。
#使用pathlib需要先使用文件路径来创建path对象。此路径可以是文件名或目录路径。
#检查路径是否存在
path = pathlib.Path("path/file")
path.exist()

#检查路径是否是文件path = pathlib.Path("path/file")
path.is_file()

###
prefix = file.split('.')[0]
suffix = file.split('.')[-1]
postfix = file.split('.')[-1]
#使用 os.path.splitext(file)[0] 可获得 文件名 。
#使用 os.path.splitext(file)[-1] 可获得以 . 开头的 文件后缀名 。
#使用 os.path.basename() 从路径中获取文件名
#使用 os.path.split() 从路径获取文件名

### 拼接文件
os.path.join(path1,path2,*)
fdir +os.path.sep+prefix + '.xml'



n1 = 3.1415926
n2 = 31415.926
n3 = 0.31415
n4 = 21
# 保 留 两 位 小 数 的 数 字 格 式 7 print(' 保 留 两 位 小 数 : %.2f' % (n1))
print(' 保 留 两 位 小 数 : {:.2f}'.format(n1))
print(f' 保 留 两 位 小 数 : {n1:.2f}')
 
# 百 分 比 格 式 2 print(' 百 分 比 格 式 : {:.2%}'.format(n3))
# 既 有 千 分 位 分 隔 符 又 有 精 度 设 定 的 数 字 格 式 5
 
print(' 既 有 千 分 位 分 隔 符 又 有 小 数 位 数 ： {:,.2f}'.format(n2))
 
# 字 符 串 对 齐 格 式 ， 设 置 默 认 宽 度 为 8
print('{:>8}'.format(n4)) # 右 对 齐
print('{:<8}'.format(n4)) # 左 对 齐
print('{:^8}'.format(n4)) # 居 中 对 齐
 
# 数 字 补 零 ， 或 者 补 特 定 符 号 ， 比 如 ‘ x ’
print(' 左 边 补 零 ： {:0>4}'.format(n4)) # 左 边 补 0 ， 宽 度 为 4
print(' 右 边 补 x ： {:x<5}'.format(n4)) # 右 边 补 x ， 宽 度 为 5
 
# 带 符 号 保 留 小 数 点 后 两 位 56 # "+"
print(' 正 数 前 加 正 号 ， 负 数 前 加 负 :')
print('{:+.2f}'.format(n1))
print('{:+.2f}'.format(n2))
 
# "-"
print(' 正 数 前 无 符 号 ， 负 数 前 加 负 号 :')
print('{:-.2f}'.format(n1))
print('{:-.2f}'.format(n2))
 
# 空 格
print(' 正 数 前 加 空 格 ， 负 数 前 加 负 号 :')
print('{: .2f}'.format(n1))
print('{: .2f}'.format(n2))
