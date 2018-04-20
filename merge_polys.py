#! /usr/bin/python

def transcript_section(reader, num):
    line = reader.next() # read (and forget) section name
    num += 1
    print(num) # The new section name    
    while line and not line.startswith("END"):
        line = reader.next().rstrip() # read (and forget) section name
        print(line)
    return num
    

def transcript_sections(reader, num):
    line = reader.next() # read file header (the name of the multipolygon)
    while line and not line.startswith("END"):
        num = transcript_section(reader, num)
        line = reader.next() # read (and forget) section name
    return num


def merge_polys(filenames):
    num_sections = 0
    print("none")  # name of the multipolygon
    for filename in filenames:
        with open(filename) as f:
            num_sections = transcript_sections(f, num_sections)
    print("END")


if __name__ == "__main__":
    import sys 
    merge_polys(sys.argv[1:])
