from classes import *;
from datetime import datetime;#manipular o tempo
import string,secrets;#usados no metodo gerar_senha_visitante gera uma letra de [a-z] minus. ou maisc.
data_base_desportistas = list();#lista para guardar desportistas
data_base_visitantes=list();#lista para guardar visitantes
nome_admin='Admin';#nome do Administrador padrao
senha_admin='pass';#senha do Administrador padrao
cont_desport=0;#contador desportista
cont_visitant=0;#contador visitante
pos=-1;#iniciada com posicao que nao existe ira guarda posica encontrada do desporista ao excluir e entrar
historico_acesso='';

def gerar_senha_visitante():
    senha='';
    for i in range (0,5):
        senha+=''.join(secrets.choice(string.ascii_letters));
    return senha;

def listar(data_base):
    for i in range (0,len(data_base)):
            print(i,'=')
            print(data_base[i].toString())
            
def contem(data_base,nome,senha):
    global pos
    for pos in range (0,len(data_base)):
        if(data_base[pos].getNome()==nome):
            if (data_base[pos].getSenha()==senha):
                pos=pos;
                return True;
    return False;

def excluir(data_base,contador):
    global cont_visitant,cont_desport;
    if(contador==0): print('Nao foi feito nenhum registo!\n==============================================');
    else:    
        excluiu=False;
        while True:
            nome = input("Insira o seu nome completo ou a posicao\n");
            senha=input('Insira a senha correspondente ao Desportista:\n')
            try: 
                posicao=int(nome)
                if(posicao>=0 and posicao<len(data_base)):
                    if(data_base[posicao].getSenha()==senha):
                       del data_base[posicao];
                       excluiu=True;
                       if(data_base=="data_base_desportistas"):
                           cont_desport=cont_desport-1;
                       if(data_base=="data_base_visitantes"):
                           cont_visitant=cont_visitant-1;   
                       print('Excluido com sucesso!')
                       break;
                else: print("Posicao inserida invalida!")    
            except Exception:
                if(contem(data_base,nome,senha)):
                    del data_base[pos];
                    if(data_base=="data_base_desportistas"):
                        cont_desport=cont_desport-1;
                    if(data_base=="data_base_visitantes"):
                        cont_visitant=cont_visitant-1;   
                    print('Excluido com sucesso!')
                    break;
                else:
                    print('Nome ou Senha nao correspondente!')
                    resul=input("Tentar novamente! Y/N\n")
                    if(resul=='N' or resul== 'n'): break;
                    elif (resul=='Y' or resul== 'y'): print('======================--------')
                if(excluiu): break;

def validar_acesso(data_base,contador):
    global historico_acesso;
    while True:
        nome = input("Insira o seu nome completo\n");
        senha=input('Insira a senha correspondente:\n')
        if(contem(data_base,nome,senha)):
            if(data_base[pos].get_estado_ativ_desat()=='Invalido'): 
                print(' Impossivel entrar validade atestado medico invalida, valido de [1-6-2022 a 1-12-2022]\n Dica: Possivel alterar no comado 6 do menu!\n======================------')
                break;
            else:
                historico_acesso+=f'Nome: {data_base[pos].getNome()} Login: {datetime.today().strftime("%Y-%m-%d %H:%M")}';
                print(f'Inicio da seccao em {datetime.today().strftime("%Y-%m-%d %H:%M")} como {data_base[pos].getNome()}')
                print(f'Logado como {data_base[pos].getNome()}');
                while True:
                    resul=input("Sair! Y/N\n")
                    if(resul=='N' or resul== 'n'): 
                        print(f'Logado como {data_base[pos].getNome()}')
                    elif (resul=='Y' or resul== 'y'):
                        historico_acesso+=f' Logout: {datetime.today().strftime("%Y-%m-%d %H:%M")}\n ';
                        print(f'Fim da seccao em {datetime.today().strftime("%Y-%m-%d %H:%M")}  como {data_base[pos].getNome()}')
                        print('======================------')
                        break
                break;    
        else :
            print("Falha ao entrar!\nSenha e/ou nome incorretos!!");
            resul=input("Tentar novamente! Y/N\n")
            if(resul=='N' or resul== 'n'): break;
            else: print('')
  
