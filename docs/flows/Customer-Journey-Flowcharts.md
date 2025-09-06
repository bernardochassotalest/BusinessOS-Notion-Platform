# Fluxogramas da Jornada do Cliente
## Business OS Integrado no Notion

**Versão:** 1.0  
**Data:** 06 de Setembro de 2025  
**Status:** Em Validação

---

## 1. Fluxo Principal da Jornada do Cliente

```mermaid
flowchart TD
    A[Novo Lead Qualificado] --> B{Aprovação Técnica?}
    B -->|Não| C[Rejeitar Lead]
    B -->|Sim| D[Criar Cliente - Fase: Pré-venda]
    
    D --> E[Alocar Equipe Técnica]
    E --> F[Elaborar Proposta]
    F --> G{Cliente Aprovou?}
    
    G -->|Não| H[Renegociar/Arquivar]
    G -->|Sim| I[Mover para: Implantação/Onboarding]
    
    I --> J[Auto-criar Projeto de Implantação]
    J --> K[Alocar Equipe do Projeto]
    K --> L[Executar Implantação]
    
    L --> M{Projeto Concluído?}
    M -->|Não| N[Continuar Execução]
    N --> L
    M -->|Sim| O[Mover para: Ongoing CS]
    
    O --> P[Criar Atividades Recorrentes]
    P --> Q[Gestão de Customer Success]
    Q --> R{Renovação/Expansão?}
    
    R -->|Sim| S[Novo Projeto/Contrato]
    R -->|Não| T[Manter CS Ativo]
    S --> K
    T --> Q
    
    Q --> U{Encerrar Conta?}
    U -->|Não| Q
    U -->|Sim| V[Mover para: Concluído/Inativo]
    
    C --> W[Arquivar Lead]
    H --> W
    V --> X[Arquivo Final]
    
    style A fill:#e1f5fe
    style I fill:#f3e5f5
    style O fill:#e8f5e8
    style V fill:#fff3e0
```

## 2. Fluxo Detalhado: Fase Pré-venda

```mermaid
flowchart TD
    A[Lead Qualificado Recebido] --> B[Criar Registro na Base Clientes]
    B --> C[Definir Fase: Pré-venda]
    C --> D[Analisar Necessidades Técnicas]
    
    D --> E{Competências Disponíveis?}
    E -->|Não| F[Buscar Recursos Externos]
    E -->|Sim| G[Alocar Equipe Técnica]
    
    F --> H{Recursos Encontrados?}
    H -->|Não| I[Rejeitar - Falta de Capacidade]
    H -->|Sim| G
    
    G --> J[Registrar Equipe no Cliente]
    J --> K[Criar Atividades de Pré-venda]
    K --> L[Reunião de Discovery]
    
    L --> M[Documentar Requisitos]
    M --> N[Elaborar Proposta Técnica]
    N --> O[Definir Cronograma]
    O --> P[Calcular Orçamento]
    
    P --> Q[Apresentar Proposta]
    Q --> R{Cliente Aprova?}
    
    R -->|Não| S[Registrar Feedback]
    S --> T{Possível Ajuste?}
    T -->|Sim| U[Ajustar Proposta]
    T -->|Não| V[Arquivar - Não Aprovado]
    U --> Q
    
    R -->|Sim| W[Atualizar Status: Aprovado]
    W --> X[Preparar Transição para Implantação]
    
    I --> Y[Arquivar Lead]
    V --> Y
    X --> Z[Mover para Fase: Implantação]
    
    style A fill:#e3f2fd
    style Z fill:#f3e5f5
    style Y fill:#ffebee
```

## 3. Fluxo Detalhado: Fase Implantação/Onboarding

