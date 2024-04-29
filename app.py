

import os 
#inserir 2 restaurantes na list
# restaurantes=['Bife Sujo', 'Saco de Feijão'] 
restaurantes=[{'nome':'Bife Sujo','categoria':'prato-feito','ativo':True},
              {'nome':'Saco de Feijão','categoria':'feijoada', 'ativo':False},
              {'nome':'Pé de Banha','categoria':'pastelaria','ativo':True}]

def mostrar_subtitulo():
    os.system('cls')
    print ('texto')
    print()
    
def finalizar_app():
    # os.system('cls')
    # print ('Finalizando app\n')
    mostrar_subtitulo('Finalizando o app')

def chamar_nome_do_app():
     print ('''ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠''') 

def opcao_invalida():
    print('Opção invalida\n')
    # input('Digite uma tecla para voltar ao menu principal: ')
    # main() 
    voltar_ao_menu_principal()

def exibir_opcoes():
    print('1-Cadastrar um restaurante')
    print('2-Listar restaurantes')
    print('3-Ativar um restaurante')
    print('4-Sair do programa')

def voltar_ao_menu_principal():
     input("\n Digite uma tecla para voltar ao menu principal: \n")
     main() 

def cadastrar_novo_restaurante():
     os.system('cls')
     nome_do_restaurante=input('Digite o nome do novo restaurante: \n')
     restaurantes.append(nome_do_restaurante)
     print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
     voltar_ao_menu_principal()

def listar_restaurantes():
    os. system('cls')
    print('Listando os restaurantes \n')
    #em português
    for restaurante in restaurantes:
        # print(f'-{restaurante}')
    #modificando a maneira de listar restaurante
    #para manipular o dicionário
        nome_res=restaurante['nome']
        categoria=restaurante['categoria']
        print(f'-{nome_res} |- {categoria}')
        voltar_ao_menu_principal()

def escolher_opcoes(): 
    try:
        opcao_digitada=(int(input('Escolha uma opção: ')))
        print('Você selecionou a opção: ',opcao_digitada,'\n')
        if(opcao_digitada==1):
            print('Você escolheu cadastrar um restaurante\n')
            cadastrar_novo_restaurante()
        elif (opcao_digitada==2):
            # print('Você escolheu listar os restaurantes do app\n')
            listar_restaurantes()
        elif (opcao_digitada==3):
            print('Você escolheu ativar um restaurante\n')
        elif (opcao_digitada==4):
            print('Você escolheu sair do programa\n')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 

def main():
    os.system('cls') 

    chamar_nome_do_app() 

    exibir_opcoes() 

    escolher_opcoes() 


if(__name__=='__main__'):
    main()