def entrar():
    if(cont_desport==0 and cont_visitant==0): print('Nao ha nenhum desportista/visitante registado!')
    else: 
        while True:
            while True:
                try:
                    opc = int(input(" 1-Entrar como registado       2-Entrar como visitante\n 0-Sair\n=========================\n"));
                    if(opc>=0 and opc<3): break;
                    else:
                        print('Opcao a escolher entre [1 - 2]')
                except ValueError: print('Insira valores numericos');
            if(opc==0):
                break;
            if(opc==1):
                if(cont_desport==0): print('Nao foi feito nenhum registo de despotista!')
                else: 
                    validar_acesso(data_base_desportistas,cont_desport);
            if(opc==2):
                if(cont_visitant==0): print('Nao ha visitante registado!')
                else:
                   validar_acesso(data_base_visitantes,cont_visitant);
                   
def registrar():
    global cont_desport,cont_visitant;
    while True:
        print("=============Menu de cadastro=============")
        while True:
            try:
                print(" 1-Atleta\n 2-Dirigente\n 3-Visitante\n 0-Sair\n=========================");
                opc = int(input());
                if(opc>=0 and opc<4): break;
                else:
                    print('Opcao a escolher entre [1 - 3]')
            except ValueError: print('Insira valores numericos')   ;
        if(opc==0):
           print('===============================')
           break;
        elif(opc==3):
            data='';
            nome=str(input('Insira o nome do visitante\n'))
            senha=gerar_senha_visitante();
            print(f'Sua senha é {senha}')
            while True:
                sexo=str(input("Insira o sexo M/F\n").upper()[0])
                if sexo in 'MF': break;
                print('Insira apenas M ou F !!')
            while True: 
                try:
                    print("Preencha a data validade atestado medico");
                    dia = int(input(' Dia =>'));
                    mes = int(input(' Mes =>'))
                    ano =int(input(' Ano =>'))
                    if (dia >0 and dia<32) and (mes>5 and mes<13) and (ano==2022):
                        data=(f'{dia}-{mes}-{ano}')
                        break;
                    else: print("Preencha uma data valida!!")
                except ValueError: print("Insira valores numericos!!")
            
            visitante = Visitante(nome,data,sexo,senha);  
            if(mes>5 and mes <13):  visitante.set_estado_ativ_desat('Valido')
            else: visitante.set_estado_ativ_desat('Invalido')
            data_base_visitantes.append(visitante)
            cont_visitant+=1;
            print("Visitante registado com sucesso!\n=================================");
                    
        elif(opc==1 or opc==2):         
            nome =str(input("Insira o seu nome\n"));
            while True:
                sexo=str(input("Insira o sexo M/F\n").upper()[0])
                if sexo in 'MF': break;
                print('Insira apenas M ou F !!')
                
            while True: 
                try:
                    num_BI = int(input("Insira o numero de BI \n"));
                    if num_BI >100000 and num_BI <200000: break
                except ValueError: print("Insira valores numericos.")
                        
            morada = str(input("Insira a morada\n"));
                
            while True: 
                try:
                    print("Preencha a data validade atestado medico");
                    dia = int(input(' Dia =>'));
                    mes = int(input(' Mes =>'))
                    ano =int(input(' Ano =>'))
                    if (dia >0 and dia<32) and (mes>5 and mes<13) and (ano==2022):
                        data=(f'{dia}-{mes}-{ano}')
                        break;
                    else: print("Preencha uma data valida!!")
                except ValueError: print("Insira valores numericos!!")
                
            while True: 
                try:
                    contacto = int(input("Insira o contacto\n"));
                    if (contacto>9000000 and contacto<9999999): break;
                except ValueError: print("Insira valores numericos\n======================-------------")
                        
            senha = input("Insira sua senha\n");
            if (opc == 1) :
                atleta = Atleta(nome, num_BI, morada, data, contacto, senha,sexo);
                if(mes>5 and mes <13):  atleta.set_estado_ativ_desat('Valido')
                else: atleta.set_estado_ativ_desat('Invalido')
                data_base_desportistas.append(atleta)
                cont_desport+=1;
                print("Atleta registado com sucesso!\n===============================---");
                    
            elif (opc == 2) :
                dirigente = Dirigente(nome, num_BI, morada, data, contacto, senha,sexo);
                if(mes>5 and mes <13):  dirigente.set_estado_ativ_desat('Valido')
                else: dirigente.set_estado_ativ_desat('Invalido')
                data_base_desportistas.append(dirigente)
                cont_desport+=1;
                print("Dirigente registado com sucesso!\n===============================---");

