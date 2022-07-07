def median(lst):
    return sorted(lst)[len(lst)//2] if len(lst) %2!=0 else (sorted(lst)[len(lst)//2-1]+sorted(lst)[len(lst)//2])/2

def main():
    print(median([1,2,3,4]))
    
if __name__ == "__main__":
    main()
    