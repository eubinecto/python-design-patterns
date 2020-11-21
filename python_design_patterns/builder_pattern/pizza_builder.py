from enum import Enum, auto
import time
# all ingredients are laid out here, using Enum
from typing import Tuple, Optional, Dict, List
from termcolor import colored


# sub-classing enums to define constants
class PizzaProgress(Enum):
    # auto function assigns unique values to them
    # use this function when the exact values don't matter
    QUEUED = auto()
    PREPARATION = auto()
    BAKING = auto()
    READY = auto()


class PizzaDough(Enum):
    THIN = auto()
    THICK = auto()


class PizzaSauce(Enum):
    TOMATO = auto()
    CREME_FRAICHE = auto()


class PizzaTopping(Enum):
    MOZZARELLA = auto()
    DOUBLE_MOZZARELLA = auto()
    BACON = auto()
    HAM = auto()
    OREGANO = auto()


# delay for each step. to be used with time.sleep().
STEP_DELAY = 3


# This is the object we want to build
class Pizza:
    def __init__(self, kind: str):
        self.kind: str = kind
        self.dough: Optional[PizzaDough] = None
        self.sauce: Optional[PizzaSauce] = None
        self.toppings: List[PizzaTopping] = []

    def __str__(self):
        return self.kind

    # the end product is typically minimal,
    # but that does not mean you should not assign any
    # responsibility to it.
    # here, prepare_dough is assigned to Pizza instead of the builders
    # to promote code reuse through composition.
    def prepare_dough(self, dough: PizzaDough):
        global STEP_DELAY
        self.dough = dough
        print("preparing the {} dough of your {}..."
              .format(dough.name, self.kind))
        time.sleep(STEP_DELAY)
        print("done with preparing the dough")


# superclass for all builders
class PizzaBuilder:
    def __init__(self, kind: str):
        # pizza builder maintains a pizza.
        self.pizza: Pizza = Pizza(kind)
        self.progress: Optional[PizzaProgress] = None

    def prepare_dough(self):
        raise NotImplementedError

    def add_sauce(self):
        raise NotImplementedError

    def add_topping(self):
        raise NotImplementedError

    def bake(self):
        raise NotImplementedError


# This is the builder to be used for constructing a margarita pizza
class MargaritaBuilder(PizzaBuilder):
    # ingredients defined for building margaritaBuilder
    KIND: str = 'margarita'
    DOUGH: PizzaDough = PizzaDough.THIN
    SAUCE: PizzaSauce = PizzaSauce.TOMATO
    TOPPINGS: List[PizzaTopping] = [PizzaTopping.DOUBLE_MOZZARELLA, PizzaTopping.OREGANO]
    BAKING_TIME: int = 5  # 5 seconds for baking Margarita

    def __init__(self):
        super(MargaritaBuilder, self).__init__(self.KIND)
        self.progress = PizzaProgress.QUEUED

    def prepare_dough(self):
        # update the status
        self.progress = PizzaProgress.PREPARATION
        self.pizza.prepare_dough(dough=self.DOUGH)

    def add_sauce(self):
        global STEP_DELAY
        # add sauce to the pizza
        print("adding {} sauce to the pizza...".format(self.SAUCE))
        self.pizza.sauce = self.SAUCE
        time.sleep(STEP_DELAY)
        print("done adding the sauce.")

    def add_topping(self):
        global STEP_DELAY
        toppings_desc = "|".join((topping.name for topping in self.TOPPINGS))
        print("adding {} toppings to the pizza..."
              .format(toppings_desc))
        for topping in self.TOPPINGS:
            self.pizza.toppings.append(topping)
        time.sleep(STEP_DELAY)
        print("adding toppings done.")

    def bake(self):
        # update the status
        print("baking your Margarita for {} seconds...".format(self.BAKING_TIME))
        self.progress = PizzaProgress.BAKING
        time.sleep(self.BAKING_TIME)
        # the pizza is now ready
        self.progress = PizzaProgress.READY
        print("Your Margarita is ready.")


