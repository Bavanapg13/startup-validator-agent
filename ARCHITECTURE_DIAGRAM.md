# Startup Validator Agent - System Architecture Diagram

## High-Level Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        CLI["CLI/Web Interface"]
        INPUT["User Startup Idea Input"]
    end
    
    subgraph "Configuration & Setup"
        CONFIG["config.py<br/>API Keys, Settings"]
        PROMPTS["prompts.py<br/>AI Prompts"]
    end
    
    subgraph "Core Agent Modules"
        IA["Idea Analyzer<br/>idea_analyzer.py"]
        MA["Market Analyzer<br/>market_analyzer.py"]
        RA["Risk Analyzer<br/>risk_analyzer.py"]
        FG["Feature Generator<br/>feature_generator.py"]
        MP["MVP Planner<br/>mvp_planner.py"]
        TP["Timeline Planner<br/>timeline_planner.py"]
    end
    
    subgraph "Processing Engine"
        LLM["LLM Engine<br/>Claude/GPT API"]
        PROCESSOR["Response Processor<br/>utils.py"]
    end
    
    subgraph "Data & Support"
        UTILS["Utilities<br/>Helper Functions"]
        MEMORY["Analysis Memory<br/>Context Storage"]
    end
    
    subgraph "Output Layer"
        REPORT["Report Generator"]
        OUTPUT["Analysis Output<br/>6-Step Report"]
    end
    
    %% User Flow
    CLI --> INPUT
    INPUT --> IA
    
    %% Configuration Flow
    CONFIG -.->|Settings| IA
    PROMPTS -.->|Prompts| IA
    
    %% Analysis Modules
    IA --> LLM
    MA --> LLM
    RA --> LLM
    FG --> LLM
    MP --> LLM
    TP --> LLM
    
    INPUT --> MA
    INPUT --> RA
    INPUT --> FG
    INPUT --> MP
    INPUT --> TP
    
    %% Processing
    LLM --> PROCESSOR
    PROCESSOR --> MEMORY
    
    %% Utilities Support
    IA -.->|Use| UTILS
    MA -.->|Use| UTILS
    RA -.->|Use| UTILS
    FG -.->|Use| UTILS
    MP -.->|Use| UTILS
    TP -.->|Use| UTILS
    
    %% Output
    MEMORY --> REPORT
    REPORT --> OUTPUT
    OUTPUT --> CLI
    
    %% Styling
    classDef interface fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef module fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef engine fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef output fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    
    class CLI,INPUT interface
    class IA,MA,RA,FG,MP,TP module
    class LLM,PROCESSOR engine
    class REPORT,OUTPUT output
```

---

## Detailed Component Architecture

```mermaid
graph LR
    subgraph INPUT["INPUT LAYER"]
        A["User Startup Idea"]
    end
    
    subgraph CONFIG["CONFIGURATION"]
        B["API Configuration"]
        C["Model Settings"]
        D["Prompt Templates"]
    end
    
    subgraph ANALYSIS["ANALYSIS MODULES"]
        E["Step 1: Feasibility"]
        F["Step 2: Market"]
        G["Step 3: Risk"]
        H["Step 4: Improvement"]
        I["Step 5: MVP Roadmap"]
        J["Step 6: Timeline"]
    end
    
    subgraph ENGINE["LLM ENGINE"]
        K["Prompt Construction"]
        L["API Call Handler"]
        M["Response Parsing"]
    end
    
    subgraph PROCESSING["POST PROCESSING"]
        N["Data Validation"]
        O["Format Conversion"]
        P["Context Aggregation"]
    end
    
    subgraph OUTPUT["OUTPUT LAYER"]
        Q["Final Report"]
        R["Recommendations"]
        S["Action Items"]
    end
    
    A --> B
    A --> E
    A --> F
    A --> G
    A --> H
    A --> I
    A --> J
    
    B --> K
    C --> K
    D --> K
    
    E --> K
    F --> K
    G --> K
    H --> K
    I --> K
    J --> K
    
    K --> L
    L --> M
    
    M --> N
    N --> O
    O --> P
    
    P --> Q
    Q --> R
    R --> S
    
    style INPUT fill:#e3f2fd
    style CONFIG fill:#f5f5f5
    style ANALYSIS fill:#fff9c4
    style ENGINE fill:#f3e5f5
    style PROCESSING fill:#e0f2f1
    style OUTPUT fill:#c8e6c9
```

---

## Data Flow Diagram

```mermaid
graph TD
    A["📝 User Input<br/>Startup Idea"] 
    B["✓ Input Validation"]
    C["🔄 Parallel Analysis<br/>6 Modules"]
    D["🤖 LLM Processing<br/>Claude API"]
    E["📊 Response Aggregation"]
    F["✨ Report Formatting"]
    G["📋 Final Output<br/>6-Step Analysis"]
    
    A -->|validated| B
    B -->|parsed| C
    C -->|prompts sent| D
    D -->|responses| E
    E -->|structures data| F
    F -->|compiled| G
    
    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style B fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style C fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    style D fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style E fill:#e0f2f1,stroke:#004d40,stroke-width:2px
    style F fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    style G fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
```

---

## Technology Stack

| Layer | Technology | Component |
|-------|-----------|-----------|
| **Frontend** | Python CLI | main.py |
| **Config** | Python | config.py |
| **Agents** | Python Classes | agent/*.py |
| **LLM** | Claude/OpenAI API | LLM Engine |
| **Utils** | Python | utils.py |
| **Prompts** | Prompt Templates | prompts/prompts.py |

---

## Dependencies & Interactions

```
main.py
├── config.py (Settings & API keys)
├── utils.py (Helper functions)
├── prompts/prompts.py (Prompt templates)
└── agent/
    ├── idea_analyzer.py (Uses LLM, utils)
    ├── market_analyzer.py (Uses LLM, utils)
    ├── risk_analyzer.py (Uses LLM, utils)
    ├── feature_generator.py (Uses LLM, utils)
    ├── mvp_planner.py (Uses LLM, utils)
    └── timeline_planner.py (Uses LLM, utils)
```

---

## Key Features

✅ **Modular Design** - Each analysis module is independent
✅ **Scalable** - Easy to add new analysis modules
✅ **Configurable** - Centralized configuration management
✅ **Extensible** - Supports multiple LLM providers
✅ **Maintainable** - Clear separation of concerns
