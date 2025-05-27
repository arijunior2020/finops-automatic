# 📊 Projeto FinOps-Automatic

[![AWS](https://img.shields.io/badge/Built%20for-AWS-orange?logo=amazonaws)](https://aws.amazon.com)
[![FinOps](https://img.shields.io/badge/FinOps%20Enabled-Práticas%20Financeiras%20em%20Nuvem-blueviolet?logo=finops)](https://www.finops.org)


**FinOps-Automatic** é uma solução simples, conteinerizada e automatizada que realiza **avaliações de maturidade FinOps**, gera **relatórios profissionais** e promove a **governança financeira na nuvem** com base em boas práticas e frameworks reconhecidos.

Projetado para **ambientes em AWS**, o objetivo principal é:

- ✅ Eliminar desperdícios  
- 💸 Otimizar custos  
- 🧭 Estabelecer governança baseada em dados  
- 🔄 Impulsionar a cultura FinOps nas organizações

A solução combina os princípios da **FinOps Foundation (finops.org)** com os **4 pilares do AWS Cloud Financial Management (CFM)**:  
🔹 *See* | 🔹 *Save* | 🔹 *Plan* | 🔹 *Run*

---

## 🔍 Modelo de Maturidade FinOps (Resumo)

A avaliação segue a abordagem **Crawl, Walk, Run** para medir o nível de adoção de cada capacidade FinOps:

| Nível     | Características-chave | Indicadores esperados |
|-----------|------------------------|------------------------|
| **Rastejar (Crawl)** | Visibilidade parcial, processos manuais, KPIs básicos | ≥50% alocação de custos, ±20% de precisão |
| **Andar (Walk)**     | Processos definidos, automação parcial, KPIs intermediários | ≥80% alocação, ±15% de precisão |
| **Correr (Run)**     | Governança ativa, automação ampla, KPIs estratégicos | >90% alocação, ±12% de precisão |

> **Importante:** A meta não é alcançar o nível máximo em todas as capacidades, mas sim **focar naquelas que trazem maior valor de negócio**.

---

## ⚙️ Como Funciona

1. Preencha os formulários localizados na pasta `dados/` com informações sobre seu ambiente em nuvem.
2. Execute o projeto com `docker-compose up`.
3. O container Python processa os dados, gera gráficos e cria automaticamente relatórios `.docx` na pasta `relatorios/`.
4. Os relatórios são prontos para apresentações executivas, auditorias ou planejamento estratégico.

---

## 📂 Estrutura dos Formulários (`/dados`)

### [01_avaliacao_maturidade.xlsx](dados/01_avaliacao_maturidade.xlsx)
Avaliação de maturidade FinOps por capacidade/domínio (Rastejar, Andar, Correr). Inclui gráfico radar e média automática por domínio.

### [02_papeis_personas.xlsx](dados/02_papeis_personas.xlsx)
Mapeamento dos papéis FinOps nas áreas de Engenharia, Produto, Finanças e Liderança.

### [03_ferramentas_aws.xlsx](dados/03_ferramentas_aws.xlsx)
Checklist de ferramentas AWS voltadas para gestão financeira (Cost Explorer, Budgets, CUR etc.).

### [04_execucao_piloto.xlsx](dados/04_execucao_piloto.xlsx)
Registro de execuções-piloto FinOps com responsáveis, escopo, KPIs e resultados.

### [05_governanca_indicadores.xlsx](dados/05_governanca_indicadores.xlsx)
Monitoramento de indicadores-chave como Custo Mensal, Alertas, Cobertura de Tags, Economia estimada.

### [06_finops_executivo](dados/06_finops_executivo.xlsx)
Relatório executivo com recomendações, melhores práticas e plano de ação orientado ao seu ambiente.

---

## 🚀 Executando o Projeto

### 🔧 Requisitos
- Docker e Docker Compose instalados

### ▶️ Comando

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

## 🎯 Objetivo Final

Capacitar sua organização a adotar uma cultura FinOps contínua, com:
- Transparência e visibilidade financeira
- Colaboração entre áreas
- Otimização contínua de custos
- Governança escalável e sustentável

---

## 📜 Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## 👨‍💻 Autor

Arimatéia Júnior
Arquiteto de Software e Soluções | Especialista em Cloud e DevOps

---

## 🤝 Contribua

Sinta-se à vontade para contribuir com o projeto:

- Faça um fork
- Envie seu Pull Request
- Abra uma issue caso encontre algum problema
