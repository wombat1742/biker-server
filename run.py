from subprocess import call
import sys
def main():
    call(["uv run fastapi", *sys.argv[1:]], shell=True)