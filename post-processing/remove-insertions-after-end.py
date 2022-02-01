import sys

filename = sys.argv[1]

threshold=3

length_of_reference =  int(sys.argv[2])
#output_file = open(filename + '.corrected','w+')

found_non_empty_line=False
n=0

with open(filename) as f:
    lines = f.readlines()
    for i in range(1,len(lines)):
        cleanline = lines[i].rstrip()
        #if not cleanline=='0 0' and not cleanline=='1 0' and not cleanline=='0 1' and not cleanline=='2 0' and not cleanline=='0 2': found_non_empty_line=True
        found_non_empty_line=True

        if found_non_empty_line:
            n+=1
            if n<length_of_reference:
                fields = cleanline.split(' ')
                newline=''
                
                if int(fields[0])<threshold: newline='0 '
                else: newline=fields[0] + ' '

                if int(fields[1])<threshold: newline=newline + '0'
                else: newline=newline + fields[1]
                
                print(newline)
        
#output_file.flush()
#output_file.close()

num_lines_removed=len(lines) - length_of_reference
