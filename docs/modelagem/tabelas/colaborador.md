# Tabela: `colaborador`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Armazena os colaboradores que participam das atividades da empresa, incluindo colaboradores próprios e colaboradores vinculados a empresas terceiras.

## Atributos

| Atributo     | Tipo de dado | Restrições         | Descrição                                                 |
| ------------ | ------------ | ------------------ | --------------------------------------------------------- |
| `id`         | INT          | PK, AUTO_INCREMENT | Identificador único do colaborador.                       |
| `nome`       | VARCHAR(150) | NOT NULL           | Nome completo do colaborador.                             |
| `cpf`        | CHAR(11)     | NOT NULL, UNIQUE   | CPF do colaborador.                                       |
| `empresa_id` | INT          | FK, NOT NULL       | Identifica a empresa à qual o colaborador está vinculado. |
| `setor_id`   | INT          | FK, NOT NULL       | Identifica o setor ao qual o colaborador pertence.        |
| `cargo_id`   | INT          | FK, NOT NULL       | Identifica o cargo ocupado pelo colaborador.              |

## Regras e observações

* Cada colaborador pertence a **uma única empresa**.
* A empresa pode ser **própria ou terceira**, conforme o cadastro realizado em `empresa`.
* Uma empresa pode possuir vários colaboradores.
* Cada colaborador pertence a **um único setor**.
* Um setor pode possuir vários colaboradores.
* Cada colaborador ocupa **um único cargo**.
* Um cargo pode estar associado a vários colaboradores.
* O CPF deve ser único no sistema.
* O colaborador pode atuar como **professor/instrutor** de um `treinamento`, sendo referenciado pelo atributo `professor_id` da tabela `treinamento`.
* O vínculo com a empresa permite identificar se o colaborador é próprio ou terceirizado sem duplicar essa informação na tabela.

## Relacionamentos

**EMPRESA 1:N COLABORADOR**

**SETOR 1:N COLABORADOR**

**CARGO 1:N COLABORADOR**

**COLABORADOR 1:N TREINAMENTO**
*(como professor/instrutor)*

**COLABORADOR 1:N TREINAMENTO_COLABORADOR**
*(como participante dos treinamentos)*
