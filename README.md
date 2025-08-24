# AI Application Observability & Traceability Powered by LangSmith

This repository shows how to build AI applications with **LangChain** and **LangSmith**, with a special focus on **observability** and **traceability**—making it easy to monitor, debug, and understand every step your AI app takes in production.

## 🔍 What are LangChain and LangSmith?

### LangChain
**LangChain** is a framework for developing applications powered by language models. It provides:
- **Modular components** for building AI chains and agents
- **Standard interfaces** for working with different LLM providers
- **Built-in tools** for common AI tasks (memory, retrieval, etc.)
- **Easy integration** with various data sources and APIs

### LangSmith ⭐ (The Star of the Show!)
**LangSmith** is LangChain's **observability and debugging platform** that gives you:
- **Real-time tracing** of your AI application's execution
- **Performance monitoring** and metrics
- **Debugging tools** to understand why your AI made certain decisions
- **A/B testing** capabilities for prompt optimization
- **Production monitoring** for deployed AI applications

Think of LangSmith as your **AI application's black box** - it records every step, decision, and interaction, making it possible to understand, debug, and improve your AI systems.

## 🎯 Why Use LangSmith?

- **🔍 Debug AI Decisions**: See exactly how your AI arrived at an answer
- **📊 Monitor Performance**: Track response times, token usage, and success rates
- **🚀 Optimize Prompts**: A/B test different prompts to find the best ones
- **🐛 Fix Issues Fast**: Quickly identify where things go wrong in your AI chains
- **📈 Scale with Confidence**: Monitor production AI applications in real-time

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key

### Setup Steps

1. **Clone and navigate to the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-observability-langsmith
   ```

2. **Initialize the project with uv**
   ```bash
   uv init ai-observability-langsmith
   cd ai-observability-langsmith
   ```

3. **Create and activate virtual environment**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   uv add langchain-openai langchain langsmith
   ```

5. **Set up environment variables**
   Create a `.env` file in your project root:
   ```bash
   # .env
   OPENAI_API_KEY=your_openai_api_key_here
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   LANGCHAIN_PROJECT=your_project_name
   ```

6. **Get your LangSmith API key**
   - Visit [LangSmith](https://smith.langchain.com/)
   - Sign up/Login
   - Go to API Keys section
   - Create a new API key

7. **Run the app with uv**
   ```bash
   uv run langsmith-app.py

   uv run langsmith-app2.py
   ```

## 🔍 Viewing Traces in LangSmith
<img width="1201" height="737" alt="image" src="https://github.com/user-attachments/assets/592fb263-1df0-418c-88c9-80537e611951" />
<img width="1199" height="748" alt="image" src="https://github.com/user-attachments/assets/be92aff0-cbe3-4a2f-8796-c347dd78dc50" />

## 🔍 Viewing Monitoring in LangSmith
<img width="1420" height="573" alt="image" src="https://github.com/user-attachments/assets/9eca48e6-9c35-4066-8fb3-eba5fd4771ed" />
<img width="1221" height="710" alt="image" src="https://github.com/user-attachments/assets/0f5cb98a-dc50-4d24-a642-71592977700b" />

### 1. **Real-Time Tracing**
- Every function call decorated with `@traceable` is automatically traced
- Visit [LangSmith](https://smith.langchain.com/) to see your traces in real-time
- Each trace shows the complete execution flow of your AI application

### 2. **What You'll See in LangSmith**
- **Execution Timeline**: Step-by-step breakdown of your AI chain
- **Input/Output**: All inputs and outputs at each step
- **Token Usage**: Cost tracking and token consumption
- **Latency**: Response time for each component
- **Model Calls**: Detailed information about LLM interactions

### 3. **Debugging Features**
- **Trace Comparison**: Compare different runs to spot inconsistencies
- **Error Analysis**: See exactly where and why failures occur
- **Prompt Testing**: Test different prompts and compare results
- **Performance Metrics**: Identify bottlenecks in your AI chains

### 4. **Production Monitoring**
- **Success Rates**: Track how often your AI succeeds vs. fails
- **User Feedback**: Collect and analyze user satisfaction
- **Cost Tracking**: Monitor API usage and costs
- **Alerting**: Set up notifications for issues

## 🎯 Example Trace in LangSmith

## 🚀 Next Steps

1. **Explore LangSmith Dashboard**: Visit [smith.langchain.com](https://smith.langchain.com/) to see your traces
2. **Build Complex Chains**: Create multi-step AI workflows with different tools
3. **Add Memory**: Implement conversation memory using LangChain's memory components
4. **Integrate Tools**: Add external API calls and data retrieval
5. **Deploy**: Move your AI application to production with confidence

## 📚 Resources

- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith Blog](https://blog.langchain.dev/)
- [Community Discord](https://discord.gg/langchain)
