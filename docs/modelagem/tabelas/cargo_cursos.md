# Tabela: `cargo_cursos`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Tabela intermediária que relaciona os cargos aos cursos obrigatórios para o exercício de suas atividades.

## Atributos

| Atributo   | Tipo de dado | Restrições         | Descrição                                    |
| ---------- | ------------ | ------------------ | -------------------------------------------- |
| `id`       | INT          | PK, AUTO_INCREMENT | Identificador único do relacionamento.       |
| `cargo_id` | INT          | FK, NOT NULL       | Identifica o cargo relacionado.              |
| `curso_id` | INT          | FK, NOT NULL       | Identifica o curso obrigatório para o cargo. |

## Regras e observações

* Um cargo pode exigir vários cursos.
* Um curso pode ser obrigatório para vários cargos.
* O mesmo curso não pode ser associado mais de uma vez ao mesmo cargo.
* Deve existir uma restrição de unicidade composta sobre `cargo_id` e `curso_id`.
* A tabela representa a **obrigatoriedade do curso para o cargo**, e não a realização do curso pelo colaborador.
* A realização do curso é registrada posteriormente em `treinamento` e `treinamento_colaborador`.
* A partir do cargo de um colaborador, o sistema pode identificar automaticamente quais cursos devem ser verificados para determinar sua situação de conformidade.

## Relacionamentos

**CARGO 1:N CARGO_CURSOS**

**CURSO 1:N CARGO_CURSOS**

**CARGO N:N CURSO**
*Relacionamento realizado por meio da tabela `cargo_cursos`.*