```mermaid
flowchart TD
    A[Cliente Movido para Implantação] --> B[Trigger: Auto-criar Projeto]
    B --> C[Aplicar Template de Onboarding]
    C --> D[Definir Escopo Detalhado]
    
    D --> E[Analisar Competências Necessárias]
    E --> F[Consultar Mapa de Competências]
    F --> G{Equipe Ideal Disponível?}
    
    G -->|Não| H[Buscar Alternativas]
    G -->|Sim| I[Alocar Equipe do Projeto]
    
    H --> J{Alternativas Viáveis?}
    J -->|Não| K[Escalar para Liderança]
    J -->|Sim| I
    
    K --> L[Decisão de Recursos]
    L --> M{Aprovado Recursos Extras?}
    M -->|Não| N[Renegociar Escopo]
    M -->|Sim| O[Contratar/Realocar Recursos]
    
    N --> P{Novo Escopo Aceito?}
    P -->|Não| Q[Cancelar Projeto]
    P -->|Sim| I
    O --> I
    
    I --> R[Definir Líder do Projeto]
    R --> S[Criar Cronograma Detalhado]
    S --> T[Kickoff Meeting]
    
    T --> U[Executar Fases do Projeto]
    U --> V[Atualizar Progresso Regularmente]
    V --> W{Milestone Atingido?}
    
    W -->|Não| X[Analisar Desvios]
    X --> Y{Ação Corretiva Necessária?}
    Y -->|Sim| Z[Implementar Correções]
    Y -->|Não| U
    Z --> U
    
    W -->|Sim| AA[Validar com Cliente]
    AA --> BB{Cliente Aprova Milestone?}
    BB -->|Não| CC[Ajustar Entrega]
    BB -->|Sim| DD{Projeto Completo?}
    
    CC --> U
    DD -->|Não| U
    DD -->|Sim| EE[Entrega Final]
    
    EE --> FF[Validação Final do Cliente]
    FF --> GG{Aceite Final?}
    GG -->|Não| HH[Ajustes Finais]
    GG -->|Sim| II[Concluir Projeto]
    
    HH --> EE
    II --> JJ[Preparar Transição para CS]
    JJ --> KK[Mover Cliente para: Ongoing CS]
    
    Q --> LL[Arquivar Projeto Cancelado]
    
    style A fill:#f3e5f5
    style KK fill:#e8f5e8
    style LL fill:#ffebee
```

## 4. Fluxo Detalhado: Fase Ongoing (Customer Success)

```mermaid
flowchart TD
    A[Cliente Movido para Ongoing CS] --> B[Handover: Projeto → CS]
    B --> C[Designar Customer Success Manager]
    C --> D[Criar Plano de CS Personalizado]
    
    D --> E[Definir Atividades Recorrentes]
    E --> F[Agendar Health Checks Regulares]
    F --> G[Configurar Métricas de Sucesso]
    
    G --> H[Primeira Reunião de CS]
    H --> I[Estabelecer Cadência de Contato]
    I --> J[Ciclo de Atividades CS]
    
    J --> K[Executar Atividade Programada]
    K --> L{Tipo de Atividade?}
    
    L -->|Health Check| M[Avaliar Saúde da Conta]
    L -->|Reunião Regular| N[Reunião de Acompanhamento]
    L -->|Suporte| O[Resolver Questão Técnica]
    L -->|Training| P[Sessão de Treinamento]
    
    M --> Q[Registrar Status da Conta]
    N --> R[Documentar Feedback]
    O --> S[Resolver e Documentar]
    P --> T[Avaliar Aprendizado]
    
    Q --> U{Conta Saudável?}
    R --> V{Necessidades Identificadas?}
    S --> W{Problema Resolvido?}
    T --> X{Treinamento Efetivo?}
    
    U -->|Não| Y[Criar Plano de Ação]
    U -->|Sim| Z[Continuar Monitoramento]
    
    V -->|Sim| AA[Identificar Oportunidades]
    V -->|Não| Z
    
    W -->|Não| BB[Escalar Suporte]
    W -->|Sim| Z
    
    X -->|Não| CC[Replanejar Treinamento]
    X -->|Sim| Z
    
    Y --> DD[Implementar Ações Corretivas]
    AA --> EE{Oportunidade de Expansão?}
    BB --> FF[Suporte Especializado]
    CC --> P
    
    DD --> GG[Monitorar Melhoria]
    EE -->|Sim| HH[Propor Expansão]
    EE -->|Não| II[Documentar para Futuro]
    FF --> S
    
    GG --> U
    HH --> JJ[Criar Novo Projeto]
    II --> Z
    
    JJ --> KK[Voltar para Fase Implantação]
    
    Z --> LL{Próxima Atividade?}
    LL -->|Sim| MM[Agendar Próxima]
    LL -->|Não| NN{Renovação Próxima?}
    
    MM --> J
    NN -->|Sim| OO[Processo de Renovação]
    NN -->|Não| PP{Encerrar Conta?}
    
    OO --> QQ[Negociar Renovação]
    PP -->|Não| J
    PP -->|Sim| RR[Processo de Offboarding]
    
    QQ --> SS{Renovação Aprovada?}
    SS -->|Sim| TT[Atualizar Contrato]
    SS -->|Não| RR
    
    TT --> J
    RR --> UU[Mover para: Concluído/Inativo]
    
    style A fill:#e8f5e8
    style KK fill:#f3e5f5
    style UU fill:#fff3e0
```

## 5. Fluxo de Alocação de Equipe

