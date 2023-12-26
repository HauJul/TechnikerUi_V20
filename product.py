import pandas as pd


class Product:
    def __init__(self):
        self.df_tool = pd.DataFrame
        self.df_product = pd.DataFrame
        self._artNo = 00000000
        self._name = ""
        self._steps = 0
        self.read_csv()

    # Read actual Product and Tool Data
    def read_csv(self):
        file = open("Lists/Produktliste.csv", 'r')
        self.df_product = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()
        file = open("Lists/Toolliste.csv", 'r')
        self.df_tool = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()

    # Set Article Number according to User Input
    def set_art_no(self, value):
        self._artNo = value

    def get_name(self):
        return self._name

    def get_steps(self):
        return self._steps

    # get Product Data when sselected Product changed
    def select_product(self, art_no):
        self.set_art_no(art_no)
        # If selected Article Number is in Product Data read values
        if self._artNo in self.df_product.index:
            self._name = self.df_product.at[self._artNo, "Bezeichnung"]
            self._steps = self.df_product.at[self._artNo, "Anzahl Schritte"]
            return True
        else:
            return False

    def get_cyc(self, step):
        return self.df_product.at[self._artNo, "S" + str(step) + "_Prog"]

    def get_toolno(self, step):
        return self.df_product.at[self._artNo, "S" + str(step) + "_Tool"]

    def get_toolname(self, step):
        toolno = self.df_product.at[self._artNo, "S" + str(step) + "_Tool"]

        return self.df_tool.at[toolno, "Tool"]
