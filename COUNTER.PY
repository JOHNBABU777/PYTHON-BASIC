class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def __str__(self):
        return str(self.value)

def main():
    counter = Counter(5)
    print("Initial value:", counter)

    print("\nIncrementing counter:")
    counter.increment()
    print("Counter value after increment:", counter)

    print("\nDecrementing counter:")
    counter.decrement()
    print("Counter value after decrement:", counter)

    print("\nIncrementing counter by 2:")
    counter += 2
    print("Counter value after increment:", counter)

    print("\nDecrementing counter by 1:")
    counter -= 1
    print("Counter value after decrement:", counter)

if __name__ == "__main__":
    main()