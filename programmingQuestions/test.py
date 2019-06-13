if __name__ == "__main__":
    import math

    def mathe(tup):
        if len(tup) > 2: 
            print("Length of tuple > 2")
        else:
            tot = sum(tup)
            diff = tup[1] - tup[0]
            multi = tup[0] * tup[1]
            div = tup[1] / tup[0]
            return(tot, diff, multi, div)

    ans = mathe((2,3))
    print(ans)


       
