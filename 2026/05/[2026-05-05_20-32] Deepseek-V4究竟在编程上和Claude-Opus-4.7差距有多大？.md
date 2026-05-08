# Deepseek-V4究竟在编程上和Claude-Opus-4.7差距有多大？

---

目前主流的编程 benchmark 就三个：**SWE-Bench Verified**、**SWE-Bench Pro** 和 **Terminal Bench 2.0**。下面 DeepSeek-V4-Pro 和 [DeepSeek-V4-Flash](https://zhida.zhihu.com/search?content_id=779675401&content_type=Answer&match_order=1&q=DeepSeek-V4-Flash&zhida_source=entity) 在这三个基准测试上与其它大模型的对比：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004972308.jpg)
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004972758.webp)
这里也简单介绍一下这三个基准测试。SWE-Bench Verified 由 [OpenAI](https://zhida.zhihu.com/search?content_id=779675401&content_type=Answer&match_order=1&q=OpenAI&zhida_source=entity) 于 2023 年 8 月提出，是业内长期使用的经典基准，主要评测大模型在真实软件工程修复任务中的能力[[1]](#ref_1)，它考的是：**模型能不能在真实开源项目里完成真实 GitHub Issue 的修复任务。**
原始的 SWE-Bench 是从大量开源仓库的真实 Issue 与 Pull Request 中构建任务。每个任务通常会提供一个真实代码仓库、一条描述 Bug 或功能需求的 Issue、修复前的代码版本，以及对应的测试用例。模型需要根据 Issue 理解问题、修改代码，并最终让测试通过。而 SWE-Bench Verified 则是在原版 SWE-Bench 基础上的“高质量人工筛选版”（500条）。OpenAI 对原始任务进行了人工审核与清洗，剔除了描述模糊、测试不稳定或评估标准存在问题的样本，使测试结果更稳定、更可信，也更能真实反映模型的工程修复能力。
不过，OpenAI 最近又发现这一基准本身存在明显缺陷：一部分题目的测试用例会误判正确解法，同时数据集还可能受到训练数据污染，导致成绩无法真实反映模型的实际软件工程能力。所以他们不再采用 SWE-bench Verified 作为核心评测标准[[2]](#ref_2)。
其实大家从上面的对比可以看到，除了比较变态的 Claude Mythos 和 [Opus 4.7](https://zhida.zhihu.com/search?content_id=779675401&content_type=Answer&match_order=1&q=Opus+4.7&zhida_source=entity)，大部分模型在SWE-Bench Verified 都达到了80+，指标已经趋于饱和。
OpenAI 放弃 SWE-bench Verified 之后，建议改用 SWE-bench Pro 来评估模型的编程能力。SWE-bench Pro 可以看作是 SWE-Bench Verified 的高难度版本，由 [Scale AI](https://zhida.zhihu.com/search?content_id=779675401&content_type=Answer&match_order=1&q=Scale+AI&zhida_source=entity) 在 2025 年 9 月推出[[3]](#ref_3)。一方面，为降低数据污染风险，其公开子集与开源隔离子集均采用强著佐权许可协议（如 GPL 协议）。另外一方面，这个评测集的难度要更大：每个任务至少需要修改 10 行代码，其中超过 100 个任务需要修改 100 行以上代码。所以，目前各家大模型在 SWE-bench Pro 上的得分都不高，基本都低于 60分。但是，Claude Mythos 和 Opus 4.7 均超过了 60 分。
如果拿 SWE-bench Pro 来衡量模型的编程能力的话，**DeepSeek-V4-Pro 应该是略差于 Kimi K2.6 和 GLM 5.1的**。
而**Terminal Bench 2.0**[[4]](#ref_4)，是一个专门评测 AI Agent 在 **命令行 / 终端环境中真实执行任务能力**的基准测试。它测的不是单纯答题能力，而是模型能否在 shell 环境里真正完成复杂任务。所以，Terminal Bench 2.0 考察的是模型 agentic coding 能力。看对比，这里 DeepSeek-V4-Pro 是略好于 Kimi K2.6 和 GLM 5.1。
除了公开评测集，我们还可以看看第三方平台的评测。
目前，Artificial Analysis 已经出了对 DeepSeek-V4 的评测，DeepSeek-V4-Pro 的Coding Index 达到了 47，和 Kimi K2.6相当，略好于 MiMo-V2.5-Pro（46）和 GLM 5.1 （43）。
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004972895.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='4640' height='1888'></svg>)
在 [Code Arena](https://zhida.zhihu.com/search?content_id=779675401&content_type=Answer&match_order=1&q=Code+Arena&zhida_source=entity) 的开源榜单上，DeepSeek-V4-Pro 目前排行第四，仅次于 GLM-5.1，Kimi K2.6 和 MiMo-V2.5-Pro：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004974643.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1889'></svg>)
如果看完整榜单的话，Claude Opus 4.7 排第一：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004976824.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1926'></svg>)
此外，还有一个 **Vibe Code Bench**[[5]](#ref_5)，这是一个面向端到端 Web 应用开发能力的基准测试集。每个任务都会要求模型在一个沙盒环境中，从零开始构建应用，并可使用浏览器、终端，以及常见生产级服务（例如身份认证、数据库、支付和邮件服务），最终，生成的应用将由一个自主浏览器 Agent 执行端到端操作流程，并根据各子步骤的完成情况进行评分。在这个基准测试上，DeepSeek-V4 的表现要好于 Kimi K2.6 和 GLM 5.1：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004978575.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1320' height='1532'></svg>)
此外 DeepSeek 也自建了内部编程评测集，发现了当前自己的模型在编程智能体方面要差于 Claude Opus 4.6。
具体来说，DeepSeek 从 50 多位公司工程师的真实研发任务中筛选出约 200 个高难度案例，覆盖开发、Bug 修复、重构和诊断等场景，并配套代码仓库、运行环境和人工评分标准，最终筛选出 30 个高质量任务作为评测集。结果显示，DeepSeek-V4-Pro 已明显优于 Claude Sonnet 4.5，并接近 Claude Opus 4.5，但相比 Claude Opus 4.6 仍有差距。
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004980134.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1626' height='328'></svg>)
综合各方的评测，我的结论是DeepSeek-V4-Pro 的编程能力应该和国产大模型Kimi K2.6 和 GLM 5.1 是接近的，但是应该还是差于国外的顶尖模型，比如 Claude Opus 4.7 和 GPT-5.5。
不过，就是 DeepSeek-V4-Pro 的输入价格有点小贵：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004980720.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1536' height='1024'></svg>)
但是现在官方宣布开启限时特惠，打2.5折，想测试的可以去看看。
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004982143.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1790' height='1516'></svg>)
最后放一个使用 API 测试的 SVG 生成对比：
![](%5B2026-05-05_20-32%5D%20Deepseek-V4%E7%A9%B6%E7%AB%9F%E5%9C%A8%E7%BC%96%E7%A8%8B%E4%B8%8A%E5%92%8CClaude-Opus-4.7%E5%B7%AE%E8%B7%9D%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9F/_1778004982736.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2841' height='1906'></svg>)
还是得上 max
## 参考
1. [^](#ref_1_0)<https://openai.com/index/introducing-swe-bench-verified/>
2. [^](#ref_2_0)<https://openai.com/zh-Hans-CN/index/why-we-no-longer-evaluate-swe-bench-verified/>
3. [^](#ref_3_0)<https://github.com/scaleapi/SWE-bench_Pro-os>
4. [^](#ref_4_0)<https://www.tbench.ai/>
5. [^](#ref_5_0)<https://www.vals.ai/benchmarks/vibe-code>

---
### 💬 精选评论 (第一页)

> **厂长L**：专业的内容没人点赞，那些搞个小 demo ，纯演示点赞那么多，太搞笑了。deepseek 打折只有 4 倍用量，正常的 coding plan 都是 10 倍起步，gpt pro 更是 50 倍的额度。ds 编程基本没有竞争力可言。
>
> **goto temp1**：实际上大模型发展到现在基本上都够用了，即使倒退一年，那时候用AI写代码都觉得整体不错，对开发者来说价格权重变得越来越大。
>
> **cyber**：实际用起来区别大吗?不论你用最贵最好的模型，还不是要一个个指令的去修复？实际场景中就没见什么模型能一次性调通全部代码的。结果是，乱七八糟的指令用了一大堆，github说你的额度用完了，老老实实回去用gpt. 99％的任务，便宜是硬道理。
>
> **沙耶博士**：glm5.1我自己用swe agent标准流程+swe agent配置最佳实践跑满过500个swe verified的实例，最终结果解决了391个问题，也就是78.2%。
> 
> 如果swe verified做满五百道题，那么最后的百分比小数位一定是偶数，也就是Xxx/500的百分比。如果跑出来了奇数只有两种可能：要么是分数完全造假，要么是500题里跳题了（比如说80.9%可以通过399/493，跳7题跑出来，93.7%可以通过461/495跳5题跑出来，最过分的有的模型自己发布的swe verified成绩跳了几十题）查看图片
>
> **Lyuih**：deepseek用起来体验不错的，而且还便宜
>
> **天清**：我是kimi code的20倍plan，体验很好
>
> **技术老幺**：这些参数评测没啥意义，就跟热身赛是冠军，正式比赛就拉胯
>
> **无名**：用过gemini3.1，gpt5.5，glm5，deepseek4，体感来说，前面两个很强很强，但是两者之间我还没有足够多的样本评价哪一个更好，差距多大。glm5用得最多（公司掏钱），有解决不了问题的时候，但是整体感觉已经能有效提升工作效率。ds4用的最少，能力也很强，体感很不错，肯定是超过glm5的。只因为是花同事的钱，没好意思多用。
>
> **吉哈德韦伯**：我试了下gemini pro preview，那个能力和gpt没法比，系统化理解代码项目的能力差的很，gpt一句话理解的事儿得我说好几遍，deepseek还在它下面吗[捂脸]
>
> **老杨**：文章很不错
>
> **华华**：请问文章中的手绘表格是怎么制作的呢
>