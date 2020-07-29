def no_dups(s):
    # Implement me.
    # s = s.rstrip()
    # if s == "":
    #     return s
    # ordered = set()
    # return [i.rstrip() for i in s if not(i in ordered or ordered.add(i))]
    if s == "":
        return s
    s = s.split()
    # j = ""
    j = "".join(s)
    if s == "":
        return s
    
    return [i for n,  i in enumerate(j) if i not in j[:n]]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))