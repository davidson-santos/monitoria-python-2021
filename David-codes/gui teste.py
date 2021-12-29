#gui teste
import PySimpleGUI as ui
import os.path
import conexao_python_mysql as BD

def inicio_menu():
    ui.theme('DarkAmber')
    layout = [
        [ui.Text("Menu inicial")],
        [ui.Button("Cadastrar Pergunta"),
            ui.Button("Cadastrar Assunto")]
    ]

    return ui.Window("Menu", layout,finalize=True)

def cadastro_pergunta():
    ui.theme('DarkPurple')
    assuntos = consulta_assuntos()
    layout = [
        [ui.Text("Digite as informações da pergunta")],
        [ui.Text("Enunciado"), ui.Input(size=(20,4),key="Enunciado")],
        [ui.Text("Alternativa 1"), ui.Input(size=(20,1),key="Alternativa 1")],
        [ui.Text("Alternativa 2"), ui.Input(size=(20,1),key="Alternativa 2")],
        [ui.Text("Alternativa 3"), ui.Input(size=(20,1),key="Alternativa 3")],
        [ui.Text("Alternativa 4"), ui.Input(size=(20,1),key="Alternativa 4")],
        [ui.Text("Dificuldade"), ui.Input(size=(1,1),key="Dificuldade")],
        [ui.Text("Assunto"),ui.Combo([x[1] for x in assuntos],default_value=assuntos[0][1],key="Assunto")],
        [ui.Button("Cadastrar",key=("OK-pergunta"))]
    ]
    return ui.Window("Cadastro", layout,finalize=True)

def cadastro_assunto():
    ui.theme('DarkPurple')
    valor = consulta_assuntos()
    cad_column = [
        [ui.Text("Digite o novo assunto")],
        [ui.Text("Assunto"), ui.Input(size=(20,1), key="-cadastroA-")],
        [ui.Button("Cadastrar",key=("OK-assunto"))]
    ]
    result_column = [
        [ui.Listbox(values=valor,size=(20,20))]
    ]
    
    layout = [[cad_column],
        [ui.VSeparator()],
        [result_column]
    ]
    return ui.Window("Cadastro", layout ,finalize=True)

def consulta_assuntos() -> list:
    assuntos = []
    assuntos = BD.executa_conculta("select * from assunto")   
    valor = []
    for itens in assuntos:
        valor.append(itens)
    return valor

# programa #
tela = inicio_menu()
cadast = None

while True:
    window,events,values = ui.read_all_windows()
    if window == tela and events == ui.WIN_CLOSED:
        break
    elif window == cadast and events == ui.WIN_CLOSED:
        cadast.close()
    if events == "Cadastrar Pergunta":
        cadast = cadastro_pergunta()
    elif events == "Cadastrar Assunto":
        cadast = cadastro_assunto()

    if events == "OK-assunto":
        inserts = values["-cadastroA-"]
        print(inserts)
        BD.manipula_dados("insert into assunto values (null,'"+ inserts +"')")

    if events == "OK-pergunta":
        BD.manipula_dados("insert into pergunta values"+
        "(null,'"+values["Enunciado"]+"', '"+values["Alternativa 1"]+"','"+
        values["Alternativa 2"]+"','"+values["Alternativa 3"]+"','"
        +values["Alternativa 4"]+"', "+values["Dificuldade"]+","
        +values["Assunto"]+")")

tela.close()