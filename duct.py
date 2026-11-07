class CSVExporter :
	def Export(self,data):
		print("CSV")
		print(data)

class JsonExporter :
	def Export(self,data):
		print("Json")
		print(data)

def export_data(exporter,data):
	exporter.Export(data)

st = ["a","b","c"]

csv = CSVExporter()
json = JsonExporter()

export_data(csv,st)
export_data(json,st)


