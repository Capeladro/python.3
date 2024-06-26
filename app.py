

import os


#restaurantes=['Bife Sujo', 'Saco de Feijão']
#inserir dicionario-em outras linguagens chave valor
restaurantes=[{'nome':'Bife-sujo','categoria':'prato-feito','ativo': True},
              {'nome':'Saco do feijão','categoria':'feijoada','ativo': False},
               {'nome':'O bola 8 de coco','categoria':'doceria','ativo': True},] 

def mostrar_subtitulo(texto):
    os.system('clear')
    print (texto)
    print()

#2 declarando a função finalizar_app
def finalizar_app():
    
    mostrar_subtitulo()

def chamar_nome_do_app():
    print ('ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠')

def voltar_ao_menu_principal():
     input('\nDigite uma tecla para voltar ao menu principal')
     main()

# 12 criando opção_invalida
def opcao_invalida():
    print ('opção invalida\n')
    #input('Digite uma tecla para voltar ao menu principal:')
    #main()
    voltar_ao_menu_principal()
    
def exibir_opcoes():
    print ("1 Cadastrar Restaurante")
    print ("2 Listar Restaurante")
    print ("3 Ativar Restaurente")
    print ("4 Sair\n")


def cadatrar_novo_restaurante():
    os.system('clear')
    nome_do_restaurante= input('digite o nome do novo restaurante:')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante={'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}, foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    mostrar_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
       # print(f'- {restaurantes}')
       #modificando a maneira de listar dicionario
       nome_restaurante=restaurante['nome']
       categoria=restaurante['categoria']
       ativo=restaurante ['ativo']
       print(f'-{nome_restaurante} | -{categoria} | -{ativo}')
    #chamar a duas funções e saída
    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    mostrar_subtitulo('Alternando o estado do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que desejas alternar o estado: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'Restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()


#8 declarando a função opcao_digitada1
def escolher_opcao():
    #11 adcionando o try
    try:
        opcao_digitada = (int(input("Escolha uma opção")))
        print ("Você selecionou:",opcao_digitada, "\n")
        if(opcao_digitada==1):
            print("Você escolheu Cadastrar Restaurante\n")
            cadatrar_novo_restaurante()
            finalizar_app()
        elif(opcao_digitada==2):
           # print("Você escolheu Listar Restaurante\n") 
           listar_restaurantes()
           finalizar_app()
        elif(opcao_digitada==3):
            #mostrar_subtitulo("Voce escolheu Ativar Restaurante")
            alterar_estado_restaurante()
            finalizar_app()
        elif(opcao_digitada==4):
            # print('Voce escolheu sair do programa') 
             finalizar_app()
        #3 chamando a função finalizar_app 
        else:
            opcao_invalida()
    except:
        opcao_invalida()         
  
  
def main():
    
    os.system('clear')
    
    chamar_nome_do_app()
    
    exibir_opcoes()
    
    escolher_opcao()


if(__name__=='__main__'):
    main()