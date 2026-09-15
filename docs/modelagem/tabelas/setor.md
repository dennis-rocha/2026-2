# Tabela: `setor`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Armazena os setores organizacionais da empresa e permite identificar a estrutura à qual os colaboradores estão vinculados.

## Atributos

| Atributo    | Tipo de dado | Restrições         | Descrição                     |
| ----------- | ------------ | ------------------ | ----------------------------- |
| `id`        | INT          | PK, AUTO_INCREMENT | Identificador único do setor. |
| `descricao` | VARCHAR(100) | NOT NULL, UNIQUE   | Nome ou descrição do setor.   |

## Regras e observações

* Cada setor pode possuir vários colaboradores.
* Cada colaborador pertence a um único setor.
* A descrição do setor deve ser única para evitar cadastros duplicados.
* O setor não possui vínculo direto com `cargo`, pois um mesmo cargo pode ser utilizado por colaboradores de diferentes setores.
* O relacionamento entre setor e colaborador é realizado diretamente por meio de `colaborador.setor_id`.
* Caso seja necessário representar coordenadores responsáveis por um ou mais setores, esse relacionamento poderá ser tratado posteriormente por uma tabela associativa específica, como `setor_coordenadores`.

## Relacionamentos

**SETOR 1:N COLABORADOR**

**SETOR N:N COLABORADOR**
*Não se aplica neste modelo. Cada colaborador pertence a um único setor.*
