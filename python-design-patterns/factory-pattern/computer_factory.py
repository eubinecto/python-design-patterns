#  compare this with builder/computer_builder

class AppleFactory:
    class Computer:
        def __init__(self, model, cpu, memory, active_cooling):
            self.model = model
            self.cpu = cpu
            self.memory = memory
            self.active_cooling = active_cooling

        def __str__(self):
            return "\n".join([self.model,
                              self.cpu,
                              str(self.memory),
                              str(self.active_cooling)
                              ])

    class MacBookAirLate2020(Computer):
        def __init__(self):
            # In Factory class, everything is built pre-configured
            super().__init__('air', 'M1', 16, False)

    class MacBookProLate2020(Computer):
        def __init__(self):
            # In Factory class, everything is built pre-configured
            super().__init__('pro', 'M1', 16, True)

    def build_computer(self, model):
        if model == "air":
            return self.MacBookAirLate2020()
        elif model == "pro":
            return self.MacBookProLate2020()
        else:
            raise ValueError("AppleFactory does not build the given model")


# the snippet which uses the factory class
def main():
    # instantiate a factory.
    apple_factory = AppleFactory()
    # build a computer you want.
    # again, you don't get to choose the configuration, every configuration
    # is pre-configured within the classes
    air_2020 = apple_factory.build_computer("air")
    pro_2020 = apple_factory.build_computer("pro")
    print(air_2020)
    print("------")
    print(pro_2020)


if __name__ == '__main__':
    main()
