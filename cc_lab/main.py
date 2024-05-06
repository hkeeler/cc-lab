from time import gmtime, strftime

def get_time() -> str:
    """
    Get the current time
    """
    strftime("%Y-%m-%d %H:%M:%S", gmtime())

def main():
    now = get_time()
    print(f"Hello World @ {now}!")

if __name__ == "__main__":
    main()
    
