from peewee import *
import os

arq = "wagnerelindo.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db
        

class Casa(BaseModel):
    numero = IntegerField()
    nomeFamilia = CharField()
    def __str__(self):
        return "CASA = numero da casa: " + str(self.numero) + " nome da familia: " + self.nomeFamilia

class Restaurante(BaseModel):
    fornecedores = CharField()
    pratos = CharField()
    materiaisCozinha = CharField()
    def __str__(self):
        return "RESTAURANTE = fornecedores: " + self.fornecedores + " pratos do dia: " + self.pratos + " materiais: " + self.materiaisCozinha

class Academia(BaseModel):
    aparelhos = CharField()
    numeroParticipantes = IntegerField()
    horarios = CharField()
    def __str__(self):
        return "ACADEMIA = aparelhos: " + self.aparelhos + " numero de participantes: " + str(self.numeroParticipantes) + " horário: " + self.horarios

class Jardim(BaseModel):
    plantas = CharField()
    situacaoCuidados = CharField()
    equipamentos = CharField()
    def __str__(self):
        return "JARDIM = plantas: " + self.plantas + " situação do jardim: " + self.situacaoCuidados + " equipamentos: " + self.equipamentos

class Seguranca(BaseModel):
    numeroCameras = IntegerField()
    ocorrencias = CharField()
    situacaoSistema = CharField()
    def __str__(self):
        return "SEGURANCA = numeroCameras: " + str(self.numeroCameras) + " ocorrencias: " + self.ocorrencias + " situação do Sistema: " + self.situacaoSistema

class Piscina(BaseModel):
    equipamentosPiscina = CharField()
    diasAbertos = CharField()
    situacaoAgua = CharField()
    def __str__(self):
        return "PISCINA = equipamentos: " + self.equipamentosPiscina + " dias abertos: " + self.diasAbertos + " situação agua: " + self.situacaoAgua

class Parque(BaseModel):
    brinquedos = CharField()
    situacaoBrinquedos = CharField()
    numeroVizitantes = IntegerField()
    def __str__(self):
        return "PARQUE = brinquedos: " + self.brinquedos + " situação brinquedos: " + self.situacaoBrinquedos + " numero vizitantes: " + str(self.numeroVizitantes)

class AreaLazer(BaseModel):
    aparelhosArea = CharField()
    reservas = CharField()
    horarioFuncionamento = CharField()
    def __str__(self):
        return "AREA DE LAZER = aparelhos: " + self.aparelhosArea + " reservas: " + self.reservas + " horario de funcionamento: " + self.horarioFuncionamento

class Funcionario(BaseModel):
    nome = CharField()
    salario = IntegerField()
    cargaHoraria = IntegerField()
    areaAtuacao = CharField()
    def __str__(self):
        return "FUNCIONARIO = nome: " + self.nome + " salario: " + str(self.salario) + " carga horaria: " + str(self.cargaHoraria) + " area atuacao: " + self.areaAtuacao

class Manutencao(BaseModel):
    dataManutencao = CharField()
    materiais = CharField()
    funcionario = ForeignKeyField(Funcionario)
    def __str__(self):
        return "MANUTENÇÃO = data: " + self.dataManutencao + " materiais: " + self.materiais + str(self.funcionario)

class Condominio(BaseModel):
    nome = CharField()
    casa = ForeignKeyField(Casa)
    restaurante = ForeignKeyField(Restaurante)
    seguranca = ForeignKeyField(Seguranca)
    academia = ForeignKeyField(Academia)
    jardim = ForeignKeyField(Jardim)
    parque = ForeignKeyField(Parque)
    piscina = ForeignKeyField(Piscina)
    area_lazer = ForeignKeyField (AreaLazer)

    def __str__(self):
        linha = "Condominio " + self.nome + "\n"
        linha += "\t" + str(self.casa) + "\n"
        linha += "\t" + str(self.restaurante) + "\n"
        linha += "\t" + str(self.seguranca) + "\n"
        linha += "\t" + str(self.academia) + "\n"
        linha += "\t" + str(self.jardim) + "\n"
        linha += "\t" + str(self.parque) + "\n"
        linha += "\t" + str(self.piscina) + "\n"
        linha += "\t" + str(self.area_lazer) + "\n"
        return linha

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Funcionario,Manutencao,Casa,Restaurante,Academia,Jardim,Seguranca,Piscina,Parque,AreaLazer, Condominio])          

    except OperationsError as e:
        print ("erro ao criar tabelas: " + str(e))
    

    joao = Funcionario.create(nome = "joao", salario = "1200", cargaHoraria = 8, areaAtuacao = "jardineiro")
    manutencao1 = Manutencao.create(dataManutencao = "amanhã", materiais = "pá, adubo", funcionario = joao)
    casa8 = Casa.create(numero = 8, nomeFamilia = "Silva")
    restaurante = Restaurante.create(fornecedores = "mercadinho", pratos = "macarronada, feijoada", materiaisCozinha = "faca")
    academia = Academia.create(aparelhos = "esteira, pesos" , numeroParticipantes = 70, horarios = "segunda a sexta das 8 as 19")
    jardim_frente = Jardim.create(plantas = "rosas e capim", situacaoCuidados = "Tem q arrumar", equipamentos = "fonte, vasos, amor e carinho" )
    seguranca = Seguranca.create(numeroCameras = 21, ocorrencias = "semana passada deu briga", situacaoSistema = "ta desatualizado")
    piscina3 = Piscina.create(equipamentosPiscina = "cloro, penera", diasAbertos = "sexta a domingo", situacaoAgua = "ta verde")
    parque2 = Parque.create(brinquedos = "escorregador, gangorra", situacaoBrinquedos = "ta inferrujado",numeroVizitantes = 120 )
    areaLazer1 = AreaLazer.create(aparelhosArea = "cadeiras, puff", reservas = "familia silva dia 7", horarioFuncionamento = "só abre em reservas")
    condominio = Condominio.create(nome="do Wagner", casa=casa8, restaurante=restaurante, seguranca = seguranca, academia = academia, jardim = jardim_frente, piscina = piscina3, parque = parque2, area_lazer = areaLazer1)
    print(condominio)


