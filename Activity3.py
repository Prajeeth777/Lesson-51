outputfile=open("MichaelJordan.txt","w")
inputfile=open("KobeBryant.txt","r")
lines_seen_so_far=set()
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)

inputfile.close()
outputfile.close()
