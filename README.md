# AI大模型RAG与智能体开发 (Agent Project)

## 📖 项目简介

本项目是一个基于 Python 构建的模块化 AI 应用框架，集成了 **检索增强生成 (RAG)** 和 **ReAct 智能体 (Agent)** 技术。项目采用配置驱动的设计模式，支持灵活切换大模型后端和向量数据库，旨在提供高效的知识问答与自主任务执行能力。

### 核心特性
- **🧠 ReAct Agent**: 基于推理-行动（Reasoning-Acting）循环的智能体，能够动态调用工具解决复杂问题。
- **📚 RAG 引擎**: 集成 Chroma 向量数据库，支持文档加载、切片、向量化及高精度语义检索。
- **⚙️ 配置化管理**: 使用 YAML 文件统一管理 LLM 参数、Prompt 模板、向量库配置及 Agent 行为策略。
- **🛠️ 可扩展工具集**: 模块化设计的工具中间件，便于自定义扩展 Agent 的能力边界。

## 🏗️ 项目结构

```text
.
├── agent/                  # 智能体核心模块
│   ├── tools/              # 工具定义与中间件
│   │   ├── agent_tools.py  # 具体工具实现 (如搜索、计算等)
│   │   └── middleware.py   # 工具调用中间件/拦截器
│   └── react_agent.py      # ReAct 算法主逻辑实现
├── config/                 # 配置文件目录 (YAML)
│   ├── agent.yml           # Agent 超参数配置 (迭代次数、超时等)
│   ├── chroma.yml          # Chroma 向量库连接配置
│   ├── prompts.yml         # 系统提示词与模板管理
│   └── rag.yml             # RAG 流程配置 (切片大小、重叠率等)
├── model/                  # 模型层
│   └── factory.py          # 模型工厂模式，统一创建 LLM 实例
├── rag/                    # RAG 核心模块
│   ├── rag_service.py      # RAG 业务逻辑服务 (索引、查询)
│   └── vector_store.py     # 向量数据库封装 (Chroma)
├── utils/                  # 通用工具类
│   ├── config_handler.py   # YAML 配置加载器
│   ├── file_handler.py     # 文件读写与预处理
│   ├── logger_handler.py   # 日志记录配置
│   ├── path_tool.py        # 路径处理工具
│   └── prompt_loader.py    # Prompt 模板加载器
├── app.py                  # 应用入口 / API 服务启动文件
├── README.md               # 项目说明文档
└── requirements.txt        # 依赖列表 (需自行创建)
```

## 🛠️ 技术栈

- **语言**: Python 3.9+
- **核心库**: 
  - `LangChain`: 编排 LLM 应用
  - `ChromaDB`: 轻量级向量数据库
  - `PyYAML`: 配置文件解析
- **模型支持**: 通过 [`model/factory.py`](\AI大模型RAG与智能体开发_Agent项目\model\factory.py) 支持多种 LLM (如 OpenAI, Qwen, ZhipuAI 等)。

## 🚀 快速开始

### 1. 环境安装

```bash
# 克隆项目
git clone <your-repo-url>
cd AI大模型RAG与智能体开发_Agent项目

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

在项目根目录创建 [.env]件，配置必要的 API Key：

```env
# 示例：通义千问 API Key
DASHSCOPE_API_KEY=your_api_key_here
# 或 OpenAI
OPENAI_API_KEY=sk-...
```

### 3. 修改配置文件

根据需求调整 [`config/`](\AI大模型RAG与智能体开发_Agent项目\config) 目录下的 YAML 文件：

- **[[rag.yml](\AI大模型RAG与智能体开发_Agent项目\config\rag.yml)](\AI大模型RAG与智能体开发_Agent项目\config\rag.yml)**: 调整文本切片大小 ([chunk_size](\AI\P4_RAG项目案例\config_data.py#L10-L10)) 和重叠 ([chunk_overlap](\AI\P4_RAG项目案例\config_data.py#L11-L11))。
- **[[prompts.yml](\AI大模型RAG与智能体开发_Agent项目\config\prompts.yml)](\AI大模型RAG与智能体开发_Agent项目\config\prompts.yml)**: 优化 RAG 回答提示词或 Agent 的系统指令。
- **[[chroma.yml](\AI大模型RAG与智能体开发_Agent项目\config\chroma.yml)](\AI大模型RAG与智能体开发_Agent项目\config\chroma.yml)**: 设置向量库持久化路径。

### 4. 运行项目

```bash
python app.py
```

## 💡 核心模块说明

### 1. RAG 服务 ([`rag/`](\AI大模型RAG与智能体开发_Agent项目\rag))
- **[[vector_store.py](\AI大模型RAG与智能体开发_Agent项目\rag\vector_store.py)](\AI大模型RAG与智能体开发_Agent项目\rag\vector_store.py)**: 封装了 Chroma 的初始化、文档添加和相似性搜索逻辑。
- **[[rag_service.py](\AI大模型RAG与智能体开发_Agent项目\rag\rag_service.py)](\AI大模型RAG与智能体开发_Agent项目\rag\rag_service.py)**: 协调文件加载、切片、嵌入和检索的全流程服务。

### 2. Agent 智能体 ([`agent/`](\AI大模型RAG与智能体开发_Agent项目\agent))
- **[[react_agent.py](\AI大模型RAG与智能体开发_Agent项目\agent\react_agent.py)](\AI大模型RAG与智能体开发_Agent项目\agent\react_agent.py)**: 实现 ReAct 范式，解析 LLM 输出，决定下一步是“思考”、“行动”还是“最终回答”。
- **[`tools/agent_tools.py`](\AI大模型RAG与智能体开发_Agent项目\agent\tools\agent_tools.py)**: 定义 Agent 可调用的具体工具函数。

### 3. 配置与工具 ([`utils/`](\AI大模型RAG与智能体开发_Agent项目\utils) & [`config/`](\AI大模型RAG与智能体开发_Agent项目\config))
- **[[config_handler.py](\AI大模型RAG与智能体开发_Agent项目\utils\config_handler.py)](\AI大模型RAG与智能体开发_Agent项目\utils\config_handler.py)**: 单例模式加载 YAML 配置，确保全局配置一致性。
- **[[prompt_loader.py](\AI大模型RAG与智能体开发_Agent项目\utils\prompt_loader.py)](\AI大模型RAG与智能体开发_Agent项目\utils\prompt_loader.py)**: 动态加载提示词模板，支持变量注入。

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/YourFeature`)
3. 提交更改 (`git commit -m 'Add some feature'`)
4. 推送到分支 (`git push origin feature/YourFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目遵循 MIT 许可证。
