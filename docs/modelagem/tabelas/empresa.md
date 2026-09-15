# Tabela: `empresa`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Armazena as empresas envolvidas no sistema, identificando se são empresas próprias ou terceiras.

## Atributos

| Atributo       | Tipo de dado                | Restrições         | Descrição                                      |
| -------------- | --------------------------- | ------------------ | ---------------------------------------------- |
| `id`           | INT                         | PK, AUTO_INCREMENT | Identificador único da empresa.                |
| `razao_social` | VARCHAR(150)                | NOT NULL           | Razão social da empresa.                       |
| `cnpj`         | CHAR(14)                    | NOT NULL, UNIQUE   | CNPJ da empresa.                               |
| `tipo`         | ENUM('PROPRIA', 'TERCEIRA') | NOT NULL           | Identifica se a empresa é própria ou terceira. |

## Regras e observações

* Cada empresa possui um único cadastro no sistema.
* O CNPJ deve ser único.
* O atributo `tipo` identifica se a empresa é **própria** ou **terceira**.
* Uma empresa própria pode possuir vários colaboradores.
* Uma empresa terceira também pode possuir vários colaboradores.
* O vínculo do colaborador com a empresa é realizado por meio de `colaborador.empresa_id`.
* Empresas próprias e terceiras são armazenadas na mesma tabela para evitar duplicação de estrutura.

## Relacionamentos

**EMPRESA 1:N COLABORADOR**

**EMPRESA 1:N PRESTACAO_SERVICO**
*(como empresa própria ou empresa terceira)*
