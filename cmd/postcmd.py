import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, arg):
        """Say hello to the user."""
        print("Hello,", arg)

    def postcmd(self, stop, line):
        """Print a message after command execution."""
        print("Command execution finished.")
        return stop

if __name__ == '__main__':
    cmd_instance = MyCmd()
    cmd_instance.cmdloop()

