import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, arg):
        """Say hello to the user."""
        print("Hello,", arg)

    def do_exit(self, arg):
        """Exit the program."""
        print("Exiting...")
        return True  # Exit the cmdloop

if __name__ == '__main__':
    cmd_instance = MyCmd()
    cmd_instance.onecmd("hello Yehia Medhat")
