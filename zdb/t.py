from struct import Struct as Packer
a = '<' 
b = 'B'

str = Packer(a+b)
print 'length:', str.size
print str.format
StaticField.__init__(name, str.size)