def alterar_validade_at_medico(data_base):
 while True:    
        nome = input("Insira o seu nome completo\n");
        senha=input('Insira a senha correspondente ao Desportista:\n')
        if(contem(data_base,nome,senha)):
                while True: 
                    try:
                        print("Preencha a nova data validade atestado medico:");
                        dia = int(input('Dia =>'));
                        mes = int(input('Mes =>'))
                        ano = int(input('Ano =>'))
                        if (dia >0 and dia<32) and (mes>5 and mes<13) and (ano==2022):
                            data=(f'{dia}-{mes}-{ano}')
                            data_base[pos].setValidade_atest_medico(data);
                            data_base[pos].set_estado_ativ_desat('Valido');
                            print('Validade alterada\n======================')
                            break;
                        else: print("Preencha uma data valida!!")
                    except ValueError: print("Insira valores numericos!!")
                    break;
                break;
        else: 
            print('Nome ou Senha nao correspondente!')
            resul=input("Tentar novamente! Y/N\n")
            if(resul=='N' or resul== 'n'): break;
            elif (resul=='Y' or resul== 'y'): print('============================')

def alterar_dados_admin():
    global nome_admin,senha_admin;
    while True:
        nome=str(input('Insira o nome atual do Administrador \n'))
        senha=str(input('Insira a senha atual do administrador \n'))
        if(nome == nome_admin and senha ==senha_admin):
            while True:
                try:
                    opc = int(input("=========================\n 1-Alterar dados do administrador    0-Sair\n"));
                    if(opc==1):
                        nome_admin=str(input('Qual o novo nome do Administrador\n'))
                        senha_admin=str(input('Qual a nova senha do Administrador\n'))
                        print('Nome e senha do Administrador alterados!')
                    elif (opc==0):
                        break;
                    else:
                        print('Opcao a escolher entre [0 - 1]')
                except ValueError: print('Insira valores numericos');
            break;    
        else:
            resul=input("Falha ao entrar Como Administrador!\n Senha e/ou nome incorretos!\n Tentar novamente! Y/N\n")
            if(resul=='N' or resul== 'n'): break;
            elif resul=='Y' or resul=='y': print('=========================')      
            
