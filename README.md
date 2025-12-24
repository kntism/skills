# 🎯 Agent Skills - Awesome Skills Collection

> A comprehensive collection of pre-built Agent Skills to supercharge your AI workflow

![Skills](https://img.shields.io/badge/Skills-Collection-blue?style=for-the-badge&logo=robot&logoColor=white)
![Last Updated](https://img.shields.io/badge/Updated-November%202025-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📖 Introduction

Welcome to the **Agent Skills Collection** - your ultimate resource for enhancing AI agent capabilities with specialized skills. This repository contains a curated collection of ready-to-use skills that extend AI agent functionality across various domains, from development and design to content creation and productivity.

**What are Agent Skills?**
Agent Skills are modular packages containing instructions, scripts, and resources that AI agents can dynamically load when relevant to a task. They transform general-purpose AI agents into specialized assistants capable of handling specific workflows, tools, or domains. While originally popularized by Claude, Agent Skills are now a universal pattern for extending AI agent capabilities across platforms.

---

## ✨ Featured Skills by Category

### 🚀 Development & Programming
- **[clean-code-checker](./clean-code-checker/)** - Code quality analysis and optimization following Clean Code principles
- **[subagent-driven-development](./subagent-driven-development/)** - Execute implementation plans with independent task dispatching
- **[using-git-worktrees](./using-git-worktrees/)** - Create isolated development environments with git worktrees
- **[test-driven-development](./test-driven-development/)** - Write tests before implementation code
- **[mcp-builder](./mcp-builder/)** - Build high-quality MCP servers for external integrations
- **[requesting-code-review](./requesting-code-review/)** - Request comprehensive code reviews before major features
- **[receiving-code-review](./receiving-code-review/)** - Receive and implement code review feedback effectively
- **[model-trainer](./model-trainer/)** - Train and fine-tune language models using TRL on Hugging Face Jobs infrastructure

### 🎨 Design & Creative
- **[artifacts-builder](./artifacts-builder/)** - Create complex HTML artifacts using React, Tailwind CSS, and shadcn/ui
- **[canvas-design](./canvas-design/)** - Generate beautiful visual designs and artwork
- **[brand-guidelines](./brand-guidelines/)** - Apply consistent branding across your projects
- **[theme-factory](./theme-factory/)** - Apply pre-set themes to your artifacts and projects
- **[slack-gif-creator](./slack-gif-creator/)** - Create animated GIFs optimized for Slack

### 📝 Content & Writing
- **[content-research-writer](./content-research-writer/)** - Research-assisted content creation with proper citations
- **[changelog-generator](./changelog-generator/)** - Generate user-friendly changelogs from git commits
- **[brainstorming](./brainstorming/)** - Refine ideas into fully-formed designs through collaborative questioning

### 📊 Data & Business
- **[xlsx](./document-skills/xlsx/)** - Create and manage Excel spreadsheets with formulas
- **[docx](./document-skills/docx/)** - Generate professional Word documents
- **[pptx](./document-skills/pptx/)** - Build compelling PowerPoint presentations
- **[pdf](./document-skills/pdf/)** - Work with PDF documents and fillable forms
- **[hugging-face-dataset-creator](./hugging-face-dataset-creator/)** - Create and manage datasets on Hugging Face Hub
- **[hugging-face-evaluation-manager](./hugging-face-evaluation-manager/)** - Add and manage evaluation results in Hugging Face model cards
- **[hugging-face-paper-publisher](./hugging-face-paper-publisher/)** - Publish and manage research papers on Hugging Face Hub
- **[competitive-ads-extractor](./competitive-ads-extractor/)** - Analyze competitors' advertising strategies
- **[lead-research-assistant](./lead-research-assistant/)** - Identify high-quality business leads
- **[invoice-organizer](./invoice-organizer/)** - Organize invoices and receipts for tax preparation

### 🧠 Productivity & Organization
- **[file-organizer](./file-organizer/)** - Intelligently organize files and folders across your computer
- **[domain-name-brainstormer](./domain-name-brainstormer/)** - Generate and check domain name availability
- **[raffle-winner-picker](./raffle-winner-picker/)** - Pick random winners for giveaways and contests
- **[meeting-insights-analyzer](./meeting-insights-analyzer/)** - Analyze meeting transcripts for behavioral patterns
- **[internal-comms](./internal-comms/)** - Write professional internal communications

### 🔧 System & DevOps
- **[webapp-testing](./webapp-testing/)** - Test local web applications using Playwright
- **[video-downloader](./video-downloader/)** - Download videos from various platforms
- **[condition-based-waiting](./condition-based-waiting/)** - Replace arbitrary timeouts with condition polling

### 🎓 Learning & Development
- **[writing-plans](./writing-plans/)** - Create detailed implementation plans for engineers
- **[writing-skills](./writing-skills/)** - Write and test new skills before deployment
- **[finishing-a-development-branch](./finishing-a-development-branch/)** - Complete development work with structured options
- **[verification-before-completion](./verification-before-completion/)** - Verify work before claiming completion
- **[systematic-debugging](./systematic-debugging/)** - Four-phase debugging framework
- **[root-cause-tracing](./root-cause-tracing/)** - Trace bugs back to their source
- **[dispatching-parallel-agents](./dispatching-parallel-agents/)** - Dispatch multiple agents for independent investigations
- **[executing-plans](./executing-plans/)** - Execute implementation plans in controlled batches
- **[testing-anti-patterns](./testing-anti-patterns/)** - Prevent common testing mistakes
- **[testing-skills-with-subagents](./testing-skills-with-subagents/)** - Verify skills work under pressure
- **[defense-in-depth](./defense-in-depth/)** - Implement validation at multiple system layers
- **[using-superpowers](./using-superpowers/)** - Establish mandatory workflows for finding and using skills

---

## 📦 Installation

### For Claude Code Users (Plugin Marketplace)

The easiest way to install and manage skills is through the Claude Code Plugin Marketplace:

```bash
# 1. Add this repository as a marketplace
/plugin marketplace add kntism/skills

# 2. Browse available skills
/plugin marketplace list

# 3. Install individual skills
/plugin install test-driven-development@top-agent-skills
/plugin install frontend-design@top-agent-skills
/plugin install brainstorming@top-agent-skills

# 4. Or install all skills at once
/plugin install all-skills@top-agent-skills
```

### Available Skills

The marketplace includes 50+ skills organized by category:

| Category | Skills |
|----------|--------|
| **Development** | `test-driven-development`, `systematic-debugging`, `mcp-builder`, `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `subagent-driven-development` |
| **Design** | `frontend-design`, `artifacts-builder`, `canvas-design`, `brand-guidelines`, `theme-factory`, `slack-gif-creator` |
| **AI/ML** | `model-trainer`, `hugging-face-dataset-creator`, `hugging-face-evaluation-manager`, `hugging-face-paper-publisher` |
| **Content** | `content-research-writer`, `changelog-generator`, `brainstorming`, `internal-comms` |
| **Productivity** | `file-organizer`, `invoice-organizer`, `meeting-insights-analyzer`, `domain-name-brainstormer`, `raffle-winner-picker` |
| **Testing** | `webapp-testing`, `condition-based-waiting`, `testing-anti-patterns`, `testing-skills-with-subagents` |
| **Workflow** | `writing-plans`, `writing-skills`, `finishing-a-development-branch`, `verification-before-completion` |

### Update Skills

```bash
# Update the marketplace to get the latest skills
/plugin marketplace update kntism/skills

# Update individual installed skills
/plugin update test-driven-development@top-agent-skills
```

### Manual Installation

For Claude Code and other compatible platforms:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kntism/skills.git
   cd skills
   ```

2. **Copy skill folders** to your agent's skills directory:
   ```bash
   # For Claude Code
   cp -r test-driven-development ~/.claude/skills/

   # Or copy all skills
   cp -r */ ~/.claude/skills/

   # For other platforms, check your agent's documentation
   # for the correct skills directory path
   ```

3. **Restart your AI agent application** to load the new skills

### Universal Compatibility

These skills follow the standard Agent Skills format and can be adapted for:
- **Claude Code** - Native support via `/plugin marketplace`
- **Claude API** - Load skills as context for API calls
- **Other AI Agents** - Adapt skill structure for your platform
- **Custom Implementations** - Use skill patterns in your own agent framework

---

## 🚀 Getting Started

### For Users

1. **Browse Skills**: Explore the categories above to find skills that match your needs
2. **Install via Marketplace**: Use `/plugin marketplace add kntism/skills` for easy installation
3. **Or Install Manually**: Copy skill folders to your `~/.claude/skills` directory
4. **Use Automatically**: Claude will automatically load relevant skills when needed

### For Developers

1. **Create Custom Skills**: Use the `skill-creator` skill to generate new skills
2. **Follow Structure**: Each skill should contain:
   - `SKILL.md` - Skill description and usage instructions
   - `LICENSE.txt` - License information
   - Additional scripts and resources as needed
3. **Share with Community**: Submit pull requests to add new skills to the collection

---

## 🎯 Key Benefits

### ✨ Composable
Skills stack together automatically. AI agents identify which skills are needed and coordinate their use seamlessly.

### 📦 Portable
Skills use a consistent format. Build once, use across different AI platforms and applications.

### ⚡ Efficient
Only loads what's needed, when it's needed, keeping AI agents fast while accessing specialized expertise.

### 🔧 Powerful
Skills can include executable code for tasks where traditional programming is more reliable than AI generation alone.

### 🌐 Universal
Works across different AI platforms that support the Agent Skills pattern.

---

## 🛠️ How to Contribute

We welcome contributions! Here's how you can help:

1. **Add New Skills**: Create a new folder with your skill and a `SKILL.md` file
2. **Improve Existing Skills**: Enhance documentation or add new features
3. **Report Issues**: Open issues for bugs or improvement suggestions
4. **Share Examples**: Add usage examples to skill documentation

### Skill Requirements
- Must include a `SKILL.md` file with clear description and usage instructions
- Must include a `LICENSE.txt` file (MIT license recommended)
- Should provide clear value for users
- Should follow the existing structure and format

---

## 📚 Documentation

### For Claude Users
- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)

### General Resources
- [Anthropic Academy](https://www.anthropic.com/learn/build-with-claude)
- [Agent Skills Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### Skill Creation
- Use the `skill-creator` skill for interactive guidance
- Follow the [engineering blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) for deep technical insights

---

## 🔗 Related Projects

- [Anthropic/skills](https://github.com/anthropics/skills) - Official Claude skills repository
- [claude-cookbooks](https://github.com/anthropics/claude-cookbooks) - Comprehensive cookbook and examples
- [Claude Developer Platform](https://www.claude.com/platform/api) - API documentation
- [Claude Code](https://code.claude.com/) - Desktop application documentation

---

## ⚠️ Security Notice

Agent Skills may include executable code and system access. While powerful, this means being mindful about which skills you use. Always:

- Stick to trusted sources to keep your data safe
- Review skills before installation
- Only use skills from reputable creators
- Be cautious with skills that request system access or sensitive data
- Test skills in isolated environments before production use

---

## 📄 License

This collection is licensed under the MIT License. See individual skill folders for specific license information.

---

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) - For creating Claude and pioneering the Agent Skills framework
- The AI agent community - For contributing and testing these skills across platforms
- All skill authors - For their innovative and useful contributions
- Contributors who help adapt skills for universal compatibility

---

## 📞 Support

- 📖 [Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- 💬 [Community Support](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)
- 🐛 [Issue Tracker](../../issues)
- 💡 [Feature Requests](../../issues/new)

---

**Made with ❤️ by the [aiskills.top](https://www.aiskills.top/)**

---

*Last updated: November 2025*