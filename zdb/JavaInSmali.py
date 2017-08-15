import sys  
  

for arg in sys.argv:  
    print arg  
  
package_name = raw_input("input package (eg. a.b.b.c): ")

package_name_c = package_name.replace('.','/')


class_name = raw_input("input class : ")

#class_name_c = class_name.replace('.','/')

class_function_value = raw_input("input function name: ")

print 'L' + package_name_c + "/" + class_name + ";->"+class_function_value

raw_input("")