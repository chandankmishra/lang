import os
from datetime import datetime

# to list all the os modules
# print (dir(os))

# to get the current working directory
print (os.getcwd())

directory = (os.path.join(os.environ.get('HOME'), 'git2/python/lang'))

# remove multiple directories
if os.path.isdir(directory):
    os.removedirs(directory)

# mkdir will create a direcdtory but makedirs will create all directories in the path
os.makedirs(directory)

# to change a directory
os.chdir(directory)

# create a file
open(os.path.join(directory, 'demo.txt'), 'w')

# list file a directory
print (os.listdir())

# rename the file
os.rename('demo.txt', 'test.txt')

# list file a directory
print (os.listdir())

# list the property of the file. st_mtime time modified, st_size size of the file
print (os.stat('test.txt'))

# print the modified time for the file
mod_time = os.stat('test.txt').st_mtime
print (datetime.fromtimestamp(mod_time))

# remove a file
if os.path.exists(directory):
    os.remove(directory + '/test.txt')

file_path = (os.path.join(os.environ.get('HOME'), 'git/python/lang'))

# change to new directory
os.chdir(file_path)

# to print the current working directory
print (os.getcwd())

# print envirnment variables
print (os.environ.get('HOME'))

# print
print (os.path.exists('/var/tmp/temp.txt'))
print (os.path.split('/var/tmp/temp.txt'))
print (os.path.splitext('/var/tmp/temp.txt'))

# to see all methods available in os.path module
print (dir(os.path))

# to list all the files and folder in a directory
# for dirpath, dirnames, filenames in os.walk('/Users/cmishra/git/'):
#     print ('Current path:', dirpath)
#     print ('Directories:', dirnames)
#     print ('Files:', filenames)
#     print()
