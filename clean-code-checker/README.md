# Clean Code Checker Skill

这是一个根据Clean Code编码准则检查和优化代码的技能，支持JavaScript、TypeScript和Python。

## 功能特点

- **多语言支持**: JavaScript、TypeScript、Python
- **系统性检查**: 逐一检查10项Clean Code准则
- **智能分析**: 自动检测代码质量问题
- **优化建议**: 提供具体的改进建议
- **自动重构**: 应用批准的优化措施

## Clean Code准则

技能将检查以下准则：

1. **命名规范** - 变量、函数、类的命名清晰性
2. **函数设计** - 短小、单一职责、清晰的参数列表
3. **注释规范** - 有意义的注释，避免无用的注释
4. **代码格式** - 一致的缩进、空格、换行
5. **错误处理** - 适当的异常处理和错误信息
6. **重复代码** - 识别和消除重复代码
7. **复杂度控制** - 减少嵌套、控制循环复杂度
8. **可测试性** - 便于单元测试的代码结构
9. **设计模式** - 适当使用设计模式
10. **魔法数字** - 消除硬编码值

## 使用方法

### 1. 代码分析

```bash
python scripts/analyze_code.py --file <文件路径> --language <js|ts|python> [--output json]
```

**示例:**
```bash
# 分析JavaScript文件
python scripts/analyze_code.py --file src/example.js --language js

# 分析Python文件并以JSON格式输出
python scripts/analyze_code.py --file src/example.py --language python --output json
```

### 2. 代码重构

```bash
python scripts/refactor_code.py --file <文件路径> --language <js|ts|python> [--rules 规则列表] [--dry-run]
```

**示例:**
```bash
# 重构所有规则
python scripts/refactor_code.py --file src/example.js --language js

# 仅应用特定规则
python scripts/refactor_code.py --file src/example.js --language js --rules fix_naming shorten_functions

# 预览更改而不实际修改
python scripts/refactor_code.py --file src/example.js --language js --dry-run
```

### 3. 技能验证

```bash
python scripts/validate_skill.py --help
```

## 示例代码

### JavaScript问题代码示例

```javascript
// 问题代码
function old_style_function() {
    var user_data = get_user_data();
    var processed_data = process_data(user_data);
    var result = save_to_db(processed_data);
    return result;
}

function calculate_total(items) {
    var total = 0;
    for (var i = 0; i < items.length; i++) {
        total = total + items[i].price * 0.15; // 魔法数字
        // 错误处理不当
        try {
            if (items[i].price < 0) throw new Error("Negative price");
        } catch (e) {
            console.log("Error occurred");
        }
    }
    return total;
}
```

### 分析结果

```
Clean Code Analysis Report
File: example.js
Language: JS
Total Violations: 14

[ERROR] Line 4: Use camelCase: user_data
   Suggestion: Change variable/function name to camelCase
   Code: var user_data = get_user_data();

[ERROR] Line 6: Use camelCase: processed_data
   Suggestion: Change variable/function name to camelCase
   Code: var processed_data = process_data(user_data);

[WARN] Line 10: Function is too long (38 lines)
   Suggestion: Break down into smaller functions
   Code: function calculate_total(items) {...}

[INFO] Line 14: Potential magic number: 15
   Suggestion: Replace with a named constant
   Code: total = total + items[i].price * 0.15;
```

## 技能结构

```
clean-code-checker/
├── SKILL.md                    # 技能定义和说明
├── README.md                   # 使用说明
├── scripts/                     # 工具脚本
│   ├── analyze_code.py          # 代码分析工具
│   ├── refactor_code.py         # 代码重构工具
│   └── validate_skill.py        # 技能验证工具
├── references/                   # 参考资料和指南
│   └── clean_code_principles.md # Clean Code原则详解
└── assets/                      # 示例和模板
    ├── javascript-example.js   # JavaScript示例代码
    └── python-example.py        # Python示例代码
```

## 语言特性

### JavaScript/TypeScript
- 遵循camelCase命名约定
- 使用const/let声明变量
- 优先使用箭头函数
- 使用模板字符串
- 遵循ESLint规则

### Python
- 遵循snake_case命名约定
- 遵循PEP 8风格指南
- 使用f-string格式化
- 使用上下文管理器
- 添加类型提示

## 最佳实践

1. **增量优化**: 一次处理一个问题，逐步改进
2. **备份重要代码**: 重构前自动创建备份
3. **理解建议**: 仔细阅读每个优化建议
4. **测试更改**: 重构后运行测试确保功能正常
5. **持续学习**: 参考Clean Code原则文档

## 扩展功能

这个技能可以轻松扩展支持：
- 更多编程语言
- 额外的Clean Code规则
- 集成开发环境
- 版本控制系统
- 持续集成管道

## 反馈和支持

如果你在使用过程中遇到问题或有改进建议，请：
1. 查看参考文档中的Clean Code原则
2. 使用验证工具检查技能配置
3. 尝试不同的分析选项
4. 参考示例代码学习最佳实践