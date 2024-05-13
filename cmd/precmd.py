import cmd

class MyCmd(cmd.Cmd):
    def precmd(self, line):
        """Modify the command line before execution."""
        return line.upper()  # Convert the command to uppercase

    def do_hello(self, arg):
        """Say hello to the user."""
        print("Hello,", arg)

if __name__ == '__main__':
    cmd_instance = MyCmd()
    cmd_instance.cmdloop()

