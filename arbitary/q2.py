def LengthOfString(*words):
    length = len(words)
    i = 0
    while i<length:
        print(f"Length of a given words  {words[i]} is {len(words[i])}")
        i=i+1

LengthOfString('amruta','dharmi','parth','pritesh')