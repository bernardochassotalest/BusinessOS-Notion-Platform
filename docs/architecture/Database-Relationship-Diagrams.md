# Diagramas de Relacionamento entre Bases de Dados
## Business OS Integrado no Notion

**Versão:** 1.0  
**Data:** 06 de Setembro de 2025  
**Status:** Em Validação

---

## 1. Diagrama Entidade-Relacionamento (ERD) Principal

```mermaid
erDiagram
    CLIENTES {
        string nome_empresa PK
        string fase_jornada
        date data_inicio
        number valor_contrato
        text proxima_acao
        string created_by
        datetime created_time
        datetime last_edited_time
    }
    
    PROJETOS {
        string nome_projeto PK
        string status
        date prazo
        date data_inicio
        number progresso
        number orcamento
        string created_by
        datetime created_time
    }
    
    COLABORADORES {
        string nome_colaborador PK
        string email UK
        string cargo
        string disponibilidade
        string senioridade
        file foto
        datetime created_time
    }
    
    MAPA_COMPETENCIAS {
        string competencia PK
        string ferramenta
        string nivel_proficiencia
        date data_certificacao
        text observacoes
        datetime created_time
    }
    
    ATIVIDADES {
        string tarefa PK
        string status
        string tipo
        date data_prevista
        date data_execucao
        number duracao
        datetime created_time
    }
    
    CATALOGO_PRODUTOS {
        string nome_produto PK
        text descricao
        number preco
        string categoria
        boolean ativo
    }
    
    CLIENTES ||--o{ PROJETOS : "possui"
    CLIENTES ||--o{ ATIVIDADES : "relaciona"
    CLIENTES }o--o{ COLABORADORES : "equipe_responsavel"
    CLIENTES }o--o{ CATALOGO_PRODUTOS : "produtos_contratados"
    
    PROJETOS }o--|| COLABORADORES : "lider_projeto"
    PROJETOS }o--o{ COLABORADORES : "equipe_projeto"
    
    COLABORADORES ||--o{ MAPA_COMPETENCIAS : "possui"
    COLABORADORES ||--o{ ATIVIDADES : "responsavel"
    
    MAPA_COMPETENCIAS }o--|| COLABORADORES : "pertence"
```

## 2. Diagrama de Cardinalidade Detalhado

```mermaid
graph TB
    subgraph "CLIENTES (1)"
        C1[Nome da Empresa]
        C2[Fase da Jornada]
        C3[Data Início]
        C4[Valor Contrato]
    end
    
    subgraph "PROJETOS (N)"
        P1[Nome do Projeto]
        P2[Status]
        P3[Prazo]
        P4[Progresso]
    end
    
    subgraph "COLABORADORES (N)"
        CO1[Nome do Colaborador]
        CO2[Cargo]
        CO3[Disponibilidade]
        CO4[Email]
    end
    
    subgraph "MAPA_COMPETENCIAS (N)"
        M1[Competência]
        M2[Ferramenta]
        M3[Nível Proficiência]
        M4[Data Certificação]
    end
    
    subgraph "ATIVIDADES (N)"
        A1[Tarefa]
        A2[Status]
        A3[Tipo]
        A4[Data Prevista]
    end
    
    C1 -->|1:N| P1
    C1 -->|1:N| A1
    C1 -->|N:M| CO1
    
    P1 -->|N:1| CO1
    P1 -->|N:M| CO1
    
    CO1 -->|1:N| M1
    CO1 -->|1:N| A1
    
    style C1 fill:#e3f2fd
    style P1 fill:#f3e5f5
    style CO1 fill:#e8f5e8
    style M1 fill:#fff3e0
    style A1 fill:#fce4ec
```

## 3. Diagrama de Fluxo de Dados

```mermaid
flowchart LR
    subgraph "Entrada de Dados"
        E1[Formulário Cliente]
        E2[Template Projeto]
        E3[Perfil Colaborador]
        E4[Registro Competência]
        E5[Log Atividade]
    end
    
    subgraph "Processamento"
        P1[Validação]
        P2[Relacionamento]
        P3[Automação]
        P4[Notificação]
    end
    
    subgraph "Armazenamento"
        S1[(Base Clientes)]
        S2[(Base Projetos)]
        S3[(Base Colaboradores)]
        S4[(Base Competências)]
        S5[(Base Atividades)]
    end
    
    subgraph "Saída"
        O1[Dashboard Pipeline]
        O2[Dashboard Talentos]
        O3[Relatórios]
        O4[Alertas]
    end
    
    E1 --> P1 --> S1
    E2 --> P1 --> S2
    E3 --> P1 --> S3
    E4 --> P1 --> S4
    E5 --> P1 --> S5
    
    S1 --> P2
    S2 --> P2
    S3 --> P2
    S4 --> P2
    S5 --> P2
    
    P2 --> P3 --> P4
    
    S1 --> O1
    S2 --> O1
    S3 --> O2
    S4 --> O2
    S5 --> O3
    
    P4 --> O4
    
    style S1 fill:#e3f2fd
    style S2 fill:#f3e5f5
    style S3 fill:#e8f5e8
    style S4 fill:#fff3e0
    style S5 fill:#fce4ec
```

