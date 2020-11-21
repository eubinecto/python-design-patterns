# What if you want to configure your computer yourself?
# (instead of buying a computer model, we want to configure
# the parts of the computer ourselves, and let our hardware engineer
# friend to build the computer from the parts.

class Computer:
    """
    this the object we want to build.
    """
    def __init__(self):
        # these are the parts of the computer to be built.
        self.model = None
        self.cpu = None
        self.memory = None
        self.active_cooling = None

    def __str__(self):
        return "\n".join([
         self.model,
         self.cpu,
         str(self.memory),
         str(self.active_cooling)
        ])


class ComputerBuilder:
    """
    this is the builder that builds the object that we want to build.
    a computer, in this case.
    """
    def __init__(self):
        # ComputerBuilder maintains a computer instance.
        self.computer = Computer()

    def config_model(self, model):
        self.computer.model = model

    def config_cpu(self, cpu):
        self.computer.cpu = cpu

    def config_memory(self, memory):
        self.computer.memory = memory

    def config_active_cooling(self, active_cooling):
        self.computer.active_cooling = active_cooling


class HardwareEngineer:
    """
    this is the director which will use the builder class to build the object
    that we want to build, given the specification by the user.
    """
    def __init__(self):
        # an engineer maintains a builder instance
        self.computer_builder = ComputerBuilder()

    # a director constructs a computer.
    def construct_computer(self, model, cpu, memory, active_cooling):
        # the builder instance configures parts of the computer,
        # **step-by-step**.
        self.computer_builder.config_model(model)
        self.computer_builder.config_cpu(cpu)
        self.computer_builder.config_memory(memory)
        self.computer_builder.config_active_cooling(active_cooling)

    # alias to the computer
    @property
    def computer(self):
        return self.computer_builder.computer


def main():
    # the end-user asks a hardware engineer to construct a computer.
    engineer = HardwareEngineer()
    engineer.construct_computer(model="dream computer", cpu="M100",
                                memory=128, active_cooling=True)
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    main()
