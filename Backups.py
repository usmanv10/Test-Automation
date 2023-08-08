import os, shutil
import time

# Remove everything within the directory     shutil.rmtree('C:/Users/usman.ali/OneDrive/Pycharm/Pytests')

try:
    shutil.rmtree('C:/Users/usman.ali/OneDrive/Pycharm/TestFramework')
except:
    pass

time.sleep(20)
print('Previous folder deleted')


# Copies everything in the directory
shutil.copytree('C:/Users/usman.ali/PycharmProjects/TestFramework', 'C:/Users/usman.ali/OneDrive/Pycharm/TestFramework')

print ('New Folder created')