# This is the builder to be used for constructing a creamy bacon pizza
class CreamyBaconBuilder(PizzaBuilder):
    KIND: str = "creamy bacon"
    DOUGH: PizzaDough = PizzaDough.THICK
    SAUCE: PizzaSauce = PizzaSauce.CREME_FRAICHE
    TOPPINGS: List[PizzaTopping] = [
        PizzaTopping.MOZZARELLA,
        PizzaTopping.BACON,
        PizzaTopping.OREGANO
    ]
    BAKING_TIME: int = 7

    def __init__(self):
        super(CreamyBaconBuilder, self).__init__(self.KIND)
        self.progress = PizzaProgress.QUEUED

    def prepare_dough(self):
        # update the status
        self.progress = PizzaProgress.PREPARATION
        self.pizza.prepare_dough(dough=self.DOUGH)

    def add_sauce(self):
        global STEP_DELAY
        # add sauce to the pizza
        print("adding {} sauce to the pizza...".format(self.SAUCE.name))
        self.pizza.sauce = self.SAUCE
        time.sleep(STEP_DELAY)
        print("done adding the sauce.")

    def add_topping(self):
        global STEP_DELAY
        toppings_desc = "|".join((topping.name for topping in self.TOPPINGS))
        print("adding {} toppings to the pizza..."
              .format(toppings_desc))
        for topping in self.TOPPINGS:
            self.pizza.toppings.append(topping)
        time.sleep(STEP_DELAY)
        print("adding toppings done.")

    def bake(self):
        # update the status
        print("baking your {} for {} seconds...".format(self.KIND, self.BAKING_TIME))
        self.progress = PizzaProgress.BAKING
        time.sleep(self.BAKING_TIME)
        # the pizza is now ready
        self.progress = PizzaProgress.READY
        print("Your {} is ready.".format(self.KIND))


# if you want to add another pizza, define a new class, or subclass existing builders.
class NewPizzaBuilder(PizzaBuilder):
    def prepare_dough(self):
        pass

    def add_sauce(self):
        pass

    def add_topping(self):
        pass

    def bake(self):
        pass


# The waiter is the director which will use given builders to construct pizzas
# as ordered, step by step.
class Waiter:

    def __init__(self):
        # the waiter maintains a pizza builder.
        # this could be Margarita builder or CreamyBacon, depending on
        # the order at stake.
        self.pizza_builder: Optional[PizzaBuilder] = None

    # director should have a construct_...() function
    # in this case, the waiter constructs a pizza, with the given builder.
    def construct_pizza(self, pizza_builder: PizzaBuilder):
        # first, we save the pizza_builder as an instance variable
        self.pizza_builder = pizza_builder
        # constructs  a pizza, step-by-step. The order of construction matters.
        steps = [
            self.pizza_builder.prepare_dough,
            self.pizza_builder.add_sauce,
            self.pizza_builder.add_topping,
            self.pizza_builder.bake
        ]
        # execute the steps
        for step in steps:
            # remember, functions are objects in python.
            step()

    # shortcut to the pizza
    @property
    def pizza(self) -> Pizza:
        return self.pizza_builder.pizza


# a function to validate user's input
# checks if we serve such a pizza.
def validate_order(builders: Dict[str, PizzaBuilder]) -> Tuple[bool, Optional[PizzaBuilder]]:
    in_msg = "What pizza would you like? [m]agarita or [c]reamy bacon?:"
    order = input(in_msg)
    pizza_builder = builders.get(order, None)
    # we don't serve such order
    if not pizza_builder:
        return False, None
    return True, pizza_builder


def main():
    # instantiate available builders
    pizza_builders = dict(
        m=MargaritaBuilder(),
        c=CreamyBaconBuilder()
    )
    # get an order from the end user.
    # check if we are available to get such an order.
    input_is_valid = False
    # init a pizza builder variable
    pizza_builder = None
    while not input_is_valid:
        input_is_valid, pizza_builder = validate_order(builders=pizza_builders)
    else:
        # instantiate a director
        waiter = Waiter()
        # ask the director to construct pizza with the given builder
        waiter.construct_pizza(pizza_builder)
        # get the pizza
        print("here is your order!: " + colored(waiter.pizza, 'blue'))


if __name__ == '__main__':
    main()
