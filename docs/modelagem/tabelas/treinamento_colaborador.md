# Tabela: `treinamento_colaborador`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos
**Descrição:** Relaciona os colaboradores aos treinamentos realizados e registra os dados referentes à conclusão e validade da capacitação.

## Atributos

| Atributo         | Tipo de dado | Restrições         | Descrição                                                      |
| ---------------- | ------------ | ------------------ | -------------------------------------------------------------- |
| `id`             | INT          | PK, AUTO_INCREMENT | Identificador único do registro.                               |
| `treinamento_id` | INT          | FK, NOT NULL       | Identifica o treinamento realizado.                            |
| `colaborador_id` | INT          | FK, NOT NULL       | Identifica o colaborador que realizou o treinamento.           |
| `nota`           | DECIMAL(5,2) | NOT NULL           | Nota obtida pelo colaborador na avaliação do treinamento.      |
| `aprovado`       | BOOLEAN      | NOT NULL           | Indica se o colaborador foi aprovado no treinamento.           |
| `data_validade`  | DATE         | NOT NULL           | Data até a qual a capacitação do colaborador permanece válida. |

## Regras e observações

* Um colaborador pode realizar vários treinamentos ao longo do tempo.
* Um treinamento pode possuir vários colaboradores participantes.
* A combinação `treinamento_id` + `colaborador_id` deve ser única, evitando que o mesmo colaborador seja registrado duas vezes no mesmo treinamento.
* `data_validade` deve ser calculada a partir da data do treinamento e da validade definida no curso.
* A `data_validade` deve ser armazenada para preservar o histórico da regra de validade aplicada no momento da realização do treinamento.
* A situação de validade não deve ser armazenada como um campo como `vigente` ou `vencido`. Ela deve ser determinada comparando `data_validade` com a data atual.
* O registro mais recente do colaborador para determinado curso deve ser considerado para identificar sua capacitação vigente.
* Um registro de `treinamento_colaborador` pode possuir zero ou um certificado.

## Relacionamentos

```text id="r52nvm"
TREINAMENTO
     │
     │ 1:N
     ▼
TREINAMENTO_COLABORADOR
     │
     │ 1:0..1
     ▼
CERTIFICADO
```
