import pandas


class DBTools:
	def __init__(self):
		self.df = pandas.read_csv("data/Банки.csv")

	@property
	def csv(self):
		return self.df.to_csv()

	def bank_info(self, index: int):
		return self.df.loc[[index]]
