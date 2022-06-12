import sys
from pathlib import Path
from typing import List


class FDGenerator:
    """ File and Directory Generator.
    """
    CURRENT_DIR: str = Path(__file__).resolve().parents[0]
    OUTPUT_DIR: str = f"{CURRENT_DIR}/output"

    def main(self):
        args: List = sys.argv
        if len(args) != 2:
            sys.exit(f"Invalid arguments.")

        option: str = args[1]
        if option not in ["file", "dir"]:
            sys.exit(f"[{option}] is invalid argument. How to use command: fd_generator.py [file | dir]")

        source_file: str = f"{self.CURRENT_DIR}/source.txt"
        if not Path(source_file).exists():
            sys.exit(f"Create source.txt on {self.CURRENT_DIR}, and write file or directory names you'd like to generate.")
        
        print(f"Creating {option} starts.")
        with open(source_file, "r") as r:
            for line in r:
                target: str = f"{self.OUTPUT_DIR}/{line}".strip()
                if option == "file":
                    target = target + ".txt"
                    with open(target , "w") as w:
                        w.write("")
                elif option == "dir":
                    Path(target).mkdir(parents=True, exist_ok=True)

        print(f"Creating {option} ends.")

if __name__ == "__main__":
    FDGenerator().main()
