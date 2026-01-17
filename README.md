AutoU – Email Triage AI
📌 Descrição do Projeto

Este projeto foi desenvolvido como parte do case prático da AutoU e tem como objetivo resolver um problema comum em empresas financeiras: a triagem manual de grandes volumes de emails.

Empresas desse setor recebem centenas ou milhares de emails diariamente, misturando solicitações críticas de negócio com mensagens irrelevantes, como agradecimentos ou felicitações. Esse cenário gera perda de tempo operacional, atraso em atendimentos importantes e sobrecarga das equipes.

A solução proposta utiliza Inteligência Artificial para classificar automaticamente os emails e gerar respostas profissionais de forma imediata.

🎯 Problema Resolvido

Alto volume de emails analisados manualmente

Perda de tempo da equipe com mensagens irrelevantes

Atraso no atendimento de solicitações críticas

Baixa escalabilidade do processo humano

💡 Solução Proposta

O sistema realiza:

Classificação automática de emails em:

Produtivo → requer ação da equipe

Improdutivo → não requer ação

Geração de respostas automáticas de acordo com a classificação

Interface web simples para upload ou inserção direta do conteúdo do email

⚙️ Funcionamento da IA

A lógica da aplicação segue os seguintes passos:

O usuário insere o texto do email ou faz upload de um arquivo (.txt ou .pdf)

O texto é processado por um modelo de linguagem treinado para Português (PT-BR)

A IA identifica padrões semânticos e palavras-chave

O email é classificado como Produtivo ou Improdutivo

O sistema gera automaticamente uma resposta profissional adequada

A acurácia estimada do modelo fica entre 80% e 90%, sendo suficiente para automatizar grande parte da triagem inicial.

🖥️ Interface Web

A aplicação possui uma interface web simples que permite:

Upload de arquivos .txt ou .pdf

Inserção direta do texto do email

Visualização da classificação do email

Exibição da resposta automática sugerida

📈 Exemplo Prático

Email recebido:
"Qual o status da minha requisição #12345?"

Resultado:

Classificação: Produtivo

Resposta automática:
"Olá! O status da requisição #12345 é 'Em análise'. Previsão: 2 dias úteis."

Email recebido:
"Feliz 2026! Boas festas!"

Resultado:

Classificação: Improdutivo

Resposta automática:
"Obrigado! Feliz ano novo! 😊"

🚀 Impacto Gerado

Redução de 70% a 80% do tempo gasto com triagem manual

Foco da equipe apenas nos casos realmente críticos

Maior agilidade no atendimento ao cliente

Processo escalável, sem aumento de custo operacional

🛠️ Tecnologias Utilizadas

Python

Flask

HTML / CSS

Modelos de linguagem natural (NLP)

Hugging Face (para deploy e testes)

Git e GitHub

▶️ Como Executar o Projeto Localmente
1. Clone o repositório
git clone https://github.com/seu-usuario/autou-email-triage-ai.git
cd autou-email-triage-ai

2. Crie um ambiente virtual
python -m venv venv


Ative o ambiente:

Windows:

venv\Scripts\activate


Linux / Mac:

source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Execute a aplicação
python app/main.py

5. Acesse no navegador
http://localhost:5000

🧠 Principais Aprendizados

Aplicação prática de IA para resolver problemas reais de negócio

Estruturação de soluções escaláveis

Comunicação clara entre tecnologia e impacto empresarial

Integração entre backend, IA e interface web

🔮 Possíveis Evoluções

Transformar a solução em uma API REST

Integração com serviços de email (Gmail, Outlook)

Uso de modelos LLM mais avançados

Dashboard de métricas e performance

Treinamento contínuo com dados reais

# AutoU – Email Triage AI (Web)

## Executar
pip install -r requirements.txt
uvicorn app.main:app --reload

Acesse http://127.0.0.1:8000/
