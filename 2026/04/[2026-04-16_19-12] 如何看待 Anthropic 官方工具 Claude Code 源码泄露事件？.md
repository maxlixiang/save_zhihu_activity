# 如何看待 Anthropic 官方工具 Claude Code 源码泄露事件？

---

基本上把[Claude code](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=Claude+code&zhida_source=entity)泄露的源码摸透了，并把这9个思想提取成了skill。
明白了这些，你大概能理解CC的工程是如何构建的。
你可以直接把这些Skill安装到claude code里，按需使用。  
也可以未来内嵌在自己的Agent当中。
可以在这里直接下载安装使用：  
[https://claudeleakage.com/zh/opensource-for-dev/](https://link.zhihu.com/?target=https%3A//claudeleakage.com/zh/opensource-for-dev/)
做完这些，下一步就是应用到各种业务场景中了。
以下是详细介绍
---
## 一、记忆与上下文管理
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366089253.jpg)
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366090967.webp)
### memory-architect
**title**：[MEMORY.md](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=MEMORY.md&zhida_source=entity) 快 200 行了，帮我清理重构一下
**what**：扫描现有 MEMORY.md，将内容段落拆分为「索引层（指针）→ 主题文件（内容）→ 归档层（历史）」三层结构，确保索引始终保持在 200 行以内，每条仅为一行指针。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366091343.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
### [compact-with-memory](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=compact-with-memory&zhida_source=entity)
**title**：/compact，但别丢掉这次会话的关键决策
**what**：压缩前先回顾整个对话，提取做了哪些决策、走了哪些弯路、当前卡在哪，写入 MEMORY.md 对应主题文件，再执行标准压缩。压缩后，下次会话可以重建本次推理过程，而不只是状态结果。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366092813.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
### [session-dream](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=session-dream&zhida_source=entity)
**title**：保存这次会话的关键发现，/dream
**what**：按 autoDream 的四阶段流程（定向 → 采集信号 → 整合 → 修剪索引）回顾当前对话，识别值得持久化的内容，写入或更新 MEMORY.md 主题文件，并同步更新索引指针。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366094497.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
### [context-budget-planner](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=context-budget-planner&zhida_source=entity)
**title**：帮我规划这次大重构的 context 预算
**what**：按任务阶段估算 token 消耗，对照 autoCompact 的四级触发阈值（警告区 / 错误区 / 自动压缩触发点 13,000 tokens / 阻塞线 3,000 tokens），输出各阶段预算分配表和推荐手动 /compact 的检查点位置。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366096210.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
## 二、Prompt 与缓存优化
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366097738.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
### [prompt-architect](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=prompt-architect&zhida_source=entity)
**title**：优化我的 CLAUDE.md，提高 prompt cache 命中率
**what**：扫描 CLAUDE.md，识别混入静态区的动态内容（时间戳、当前路径、状态变量等缓存破坏源），按 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 模式重构为静态前缀 + 动态后缀，使稳定内容最大化命中 Anthropic prompt cache。
**title**：减少 API 费用，诊断为什么缓存命中率这么低
**what**：依据 `promptCacheBreakDetection.ts` 中的 14 个失效向量，逐项检测 CLAUDE.md、MCP 服务配置、settings.json 的缓存破坏点，输出 0–100 评分报告，并按破坏频率从高到低排列修复建议。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366099070.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
## 三、 多 Agent 架构
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366100437.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
### agent-squad-designer
**title**：为我的项目设计 Agent 团队，规划多 Agent 工作流
**what**：输出一份 Agent 团队设计文档，包含每个 Agent 的单一职责定义、工具权限白名单/黑名单、`whenToUse` 路由字段，以及 orchestrator 如何综合子 Agent 结果而非下放决策权。可附带生成各 Agent 的 `.md` 文件模板。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366101263.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
### delegation-rules
**title**：设计 orchestrator/worker 模式，避免 orchestrator 和 sub-agent 重复工作
**what**：生成一份委派规则文档，明确哪些任务保留在 orchestrator 主上下文处理、哪些下放给 sub-agent，并提供自包含 sub-agent prompt 的写法规范——让每个 sub-agent 在不知道上下文的情况下也能独立执行。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366101736.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
## 四、场景切换与自主模式
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366103431.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
### [context-persona-switch](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=context-persona-switch&zhida_source=entity)
**title**：帮我为不同仓库设置不同的 Claude 行为规则
**what**：设计基于环境信号（git remote、工作目录、分支名前缀）的自动人格切换规则，为每个 persona 定义输出限制列表（禁止提及的内容、必须过滤的词汇），默认在检测模糊时落回限制最严的 persona。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366104886.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
### [autonomous-mode-scaffold](https://zhida.zhihu.com/search?content_id=777756834&content_type=Answer&match_order=1&q=autonomous-mode-scaffold&zhida_source=entity)
**title**：帮我配置离场自主工作，我不在的时候让 Claude 自动运行
**what**：参照 KAIROS 模式生成自主工作配置文档，包含存在感检测策略、边界定义（哪些操作需要用户确认）、tick 心跳处理逻辑，以及空闲时必须调用 SleepTool 而非输出文字的约束规则。
![](%5B2026-04-16_19-12%5D%20%E5%A6%82%E4%BD%95%E7%9C%8B%E5%BE%85%20Anthropic%20%E5%AE%98%E6%96%B9%E5%B7%A5%E5%85%B7%20Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%EF%BC%9F_%E5%9B%BE%E7%89%87/_1776366105616.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='1200'></svg>)
---
*开源地址：[claude-code-skill](https://link.zhihu.com/?target=https%3A//claudeleakage.com/zh/opensource-for-dev/)*