# raspagem-dados

# 🤖 Automação de Dados Financeiros: Cotação de Moedas

## 📌 Sobre o Projeto
Este é um projeto ponta a ponta de Engenharia de Dados e Automação Web. O objetivo principal do script é realizar a extração (Web Scraping) de dados de moedas estrangeiras em relação ao Real brasileiro, tratar e limpar esses dados, e gerar um relatório automatizado.

O projeto foi construído focado em resiliência, contornando proteções de sites dinâmicos utilizando navegadores automatizados (headless browser) ao invés de requisições simples de HTML.

## 🛠️ Tecnologias Utilizadas
* **Python 3** - Linguagem principal.
* **Playwright** - Para o Web Scraping assíncrono/síncrono e simulação de navegação.
* **Pandas** - Para a criação do DataFrame, limpeza e manipulação dos dados (ETL).

## 🚀 Status e Funcionalidades (Roadmap)
O projeto está sendo desenvolvido em etapas. Abaixo estão as funcionalidades já implementadas e os próximos passos:

- [x] **Módulo de Extração:** Web Scraping da tabela de cotações contornando carregamentos dinâmicos via JavaScript.
- [x] **Módulo de Transformação:** Conversão dos dados extraídos do HTML para um DataFrame estruturado no Pandas.
- [ ] **Módulo de Limpeza:** Tratamento de strings (remoção de % e R$) e conversão para tipos numéricos (float).
- [ ] **Módulo de Armazenamento:** Inserção do histórico diário em um banco de dados local (SQLite).
- [ ] **Módulo de Relatório:** Envio automático dos dados processados via E-mail.
- [ ] **Agendamento:** Execução autônoma do script na nuvem/servidor.

## ⚙️ Como executar o projeto localmente

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina.

### 2. Instalação das bibliotecas
Abra o seu terminal e instale as dependências necessárias executando os seguintes comandos:

```bash
# Instalar o Pandas e o Playwright
pip install pandas playwright

# Baixar os navegadores do Playwright
playwright install
