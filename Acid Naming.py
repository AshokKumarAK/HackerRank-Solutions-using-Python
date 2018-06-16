def acidNaming(acid_name):
    l=len(acid_name)
    if acid_name[l-2:l]=="ic" and acid_name[0:5]=="hydro":
        print("non-metal acid")
    elif acid_name[l-2:l]=="ic":
        print("polyatomic acid")
    else:
        print("not an acid")

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)