#_*_ coding:utf-8 _*_

name = u'中文'
print type(name)
print name

uft8_name = name.encode('utf-8')
print type(uft8_name)
print uft8_name

print type(uft8_name.decode('utf-8'))
