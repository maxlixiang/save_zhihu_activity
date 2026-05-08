# 如何比较Gemini CLI和Claude Code？

---

其实我本身以为大部分人开了 Gemini 会员后，都会多少用一下 [Gemini CLI](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=Gemini+CLI&zhida_source=entity)。
但实际上和一些朋友聊下来，使用 Gemini CLI 的比例很少，甚至使用 Antigravity 的也不多。
大部分人用的还只是网页版，而习惯用终端工作的朋友，80% 用的是 Claude code。
Gemini CLI 正好处在一个尴尬的地位，论方便程度，它不如网页版，论 agent 能力它不如 claude code。
但是，但是，它免费啊！
你就是用性价比超高的 [DeepSeek](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=DeepSeek&zhida_source=entity) 它也是按量付费，但 Gemini CLI，你只要有个谷歌账号就能开始用了。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948782503.jpg)
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948784119.webp)
目前的免费用户，每天请求次数是 1000 次，每分钟最多 60 次请求。
1000 次请求是啥概念？
输入一行命令，AI 回复一行，这算 1 次。即使每 1 分钟提问一次，也需要连续不停地提问 16.6 个小时 才能用完这 1,000 次额度。
如果你正好有个 PRO 会员，那就更好了，每天 1500 次请求，轻量的代码任务也可以满足了。
注意了！
这里说的请求（PRO 版）不是降智的低端模型，而是谷歌最新的 gemini-3.1-pro-preview，就是 DeepSeek V4 官宣对比测试中，稍逊一筹的 gemini-3.1-pro-preview。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948784404.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='988' height='1760'></svg>)
说句谷歌大圣人也不为过了，这玩意人家是真给啊！
而且对于轻量任务，也确实好用。你可以把一些基础的工作交给它。
**上周，我把管理 [obsidian](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=obsidian&zhida_source=entity) 的任务交给了 Gemini CLI。**
就是参考 [Karpathy](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=Karpathy&zhida_source=entity) 的思路，把自己的 obsidain 某个文件夹做成一个 wiki 百科。
这里我只让它管理一个文件夹，而不是整个 vault，这样会更轻量，任务也更明确。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948785135.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='402' height='208'></svg>)
我让它帮我找笔记里所有 gemini 的用法。这东西在散落在十几篇不同的文章里，我自己都记不清写了哪些。
但它可以直接通过 wiki 寻找到相关内容把这些内容从各个角落捞出来，重新整理、串联，写成了一篇新笔记，存进新的 md 文件。
我每次写完文章，都让它帮我更新一次 wiki，这样写过所有的内容都可以串起来，形成一个知识库，随用随取。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948785835.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1812' height='1172'></svg>)
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948786517.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1808' height='464'></svg>)
如果你之前没有用过终端，只是用过网页版聊天，相信我，这绝对是一次奇妙的体验。
不是因为它做对了。是因为大部分人习惯了网页版 Gemini 的"问-答-复制-粘贴"。
CLI 版跳过了后面两步。同一个 Gemini，同一个 Gemini 3.1 Pro 模型。
但 99%的人在网页版里用了它半年，从来不知道它能这么干。
这是两种完全不同的工具，恰好叫同一个名字。
**安装也非常的简单**
把你的魔法工具配好，安装好 node.js ， 然后终端依次执行下面命令。
# 全局安装 npm install -g @google/gemini-cli # 验证安装 gemini --version
搞定。
安装好了后，在终端输入 gemini ，按下回车，选择 Sign in with Google ，用你的谷歌账号登录上就行了。
登录之后的界面是这样的。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948786935.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1680' height='756'></svg>)
你可以使用/model 命令切换模型，右下角查看额度使用量，上面一点还能看到 gemini.md文件和 skill 数量。
那么它相对网页版有哪些优势？
**1M 上下文让它可以一次读完你的整个知识库**
网页版 Gemini 能聊多少轮？不好说，体感上聊十几轮之后它会开始忘。Google 官方也没给一个明确的数字，甚至模型是不是满血也很不好说，网页版的上下文窗口一直是个黑盒。
CLI 版的数字是公开的。100 万 token。而且是满血。
这是什么概念？一百万个 token 能一次装下整个中大型项目的代码库，或者你积累了五六年的 Obsidian vault。
启动方式很简单。
打开终端，进到你的 Obsidian 仓库目录，执行：
cd /path/to/your-obsidian-vault gemini
这里有一个很多人第一次用会踩到的坑：启动后终端可能显示 "This folder is untrusted" 的警告。这是 Gemini CLI 的隐私防火墙，默认禁止 AI 读取任何未授权的本地目录。输入以下命令授权：
/trust .
授权记录会被保存在 ~/.gemini/trustedFolders.json 里。以后想撤销某个目录的权限，编辑这个文件删掉对应路径就行了。
过了这道权限墙，Gemini CLI 就能读取你整个 vault 的所有文件。
剩下的就是根据你的工作流，和它对话就行了，有什么活直接吩咐它去干。
网页版 Gemini 也能回答你的问题，但它只能就你当前对话里给的那点信息作答，虽然现在也能用 notebookLM，但是你想保存到本地管理，总是隔了那么一层。
CLI 版能读完你积累了多年的全部笔记，然后在全局视角下给你答案，并且直接帮你整理好。
上下文不是技术参数。是它对你了解多少。
**Agent 能力让它能干活**
网页版 Gemini 的交互方式只有一种：你打字，它回复，你手动去执行。
浏览器的界面决定了它最多只能给你信息，不能帮你管理。
CLI 版的 Gemini 换了一套架构。
它底层跑的是 [ReAct](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=ReAct&zhida_source=entity)（Reason + Act）循环——理解任务 → 调用工具 → 读结果 → 推理下一步 → 继续执行 → 完成汇报。
它内置了文件系统操作（读、写、编辑文件）、Shell 命令执行、Google Search 实时搜索、Web 内容抓取。你给任务，它会自己想办法搞定。
你可以让它自动生成每日总结，Gemini CLI 会自动扫描当天修改过的所有文件、读内容、按模板维度整理、生成日报、写入对应文件夹。整个过程它自己搞定，不用你手动翻文件、不用复制粘贴、不用格式化。
你可以让它代码辅助，进入项目目录，启动 Gemini CLI。让它分析项目架构，它会自动读取文件树和关键模块，给出一份结构分析。发现一个报错，告诉它错误信息，它会自动追踪调用链、定位问题文件、直接修改代码，修改前展示 diff 让你确认。一个文件里重复代码太多，让它重构，它直接动手改。
有第三方机构 [Composio](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=Composio&zhida_source=entity) 做过对比测试：同一个复杂任务，[Claude Code](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=Claude+Code&zhida_source=entity) 平均 1 小时 17 分钟完成，Gemini CLI 需要约 2 小时 2 分钟。代码质量上 Claude Code 有优势，尤其在多文件重构场景。但对于大多数日常任务「修 Bug、写脚本、生成脚手架、重构单个文件」差距并不明显。
而 Claude Code 每月至少 20 刀，Gemini CLI 零。
还可以辅助内容创作。
这是我开始用 Gemini CLI 之后最常用的场景。核心就是在 Obsidian 里跑 Gemini CLI。
流程是这样的：让 Gemini CLI 读取 Obsidian 里的历史文章 → 学习写作风格 → 给灵感选题 → 起标题 → 检索素材库找金句 → 自动写入当前文章 → 通过 [MCP](https://zhida.zhihu.com/search?content_id=779698457&content_type=Answer&match_order=1&q=MCP&zhida_source=entity) 调用 Minimax 生成配图 → 嵌入文章 → 手动发布。
AI 的输出是初稿和素材，人的判断和改写在每一个环节参与。
**MCP 万能接口**
Gemini CLI 最被低估的能力，不在它自己身上，在它能连什么。
网页版 Gemini 被困在浏览器里。它能看到的世界，只有你当前这个标签页的对话框。CLI 版通过 MCP（Model Context Protocol）能接入 GitHub、连 Notion、读写 Obsidian、调 Supabase 查数据库.
它不仅知道 Gemini 模型能回答什么，它知道你硬盘里有什么、你的 Git 仓库里有什么、你的笔记应用里有什么。
怎么把 Gemini CLI 嵌进 Obsidian：
1.
在 Obsidian 插件市场搜索 "Terminal"，安装
2.
打开插件配置，选择你的终端类型（macOS 选 macOS），在参数栏加一个 -l
3.
cmd+p 调出命令面板，搜"终端"，选"整合式"，右侧会出现终端窗口
4.
在终端里装 Gemini CLI（已经装好的就不用装了）：npm install -g @google/gemini-cli
5.
输入 gemini，登录 Google 账号
6.
首次使用 cd 到你的 vault 目录，执行 /trust . 授权
搞完之后，Gemini CLI 就住在了你的 Obsidian 旁边。左边是笔记编辑器，右边是 AI 终端——Agent 能读写你的仓库、管理你的知识库、辅助你写文章。
配置 MCP 也很简单。在项目根目录创建 .gemini/settings.json：
{ "mcpServers": { "github": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": { "GITHUB\_PERSONAL\_ACCESS\_TOKEN": "your\_token\_here" } }, "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/workspace"] } } }
重启 Gemini CLI，这些外部服务会自动挂载。用 /mcp 命令可以查看所有已连接的服务。
MCP 这个协议不是 Gemini 专属的, Claude Code 也支持。
但 Gemini CLI 把 MCP 配到了零门槛，再加上它是免费的，你等于不花一分钱就拿到了一个可以调度你全部数字工具的 AI 中枢。
每次我跟人安利完 Gemini CLI，对方都会问同一个问题：免费的，靠谱吗？会不会哪天突然收费或者砍掉？
这个问题的答案，不在产品里，在商业模式里。
**免费是最有底气的商业模式**
说到这里，有一个避不开的问题：Google 为什么要把这东西免费开源？
不只是因为 Google 大方。
Google 的搜索引擎年收入是一个天文数字，谷歌云在这次公布的财报中增长 63%。
AI 不是它主要收入来源，但却是它未来主要的增长动力。
它免费给所有人用，抢占 AI 的入口权。
换个角度。Anthropic 的收入是 API 调用费和订阅。Cursor 的收入是什么？用户的 $20/月。
它们每降一美元，都在直接割自己的营收。它们也想免费，但免费之后活不下去。
这就是不对称战争。不是价格战。
价格战双方都疼。是 Google 拿一个广告印钞机养的产品，去砸对手的核心收入来源。
Composio 的数据确实说了，Claude Code 在代码质量上比 Gemini CLI 更好。但不重要。
重要的不是谁现在更好用。而是谁能获得更多的用户，谁有更深的财力支持，谁有更强大的基础设施。Gemini CLI 它用 1M 上下文、Agent 能力、有 MCP 生态，免费获取客户，不断进化，不断和行业顶尖水平对齐。
而且 Gemini CLI 态度很好，更新很快，有问题也及时解决。前些时正式上线了子代理功能，挺好用的。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948789131.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1912' height='1156'></svg>)
代码质量的差距可以用时间抹平，付费用户也自然会涌向服务更好，生态更好，更稳定的产品。
**它毛病也挺多**
Gemini CLI 有些非常不好的坏习惯，它偶尔会主动替我做决定，执行 skill 能力也不太强。
最近准备做个游戏，结果被它整的有点崩溃。
它总是会主动发起改我内容的选项。
![](%5B2026-05-05_10-39%5D%20%E5%A6%82%E4%BD%95%E6%AF%94%E8%BE%83Gemini%20CLI%E5%92%8CClaude%20Code%EF%BC%9F/_1777948790435.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1722' height='704'></svg>)
不过除了这些，整体还是很好的。
越来越好用，越来越顺手，而且量大便宜。
目前 claude ，GPT，都发布了新模型，现在就等 gemini 了。
**说到最后**
如果你一直只用 Gemini 网页版，打开终端试一试。
同一个模型，同一个 Google 账号，敲一下 gemini。
让它去触碰你的文件、你的笔记、你的代码、你的其他工具。
第一次看到它直接往你的电脑里写文件的时候，你也会愣一下。
然后你就回不去了。
文章首发于公号「甲子渡口」

---
### 💬 精选评论 (第一页)

> **羚羊**：pro模型老是429你是一点都不提啊，至少1个月前是这样
>
> **MKFLA**：怎么说呢，1500次也分模型的，Pro的额度很少，主要给的多的是flash和lite[滑稽]
>
> **苏Su**：antigravity都没法用了，geminiCli能用？节点换了个遍都不行[尴尬]
>
> **青麻青空**：虽然但是，你只是需要知识库的话为什么不直接用notebooklm
>
> **文若**：现在的问题是谷歌账号国内很难申请了，手机验证卡的太死
>
> **MaAaM**：google cli 几分钟十几分钟才能响应，免费又有什么用呢？排队罢了。
>
> **基本无害**：你的时间很宝贵，用gemini cli 做一个项目的时间，cc和 codex做完四五个任务了
>
> **小机箱典王**：你用过嘛，pro高峰期经常个位数token/s你就慢慢等吧你[酷]
>
> **逐漸腐儒的大學生**：Antigravity之前那麼多香甜的Opus額度誒
>
> **发哥**：我是Gemini CLI的主力用户，大部分时间都在Gemini CLI上。但是有一点有一说一，Gemini CLI真的会跑偏，真的很不爽。
>
> **ShingU**：正好昨晚试了一下，Google现在比较认国家地区，国内想找个合适的节点有点麻烦😮‍💨
>
> **董不懂**：cli 免费用户也用不了3.1Pro啊
>
> **alinnb**：哪来的 1500 次，不可能的
>
> **chen justin**：确实，免费里最大方的还是gemini
>
> **LastWhisper**：gemini-cli 我们自己内部都用的吐血 直接 hanging 到死，不过最近有新东西要出来了，我用下来感觉挺不错的，等 IO 了。
>