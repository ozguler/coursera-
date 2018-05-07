import string

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    line1 = list(line1)
    line2 = list(line2)
    length_l1 = len(line1)
    length_l2 = len(line2)
    #print (line1)
    #print (line2)
    length_l = min(length_l1,length_l2)

    for i in range(0,length_l):
        if line1[i] == line2[i]:
            # print ("Match", line1[i])
            pass
        elif line1[i] != line2[i]:
            return i
    if length_l1 == length_l2:
        return "IDENTICAL"
    else:
        return length_l

def singleline_diff_format(line1, line2, x):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    # print x
    # print(line1)
    # print(line2)
    # print(len(line1))
    # print(len(line2))
    # if line1.find("\n") & line2.find("\n"):
    #     print("ok")
    #     return ""
    if (min(len(line1),len(line2)) >=x & x>=0):
        print ("pass")
        print(line1[:x+1])
        print("="*x + "^")
        print(line2[:x+1])
    else:
        return ""

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    line_list1 = lines1
    line_list2 = lines2
    # line_list1 = lines1.split("\n")
    # line_list2 = lines2.split("\n")
    print(line_list1)
    print(line_list2)
    length_line_list1 = len(line_list1)
    length_line_list2 = len(line_list2)
    length_line_list = min(length_line_list1,length_line_list2)
    # print(length_line_list1)
    # print(length_line_list2)
    # print(length_line_list)
    if length_line_list1 > length_line_list2:
        x = line_list1
        y = line_list2
        line_list1 = y
        line_list2 = x
    else:
        pass

    for i in range(0,length_line_list):
        print (length_line_list)
        print (i)
#       print(singleline_diff(line_list1[i],line_list2[i]))
        ff = singleline_diff(line_list1[i],line_list2[i])
        if ff == "IDENTICAL":
            pass
        else:
            return(i, ff )

    return ("IDENTICAL", "IDENTICAL")

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    filexx = open(filename,"rt")
    x = []
    for line in filexx:
        line_nw = line.replace("\n","")
        x.append(line_nw)
    filexx.close()
    # print (x)
    return x
    # print x

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    ll1 = get_file_lines(filename1)
    print (ll1)
    ll2 = get_file_lines(filename2)
    print (ll2)

    a,b = (multiline_diff(ll1,ll2))
    singleline_diff_format(ll1[a],ll2[a],b)

    return ""

#sdfsdfsdfsdfsd


#file_diff_format("/Users/ozguler/Downloads/xx","/Users/ozguler/Downloads/xy")

#get_file_lines("/Users/ozguler/Downloads/xx")

# line1 = "xxxxyyyzi"
# line2 = "xxxxyyyyw"
#
# x = (singleline_diff(line1,line2))
# #print (x)
# singleline_diff_format(line1,line2,x)

#testing function 3
# s1 = """ this is a very
# long string xf I had the
# energy to type more and more ..."""
#
# s2   = """ this is a very
# long string if I had the
# energy to type more and more ...
# xxxxxxxxxxxxxx"""
#
# print(multiline_diff(s1,s2))
