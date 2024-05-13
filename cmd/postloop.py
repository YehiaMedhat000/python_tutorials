import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, arg):
        """Say hello to the user."""
        print("Hello,", arg)

    def postloop(self):
        """Cleanup tasks after exiting the command loop."""
        print("Exiting MyCmd. Goodbye!")

if __name__ == '__main__':
    cmd_instance = MyCmd()
    cmd_instance.cmdloop()

