# DatabaseBenchmark
Modelo lógico usado:

<p>
Aluno(matricula, nome, semestre, nasc, sexo, cidade, UF, email, cod_curso),</br>
    com matricula sendo chave primária </br>
Curso(cod_curso, nome_curso, nome_coordenador, campus),</br>
    com cod_curso sendo chave primária </br>
CursoDisciplina(cod_curso, cod_disc, semestre_ofertado),</br>
    com cod_curso e cod_disc sendo chaves primárias e secundáras </br>
Disciplina(cod_disc, disc, nome_professor),</br>
    com cod_disc sendo chave primária </br>
</p>
