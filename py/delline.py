import os

s = '''
        111111:1
        222222:2

        '''

def del_lines(lines, name):
        intxt = open('public.xml') 
        outtxt = open('out.xml', 'w')
        for i, l in enumerate(intxt, 1):
                flag = 0
                for j in lines:
                        if j == i:
                                flag = 1
                                break
                if flag == 0:
                        outtxt.write(l)
                else:
                        outtxt.write("\n");
                        print ("del " + str(i) + " line")
        intxt.close()
        outtxt.close()
        #os.rename(filename + ".new", filename)
def get_del_line_nums():
        deltxt = open('del.txt')
        line_num = []
        for i, l in enumerate(deltxt, 1):
                #print l
                t = l.split(':')
                #print t[2]#line number
                line_num.append(int(t[2]))
        return line_num#reverse()#.sort()#reverse=True)
if __name__=='__main__':
	#del_line(10,"a")
        
        line_nums = get_del_line_nums()
        #print line_nums
        del_lines(line_nums, "")
