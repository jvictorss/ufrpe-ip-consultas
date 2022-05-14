# João Victor da Silva Santos e Marcos Fabrício Bezerra Severo
import json
from os.path import exists as existeArquivo

basePaciente = ""
"""
baseConsulta = {}
baseMedico = {}
baseFuncionario = {}
baseClinica = {}
"""

#basePaciente.json
Paciente = {"cpf": "", "nome": "", "email": "", "telefone": "", "endereco": ""}


def cadastrarPaciente():
    """
    -> Efetua o cadastro de cliente, caso ele ainda não tenha sido cadastrado.
    :return: Caso o CPF já tenha sido cadastrado, será exibido.
    """
    basePaciente = existeArquivo("basePaciente.json")
    if basePaciente is False:
        print("{:^60}".format("O arquivo base de cadastro de Pacientes ainda não existe!"))
        print("{:>50}".format(">>>  CRIANDO  >>>"))
        basePaciente = open("basePaciente.json", "w")
    else:
        basePaciente = open("basePaciente.json", "a+")
        cpf = input("Digite o CPF do paciente: ")
        verificaCPFpaciente(cpf)
        while True:
            if cpf in Paciente.get("cpf"):
                print("O CPF {} já está cadastrado para {}.".format(cpf, Paciente.get("nome")))
                break
            else:
                Paciente["cpf"] = cpf
                nome = input("Nome: ")
                email = input("E-mail: ")
                telefone = input("Telefone / Celular: ")
                endereco = input("Endereço: ")
                Paciente["nome"] = nome
                Paciente["email"] = email
                Paciente["telefone"] = telefone
                Paciente["endereco"] = endereco
                print("Paciente \"{}\", CPF nº \"{}\" Cadastrado com sucesso!".format(Paciente["nome"], Paciente["cpf"]))
                json.dump(Paciente, basePaciente, indent=4)
                continua = int(input("\tDeseja continuar? [1] Sim   [2] Não: "))
                if continua != 1:
                    print("{:-^60}".format(" Voltando para o Menu de Paciente. "))
                    break
            basePaciente.close()


def verificaCPFpaciente(cpf):
    #TODO: verificar se função é chamada de forma correta.
    return (cpf in basePaciente)


def buscarPacienteCpf():
    return None


def editarPaciente():
    return None


def removerPaciente():
    return None


def listarTodosPacientes():
    return None


#baseConsulta.json
Consulta = {"codigo": "", "paciente": "", "medico": "", "data": "", "hora": "", "retorno": "", "obs": ""}


def marcarConsulta():
    return None


def buscarConsultaPaciente():
    return None


def editarConsulta():
    return None


def removerConsulta():
    return None


def listarConsultas():
    return None


def listarConsultaRetorno():
    return None


def listarConsultaIntervData():
    return None


#baseMedico.json
Medico = {"crm": "", "nome": "", "email": "", "especialidade": "", "clinica": ""}


def cadastrarMedico():
    return None


def buscarMedicoCRM():
    return None


def editarMedico():
    return None


def removerMedico():
    return None


def listarTodosMedicos():
    return None


def pesquisarMedicoEspecialidade():
    return None


#baseFuncionario.json
Funcionario = {"matricula": "", "cpf": "", "nome": "", "email": "", "clinica": ""}


def cadastrarFuncionario():
    return None


def buscarFuncionarioMatricula():
    return None


def editarFuncionario():
    return None


def removerFuncionario():
    return None


def listarTodosFuncionarios():
    return None


#baseClinica.json
Clinica = {"cnpj": "", "nome": "", "endereco": ""}


def cadastrarClinica():
    return None


def buscarClinicaCnpj():
    return None


def editarClinica():
    return None


def removerClinica():
    return None


def listarTodasClinicas():
    return None

