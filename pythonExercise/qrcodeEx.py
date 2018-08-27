import qrcode

# 复杂的生成二维码


def make_code(text):
    #  version是二维码的尺寸，数字大小决定二维码的密度       error_correction：是指误差
    # box_size:参数用来控制二维码的每个单元(box)格有多少像素点
    # border: 参数用控制每条边有多少个单元格(默认值是4，这是规格的最小值
    qr = qrcode.QRCode(version=5,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=8,
                       border=4,
                       )
    # 添加数据
    qr.add_data(text)
    # 生成二维码
    qr.make(fit=True)
    img = qr.make_image()
    img.show()

# 简单的生成二维码


def make_code_easy(text):
    image = qrcode.make(text)
    image.save(r"C:\Users\15639\Desktop\s.png")
    image.show()
    print("image already save: \15639\Desktops.png")


if __name__ == '__main__':
    text = input("请输入你想说的话:")
    make_code(text)
