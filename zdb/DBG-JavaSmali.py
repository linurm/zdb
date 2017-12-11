import sys  
  

for arg in sys.argv:  
    print arg  
    
while(True):

    in_str = raw_input('input java or smali func   ')
    n = '0'
    m = '0'
    if in_str.find(';->') != -1:
        if in_str.find('L') != -1:
            if in_str.find('/') != -1:
                n = '2'
                if in_str.find('(') != -1:
                    m = '0'
                else:
                    m = '1'
    else:
        if in_str.find('.') != -1:
            n = '1'
            if in_str.find('(') != -1:
                m = '0'
            else:
                m = '1'
                
        
    #Lcom/jhss/youguu/util/ck;->bg:
    print n

    if n == '1':
        
        package_name = in_str#raw_input("input func (eg. a.b.b.c(...) ): ")


        package_name_c = package_name.replace('.','/')

        index = package_name_c.rfind('/')

        class_function_value = package_name_c[index + 1:]
        
        if m == '1':
            class_function_value += ':'

        class_name = package_name_c[:index]

        index = class_name.rfind('/')

        package_name_c = class_name[:index]

        class_name = class_name[index + 1:]

        print ''
        print 'L' + package_name_c + "/" + class_name + ";->"+class_function_value
        print ''
        print ''
        print 'package ' + package_name_c.replace('/','.') + ";        " + class_name + ".java"
        print ''
        #raw_input("")
    elif n == '2':
        smali_name = in_str#raw_input("input package (eg. Lcom/a/b/c/d/e;->z()Ljava/lang/String; ")
        index = smali_name.rfind('-')
        func_name = smali_name[index+2:]
        smali_name = smali_name[:index]
        print ''
        print ''
        #print "search: "
        print ".class public " + smali_name + '         in        ' + smali_name[smali_name.rfind('/')+1:-1] + ".smali"
        #print "ctrl-F:" 
        print ''
        print func_name
        print ''

        smali_name = smali_name[1:]

        package_name_c = smali_name.replace('/','.')

        index = package_name_c.rfind('.')

        class_name = package_name_c[index + 1:-1]

        package_name_c = package_name_c[:index]

        print ''
        print 'package ' + package_name_c.replace('/','.') + ";" + '         in        ' + class_name + ".java"
        print ''
        #raw_input("")
        
    elif n == '3':
        package_name = raw_input("input package (eg. a.b.b.c): ")

        package_name_c = package_name.replace('.','/')


        class_name = raw_input("input class : ")

        #class_name_c = class_name.replace('.','/')

        class_function_value = raw_input("input function name: ")

        print 'L' + package_name_c + "/" + class_name + ";->"+class_function_value
        
        #raw_input("")
        
    else:
        break