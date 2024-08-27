from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep
import resources

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

driver.get(resources.url)

def click_element(element:str):
    try:
        e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        e.click()
    except:
        print('tentando encontrar de novo')
        sleep(3)
        try:
            e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
            e.click()
        except:
            print('não encontrei')
            driver.quit()


def write_element(element:str, text:str):
    try:
        e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        e.send_keys(text)
    except:
        print('tentando encontrar de novo')
        sleep(3)
        try:
            e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
            e.send_keys(text)
        except:
            print('não encontrei')
            driver.quit()


def write_enter_element(element:str, text:str):
    try:
        e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        e.send_keys(text)
        sleep(2)
        e.send_keys(Keys.ENTER)
    except:
        print('tentando encontrar de novo')
        sleep(3)
        try:
            e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
            e.send_keys(text)
            sleep(2)
            e.send_keys(Keys.ENTER)
        except:
            print('não encontrei')
            driver.quit()


def select_menu_element(element:str, text:str):
    try:
        e = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element))))
        e.select_by_value(text)
    except:
        print('tentando encontrar de novo')
        sleep(3)
        try:
            e = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element))))
            e.select_by_value(text)
        except:
            print('não encontrei')
            driver.quit()

resources.direct = input('Caminho... ')
# resources.funcionamento = input('Qual o tipo de doc... ')

inicar_apps = '//*[@id="aSideMenuNewRequest"]'
click_element(inicar_apps)

pesquisar_chamado = '//*[@id="txtSearch"]'
write_enter_element(pesquisar_chamado, 'Realizar Pagamento | Oracle')

chamado = '//*[@id="containerRequests"]/div[1]/div/div'
chamado_certo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, chamado))).text

if 'Realizar Pagamento | Oracle' in chamado_certo:
    btn_solicitar = '//*[@id="btnRequest-31221fa2-e652-48f3-887d-1d1384b2ca20"]'
    click_element(btn_solicitar)
else:
    print('chamado errado')
    driver.quit()

sleep(18)

df = pd.read_excel('planilha_padrao_julius.xlsx')

