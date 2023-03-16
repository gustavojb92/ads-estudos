aluno = str(input("Qual é o nome do aluuno:  "))
nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
media = (nota1 + nota2) /2
if(media < 7):
    print(f"Aluno {aluno} reprovado, nota {media}")
else:
    print(f"Aluno {aluno} aprovado, nota {media}")
