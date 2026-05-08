# 怎么把通达信同花顺之类的炒股软件和python，matlab，java量化研究结合起来？

---

[通达信量化](https://zhida.zhihu.com/search?content_id=767138111&content_type=Answer&match_order=1&q=%E9%80%9A%E8%BE%BE%E4%BF%A1%E9%87%8F%E5%8C%96&zhida_source=entity)（TdxQuant）正式版已经发布有一段时间了，发现很多粉丝还不知道怎么用。今天就出一份详细的教程，文章末尾会有一个完整的选股策略代码。
### **1. 安装TdxQuant**
首先，你需要在通达信官网下载并安装TdxQuant软件。安装过程和普通软件类似，按照提示一步步操作即可，属于有手就会的操作。 下载链接：[https://www.tdx.com.cn/soft.html](https://link.zhihu.com/?target=https%3A//www.tdx.com.cn/soft.html) 找到支持TQ策略的版本，如下图红框里的2个版本。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633994560.jpg)
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633995331.webp)
打开通达信，如果菜单栏里有TQ策略这个按钮，说明你安装成功了。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633995586.jpg)
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633996252.webp)
### **2.安装[Python](https://zhida.zhihu.com/search?content_id=767138111&content_type=Answer&match_order=1&q=Python&zhida_source=entity)环境**
根据官方文档，TdxQuant 支持 64 位 Python 3.7、3.8、3.9、3.10、3.11、3.12、3.13等版本，这里官方建议使用3.13版本。后面的选股策略这里也用的是3.13版本。
**下载Python**
* 直接从Python官网下载 下载链接：[https://www.python.org/downloads/](https://link.zhihu.com/?target=https%3A//www.python.org/downloads/)
* 下载anaconda版本的Python 下载链接：[https://www.anaconda.com/products/distribution](https://link.zhihu.com/?target=https%3A//www.anaconda.com/products/distribution)
anaconda版本下载的时候需要登录下账号，才能下载。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633996555.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='623' height='512'></svg>)
这里推荐下载 anaconda distribution 版本的Python，因为它集成了很多常用的Python库，方便我们后续的开发。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633997053.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='421'></svg>)
关于下载Python官方版本还是下载anaconda版本，个人建议下载anaconda版本，后期方便Python环境的管理。后面的教程我也会基于anaconda版本的Python进行讲解。
**查看Python是否安装成功**
安装完成后，你可以在命令行中输入以下命令来查看Python是否安装成功：
```
python --version # 或者python -V
```
如果显示出Python的版本号，说明安装成功了。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633997639.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='255' height='80'></svg>)
如果没有成功，查看下python是否加入环境变量（不知道怎么加入环境变量直接上网搜一下很简单的）
### **3.安装IDE**
建议使用[vscode](https://zhida.zhihu.com/search?content_id=767138111&content_type=Answer&match_order=1&q=vscode&zhida_source=entity)或者pycharm等IDE进行开发。按照大家的喜好来选择即可。 这里推荐使用vscode，因为它免费、功能强大、支持Python等多种语言的开发。最关键的是花姐习惯使用vscode，所以这里也推荐使用vscode。
vscode下载地址：[https://code.visualstudio.com/Download](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/Download)
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633998159.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='879' height='552'></svg>)
VScode安装以后记得安装以下插件
简体中文插件
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633998768.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='364' height='398'></svg>)
Python插件
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633999211.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='551'></svg>)
### **4. 创建一个虚拟环境**
为了避免不同项目之间的依赖冲突，建议在每个项目中创建一个独立的虚拟环境。
打开Anaconda Prompt（或者在Windows中使用PowerShell），输入以下命令创建一个新的虚拟环境（这里命名为tdxquant）：
```
conda create -n tdxquant python=3.13
```
激活虚拟环境：
```
conda activate tdxquant
```
如果报错：
```
CondaError: Run 'conda init' before 'conda activate'
```
直接运行
```
activate tdxquant
```
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775633999883.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='563' height='399'></svg>)
**配置镜像源**
为了加速库的安装过程，建议配置国内的镜像源。这里以windows系统为例 打开`C:\\Users\\你的用户名\\pip\\pip.ini`文件（如果没有就创建一个），添加以下内容：
```
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```
**安装必要的库：**
**注意：** 这里安装的库都是必须的，不能缺少。
```
pip install numpy pandas backtrader vectorbt  matplotlib
```
最后出现`Successfully installed`就表示安装成功了。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634000554.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='960' height='480'></svg>)
### **5.数据下载**
用过QMT或者miniQMT的都知道，要想获取数据需要先下载，通达信也一样。
打开并登录通达信金融终端，点击【TQ策略-TQ数据设置】在弹出框就可以看到当前已经下载的数据和对应的时间，然后点击【盘后数据下载】
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634001285.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='566' height='371'></svg>)
打开【盘后数据下载】弹窗，根据你的需求选择对应的数据。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634001779.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='590' height='434'></svg>)
### **6. 开发选股策略**
打开VScode，从**文件--打开文件夹**或者下图所示方法打开通达信量化目录。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634002827.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='720'></svg>)
**通达信量化目录**：通达信安装目录--PYPlugins--user，比如我的是`H:\\new_tdx64\\PYPlugins\\user`
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634004065.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='359' height='149'></svg>)
这里需要重点说明下，文件夹中的`tqcenter.py`是最主要的**TQData**支撑文件，**请勿修改或删除，请勿修改或删除，请勿修改或删除.**
首次打开user目录vscode会提示是否信任此文件夹中的文件，这里一定要选择**是**
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634004704.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='720'></svg>)
我们选中`tdxdata_test.py`文件，点击右下角的python版本
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634005584.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='720'></svg>)
在弹出的选项框里找到我们之前创建的虚拟环境`tdxquant`，点击选择即可。
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634006528.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='720'></svg>)
最后点击右上角的小三角运行，在命令行出现下面的内容就表示你的环境搭建好了，可以开发选股策略了
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634007131.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='720'></svg>)
点击新建文件然后新建一个test001.py文件，用来执行我们的选股策略
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634007917.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='517' height='324'></svg>)
把python代码复制到test001.py文件中，如下：
选股策略：把符合5日上穿10日的均线金叉股票放到自选股里。
```
import pandas as pd
import numpy as np
from datetime import datetime
from tqcenter import tq
# 初始化tq
tq.initialize(__file__)
# 获取沪深京A股列表
pool = tq.get_stock_list(market ='5')
print(f"共获取了{len(pool)}只股票")
df_real = tq.get_market_data(
        field_list=[],
        stock_list=['001220.SZ'],
        start_time='20250101',
        end_time='',
        count=-1,
        dividend_type='front',
        period='1d',
        fill_data=False
    )
# return
golden_cross_stocks = []
for code in pool:  # 仅展示前5只股票
    df_real = tq.get_market_data(
        field_list=[],
        stock_list=[code],
        start_time='20250101',
        end_time='',
        count=-1,
        dividend_type='front',
        period='1d',
        fill_data=False
    )
    if len(df_real)==0:
        print(f"股票代码 {code} 无数据，跳过")
        continue
    print(f"处理股票代码: {code}")
    # 转换成Dataframe格式方便后期处理
    combined = pd.concat(df_real.values(), keys=df_real.keys(), axis=0)
    df = combined.stack().unstack(level=0).reset_index()
    df.columns.name = None
    df.rename(columns={'level_0': 'Date', 'level_1': 'Symbol'}, inplace=True)
    if len(df) < 20:
        print(f"股票代码 {code} 数据不足20天，跳过")
        continue
    # 选出最新日期5日上穿10日均线的股票，且是第一次上穿
    # 计算移动平均线
    df['ma5'] = df['Close'].rolling(window=5, min_periods=5).mean()
    df['ma10'] = df['Close'].rolling(window=10, min_periods=10).mean()
    #  判断金叉条件：当日ma5 > ma10，且前一日ma5 <= ma10[2,5]
    df['golden_cross'] = (df['ma5'] > df['ma10']) & (df['ma5'].shift(1) <= df['ma10'].shift(1))
    if df['golden_cross'].iloc[-1]:
        golden_cross_stocks.append(code)
print("出现5日上穿10日均线的股票有：", golden_cross_stocks)
# 创建自定义板块
# 日期字符串
date_str = datetime.now().strftime('%Y%m%d')
block_code = 'JXJC' + date_str
create_ptr = tq.create_sector(block_code=block_code, block_name='均线金叉'+date_str)
print(create_ptr)
zxg_result = tq.send_user_block(block_code=block_code, stocks=golden_cross_stocks)
print(zxg_result)
tq.close()
```
运行完以后你就会在通达信的自定义板块中看到新加的板块
![](%5B2026-01-27_23-27%5D%20%E6%80%8E%E4%B9%88%E6%8A%8A%E9%80%9A%E8%BE%BE%E4%BF%A1%E5%90%8C%E8%8A%B1%E9%A1%BA%E4%B9%8B%E7%B1%BB%E7%9A%84%E7%82%92%E8%82%A1%E8%BD%AF%E4%BB%B6%E5%92%8Cpythonmatlabjava%E9%87%8F%E5%8C%96%E7%A0%94%E7%A9%B6%E7%BB%93%E5%90%88%E8%B5%B7%E6%9D%A5_%E5%9B%BE%E7%89%87/_1775634008526.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='284' height='163'></svg>)
今天的教程就到这里了，喜欢的记得一键三连，关注我，后续会分享更多的内容。
---
### **关于花姐**
花姐，专注于Python量化与股票策略研究，兼顾Python基础知识分享，内容实用接地气，擅长用代码解读市场，用策略提升认知，干货满满，务实至上。
--- **End** ---
文章中涉及的策略仅作学术交流回测结果不代表未来表现市场有风险，决策需谨慎