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
- Recuperar os documentos mais relevantes
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

## Configuração do .env

1. Crie um arquivo `.env` na raiz do projeto:
   ```bash
   cp .env.example .env

2. Copie o codigo em env.example e cole em seu .env


### Definindo a Base de Conhecimento (PDFs)

**Para o RAG funcionar, você precisa fornecer documentos PDF para serem usados como fonte de informação.**

1. Crie uma pasta dentro do diretório raiz do projeto 
2. Adicione dentro dela todos os PDFs que deseja usar como base de conhecimento
3. Copie o diretório completo dessa pasta
4. Abra o arquivo .env e procure pela linha: ```PDF_DIRECTORY= "Cole o diretorio da pasta de documentos aqui"```
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
1. abra o arquivo: .env
2. Cole sua chave no local indicado: ```GOOGLE_API_KEY = "Cole sua chave aqui"```
3. Salve o arquivo

### Instalando as bibliotecas necessárias

**Abra o terminal dentro da pasta do projeto e siga os passos abaixo.**

1. No terminal digite: ```python -m venv .venv```
2. Depois ```.venv\Scripts\Activate```
3. Linux ou Mac : ```source .venv/bin/activate```
5. Por fim:```pip install -r requirements.txt ```

### Agora você pode iniciar o chat

No terminal execute: ``` py -m app.main.py ```

Para realizar testes unitarios utilize na raiz do projeto: ```pytest```

---

├## Estrutura do Projeto


```bash
projeto-rag/
│
── app/
│   ├── config/
│       ├──constants.py
│   ├── core/
│       ├──logger.py
│   ├── pipeline/
│       ├──chunker.py
│       ├──ingest.py
│       ├──loader.py
│       ├──loader.py
│       ├──metadata.py
│       ├──vectorstore.py
│   ├── rag/
│       ├──chain.py
│       ├──prompts.py
│       ├──retriever.py
│   ├── session/
│      ├──manager.py
│   ├── utils/
│      ├──validation.py
│   ├── main.py
│   ├── settings.py
├─ tests/
│  ├─ __init__.py
│  ├─ pipeline/
│  │  ├─ test_loader.py
│  │  ├─ test_chunker.py
│  │  ├─ test_metadata.py
│  │  └─ test_vectorstore.py
│  │
│  ├─ session/
│  │  └─ test_manager.py
│  │
│  └─ utils/
│     └─ test_validation.py
│
├─ pytest.ini
├── .env
├── requirements.txt


```
--- 
##  Agradecimento

Este projeto representa, sem dúvidas, uma das experiências mais enriquecedoras que já tive na área de tecnologia.

Ao longo do desenvolvimento, enfrentei diversos desafios técnicos, erros inesperados e muitos momentos de tentativa e falha. No entanto, cada obstáculo foi fundamental para consolidar meu aprendizado e aprofundar minha compreensão sobre o funcionamento das soluções desenvolvidas. Todo o conhecimento adquirido nesse processo foi extremamente valioso e contribuiu significativamente para minha evolução no entendimento de Inteligência Artificial, LangChain, RAG, embeddings, recuperação vetorial, integração com LLMs e da própria linguagem Python.

Embora esta seja uma primeira versão funcional, ainda há inúmeras melhorias que pretendo implementar futuramente, entre elas:

- **Guardrails**, para evitar comportamentos inadequados e aumentar a segurança e confiabilidade das respostas.

- **Busca híbrida (vetorial + lexical)**, com o objetivo de melhorar a precisão na recuperação de documentos.

- Ajustes e otimizações nos métodos de chunking e no enriquecimento de metadados.

- Melhorias na gestão de memória e contexto para suportar conversas mais longas.

- Implementação de técnicas avançadas de RAG para aumentar a consistência e a confiabilidade das respostas.

Agradeço muito por dedicar um tempo para conhecer este projeto.
Estou totalmente aberto a feedbacks, sugestões e contribuições que possam ajudar a evoluir ainda mais essa aplicação.

Muito obrigado!