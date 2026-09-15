# Tabela: `curso`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos
**Descrição:** Armazena os cursos e treinamentos obrigatórios que podem ser realizados pelos colaboradores, incluindo informações relacionadas à validade e carga horária.

## Atributos

| Atributo         | Tipo de dado | Restrições         | Descrição                                                      |
| ---------------- | ------------ | ------------------ | -------------------------------------------------------------- |
| `id`             | INT          | PK, AUTO_INCREMENT | Identificador único do curso.                                  |
| `descricao`      | VARCHAR(150) | NOT NULL, UNIQUE   | Nome ou descrição do curso, como "NR-35 - Trabalho em Altura". |
| `validade_meses` | INT          | NOT NULL           | Quantidade de meses de validade do curso.                      |
| `carga_horaria`  | DECIMAL(5,2) | NOT NULL           | Carga horária prevista para a realização do curso, em horas.   |

## Regras e observações

* A `descricao` deve identificar de forma única cada curso cadastrado.
* `validade_meses` será utilizada para calcular a data de validade da capacitação realizada pelo colaborador.
* A validade calculada deve ser registrada em `treinamento_colaborador`, preservando o histórico mesmo que a validade do curso seja alterada posteriormente.
* `carga_horaria` utiliza valor decimal para permitir cursos com duração fracionada, como `8,5` horas.
* Um curso pode possuir vários registros de `treinamento`.
* Um curso pode ser obrigatório para vários cargos por meio da tabela `cargo_cursos`.

## Relacionamentos

```text
CURSO
  │
  ├── 1:N → TREINAMENTO
  │
  └── N:N → CARGO
             │
             └── CARGO_CURSOS
```
