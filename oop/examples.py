def class_example():
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")

if __name__ == "__main__":
    class_example()