# temporary files are generally used to store data
# temporarily while your program is running. After that 
# it has no meaning. temporary files are stored in temp
# folder of the windows

# python provides a handy module for creating temporary
# files and folders called tempfile. Tempfile handles
# the deletion of the temporary files when your program
# is done with them.

# Creating temporary files

from tempfile import TemporaryFile   

tp = TemporaryFile('r+t', delete = False)
tp.write('hello world')

tp.seek(0)
data = tp.read()

tp.close()

print(data)