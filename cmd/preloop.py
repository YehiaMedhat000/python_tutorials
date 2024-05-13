import cmd

class MyCmd(cmd.Cmd):
    def preloop(self):
        """Initialization tasks before entering the command loop."""
        print("Welcome to MyCmd. Type 'help' for available commands.")

    def do_hello(self, arg):
        """Say hello to the user."""
        print("Hello,", arg)

if __name__ == '__main__':
    cmd_instance = MyCmd()
    cmd_instance.cmdloop()

