#  Chat com RAG 

Este projeto implementa um **chat inteligente baseado em RAG (Retrieval-Augmented Generation)** utilizando o modelo **Gemini**, o framework **LangChain**, e um banco vetorial **FAISS** para recuperação de documentos em PDF.

O objetivo é permitir que o usuário faça perguntas e receba respostas baseadas em documentos reais (PDFs), tornando o chat muito mais confiável e contextualizado.

---

#  O que é RAG (Retrieval-Augmented Generation)?

O **RAG (Retrieval-Augmented Generation)** é uma técnica utilizada para melhorar a qualidade e a precisão das respostas de modelos de linguagem (LLMs), combinando dois processos:

##  1. Recuperação
Antes do modelo responder, o sistema busca documentos relevantes dentro de uma base de conhecimento.

Esses documentos são armazenados em um banco vetorial e recuperados por similaridade semântica.

##  2. Geração
Depois de recuperar os documentos relevantes, o sistema envia esse conteúdo como **contexto** para o modelo (Gemini), que então gera uma resposta baseada nesse material.

 Isso evita respostas inventadas (hallucinations) e melhora muito a precisão.

---

# O que este projeto faz?

Este projeto cria um sistema completo de IA conversacional capaz de:

- Ler PDFs como base de conhecimento
- Criar embeddings e indexar documentos no FAISS
- Recuperar os documentos mais relevantes para cada pergunta
- Enviar contexto real para o modelo Gemini
- Responder perguntas de forma contextualizada
- Manter histórico de conversa durante a sessão
- Mostrar quais documentos foram recuperados e seus metadados

---

# Como rodar o projeto ?

Antes de começar, lembre-se:
Você precisa ter o **Python instalado (recomendado Python 3.10+)**

É altamente recomendado utilizar uma **IDE** como:

- VSCode
- PyCharm
- Cursor
- IntelliJ

## Passo a Passo

### Definindo a Base de Conhecimento (PDFs)

**Para o RAG funcionar, você precisa fornecer documentos PDF para serem usados como fonte de informação.**

1. Crie uma pasta dentro do diretório do projeto 
2. Adicione dentro dela todos os PDFs que deseja usar como base de conhecimento
3. Copie o diretório completo dessa pasta
4. Abra o arquivo pipeline.py e procure pela linha: ```bash pdfs = load_pdfs(r"Cole o diretorio aqui") ```
5. Cole o caminho completo da sua pasta no local indicado
6. Salve o arquivo


### Definindo a API Key do Gemini

**O projeto usa a API do Gemini, então você precisa criar uma chave de acesso.**

1. Vá até o site do Google AI Studio: https://aistudio.google.com
2. Crie uma conta ou faça login
3. No canto inferior esquerdo clique em Get API Key

- Caso você já tenha uma chave:
1. Clique na chave exibida
2. Copie a API Key que aparecer na tela
   
- Caso você ainda não tenha uma chave:
1. Clique em Criar chave de API
2. Clique novamente em Criar chave
3. Selecione a chave gerada logo abaixo da coluna Key
4. Copie a chave exibida

- Dentro do projeto
1. abra o arquivo: chaves.env
2. Cole sua chave no local indicado: GEMINI_API_KEY = "Cole sua Chave aqui"
3. Salve o arquivo

### Instalando as bibliotecas necessárias

**Abra o terminal dentro da pasta do projeto e siga os passos abaixo.**

1. No terminal digite: python -m venv .venv
2. .venv\Scripts\Activate
3. Linux ou Mac : source .venv/bin/activate
4. pip install -r requirements.txt

### Agora você pode iniciar o chat

1. No terminal execute: py main.py
2. Você verá algo como: **prompt:**
3. Digite sua pergunta e pressione Enter.
4. **Para sair do chat: Digite sair**

---

## Estrutura do Projeto


```bash
projeto-rag/
│
├── main.py
├── pipeline.py
├── api_connections.py
├── chaves.env
├── requirements.txt
│
├── faiss-db/
└── documentos/
```
--- 
##  Agradecimento

Esse projeto representa a minha **primeira IA treinada utilizando RAG**, e sem dúvidas foi uma das experiências mais desafiadoras e enriquecedoras que já tive na área.

Durante o desenvolvimento, enfrentei diversas dificuldades técnicas, erros inesperados e momentos de tentativa e falha, mas cada obstáculo foi essencial para consolidar meu aprendizado. O conhecimento adquirido ao longo desse processo foi extremamente valioso e me fez evoluir bastante no entendimento sobre **Inteligência Artificial, LangChain, embeddings, recuperação vetorial e integração com LLMs**.

Apesar de ser uma primeira versão funcional, ainda existem muitas melhorias possíveis que pretendo implementar futuramente, como por exemplo:

- **Guardrails**, para evitar comportamentos inadequados e aumentar a segurança das respostas.
- **Busca híbrida (vetorial + lexical)**, melhorando a precisão da recuperação de documentos.
- Ajustes e otimizações no método de chunking e enriquecimento de metadados.
- Melhoria na gestão de memória e contexto para conversas mais longas.
- Implementação de técnicas avançadas de RAG para aumentar consistência e confiabilidade.

Agradeço muito por ter dedicado um tempo para conhecer este projeto.  
Estou totalmente aberto a feedbacks, sugestões e contribuições que possam ajudar a evoluir ainda mais essa aplicação.

Muito obrigado! 




