import sys
sys.path.insert(0, 'src')

from TerminalTable.Table import Table

PL_Teams = ["Liverpool","Man City","Arsenal","Aston Villa","Tottenham","West Ham","Brighton","ManUnited","Chelsea"]

League = Table([[i, 0] for i in PL_Teams])

League.display()

League.conf_header("row", "add", ["Team", "Points"])

League.conf_header("col", "add", ["#default"])

League.display()

League.swap_cols_rows()

League.conf_header("col", "remove")

League.display()