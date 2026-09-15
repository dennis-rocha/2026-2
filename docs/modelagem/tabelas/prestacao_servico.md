# Tabela: `prestacao_servico`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

**Descrição:** Registra a relação de prestação de serviços entre uma empresa própria e uma empresa terceira, permitindo controlar quais empresas terceirizadas prestam serviços para a organização.

## Atributos

| Atributo              | Tipo de dado | Restrições         | Descrição                                                       |
| --------------------- | ------------ | ------------------ | --------------------------------------------------------------- |
| `id`                  | INT          | PK, AUTO_INCREMENT | Identificador único da prestação de serviço.                    |
| `empresa_propria_id`  | INT          | FK, NOT NULL       | Identifica a empresa própria que recebe a prestação de serviço. |
| `empresa_terceira_id` | INT          | FK, NOT NULL       | Identifica a empresa terceira que presta o serviço.             |
| `descricao`           | VARCHAR(200) | NOT NULL           | Descrição do serviço prestado.                                  |
| `data_inicio`         | DATE         | NOT NULL           | Data de início da prestação de serviço.                         |
| `data_fim`            | DATE         | NULL               | Data de encerramento da prestação de serviço, quando aplicável. |

## Regras e observações

* `empresa_propria_id` deve referenciar uma empresa cadastrada como **PROPRIA**.
* `empresa_terceira_id` deve referenciar uma empresa cadastrada como **TERCEIRA**.
* Uma empresa própria pode possuir várias prestações de serviços.
* Uma empresa terceira pode prestar serviços para várias empresas próprias.
* `data_fim` pode permanecer nula enquanto a prestação estiver ativa.
* O período permite manter o histórico das prestações de serviços.
* Uma mesma empresa terceira pode possuir diferentes contratos ou prestações de serviço ao longo do tempo.

## Relacionamentos

**EMPRESA 1:N PRESTACAO_SERVICO**
*(empresa própria)*

**EMPRESA 1:N PRESTACAO_SERVICO**
*(empresa terceira)*
