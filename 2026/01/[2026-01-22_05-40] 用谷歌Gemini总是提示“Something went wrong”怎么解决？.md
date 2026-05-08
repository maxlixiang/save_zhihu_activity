# 用谷歌Gemini总是提示“Something went wrong”怎么解决？

---

> [个人博客仓库](https://link.zhihu.com/?target=https%3A//github.com/existed-name/Personal-Blogs/blob/main/%25E9%2597%25AE%25E9%25A2%2598%25E6%258E%2592%25E6%259F%25A5/%25E8%25A7%25A3%25E5%2586%25B3Gemini%25E5%25BC%2582%25E5%25B8%25B8%25EF%25BC%259ASomething%2520Went%2520Wrong.md)
---
## 1、背景
（1）2个Google号：老号（2024/9/7创建，1年多了）、小号（2025/12/25创建，不到4个星期）
（2）都是创建不久就被封，然后申诉成功，绑定手机号、恢复邮箱，养号（偶尔看看Gplay、Google、Chrome，以及Gmail收发邮件）
（3）老号登录Claude，小号登录Grok，都可以正常使用，Gmail没问题
（4）然而3个星期以来，Gemini一登录过后就是`Something went wrong`/`出了点问题，请稍后再试`，只能游客模式。Edge无痕浏览/普通窗口、隔一段时间就清除所有浏览数据，依然不行
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634446430.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2524' height='1269'></svg>)
## 3、结论
本人的原因是：**恢复邮箱绑定了但没验证**、**没打开2步验证**
## 2、解决过程
（1）问AI、网上搜，也没找到满意的解决方法。今天又搜了一下（可能是之前搜出来的文章不够新 ），看了[Something went wrong解决方法](https://zhuanlan.zhihu.com/p/1995194901005104334)这篇文章后，突然有个想法：会不会是我的**谷歌账号没设置全**？（后来证明确实如此）
（2）于是登录[Google Account](https://link.zhihu.com/?target=https%3A//myaccount.google.com/)，检查设置
（3）在`Security & sign-in`中，发现`Recovery emil`竟然没有验证（我记得之前绑定的时候验证过），于是验证邮箱
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634447244.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2559' height='1328'></svg>)
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634447749.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2551' height='1320'></svg>)
（4）然后设置`2-Step Verification`  
①点击`Authenticator`
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634448136.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2467' height='1851'></svg>)
②这里需要在手机下载验证器app，作为双因素验证（`2-Factor Authentication`）。`Microsoft Authenticator`/`Google Authenticator`都可以，前者手机应用商店就可以找到（可能就叫`Authenticator`），后者需要上网 + Gplay商店
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634448758.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='905' height='1920'></svg>)
③回到①，点击`Set up authenticator`
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634449208.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1823' height='737'></svg>)
④弹出二维码，用手机authenticator扫码
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634449821.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1065' height='980'></svg>)
⑤app会给出一个验证码，写上去
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634450472.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1065' height='977'></svg>)
⑥再`Turn on 2-Step Verification`
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634450981.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1666' height='1220'></svg>)
⑦他会要求`Get backup codes`，把备份码下载保存即可
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634451428.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1758' height='662'></svg>)
⑧完成
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634452069.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2497' height='1306'></svg>)
（5）从[https://gemini.google.com/gems/create?hl=en-US&pli=1](https://link.zhihu.com/?target=https%3A//gemini.google.com/gems/create%3Fhl%3Den-US%26pli%3D1)（创建智能体）这里间接进入Gemini
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634452689.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2553' height='1328'></svg>)
点击`New chat`后就可以正常对话了（之后也可以从首页进去了）
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634453323.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2546' height='1303'></svg>)
我的小号先是直接进Gemini首页，没成功，然后从上面那个网址进去就行了
## 4、补充
（1）除了上面的设置，记得检查**年龄**、**`Recovery phone`**，反正`Personal info`和`Security & sign-in`以及各种设置都检查一遍，确定要求`Verify`的都验证了
（2）语言似乎没有限制，我老号English( United States )，小号简体中文，都可以用，但是还是用英语更安全一点
（3）IP用的美国，可以在[https://ping0.cc/ip/](https://link.zhihu.com/?target=https%3A//ping0.cc/ip/)检测自己的IP风控值，尽量固定用最稳定干净的那个
我最“干净”的美国IP也只能到这里了 （然而也过了）：
> IP类型: IDC机房IP  
> 风控值: 40% 轻微风险  
> 原生IP: 原生IP  
> 大模型检测: 家庭宽带的概率为20%，可能为商业宽带或者机房宽带  
> 共享人数: 1000 - 10000 (高危)
（4）防封号（可以问GPT/Grok）
* 平时**注意养号**，偶尔看看Gmail、Google/Chrome、Gplay什么的；
* 尽量固定用（相对）稳定干净的IP，**不频繁切IP**；
* 刚注册的Google号可以养几天（新手期容易被封）再轻度使用Gemini（问简单问题），慢慢过渡
* **装成正常的美国用户**，比如模仿IP所在地的作息，在当地时间用Gemini（这也是AI建议的，好像也有点道理 ）
（5）[Google Account](https://link.zhihu.com/?target=https%3A//myaccount.google.com/)首页可能会提醒设置住址、绑卡，我老号点了`dismiss`，小号没管，可能不管他会安全一点
然后`Security & sign-in`最上面有个`Security Checkup`，他有个“增强型安全浏览”（`Enhanced Safe Browsing`），我怕开了会识破我的伪装（虽然他肯定早就知道了 ）
![](%5B2026-01-22_05-40%5D%20%E7%94%A8%E8%B0%B7%E6%AD%8CGemini%E6%80%BB%E6%98%AF%E6%8F%90%E7%A4%BA%E2%80%9CSomething%20went%20wrong%E2%80%9D%E6%80%8E%E4%B9%88%E8%A7%A3%E5%86%B3%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634453994.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1105' height='2039'></svg>)
（6）知乎/浏览器搜`Gemini Something Went Wrong`可以找到一堆文章，但是感觉新发布的要好一点
## 5、结语
本来准备从Edge转移到Chrome，用新的QQ邮箱或者微软的outlook邮箱，以及换更好的订阅来注册新Google号，不过不确定用原来的手机号行不行（换号码的话，虚拟手机号只是临时用，可能还要长期租号）……反正也是一堆麻烦 ，还好补全设置后就过了
目前轻度用一下Gemini，再观察几天、检查下需不需要其他设置
---
> 参考文章  
> [Something went wrong解决方法](https://zhuanlan.zhihu.com/p/1995194901005104334)