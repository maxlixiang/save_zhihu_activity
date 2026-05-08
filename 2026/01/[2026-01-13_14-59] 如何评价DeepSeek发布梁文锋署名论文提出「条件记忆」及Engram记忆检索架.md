# 如何评价DeepSeek发布梁文锋署名论文，提出「条件记忆」及Engram记忆检索架构？有哪些亮点？

---

[DeepSeek](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=DeepSeek&zhida_source=entity)这个[Engram](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=Engram&zhida_source=entity)成果会成为[LLM](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=LLM&zhida_source=entity)发展的分水岭，我愿称LLM自身也进入了Vibe时代。
## 打个比方
以前的LLM没有专有记忆体，所谓的记忆实际上是通过运算的模拟，都是算出来一个结果，并不是真的从记忆体读取出来的结果。
如果LLM好比一个程序员，那也是一个没有任何基础框架的程序员，每次新开项目，他都利用他超强的编程能力，快速从头撸出React.js、SpringBoot这样的框架，然后才基于这些框架开发这个项目的专有功能。
没错，这就是我们常说的『重复发明轮子』，虽然LLM这个程序员好像每次也能把事情搞定，但是还是浪费太多精力在重复造轮子上，如果能让他能直接使用现有框架，那他表现肯定更好。
![](%5B2026-01-13_14-59%5D%20%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7DeepSeek%E5%8F%91%E5%B8%83%E6%A2%81%E6%96%87%E9%94%8B%E7%BD%B2%E5%90%8D%E8%AE%BA%E6%96%87%E6%8F%90%E5%87%BA%E3%80%8C%E6%9D%A1%E4%BB%B6%E8%AE%B0%E5%BF%86%E3%80%8D%E5%8F%8AEngram%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2%E6%9E%B6_%E5%9B%BE%E7%89%87/_1775635019524.jpg)
![](%5B2026-01-13_14-59%5D%20%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7DeepSeek%E5%8F%91%E5%B8%83%E6%A2%81%E6%96%87%E9%94%8B%E7%BD%B2%E5%90%8D%E8%AE%BA%E6%96%87%E6%8F%90%E5%87%BA%E3%80%8C%E6%9D%A1%E4%BB%B6%E8%AE%B0%E5%BF%86%E3%80%8D%E5%8F%8AEngram%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2%E6%9E%B6_%E5%9B%BE%E7%89%87/_1775635020091.webp)
注意：不是『不要重复发明轮子』，是『你不必每次都重复发明轮子』
如果让这个程序员干脆[Vibe Coding](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=Vibe+Coding&zhida_source=entity)，简单代码自动生成，那他就能还更多精力考虑架构、设计、优化这些更重要的问题，岂不是更好！
这个Engram就是这样，让LLM别每次都从头发明轮子了，一些基本信息去知识库里面去找，只需要O(1)时间复杂度，这不就减少了大量的计算量。
![](%5B2026-01-13_14-59%5D%20%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7DeepSeek%E5%8F%91%E5%B8%83%E6%A2%81%E6%96%87%E9%94%8B%E7%BD%B2%E5%90%8D%E8%AE%BA%E6%96%87%E6%8F%90%E5%87%BA%E3%80%8C%E6%9D%A1%E4%BB%B6%E8%AE%B0%E5%BF%86%E3%80%8D%E5%8F%8AEngram%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2%E6%9E%B6_%E5%9B%BE%E7%89%87/_1775635020550.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2556' height='1412'></svg>)
## 为啥叫Conditional Memory
就好比[MoE](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=MoE&zhida_source=entity)(Mixture of Experts)是Conditional Computation，有选择地激活参数来运算，Engram也是根据条件来选择如何读取现有记忆，所以是Conditional Memory。
还是拿程序员打比方，如果一个程序员所有代码全都自己从头写，那肯定浪费时间，同样，如果一个程序员所有代码都是copy-paste，那这个程序员也肯定是个渣渣。
要有条件地选择去使用现有的轮子，甚至有时候真的需要重新发明轮子，如果人类不重复发明轮子，那我们现在用的轮子还和下图最左边的那个一样。
![](%5B2026-01-13_14-59%5D%20%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7DeepSeek%E5%8F%91%E5%B8%83%E6%A2%81%E6%96%87%E9%94%8B%E7%BD%B2%E5%90%8D%E8%AE%BA%E6%96%87%E6%8F%90%E5%87%BA%E3%80%8C%E6%9D%A1%E4%BB%B6%E8%AE%B0%E5%BF%86%E3%80%8D%E5%8F%8AEngram%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2%E6%9E%B6_%E5%9B%BE%E7%89%87/_1775635021245.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='343'></svg>)
最好的结果当然是平衡——简单的、已经被证明的逻辑，可以用现成的，在Vibe Coding里就是直接按Tab键就好；复杂的、新鲜的问题，就需要程序员从头思考，仔细设计，甚至手工敲入代码。
其实就是在MoE和Engram之间的平衡。
## 什么是[U-Shaped Workflow](https://zhida.zhihu.com/search?content_id=765187127&content_type=Answer&match_order=1&q=U-Shaped+Workflow&zhida_source=entity)
DeepSeek的论文发现，当MoE占主导的时候，模型的Loss就会偏大（Loss大不是好事），当两者平衡的时候，Loss才偏小，也就形成U形。
![](%5B2026-01-13_14-59%5D%20%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7DeepSeek%E5%8F%91%E5%B8%83%E6%A2%81%E6%96%87%E9%94%8B%E7%BD%B2%E5%90%8D%E8%AE%BA%E6%96%87%E6%8F%90%E5%87%BA%E3%80%8C%E6%9D%A1%E4%BB%B6%E8%AE%B0%E5%BF%86%E3%80%8D%E5%8F%8AEngram%E8%AE%B0%E5%BF%86%E6%A3%80%E7%B4%A2%E6%9E%B6_%E5%9B%BE%E7%89%87/_1775635022907.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='974' height='722'></svg>)
还是按照程序员打比方，一个程序员如果每个项目都是从头开始，不用现有框架，不Vibe Coding，那他没有发挥最大威力；同样，一个程序员如果只会Ctrl-C和Ctrl-V，只会Vibe Coding，那他也干不出啥像样东西。
所以，Vibe可以，但不要全Vibe；Copy-Paste可以，但不要全Copy-Paste。
## 写在最后
有了Engram之后，LLM就不只是计算，不只是靠计算模拟记忆，而且有了明确的记忆能力。
也就是说，同样的模型参数，可以支持更强大的智能。
**让一个本来很厉害的程序员可以Vibe Coding，你说可怕不可怕**。
这是一个理论突破，很期待DeepSeek在接下来发布的模型中展示这个理论突破的实际威力。
咱2月份见！