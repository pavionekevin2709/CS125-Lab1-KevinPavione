# week2_lab_oop_demo.py
# Kevin Pavione
# January 20, 2026
# Week 2 Lab - Advanced OOP

class Animal:
    """Base class representing any animal."""

    def __init__(self, name, species):
        """Initialize an animal with name and species."""
        self._name = name              # protected attribute
        self.__species = species       # private attribute (name mangling)
        self._energy = 100             # protected

    def get_name(self):
        """Return the animal's name."""
        return self._name

    def get_species(self):
        """Return the animal's species (public accessor)."""
        return self.__species

    def make_sound(self):
        """Return the default animal sound (to be overridden)."""
        return "Some generic animal sound"

    def eat(self):
        """Simulate eating and gaining energy."""
        self._energy += 20
        if self._energy > 100:
            self._energy = 100
        return f"{self._name} is eating... Energy now: {self._energy}%"

    def sleep(self):
        """Simulate sleeping and recovering energy."""
        self._energy += 30
        if self._energy > 100:
            self._energy = 100
        return f"{self._name} is sleeping... Energy now: {self._energy}%"

    def get_status(self):
        """Return current status of the animal."""
        return (f"{self._name} the {self.__species} "
                f"(energy: {self._energy}%)")


class Dog(Animal):
    """Dog class – inherits from Animal."""

    def __init__(self, name, breed, favorite_toy):
        """Initialize a dog with breed and favorite toy."""
        super().__init__(name, "Dog")
        self.breed = breed
        self._favorite_toy = favorite_toy  # protected

    def make_sound(self):
        """Override: Dogs bark."""
        return "Woof woof!"

    def play(self):
        """Play with favorite toy – consumes energy."""
        if self._energy >= 15:
            self._energy -= 15
            return (f"{self._name} is happily playing with "
                    f"the {self._favorite_toy}! Energy: {self._energy}%")
        return f"{self._name} is too tired to play right now."


class Cat(Animal):
    """Cat class – inherits from Animal."""

    def __init__(self, name, color):
        """Initialize a cat with color."""
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        """Override: Cats meow."""
        return "Meow~"

    def purr(self):
        """Purring increases happiness (represented by energy gain)."""
        self._energy += 10
        if self._energy > 100:
            self._energy = 100
        return f"{self._name} is purring happily. Energy: {self._energy}%"


class Puppy(Dog):
    """Puppy – multi-level inheritance example."""

    def __init__(self, name, breed, favorite_toy, age_in_months):
        """Initialize a puppy."""
        super().__init__(name, breed, favorite_toy)
        self.age_in_months = age_in_months

    def make_sound(self):
        """Override: Puppies have higher-pitched bark."""
        return "Yip yip yip!"

    def get_status(self):
        """Override: Include age in status."""
        base_status = super().get_status()
        return f"{base_status} – puppy ({self.age_in_months} months old)"


def demonstrate_polymorphism(animals):
    """Show polymorphism in action."""
    print("\n=== Polymorphism Demonstration ===")
    for animal in animals:
        print(f"{animal.get_name()}: {animal.make_sound()}")
        print(animal.get_status())
        print("-" * 40)


def main():
    """Main demonstration of all OOP concepts."""

    # Create instances
    rex = Dog("Rex", "Golden Retriever", "tennis ball")
    luna = Cat("Luna", "black & white")
    max = Puppy("Max", "Labrador", "chew rope", 4)

    # Collection for polymorphism demo
    zoo = [rex, luna, max]

    print("=== Individual Behaviors ===")
    print(rex.eat())
    print(rex.play())
    print(rex.make_sound())
    print()

    print(luna.sleep())
    print(luna.purr())
    print(luna.make_sound())
    print()

    print(max.play())
    print(max.make_sound())
    print()

    # Demonstrate encapsulation
    print("\n=== Encapsulation Examples ===")
    print(f"Accessing protected name: {rex.get_name()}")
    # print(rex.__species)  # This would raise AttributeError
    print(f"Accessing private species via getter: {rex.get_species()}")

    # Show polymorphism
    demonstrate_polymorphism(zoo)


if __name__ == "__main__":
    main()