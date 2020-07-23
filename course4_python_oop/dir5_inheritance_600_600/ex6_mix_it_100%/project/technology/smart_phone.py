from project.technology.technology import Technology


class SmartPhone(Technology):
    def install_apps(self, app, app_memory):
        memory_left = self.get_capacity(self.memory, self.memory_taken + app_memory)
        if memory_left != 'Capacity reached!':
            self.memory_taken += app_memory
            return memory_left
        return f"You don't have enough space for {app}!"
