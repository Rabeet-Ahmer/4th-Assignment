import time 

def countdown(t: int):
    while t:
        mins, sec = divmod(t, 60)
        timer = f"{mins:02d}:{sec:02d}"
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    
    print("Time's up!")

def main():
    try:
        t = int(input("Enter the time in seconds for countdown: "))
        if t < 0:
            raise ValueError("Time cannot be negative.")
        countdown(t)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
