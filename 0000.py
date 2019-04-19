"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
"""
#PIL的Image
from PIL import Image,ImageDraw,ImageFont,ImageFilter

def add_num(img):
    draw  = ImageDraw.Draw(img)
    myFront = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', size=40)#这里的size不知道怎么设置得大一点
    fillcolor = '#000000'
    width,heigth = img.size
    draw.text((width-40, 10), '99+', front=myFront, fill=fillcolor)
    img.show()
    img.save('newImage.jpg', 'jpeg')
    #img.save("newImage2.png")

def changeToL(image,name):
    new_img = image.convert('L')
    path = 'F:\wallPaper\\forResult\\' + name + '.jpg'
    new_img.save(path, 'jpeg')

def tryBlend(imag1,imag2):
    new_image = Image.blend(imag1,imag2,0.45)
    new_image.show()
    new_image.save("F:\wallPaper\\forResult\\blend.jpg", 'jpeg')

if __name__ == '__main__':
    #open:Image.open

    #image = Image.open('F:\wallPaper\\forTest\\14.jpg')#路径里面以数字或者字母f开头要加'\'做转义？！

    #image.show()#显示图片
    #print(image.format)#显示图像格式，此处是JPEG；标识了图像来源如果不是从文件中读取，会返回None
    #print(image.mode)#显示图像的模式，表明图像所使用的像素格式，L:灰度图像（黑白）；RGB：真彩色图像；CMYK：出版图像；
    #new_image = image.convert('L')#把其他像素格式的图片转换为灰度图像
    #print(new_image.mode)
    #new_image.save('gray.jpg','jpeg')
    #add_num(image)
    #changeToL(image, '1')
    #print(image.size)#打印图片的尺寸信息
    """
    rgb2xyz = (0.4,0.3,0.1,0,
               0.2,0.7,0.07,0,
               0.02,0.12,0.95,0)
    new_img = image.convert('L',rgb2xyz)
    print(new_img.mode)
    new_img.show()
    """
    #print(image.info)#存储图像相关的字典信息

    #new:Image.new;使用给定的mode、size、color来生成一个图像,color默认黑色
    #img = Image.new('RGB', (128, 128), '#cc0000')
    #add_num(img)
    #copy:im.copy():复制图像;但是原始图像不受影响
    #crop:im.crop(box):从原图像获得矩形区域的拷贝；box((左上角的x,y),(右上角的x,y))
    #paste:im.paste(image,box):将一张图粘贴到另一张图上；可用来填充

    #filter：im.filter(filter):返回一个使用给定滤波器处理过的图像的拷贝；图像滤波在ImageFilter模块中
    #BLUR、CONTOUR、DETAIL、EDGE_ENHANCE、EDGE_ENHANCE_MORE、EMBOSS、FIND_EDGES、SMOOTH、SMOOTH_MORE、SHARPEN
    #其中BLUR就是均值滤波，CONTOUR找轮廓，FIND_EDGES边缘检测，使用该模块时，需先导入
    """
    new_image = image.filter(ImageFilter.CONTOUR)
    new_image.show()
    new_image.save("F:\wallPaper\\forResult\\filter.jpg",'jpeg')#很好用！！！
    """
    #blend:Image(img1,img2,alpha):使用给定的两张图以及透明度变量，插值得到一张新的图，要求两张图的模式mode和尺寸size一样
    #合成公式为：out = image1 (1.0 - alpha) + image2 alpha：若变量alpha为0.0，返回第一张图像的拷贝；若变量alpha为1.0，将返回第二张图像的拷贝；对变量alpha的值无限制
    #有点像双重曝光的效果？！
    """
    image1 = Image.open('F:\wallPaper\\forTest\\14.jpg')
    image2 = Image.open("F:\wallPaper\\forTest\\32.jpg")
    print(image1.mode,image1.size)
    print(image2.mode,image2.size)
    tryBlend(image1,image2)
    """
    image = Image.open('F:\wallPaper\\forTest\\1.jpg')

    #r,g,b = image.split()#返回当前图像各个通道组成的一个元组
    #print(r.mode, g.mode, b.mode)

    #draft:配置图像文件加载器，使得返回一个与给定的模式和尺寸尽可能匹配的图像的版本
    #new_img = image.draft('RGB',(200,200))
    #new_img.show()

    #im.getbands():返回包括各个通道的名称的元组
    #im.getbbox():计算图像非零区域的包围盒，包围盒是一个4元组，定义了左、上、右和下像素坐标。如果图像是空的，这个方法将返回空
    #im.resize():返回改变尺寸的图像的拷贝
    # 变量size是所要求的尺寸，是一个二元组：（width, height）
    # 变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一
    # 如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST

    #im.seek(frame)：在给定的文件序列中查找指定的帧；如果查找超越了序列的末尾，则产生一个EOFError异常；当文件序列被打开时，PIL库自动指定到第0帧上
    #im.seek(2):第2帧；im.seek():第0帧
    #im.tell() ⇒ integer:返回当前帧所处位置，从0开始计算





