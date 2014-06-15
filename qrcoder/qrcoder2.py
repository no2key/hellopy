"""暂存到内存，然后写入文件

"""

import qrcode
import io

img = qrcode.make('hello world')
code = io.BytesIO()
img.save(code)

with open('a.png', 'wb') as f:
    f.write(code.getvalue())

code.close()
