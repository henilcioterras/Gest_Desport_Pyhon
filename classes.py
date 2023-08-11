class Desportista:
    def __init__(self,nome,BI,morada,validade_atest_medico,contacto,senha,sexo):
        self.nome = nome;
        self.BI = BI;
        self.morada = morada;
        self.validade_atest_medico = validade_atest_medico;
        self.contacto =f'+239 {contacto}';
        self.nome_classe=self.__class__.__name__;
        self.senha=senha;
        self.sexo=sexo;
        
    def getNome(self):
        return self.nome;
         
    def setNome(self,nome):
       self.nome=nome;
       
    def getBI(self):
        return self.BI;
    
    def setBI(self):
        return self.BI;
    
    def setMorada(self,morada):
       self.morada=morada;
       
    def getMorada(self):
        return self.morada;
    
    def setValidade_atest_medico(self,validade_atest_medico):
       self.validade_atest_medico=validade_atest_medico;
            
    def getValidade_atest_medico(self):
       return self.validade_atest_medico;
   
    def setContacto(self,contacto):
       self.contacto=contacto;
       
    def getContacto(self):
        return self.contacto;
    
    def setSenha(self,senha):
        self.senha=senha
    
    def getSenha(self):
        return self.senha; 
    
    def setSexo(self,sexo):
        self.sexo=sexo;
        
    def getSexo(self):
        return self.sexo;    
    
    def set_estado_ativ_desat(self,estado):
        self.estado=estado;
        
    def get_estado_ativ_desat(self):
        return self.estado; 
       
    def toString(self):
        print(self.nome_classe,'=>\n - Nome: ',self.nome,'\n - BI: ',self.BI,'\n - Sexo: ',self.sexo,'\n - Morada: ',self.morada,'\n - Validade atestado medico: ',self.validade_atest_medico,'\n - Contacto: - ',self.contacto, '\n - Senha: - ',self.senha,'\n - Estado: - ',self.get_estado_ativ_desat())

class Atleta(Desportista):
    
    def __init__(self, nome, BI, morada, validade_atest_medico, contacto,senha,sexo):
        super().__init__(nome, BI, morada, validade_atest_medico, contacto,senha,sexo)

    def toString(self):
        return super().toString()
    
class Dirigente(Desportista):
       
       def __init__(self, nome, BI, morada, validade_atest_medico, contacto,senha,sexo):
           super().__init__(nome, BI, morada, validade_atest_medico, contacto,senha,sexo)
       
       def toString(self):
        return super().toString() 

class Visitante:
    def __init__(self,nome,validade_atest_medico,sexo,senha):
        self.nome = nome;
        self.validade_atest_medico = validade_atest_medico;
        self.nome_classe=self.__class__.__name__;
        self.sexo=sexo;
        self.senha=senha; 
        
    def getNome(self):
        return self.nome;
    
    def setNome(self,nome):
       self.nome=nome;
 
    def setValidade_atest_medico(self,validade_atest_medico):
       self.validade_atest_medico=validade_atest_medico;
            
    def getValidade_atest_medico(self):
       return self.validade_atest_medico;

    def setSexo(self,sexo):
        self.sexo=sexo;
        
    def getSexo(self):
        return self.sexo;    
    
    def setSenha(self,senha):
        self.senha=senha
    
    def getSenha(self):
        return self.senha; 
    
    def set_estado_ativ_desat(self,estado):
        self.estado=estado;
        
    def get_estado_ativ_desat(self):
        return self.estado; 

    def toString(self):
        print(self.nome_classe,'=>\n - Nome: ',self.nome,'\n - Sexo: ',self.sexo,'\n - Validade atestado medico: ',self.validade_atest_medico,'\n - Senha: - ',self.senha,'\n - Estado: - ',self.get_estado_ativ_desat())
