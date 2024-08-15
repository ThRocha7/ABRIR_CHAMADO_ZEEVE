import requests
import json

url = ""

headers = {
  'Authorization': 'Bearer ',
}

data = {
  "flowId": 1854,
  "isSimulation": True,
  "formFields": [
    {
      "id": 0,
      "name": "grupo",
      "value": "Bild"
    },
    {
      "id": 0,
      "name": "cidade_ogvb",
      "value": "RIBEIRAO PRETO"
    },
    {
      "id": 0,
      "name": "origem",
      "value": "Corporativo"
    },
    {
      "id": 0,
      "name": "nDocumento",
      "value": "123"
    },
    {
      "id": 0,
      "name": "documentoECte",
      "value": "Não"
    },
    {
      "id": 0,
      "name": "nPedido",
      "value": ""
    },
    {
      "id": 0,
      "name": "cpfcnpjFornecedor",
      "value": ""
    },
    {
      "id": 0,
      "name": "empresabu2",
      "value": ""
    },
    {
      "id": 0,
      "name": "contaMaeBu",
      "value": "N/A"
    },
    {
      "id": 0,
      "name": "contaCorrenteBu",
      "value": "N/A"
    },
    {
      "id": 0,
      "name": "codigoFornecedor",
      "value": ""
    },
    {
      "id": 0,
      "name": "nome",
      "value": ""
    },
    {
      "id": 0,
      "name": "razaoSocial",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "metodoDePagamento",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "banco2",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "agencia2",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "contaBancaria",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "condicaoDePagamento",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "metodoParaEstePagamento",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "banco",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "agencia",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "codigoDeBarras",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "boleto",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "possuiOutrosPedidosPoRelacionadoAoPagamento",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "tipoNotaFiscal",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "notaFiscal",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "possuiJuros",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "valorTotal",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "pagamentoParcelado",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "dataDeEmissao",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "dataQueDesejaPagar",
      "value": "Valor que seria preenchido em tela"
    },
    {
      "id": 0,
      "name": "responsavelSolicitacaoDeEntregaSe",
      "value": "Valor que seria preenchido em tela"
    },
  ],
}

r = requests.post(url, headers=headers, json=data)

print(r.text)