```mermaid
flowchart TD
    A[Necessidade de Alocação] --> B[Analisar Requisitos do Projeto]
    B --> C[Identificar Competências Necessárias]
    C --> D[Consultar Mapa de Competências]
    
    D --> E[Filtrar por Ferramenta]
    E --> F[Filtrar por Nível de Proficiência]
    F --> G[Verificar Disponibilidade]
    
    G --> H{Colaboradores Disponíveis?}
    H -->|Não| I[Buscar Alternativas]
    H -->|Sim| J[Avaliar Fit Técnico]
    
    I --> K{Realocar de Outros Projetos?}
    K -->|Sim| L[Negociar Realocação]
    K -->|Não| M[Buscar Recursos Externos]
    
    L --> N{Realocação Aprovada?}
    N -->|Sim| O[Executar Realocação]
    N -->|Não| M
    
    M --> P{Recursos Externos Disponíveis?}
    P -->|Sim| Q[Contratar Temporariamente]
    P -->|Não| R[Escalar para Liderança]
    
    O --> J
    Q --> S[Integrar ao Time]
    R --> T[Decisão Estratégica]
    
    S --> J
    T --> U{Aprovar Contratação?}
    U -->|Sim| V[Processo de Contratação]
    U -->|Não| W[Renegociar Escopo/Prazo]
    
    V --> X[Aguardar Novo Colaborador]
    W --> Y[Ajustar Projeto]
    
    X --> Z[Onboarding Novo Colaborador]
    Y --> AA[Continuar com Recursos Disponíveis]
    
    Z --> J
    AA --> J
    
    J --> BB[Formar Equipe Ideal]
    BB --> CC[Definir Papéis e Responsabilidades]
    CC --> DD[Comunicar Alocação]
    DD --> EE[Iniciar Projeto]
    
    style A fill:#e3f2fd
    style EE fill:#e8f5e8
    style R fill:#fff3e0
```

## 6. Fluxo de Automações Críticas

```mermaid
flowchart TD
    A[Evento Trigger] --> B{Tipo de Evento?}
    
    B -->|Cliente → Implantação| C[Auto-criar Projeto]
    B -->|Projeto Concluído| D[Auto-mover Cliente → CS]
    B -->|Prazo Próximo| E[Enviar Notificação]
    B -->|Dados Incompletos| F[Alertar Responsável]
    
    C --> G[Aplicar Template Onboarding]
    G --> H[Vincular Cliente ao Projeto]
    H --> I[Definir Status: Planejamento]
    I --> J[Notificar Equipe]
    
    D --> K[Criar Atividades CS]
    K --> L[Agendar Health Check]
    L --> M[Designar CS Manager]
    M --> N[Notificar Transição]
    
    E --> O{Tipo de Prazo?}
    O -->|Projeto| P[Notificar Líder Projeto]
    O -->|Atividade CS| Q[Notificar CS Manager]
    O -->|Renovação| R[Notificar Comercial]
    
    F --> S{Tipo de Dado?}
    S -->|Perfil Colaborador| T[Notificar RH]
    S -->|Info Cliente| U[Notificar Account Manager]
    S -->|Status Projeto| V[Notificar Líder Projeto]
    
    J --> W[Aguardar Ação Manual]
    N --> W
    P --> W
    Q --> W
    R --> W
    T --> W
    U --> W
    V --> W
    
    W --> X[Ação Executada]
    X --> Y[Atualizar Status]
    Y --> Z[Log da Automação]
    
    style A fill:#e3f2fd
    style Z fill:#e8f5e8
```

---

## 7. Pontos de Decisão Críticos

### 7.1 Gates de Qualidade
- **Gate 1**: Aprovação técnica na pré-venda
- **Gate 2**: Disponibilidade de recursos para implantação
- **Gate 3**: Aceite do cliente em cada milestone
- **Gate 4**: Transição bem-sucedida para CS

### 7.2 Escalações Automáticas
- **Falta de recursos**: Escalar para liderança em 24h
- **Atraso em projeto**: Notificar stakeholders em 48h
- **Problemas de CS**: Alertar gerência em tempo real
- **Dados incompletos**: Lembrete diário até resolução

### 7.3 Métricas de Fluxo
- **Tempo médio por fase**: Pré-venda (7 dias), Implantação (30 dias), CS (contínuo)
- **Taxa de conversão**: Pré-venda → Implantação (80%), Implantação → CS (95%)
- **Satisfação**: NPS > 8 em cada transição de fase

---

**Próximos Passos:**
1. Validar fluxos com equipes operacionais
2. Identificar pontos de automação adiciais
3. Definir templates para cada fase