## 4. Matriz de Relacionamentos

| Base Origem | Base Destino | Tipo Relação | Cardinalidade | Campo Chave | Descrição |
|-------------|--------------|--------------|---------------|-------------|-----------|
| CLIENTES | PROJETOS | 1:N | Um cliente pode ter múltiplos projetos | cliente_id | Projetos vinculados ao cliente |
| CLIENTES | ATIVIDADES | 1:N | Um cliente pode ter múltiplas atividades | cliente_id | Atividades relacionadas ao cliente |
| CLIENTES | COLABORADORES | N:M | Múltiplos colaboradores por cliente | equipe_responsavel | Equipe alocada ao cliente |
| PROJETOS | COLABORADORES | N:1 | Um projeto tem um líder | lider_projeto | Líder responsável pelo projeto |
| PROJETOS | COLABORADORES | N:M | Múltiplos colaboradores por projeto | equipe_projeto | Time do projeto |
| COLABORADORES | MAPA_COMPETENCIAS | 1:N | Um colaborador tem múltiplas competências | colaborador_id | Competências do colaborador |
| COLABORADORES | ATIVIDADES | 1:N | Um colaborador executa múltiplas atividades | responsavel_id | Atividades do colaborador |
| CLIENTES | CATALOGO_PRODUTOS | N:M | Cliente pode contratar múltiplos produtos | produtos_contratados | Produtos/serviços contratados |

## 5. Diagrama de Dependências Funcionais

```mermaid
graph TD
    subgraph "Dependências Primárias"
        A[COLABORADORES] --> B[MAPA_COMPETENCIAS]
        C[CLIENTES] --> D[PROJETOS]
        C --> E[ATIVIDADES]
        A --> E
    end
    
    subgraph "Dependências Secundárias"
        D --> F[Alocação de Equipe]
        B --> F
        F --> G[Execução do Projeto]
        G --> H[Transição para CS]
        H --> E
    end
    
    subgraph "Dependências de Negócio"
        I[Qualificação Lead] --> C
        C --> J[Aprovação Cliente]
        J --> D
        D --> K[Conclusão Projeto]
        K --> L[Ativação CS]
        L --> E
    end
    
    style A fill:#e8f5e8
    style C fill:#e3f2fd
    style D fill:#f3e5f5
    style E fill:#fce4ec
```

## 6. Diagrama de Integridade Referencial

```mermaid
flowchart TD
    subgraph "Regras de Integridade"
        R1[Cliente deve existir antes do Projeto]
        R2[Colaborador deve existir antes da Competência]
        R3[Cliente e Colaborador devem existir antes da Atividade]
        R4[Projeto deve ter pelo menos um Colaborador]
        R5[Colaborador deve ter pelo menos uma Competência]
    end
    
    subgraph "Validações Automáticas"
        V1[Verificar existência de referências]
        V2[Validar cardinalidade mínima]
        V3[Verificar consistência de status]
        V4[Validar datas lógicas]
    end
    
    subgraph "Ações em Cascata"
        C1[Deletar Cliente → Arquivar Projetos]
        C2[Deletar Colaborador → Reatribuir Atividades]
        C3[Alterar Status Cliente → Atualizar Projetos]
        C4[Concluir Projeto → Criar Atividades CS]
    end
    
    R1 --> V1
    R2 --> V1
    R3 --> V1
    R4 --> V2
    R5 --> V2
    
    V1 --> C1
    V2 --> C2
    V3 --> C3
    V4 --> C4
    
    style R1 fill:#ffebee
    style V1 fill:#fff3e0
    style C1 fill:#e8f5e8
```

## 7. Diagrama de Índices e Performance