for row in df.index:

    dados = {
    'grupo': str(df.loc[row, 'grupo']),
    'fornecedor': str(df.loc[row, 'fornecedor']),
    'pedido': str(df.loc[row,'po']),
    'cnpj': str(df.loc[row, 'cnpj']),
    'num_nf': str(df.loc[row,'num_doc']),
    'banco': str(df.loc[row,'banco']),
    'agencia': str(df.loc[row,'agencia']),
    'cod_barras': str(df.loc[row,'digitavel']),
    'nome_bol': str(df.loc[row, 'nome_boleto']),
    'nome_nf': str(df.loc[row, 'nome_nf']),
    'valor': str(df.loc[row, 'valor']),
    'emissao': str(df.loc[row, 'emissao']),
    'data_pgmt': str(df.loc[row, 'data_pagamento']),
    'responsavel': str(df.loc[row, 'responsavel']),
    }
                
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="dynmodal"]/div/div/iframe'))

    grupo_xpath = '//*[@id="inpgrupo"]'
    select_menu_element(grupo_xpath, dados['grupo'])

    regional_xpath = '//*[@id="inpcidade_ogvb"]'
    select_menu_element(regional_xpath, 'RIBEIRAO PRETO')

    origem_xpath = '//*[@id="inporigem"]'
    select_menu_element(origem_xpath, 'Corporativo')

    num_nf_xpath = '//*[@id="inpnDocumento"]'
    write_element(num_nf_xpath, dados['num_nf'])

    npedido_xpath = '//*[@id="inpnPedido"]'
    write_element(npedido_xpath, dados['pedido'])

    cnpj_xpath = '//*[@id="inpcpfcnpjFornecedor"]'
    write_element(cnpj_xpath, dados['cnpj'])

    pesquisar_cnpj_xpath = '//*[@id="td1cpfcnpjFornecedor"]/div/div/button'
    click_element(pesquisar_cnpj_xpath)

    sleep(6)

    metodo_xpath = '//*[@id="inpmetodoParaEstePagamento"]'
    select_menu_element(metodo_xpath, 'BR_BOLETO')

    banco_xpath = '//*[@id="inpbanco"]'
    write_enter_element(banco_xpath, dados['banco'])

    num_agencia_xpath = '//*[@id="inpagencia"]'
    agencia = resources.formatar_agencia(dados['agencia'])
    write_enter_element(num_agencia_xpath, agencia)

    cod_barras_xpath = '//*[@id="inpcodigoDeBarras"]'
    write_element(cod_barras_xpath, dados['cod_barras'])

    boleto_btn_xpaht = '//*[@id="btnUploadboleto"]'
    click_element(boleto_btn_xpaht)

    sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="dynmodal"]/div/div/iframe'))

    carregar_boleto_xpath = '//*[@id="fileupload"]/div[1]/div/div[2]'
    click_element(carregar_boleto_xpath)

    sleep(3)

    validado_bol = resources.procurar_pdf(dados['nome_bol'], dados['fornecedor'], resources.direct)

    if validado_bol:
        sleep(3)

        iniciar_upload_bol_xpath = '//*[@id="frm"]/div[5]/div[3]/button[2]'
        click_element(iniciar_upload_bol_xpath)
        
        driver.switch_to.parent_frame()

        sleep(3)

        outra_po_xpath = '//*[@id="inppossuiOutrosPedidosPoRelacionadoAoPagamento"]'
        select_menu_element(outra_po_xpath, 'Não')

        tipo_nf_xpath = '//*[@id="inptipoNotaFiscal"]'
        select_menu_element(tipo_nf_xpath, 'Serviço')

        tipo_nao_fiscal_xpath = '//*[@id="inptipoDocumentoNaoFiscal"]'
        select_menu_element(tipo_nao_fiscal_xpath, resources.funcionamento)

        nf_btn_xpath = '//*[@id="btnUploadnotaFiscal"]'
        click_element(nf_btn_xpath)

        sleep(3)

        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="dynmodal"]/div/div/iframe'))

        carregar_nf_xpath = '//*[@id="fileupload"]/div[1]/div'
        click_element(carregar_nf_xpath)

        sleep(3)    

        validado_nf = resources.procurar_pdf(dados['nome_nf'], dados['fornecedor'], resources.direct)

        if validado_nf:
            sleep(3)

            iniciar_upload_nf_xpath = '//*[@id="frm"]/div[5]/div[3]/button[2]'
            click_element(iniciar_upload_nf_xpath)

            sleep(3)

            driver.switch_to.parent_frame()

            juros_xpath = '//*[@id="inppossuiJuros"]'
            select_menu_element(juros_xpath, 'Não')

            valor_doc_xpath = '//*[@id="inpvalorTotal"]'
            valor = dados['valor'].replace('.', ',')
            click_element(valor_doc_xpath)
            sleep(1)
            write_enter_element(valor_doc_xpath, valor)

            pgmt_parcelado_xpath = '//*[@id="inppagamentoParcelado"]'
            select_menu_element(pgmt_parcelado_xpath, 'Não')

            emissao_xpath = '//*[@id="inpdataDeEmissao"]'
            write_enter_element(emissao_xpath, dados['emissao'])

            data_vencimento_xpath = '//*[@id="inpdataVencimento2"]'
            write_enter_element(data_vencimento_xpath, dados['data_pgmt'])

            data_pgmt_xpath = '//*[@id="inpdataQueDesejaPagar"]'
            write_enter_element(data_pgmt_xpath, dados['data_pgmt'])

            responsavel_xpath = '//*[@id="inpresponsavelSolicitacaoDeEntregaSe"]'
            write_enter_element(responsavel_xpath, dados['responsavel'])

            qual_funcao_xpath = '//*[@id="buttons"]/div[2]/select'
            funcao = driver.find_element(By.XPATH, qual_funcao_xpath).clear()
            select_menu_element(qual_funcao_xpath, '1150;2891')

            finalizar_xpath = '//*[@id="BtnSend"]'
            click_element(finalizar_xpath)

            driver.switch_to.default_content()

            sleep(10)

            reiniciar_chamado = '//*[@id="containerRequests"]/div[1]/div/div'
            chamado2_certo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, chamado))).text

            if 'Realizar Pagamento | Oracle' in chamado2_certo:
                btn2_solicitar = '//*[@id="btnRequest-31221fa2-e652-48f3-887d-1d1384b2ca20"]'
                click_element(btn_solicitar)
                sleep(18)
            else:
                print('chamado errado')
                driver.quit()
                break
            
        else: 
            print('não achei o arq')
            driver.quit()
            break

    else: 
        print('não achei o arq')
        driver.quit()
        break