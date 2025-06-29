import qrcode  # 安装一个第三方库 pip install qrcode
img = qrcode.make('https://cloud.fynote.com/share/d/JoJTdLc5')
img.save('test.png')