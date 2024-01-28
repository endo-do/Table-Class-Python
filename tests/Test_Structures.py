import sys
sys.path.insert(0, 'src')

from TerminalTable.Table import Table

T1 = Table([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
T1.display()

T1 = Table({1:["a", "b", "c"], 2:["d", "e", "f"], 3:["g", "h", "i"]})
T1.display()

T1 = Table([{1:"a", 2:"b", 3:"c"}, {1:"d", 2:"e", 3:"f"}, {1:"g", 2:"h", 3:"i"}])
T1.display()

T1 = Table({1:{1:"a", 2:"b", 3:"c"}, 2:{1:"d", 2:"e", 3:"f"}, 3:{1:"g", 2:"h", 3:"i"}})
T1.display()

T1.conf_header("row", "add", [1, 2, 3])
T1.display()

T1.conf_header("row", "replace", {1:1, 2:2, 3:3})
T1.display()