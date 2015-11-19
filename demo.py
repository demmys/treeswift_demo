import subprocess
import time

class PseudoTerminal:
    def __init__(self, promptStr, printer):
        self.promptStr = promptStr
        self.printer = printer
        self.prompt()

    def prompt(self):
        self.printer(self.promptStr)

    def input(self, commands):
        for command in commands:
            for c in command:
                self.printer(c)
                time.sleep(0.05)
            self.printer(" ")
            time.sleep(0.2)
        time.sleep(0.7)
        self.printer("\n")

    def output(self, output):
        for line in output.splitlines(True):
            self.printer(line)
            time.sleep(0.2)
        self.prompt()

if __name__ == '__main__':
    subprocess.call("clear")
    terminal = PseudoTerminal("$ ", lambda s: print(s, end="", flush=True))
    sources = ["Fibonacci.swift", "TypeInference.swift"]
    while True:
        for source in sources:
            command = ["treeswift", "-dump-ast", source]
            terminal.input(command)
            ast_dump = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            terminal.output(ast_dump)
