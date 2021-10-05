import commands
import config

i = True

while i:
    command = input('$~ ')
    if command in commands.EXIT:
        i = False
        print('Sistema finalizado')
    elif command in commands.CREATE:
        name = input('Nome: ')
        student = {"nome": name, "notas": [], "media": 0, "status": ''}
        quantity = int(input('Quantidade de notas: '))
        q = 1
        soma = 0

        while q <= quantity:
            nota = float(input(f'Nota {q}: '))

            if nota > config.MIN and nota <= config.MAX:
                student["notas"].append(nota)
                soma = soma + nota
                q += 1
            else:
                print('Insira uma nota valida')
        
        student['media'] = soma / quantity
        
        if student['media'] < config.MEDIUM:
            print('O aluno {} foi Reprovado'.format(student['nome']))
            student['status'] = 'Reprovado'
        else:
            print('O aluno {} foi Aprovado'.format(student['nome']))
            student['status'] = 'Aprovado'

        print('A media de {} foi {}'.format(student['nome'], student['media']))

        config.ALUNOS.append(student)
    elif command in commands.LIST:
        if config.ALUNOS == []:
            print('Nenhum dado cadastrado')
        else:
            print(config.ALUNOS)
    elif command in commands.GET:
        search_name = input('Nome do aluno: ')
        for aluno in config.ALUNOS:
            if aluno['nome'] == search_name:
                print(aluno)
            else:
                print('Aluno não encontrado')
    elif command in commands.HELP:
        print('Para criar um aluno use {}\nPara listar todos os alunos use {}\nPara ver um aluno espesifico use {}\nPara sair do programa use {}'.
        format(commands.CREATE, commands.LIST, commands.GET, commands.EXIT))
    elif command != commands:
        print('digite -help')