### 建立自己的 module 和 package, 可讓程式更加模組化, 方便使用
'''
hello.print_helloworld()
'''
'''
from hello import print_helloworld as phw

phw()
'''

## 用 package 需先新增一個空白的 __init__.py 的文件, 讓系統知了面放了 module

from mypackage.awesome import print_awesome
from mypackage.happy import print_happy

print_awesome()
print_happy()