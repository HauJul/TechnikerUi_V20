import pandas as pd


class Product:
    df = pd.read_csv("Lists/Produktliste_V03.csv", delimiter=";", index_col=0)

    def __init__(self):
        self._artNo = 00000000
        self._name = ""
        self._steps = 0

    def set_art_no(self, value):
        self._artNo = value

    def get_name(self):
        return self._name

    def get_steps(self):
        return self._steps

    def select_product(self, art_no):

        self.set_art_no(art_no)
        if self._artNo in self.df.index:
            self._name = self.df.at[self._artNo, "Bezeichnung"]
            self._steps = self.df.at[self._artNo, "Anzahl Schritte"]
            return True
        else:
            return False

    def get_cyc(self, step):
        return self.df.at[self._artNo, "S" + str(step) + "_Prog"]

    def get_toolno(self, step):
        return self.df.at[self._artNo, "S" + str(step) + "_Tool"]

    def get_toolname(self, step):
        toolno = self.df.at[self._artNo, "S" + str(step) + "_Tool"]

        dftool = pd.read_csv("Lists/Toolliste_V03.csv", delimiter=";", index_col=0)
        return dftool.at[toolno, "Tool"]