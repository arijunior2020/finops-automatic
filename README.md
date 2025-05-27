# 📊 Projeto FinOps-Automatic

**FinOps-Automatic** é uma solução completa e conteinerizada que realiza **avaliação automatizada de maturidade FinOps** e geração de relatórios profissionais com base em boas práticas de gestão financeira na nuvem.

Este projeto foi desenvolvido para **ambientes em AWS**, com o objetivo de **eliminar desperdícios**, **otimizar custos** e **estabelecer governança financeira** baseada em dados. Ele combina os princípios do **framework da FinOps Foundation (finops.org)** com os **4 pilares do AWS Cloud Financial Management (CFM)**: `See`, `Save`, `Plan`, `Run`.

---

## ⚙️ Como Funciona

1. Você preenche os **formulários de entrada** localizados na pasta `dados/` com informações da sua operação em nuvem.
2. Após o preenchimento, você executa o projeto via `docker-compose up`.
3. O container Python processa os dados, gera gráficos e produz relatórios `.docx` automaticamente na pasta `relatorios/`.
4. Os relatórios são formatados, claros e prontos para apresentação executiva ou auditoria interna.

---

## 🗂️ Estrutura dos Formulários (`/dados`)

### `01_avaliacao_maturidade.xlsx`
Avalia o nível atual de maturidade FinOps da organização. Cada linha representa uma **capacidade** e seu respectivo **nível de adoção**:
- `Rastejar`: visibilidade parcial, reativo.
- `Andar`: processos definidos, ferramentas ativas.
- `Correr`: governança contínua, metas e indicadores maduros.

🔢 Inclui cálculo automático da média por domínio e um gráfico radar embutido.

---

### `02_papeis_personas.xlsx`
Define quem são os **atores responsáveis** na prática FinOps:
- `Engenharia`, `Finanças`, `Produto`, `Liderança` etc.
- Descreve o papel de cada um na cadeia de decisão e operação.

---

### `03_ferramentas_aws.xlsx`
Controle de adoção das ferramentas nativas da AWS voltadas para gestão financeira:
- Cost Explorer, Budgets, CUR, Compute Optimizer, Trusted Advisor.
- Marque como `Ativo` ou `Inativo` e visualize em gráfico.

---

### `04_execucao_piloto.xlsx`
Detalhamento de um projeto piloto com foco FinOps:
- Nome do projeto (ex: API, ETL)
- Responsável técnico
- Indicadores/KPIs avaliados
- Resultado (%)

---

### `05_governanca_indicadores.xlsx`
Aponta os principais **indicadores financeiros e operacionais** monitorados:
- Custo Mensal, Cobertura de Tags, Alertas de Budget, Economia Estimada.
- Informe metas e valores alcançados para gerar gráficos de conformidade.

---

## 🚀 Executando o Projeto

### 1. Requisitos

- Docker e Docker Compose instalados

### 2. Comando de execução

```bash
docker-compose up --build
```

Os scripts Python serão executados automaticamente e os relatórios gerados aparecerão em `/relatorios`.

---

## 📁 Pastas Importantes

- `dados/`: onde você preenche os formulários (.xlsx)
- `scripts/`: scripts que processam os dados e geram os relatórios
- `relatorios/`: saída final dos relatórios `.docx`
- `entrypoint.py`: orquestrador dos scripts
- `docker-compose.yml` e `Dockerfile`: automação do ambiente

---

## ✍️ Personalização

Este projeto pode ser facilmente estendido para:
- Exportação em `.pdf`
- Upload automático em SharePoint ou e-mail
- Visualização via Streamlit ou Power BI
- Versionamento por unidade de negócio

---

## 💡 Objetivo Final

Capacitar sua empresa a adotar uma **cultura FinOps contínua**, com **transparência financeira**, **colaboração entre áreas** e **otimização contínua de custos** em nuvem.