```mermaid
graph TB
    subgraph "Índices Primários"
        I1[CLIENTES.nome_empresa]
        I2[PROJETOS.nome_projeto]
        I3[COLABORADORES.nome_colaborador]
        I4[MAPA_COMPETENCIAS.competencia]
        I5[ATIVIDADES.tarefa]
    end
    
    subgraph "Índices Secundários"
        S1[CLIENTES.fase_jornada]
        S2[PROJETOS.status]
        S3[COLABORADORES.disponibilidade]
        S4[MAPA_COMPETENCIAS.ferramenta]
        S5[ATIVIDADES.status]
    end
    
    subgraph "Índices Compostos"
        C1[MAPA_COMPETENCIAS.ferramenta + nivel]
        C2[ATIVIDADES.cliente + status]
        C3[PROJETOS.cliente + status]
        C4[COLABORADORES.cargo + disponibilidade]
    end
    
    subgraph "Consultas Frequentes"
        Q1[Buscar colaboradores por competência]
        Q2[Listar projetos por cliente]
        Q3[Filtrar atividades por status]
        Q4[Dashboard pipeline por fase]
    end
    
    C1 --> Q1
    I1 --> Q2
    C2 --> Q3
    S1 --> Q4
    
    style I1 fill:#e3f2fd
    style S1 fill:#f3e5f5
    style C1 fill:#e8f5e8
    style Q1 fill:#fff3e0
```

## 8. Diagrama de Sincronização e Automações

```mermaid
sequenceDiagram
    participant C as CLIENTES
    participant P as PROJETOS
    participant CO as COLABORADORES
    participant A as ATIVIDADES
    participant M as MAPA_COMPETENCIAS
    
    Note over C: Cliente move para "Implantação"
    C->>P: Trigger: Auto-criar Projeto
    P->>M: Consultar competências necessárias
    M->>CO: Identificar colaboradores disponíveis
    CO->>P: Alocar equipe ao projeto
    P->>A: Criar atividades iniciais
    
    Note over P: Projeto concluído
    P->>C: Mover cliente para "Ongoing CS"
    C->>A: Criar atividades recorrentes CS
    A->>CO: Designar CS Manager
    
    Note over A: Atividade com prazo próximo
    A->>CO: Notificar responsável
    
    Note over CO: Colaborador indisponível
    CO->>P: Verificar projetos afetados
    P->>CO: Buscar substituto
    CO->>A: Reatribuir atividades
```

## 9. Diagrama de Backup e Recuperação

```mermaid
flowchart TD
    subgraph "Dados Primários"
        D1[(CLIENTES)]
        D2[(PROJETOS)]
        D3[(COLABORADORES)]
        D4[(MAPA_COMPETENCIAS)]
        D5[(ATIVIDADES)]
    end
    
    subgraph "Backup Automático"
        B1[Backup Diário Notion]
        B2[Export Semanal JSON]
        B3[Export Mensal CSV]
    end
    
    subgraph "Armazenamento Backup"
        S1[Notion Internal]
        S2[Google Drive]
        S3[AWS S3]
    end
    
    subgraph "Recuperação"
        R1[Restore Parcial]
        R2[Restore Completo]
        R3[Migração Dados]
    end
    
    D1 --> B1 --> S1
    D2 --> B1 --> S1
    D3 --> B1 --> S1
    D4 --> B1 --> S1
    D5 --> B1 --> S1
    
    D1 --> B2 --> S2
    D2 --> B2 --> S2
    D3 --> B2 --> S2
    D4 --> B2 --> S2
    D5 --> B2 --> S2
    
    D1 --> B3 --> S3
    D2 --> B3 --> S3
    D3 --> B3 --> S3
    D4 --> B3 --> S3
    D5 --> B3 --> S3
    
    S1 --> R1
    S2 --> R2
    S3 --> R3
    
    style D1 fill:#e3f2fd
    style B1 fill:#e8f5e8
    style S1 fill:#fff3e0
    style R1 fill:#fce4ec
```

## 10. Considerações de Implementação

### 10.1 Ordem de Criação das Bases
1. **COLABORADORES** - Base fundamental para todo o sistema
2. **MAPA_COMPETENCIAS** - Depende de COLABORADORES
3. **CLIENTES** - Base central do negócio
4. **PROJETOS** - Depende de CLIENTES e COLABORADORES
5. **ATIVIDADES** - Depende de todas as anteriores
6. **CATALOGO_PRODUTOS** - Independente, pode ser criada em paralelo

### 10.2 Configuração de Relações
- **Relações bidirecionais**: Sempre configurar ida e volta
- **Nomes consistentes**: Usar convenção de nomenclatura clara
- **Validação**: Implementar regras de negócio nas fórmulas
- **Performance**: Limitar exibição de registros relacionados

### 10.3 Manutenção de Integridade
- **Auditorias regulares**: Verificação semanal de consistência
- **Limpeza de dados**: Remoção de registros órfãos
- **Monitoramento**: Alertas para inconsistências críticas
- **Documentação**: Manter registro de mudanças estruturais

---

**Próximos Passos:**
1. Validar estrutura de relacionamentos com stakeholders
2. Definir regras de negócio específicas para cada relação
3. Criar scripts de validação de integridade
4. Estabelecer procedimentos de manutenção
