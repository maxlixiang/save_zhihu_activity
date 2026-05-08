# 如果只能学会一个AI工具，我推荐 Claude Code for VSCode（保姆级教程）

---

**文/猫哥AI量化**
*ps：2000字*
朋友们，晚上好。
之前领导给过一个任务，就是AI培训，在单位推广AI的使用。最近工作虽然比较忙，但这项工作并没有落下。很多同事并没有编程基础，所以想来想去，既可以提高工作效率，又能简单易上手的AI工具，非Claude Code莫属，而且它新推出的 Claude Skills 机制，非常便于拓展。
前阵子单位搞了个表情包大赛，我就使用Claude Code+即梦4.0接口 批量制作了一堆表情包去投稿（后面感兴趣可以细讲）。
如果使用 Claude Code，我建议通过 Vscode 的插件，它是 Anthropic 公司推出的，使用非常流畅。这样既可以看代码，也可以看AI干活。
以下内容都是来自我的课件，零基础也能轻松安装使用：
### **1.Python安装（如果已安装可跳过）**
真正的零基础，从安装编程语言开始。Python估计很多人都听说过，已安装的可以跳过，没安装过的也不需要了解太多，只需要知道安装这个，可以让AI帮我们完成更多的任务就行。
下载地址：[https://www.python.org/downloads/](https://link.zhihu.com/?target=https%3A//www.python.org/downloads/)
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634583202.jpg)
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634583587.jpg)
点击上图红框，就能下载安装包。请注意Win7无法安装，需要升级到Win10操作系统。
然后在D盘新建一个文件夹，命名为Python。双击安装包，**全部勾选下方选框，**然后点击第2个 Customize installation：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634583741.jpg)
**全部勾选，然后点击下一步：**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634583898.jpg)
**然后选择D盘，安装地址选择刚才新建的Python文件夹，其他按照默认，一直点下一步即可。（安装到E、F、G等硬盘也可以）**
### **2.安装Node.js（如果已安装可跳过）**
1. 1. 访问Node.js官网：[https://nodejs.org/zh-cn](https://link.zhihu.com/?target=https%3A//nodejs.org/zh-cn)
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634584190.jpg)
1. 2. 下载LTS版本（推荐版本）
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634584376.jpg)
1. 3. 双击安装包，按提示完成安装，一直默认点击下一步就行
2. 4. 安装完成之后，验证安装：
3. 1.按下Win + R，输入cmd，回车
4. 2.在命令行中输入：
```
node --version
```
1. 3.显示版本号即安装成功
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634584559.jpg)
### **3.安装Git（如果已安装可跳过）**
**下载地址：[https://git-scm.com/downloads](https://link.zhihu.com/?target=https%3A//git-scm.com/downloads)**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634584748.jpg)
**下载之后，一路默认安装下一步就行**
### **4.安装Claude Code（如果已安装可跳过）**
**输入以下命令并回车：**
```
npm install -g @anthropic-ai/claude-code
```
**验证安装：**
```
claude --version
```
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634585036.jpg)
### **5.安装Vscode（重点）**
**下载地址**：[https://code.visualstudio.com/](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/)
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634585321.jpg)
**安装很简单，一直点下一步就行。**
安装完成之后，因为软件是英文的，需要下载一个中文插件。
点击左侧这个图标，搜索 chinese，安装此插件：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634585545.jpg)
然后输入 python ，安装这个插件：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634585742.jpg)
**重点来了！搜索 claude code 安装这个插件！！！**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634586017.jpg)
**安装完成之后，点击小齿轮按钮：**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634586202.jpg)
**点击设置**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634586560.jpg)
勾选上面的按钮，然后点击下面的 **在settings.json中** 编辑：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634586964.jpg)
然后**将下面这几行代码完整复制粘贴过去**（注意先清空之前的）：
```
{
    "explorer.confirmDelete":false,
    "extensions.ignoreRecommendations":true,
    "security.workspace.trust.untrustedFiles":"open",
    "python.createEnvironment.trigger":"off",
    "claudeCode.allowDangerouslySkipPermissions":true,
    "claudeCode.environmentVariables":[
        {
            "name":"ANTHROPIC_BASE_URL",
            "value":"https://open.bigmodel.cn/api/anthropic"
        },
        {
            "name":"ANTHROPIC_AUTH_TOKEN",
            "value":"*******************************"
        },
        "permissions":{
                "defaultMode":"bypassPermissions"
            },
    ]
}
```
**然后键盘按 Ctrl+S 保存。**
ANTHROPIC\_BASE\_URL 是输入大模型的网址，这里输入智谱的网址，可以不用改；下面的 ANTHROPIC\_AUTH\_TOKEN （\*\*\*的位置）需要填入你智谱的API-KEY。
（可以在 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://link.zhihu.com/?target=https%3A//bigmodel.cn/usercenter/proj-mgmt/apikeys) 领取）
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634587292.jpg)
PS： Claude Code对于 Tokens的消耗是非常大的所以如果使用量比较大的话，建议直接购买智谱的包月套餐
网址：[https://zhipuaishengchan.datasink.sensorsdata.cn/t/Ud](https://link.zhihu.com/?target=https%3A//zhipuaishengchan.datasink.sensorsdata.cn/t/Ud)
### **6.案例演示**
我们在桌面建一个文件夹，例如"AI加油站"。
然后打开 Vscode，左上角 **文件-打开文件夹**，打开 AI加油站 文件夹。
双击屏幕中间位置，然后右上角会出现一个 橙色图标，点击一下就能进入 AI助手界面：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634587766.jpg)
中间是对话区域：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634588134.jpg)
**提示词：写一首形容秋天的古诗**
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634588498.jpg)
**提示词：**写一个 通知，明天10点在会议室开会，会议主题是 AI加油站，保存为记事本格式
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634588955.jpg)
可以看到AI直接在文件夹生成了一个文件：
![](%5B2026-01-20_22-56%5D%20%E5%A6%82%E6%9E%9C%E5%8F%AA%E8%83%BD%E5%AD%A6%E4%BC%9A%E4%B8%80%E4%B8%AAAI%E5%B7%A5%E5%85%B7%E6%88%91%E6%8E%A8%E8%8D%90%20Claude%20Code%20for%20VSCode%EF%BC%88%E4%BF%9D%E5%A7%86_%E5%9B%BE%E7%89%87/_1775634589172.jpg)
以上就是安装过程，个人觉得除了编程开发一些产品、网站、写量化策略，对于普通人在工作中的用途也非常大，可以帮助我们提高效率，减少枯燥重复的劳动。
看看大家是否感兴趣，后面有机会继续更新一些AI提效的文章~