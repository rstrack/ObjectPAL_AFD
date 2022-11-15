import yaml

def get_categorias() -> list[str]:
	try:
		with open("./src/config/categorias.yaml", "rt", encoding="utf8") as arquivo:
			modelo = yaml.safe_load(arquivo)
			return modelo["categorias"]
		
	except IOError:
		print('Não foi possível abrir o arquivo com as categorias.')