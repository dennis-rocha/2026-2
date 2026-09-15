# Tabela: `cargo`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Armazena os cargos existentes na organização, utilizados para definir a função exercida pelos colaboradores e os cursos obrigatórios associados a cada cargo.

## Atributos

| Atributo    | Tipo de dado | Restrições         | Descrição                     |
| ----------- | ------------ | ------------------ | ----------------------------- |
| `id`        | INT          | PK, AUTO_INCREMENT | Identificador único do cargo. |
| `descricao` | VARCHAR(100) | NOT NULL, UNIQUE   | Nome ou descrição do cargo.   |

## Regras e observações

* Cada cargo possui uma descrição única.
* Um cargo pode estar associado a vários colaboradores.
* Um cargo pode possuir vários cursos obrigatórios por meio da tabela `cargo_cursos`.
* A associação entre cargo e curso representa os requisitos de treinamento necessários para o cargo.
* O cargo não possui relacionamento direto com `setor`.
* Um mesmo cargo pode ser utilizado por colaboradores pertencentes a diferentes setores e empresas.

## Relacionamentos

**CARGO 1:N COLABORADOR**

**CARGO 1:N CARGO_CURSOS**
