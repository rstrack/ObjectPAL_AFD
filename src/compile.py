import yaml

from Estado import Estado
from Transicao import Transicao
from AFD import AFD

def compile_afd() -> AFD:
	inicial: Estado = None
	finais: list[Estado] = []
	estados: list[Estado] = []
	
	try:
		with open("./src/config/afd.yaml", "rt", encoding="utf8") as arquivo:
			modelo = yaml.safe_load(arquivo)
						
			for item in modelo["estados"]:
				_estado = Estado(item)
				if modelo["inicial"] == item:
					inicial = _estado
				estados.append(_estado)
			
			for item in modelo["finais"]:
				finais.append(Estado(item))

			for item in modelo["transicoes"]:	
				_origem = None
				_destino = None
					
				for _estado in estados:
					if _estado.id == item["origem"]:
						_origem = _estado

					if _estado.id == item["destino"]:
						_destino = _estado
					
					if _origem != None and _destino != None:
						Transicao(
							estado_origem=_origem,
							simbolos=item["simbolos"],
							estado_destino=_destino
						)
						_origem = None
						_destino = None

			return AFD(inicial, estados, finais)

	except IOError:
		print('Não foi possível abrir o arquivo de modelo do ADF.')

    