#!/usr/bin/env python3
import os
# os.system("lscpu")
# print('\n')
# os.system("lsusb")
print('\n')
#os.system('ping baidu.com')
os.system('pwd')
# os.system('cd ../')
os.chdir('../')
# os.chdir('contiki-3.0/examples/rime/')
# os.system('make TARGET=sky distclean')
# os.system('make TARGET=cc2530dk distclean')
# # os.system('make TARGET=sky example-broadcast')
os.chdir('workspace/simple-gcc-stm32-project/')

# os.system('make')
# os.system('make update')
os.system('openocd -f interface/ftdi/open_jtag.cfg -f  target/stm32f1x.cfg')
# os.system('pwd')
