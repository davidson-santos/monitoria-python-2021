#gui teste
from typing import List
import PySimpleGUI as ui
import os.path
import conexao_python_mysql as BD

assunto = {}
dificuldade = {}

def tela_inicio_menu():
    ui.theme('DarkAmber')
    layout = [
        [ui.Text("Menu inicial")],
        [ui.Button("Cadastrar Pergunta")],[ui.HorizontalSeparator()],
        [ui.Button("Cadastrar Assunto"),
            ui.Button("Deletar Assunto")]
    ]

    return ui.Window("Menu", layout,finalize=True)

def tela_cadastro_pergunta():
    ui.theme('DarkPurple')
    dificuldade.clear()
    assunto.clear()
    dificuldades = BD.executa_conculta("select * from dificuldade")
    assuntos = BD.executa_conculta("select * from assunto")
    for item in dificuldades:
        dificuldade[item[1]] = item[0]
    for item in assuntos:
        assunto[item[1]] = item[0]
    layout = [
        [ui.Text("Digite as informações da pergunta")],
        [ui.Text("Enunciado"), ui.Input(size=(20,4),key="Enunciado")],
        [ui.Text("Alternativa 1"), ui.Input(size=(20,1),key="Alternativa 1")],
        [ui.Text("Alternativa 2"), ui.Input(size=(20,1),key="Alternativa 2")],
        [ui.Text("Alternativa 3"), ui.Input(size=(20,1),key="Alternativa 3")],
        [ui.Text("Alternativa 4"), ui.Input(size=(20,1),key="Alternativa 4")],
        [ui.Text("Dificuldade"), ui.Combo(list(dificuldade.keys()), default_value="Selecione", size=(20, 1),key="Dificuldade")],
        [ui.Text("Assunto"), ui.Combo(sorted(assunto.keys()), default_value="Selecione", size=(20, 1),key="Assunto")],
        [ui.Button("Cadastrar",key=("OK-pergunta"))]
    ]
    return ui.Window("Cadastro", layout,finalize=True)

def tela_cadastro_assunto():
    ui.theme('DarkPurple')
    assunto.clear()
    assuntos = BD.executa_conculta("select nome from assunto")
    # for itens in assuntos:
    #     valor.append(itens)
    cad_column = [
        [ui.Text("Digite o novo assunto")],
        [ui.Text("Assunto"), ui.Input(size=(20,1), key="-cadAssunto-")],
        [ui.Button("Cadastrar",key=("OK-assunto"))]
    ]
    result_column = [
         [ui.Listbox(values=assuntos,size=(20,5))]
     ]
    
    layout = [[cad_column],[result_column]]
    return ui.Window("Cadastro", layout ,finalize=True)

def tela_deleta_assunto():
    assunto.clear()
    assuntos = BD.executa_conculta("select * from assunto")
    for item in assuntos:
        assunto[item[1]] = item[0]

    layout=[
        [ui.Text("Selecione o assunto a ser excluído")],
        [ui.Combo(sorted(assunto.keys()), default_value="Selecione", size=(20, 1),key="delAssunto")],
        [ui.Button("Excluir",key="OK-delAssunto")]
    ]

    return ui.Window("Deleta assuntos", layout ,finalize=True)

def deleta_assunto():
    try:
        BD.manipula_dados("delete from assunto where nome='%s'"%(values["delAssunto"]))
    except:
        ui.popup("Erro na exclusão!")

def cadastro_pergunta():
    if values["Enunciado"] and values["Alternativa 1"] and values["Alternativa 2"] and values["Alternativa 3"] and values["Alternativa 4"] != "":    
        BD.manipula_dados("insert into pergunta values (null, '%s','%s','%s','%s','%s',%d,%d)"
        %(values["Enunciado"],values["Alternativa 1"],values["Alternativa 2"],values["Alternativa 3"],
        values["Alternativa 4"],dificuldade[values["Dificuldade"]],assunto[values["Assunto"]]))
    else:
        ui.popup("Preencha todos os campos!")

def cadastro_assunto():
    if values["-cadAssunto-"] !="":
        selAssunto = BD.executa_conculta("select id from assunto where nome like '%s'"%(values["-cadAssunto-"]))
        print(selAssunto)
        if selAssunto==[]:
            BD.manipula_dados("insert into assunto values (null,'%s')" %(values["-cadAssunto-"]))
        else:
            ui.popup("Esse assunto já existe!")
    else:
        ui.popup("Resposta vazia inválida!")

def tela_erro():
    ui.popup_error()

# programa #
tela = tela_inicio_menu()
cadast = None

while True:
    window,events,values = ui.read_all_windows()
    if window == tela and events == ui.WIN_CLOSED:
        break
    elif window == cadast and events == ui.WIN_CLOSED:
        cadast.close()
    if events == "Cadastrar Pergunta":
        cadast = tela_cadastro_pergunta()
    elif events == "Cadastrar Assunto":
        cadast = tela_cadastro_assunto()
    elif events == "Deletar Assunto":
        cadast = tela_deleta_assunto()
    elif events == "OK-assunto":
        try:
            cadastro_assunto()
            cadast.close()
        except:
            ui.popup("Não foi possível cadastra o assunto!")
    elif events == "OK-pergunta":
        try:
            cadastro_pergunta()
            cadast.close()
        except:
            ui.popup("Não foi possível cadastra a pergunta!")
    elif events == "OK-delAssunto":
        try:
            deleta_assunto()
            cadast.close()
        except:
            tela_erro()

tela.close()