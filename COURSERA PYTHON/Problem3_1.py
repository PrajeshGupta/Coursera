def problem3_1(textfile):
    file=open(textfile)
    s=0
    for line in file:
        print(line,end="")
        s+=len(line)
    print("\n\nThere are",s,"letters in the file.")
    file.close()