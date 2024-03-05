import requests
from datetime import datetime
from settings.settings import el_api_token, el_id_client

class ApiProtocolo:
    
    def __init__(self):
        self.requestHeader = {
            'Content-type': 'application/json',
            'Authorization': el_api_token
        }
        self.idPessoa = None
        self.idCliente = el_id_client
    
    def recuperarAssuntos(self):   
             
        self.requestURL = f"https://gpi18.cloud.el.com.br/integracaogpi/api/v2/assuntos"
        
        data = {
            'idCliente': self.idCliente 
        }
        
        response = requests.get(self.requestURL, json=data, headers=self.requestHeader)
        
        json_data=response.json()        
        return response.status_code , json_data
    
    def recuperarProcesso(self, idEcm):   
        from urllib.parse import quote
        self.requestURL = f"https://gpi18.cloud.el.com.br/integracaogpi/api/v2/ecm/visualizar/{quote(idEcm)}"
        
        response = requests.get(self.requestURL, headers=self.requestHeader)
        
        json_data=response.json()        
        return response.status_code , json_data
       
    def recuperarPessoa(self, numeroDocumentoJuridico):
        from urllib.parse import quote
        
        formatted_numeroDocumentoJuridico = "###.###.###-##".format(numeroDocumentoJuridico)
        self.requestURL = f"https://gpi18.cloud.el.com.br/integracaogpi/api/v2/ecm/recuperarPessoa?numeroDocumentoJuridico={quote(formatted_numeroDocumentoJuridico)}"
        
        response = requests.get(self.requestURL, headers=self.requestHeader)
        
        if response.status_code == 201:
            self.idPessoa = response.json()
            return 201, response.json()
        
        elif response.status_code == 500:
            return 500, response.json()
        
        
    def cadastrarProcesso(self, parametros):
        self.recuperarPessoa(parametros['numeroDocumentoJuridico'])
        
        if self.idPessoa is None:
            return
        
        data = {
            'idCliente': self.idCliente,
            "idEcmEspecie": "71BE766987394776A7D23D154AC720E6",
            "numeroProcesso": parametros['numeroProcesso'],
            "anoProcesso": parametros['anoProcesso'],
            # "dataProcesso":  datetime.strptime(parametros['dataProcesso'], '%Y-%m-%d').date().isoformat(),
            "dataProcesso":  parametros['dataProcesso'],
            "idEstruturaInteresse": "50798A6D6F92A7B57775311D284D396B",
            "idPessoaOrigem": self.idPessoa,
            "idPessoaContato": self.idPessoa,
            "idAssunto": "431203450F604EC7BC234A6E38031B8A",
            "resumoEcm": parametros['resumoEcm'],
            "idBoleanoSigiloso": "N",
            "idBoleanoPublico": "N",
            "idVisibilidade": "P",
            "idInternoExterno": "E",
            "idEcmEspecieTipo": 2,
            "idPessoaRequerente": self.idPessoa,
            "idPrioridade": "N"
        }

        self.requestURL = "https://gpi18.cloud.el.com.br/integracaogpi/api/v2/ecm/cadastrar-processo"
        
        response = requests.post(self.requestURL, json=data, headers=self.requestHeader)
        
        if response.status_code == 201:
            json_data = response.json()
            numeroECM = json_data[0]['numeroEcm']
            ids = parametros['numeroProcesso']
            dados = {
                'ids': ids,
                'num_ecm': numeroECM
            }
            return dados
        else:
            print('não foi')
            print(response.status_code)
            print(response.json())
    
    def cadastrarPessoa(self, parametros):
        self.recuperarPessoa(parametros['numeroDocumentoJuridico'])
        
        if self.idPessoa is None:
            return
        
        data = {
            "numeroDocumentoJuridico": parametros['numeroDocumentoJuridico'],
            "nomePessoa": self.nomePessoa,
            "tipoPessoa": self.tipoPessoa,
            "idCliente": self.idCliente,
        }

        self.requestURL = "https://gpi18.cloud.el.com.br/integracaogpi/api/pessoas/find-or-create"
        
        response = requests.post(self.requestURL, json=data, headers=self.requestHeader)
        
        if response.status_code == 201:
            return 201, response.json()

# Usage
# api = ApiProtocolo("4BC52BDB6AC0DBE08F922291CE6AF1C2")
# api = ApiProtocolo()

# parametros = {
#     'numeroDocumentoJuridico': '12345678900',
#     'numeroProcesso': '2023',
#     'anoProcesso': '2023',
#     'dataProcesso': '2023-08-04 16:24:04',
#     'resumoEcm': 'Testando API 2'
# }
# print(api.cadastrarProcesso(parametros))
# api.cadastrarPessoa(parametros)