def menu():
    global nome_admin,senha_admin,historico_acesso;
    while True :
        print("===================Instalações Desportivas da FCT===================\n Developed by Henilcio Terras/ Josenasio Ceita/ Eduardo Nascimento\n==============================================");
        print(" 1-Entrar                2-Registrar\n"
             ,"3-Listar                4-Excluir\n"
             ,"5-Alterar Admin         6-Alterar validade At.Medico\n"
             ,"7-Historico Acesso      0-Sair\n"
             ,"==============================================");
        while True:
            try:
                op = int(input("Insira sua opcao =>"));
                if(op>=0 and op<8): break;
                else: 
                 print('Opcao a escolher entre [0 - 7')
                 menu();
            except ValueError: 
                print('Insira opcao numerica')
                menu();    
        match op:
            case 1:
                entrar();
                print('==============================================')       
            case 2:
                while True:
                    nome=str(input('Insira o nome do Administrador \n'))
                    senha=str(input('Insira a senha do administrador \n'))
                    if(nome == nome_admin and senha ==senha_admin):
                        while True:
                            try:
                                print(" 1-Registrar 0-Sair\n==============================================");
                                opc = int(input());
                                if(opc==1):
                                    registrar();
                                    menu();
                                elif (opc==0): break;
                                else: print('Opcao a escolher entre [0 - 1]')
                            except ValueError: print('Insira valores numericos');
                        break;    
                    else:
                        print("Falha ao entrar como Administrador!\nSenha e/ou nome incorretos!!");
                        resul=input("Tentar novamente! Y/N\n")
                        if(resul=='N' or resul== 'n'): break;
                        elif resul=='Y' or resul=='y': print('==============================================')
            case 3:
               global cont_desport,cont_visitant;
               print("===================Menu de Listagem===================");
               while True:
                    nome=str(input('Insira o nome do Administrador \n'))
                    senha=str(input('Insira a senha do administrador \n'))
                    if(nome == nome_admin and senha ==senha_admin):
                        while True:
                            try:
                                print(" 1-Listar  0-Sair\n==============================================");
                                opc = int(input());
                                if(opc==1):
                                    print('===================Desportistas===================')  
                                    if(cont_desport==0): print('Nao ha nenhum desportista registado!\n')
                                    else: listar(data_base_desportistas);
                                    print('===================Visitantes===================')        
                                    if(cont_visitant==0): print('Nao ha nenhum visitante registado!\n')
                                    else: listar(data_base_visitantes);
                                elif (opc==0): break;
                                else: print('Opcao a escolher entre [0 - 1]')
                            except ValueError: print('Insira valores numericos');
                        break;    
                    else:
                        print("Falha ao entrar Como Administrador!\nSenha e/ou nome incorretos!!");
                        resul=input("Tentar novamente! Y/N\n")
                        if(resul=='N' or resul== 'n'): break;
                        elif resul=='Y' or resul=='y': print('==============================================')
                    print('==============================================')     
            case 4:
               global nome_visitante1,senha_visitante1;
               while True:
                    nome=str(input('Insira o nome do Administrador \n'))
                    senha=str(input('Insira a senha do administrador \n'))
                    if(nome == nome_admin and senha ==senha_admin):
                        while True:
                            try:
                                print(" 1-Excluir Registado   2-Excluir Visitante    \n 0-Sair\n==============================================");
                                opc = int(input());
                                if(opc==1): excluir(data_base_desportistas,cont_desport);
                                elif (opc==2): excluir(data_base_visitantes,cont_visitant);
                                elif (opc==0): break;
                                else: print('Opcao a escolher entre [0 - 1]')
                            except ValueError: print('Insira valores numericos');
                        break;    
                    else:
                        print("Falha ao entrar Como Administrador!\nSenha e/ou nome incorretos!");
                        resul=input("Tentar novamente! Y/N\n")
                        if(resul=='N' or resul== 'n'): break;
                        elif resul=='Y' or resul=='y': print('')
                    print('==============================================')     
            case 5:
                print("===================Menu alterar Admin===================")
                alterar_dados_admin();
            case 6:
                print('===================Menu alterar Atest.Medico===================')
                while True:
                    while True:
                        try:
                            opc = int(input(" 1-Alterar registado       2-Alterar visitante\n 0-Sair\n==============================================\n"));
                            if(opc>=0 and opc<3): break;
                            else: print('Opcao a escolher entre [1 - 2]')
                        except ValueError: print('Insira valores numericos');
                    if(opc==0): break;
                    if(opc==1):
                        if cont_desport==0: print("Nao foi feito nenhum registo!")
                        else: alterar_validade_at_medico(data_base_desportistas);
                    if(opc==2):
                        if cont_desport==0: print("Nao foi feito nenhum registo!")
                        else: alterar_validade_at_medico(data_base_visitantes);
            case 7:
                print('===================Menu alterar Historico Login/Logout===================')
                while True:
                    while True:
                        try:
                            opc = int(input(" 1-Historico       2-Limpar Historico\n 0-Sair\n==============================================\n"));
                            if(opc>=0 and opc<3): break;
                            else: print('Opcao a escolher entre [1 - 2]')
                        except ValueError: print('Insira valores numericos');
                    if(opc==0): break;
                    if(opc==1):
                      if(historico_acesso==''): print('Historico Vazio\n==============================================')
                      else: print(historico_acesso);
                    if(opc==2):
                      historico_acesso='';  
                      print('Historico limpo!\n==============================================')                             
            case 0:
                print('Obrigado por usar a aplicacao...\nSaindo.......\nAte Breve.......\n===================')
                exit(0);    

print(f'Dica nome Administrador = {nome_admin} e senha = {senha_admin}');#Dica nome e senha do Admin padrao possivel alterar no comando 5
menu()#responsavel por iniciar o programa                  