# 基于Tushare的Python代码免费获取股票数据

---

## tushare的API获取
### 打开网址
这个是Tushare的网址： [https://tushare.pro/](https://link.zhihu.com/?target=https%3A//tushare.pro/)
![](%5B2026-01-25_03-44%5D%20%E5%9F%BA%E4%BA%8ETushare%E7%9A%84Python%E4%BB%A3%E7%A0%81%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE_%E5%9B%BE%E7%89%87/_1775634173578.jpg)
注册登录后，我们就可以点击右上角：
![](%5B2026-01-25_03-44%5D%20%E5%9F%BA%E4%BA%8ETushare%E7%9A%84Python%E4%BB%A3%E7%A0%81%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE_%E5%9B%BE%E7%89%87/_1775634174274.jpg)
进入之后，我们可以继续注册，然后进行一个个人资料的认证，这样我们就可以得到120积分：
![](%5B2026-01-25_03-44%5D%20%E5%9F%BA%E4%BA%8ETushare%E7%9A%84Python%E4%BB%A3%E7%A0%81%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE_%E5%9B%BE%E7%89%87/_1775634174665.jpg)
我的推荐码大家可以试试： [https://tushare.pro/weborder/#/login?reg=951705](https://link.zhihu.com/?target=https%3A//tushare.pro/weborder/%23/login%3Freg%3D951705) 然后在这里我们就可以得到我们的token了，基于这个token我们可以免费获取一些股票的具体信息：
![](%5B2026-01-25_03-44%5D%20%E5%9F%BA%E4%BA%8ETushare%E7%9A%84Python%E4%BB%A3%E7%A0%81%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE_%E5%9B%BE%E7%89%87/_1775634175062.jpg)
值得注意的地方是不同积分可以获取到的内容是不同的： 具体可以通过这个链接进行访问查看：[Tushare数据](https://link.zhihu.com/?target=https%3A//tushare.pro/document/1%3Fdoc_id%3D108) 而120积分是正好可以：
![](%5B2026-01-25_03-44%5D%20%E5%9F%BA%E4%BA%8ETushare%E7%9A%84Python%E4%BB%A3%E7%A0%81%E5%85%8D%E8%B4%B9%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE_%E5%9B%BE%E7%89%87/_1775634175511.jpg)
## 代码解析
### 1. 整体逻辑概览
代码的运行遵循以下线性逻辑：
1. **标准化（Normalization）**：将用户输入的 6 位数字转化为带后缀的标准代码（如 `000560.SZ`）。
2. **多路适配（Dispatching）**：由于 Tushare 的股票和基金接口不同，脚本采用了“顺序尝试”策略，先试股票，不行再试基金。
3. **时间窗口计算**：根据用户选择，动态计算起始日期。
4. **持久化与格式化**：保存为 JSON 并自动拼装成一个供大语言模型（LLM）分析的 Prompt。  
    2. 核心模块迭代拆解
### 模块一：代码标准化 `normalize_code`
这个函数是系统的“门卫”，解决 A 股市场代码规则杂乱的问题。
```
def normalize_code(code):
    """
    这个函数的作用是把用户随便输入的数字（比如 600519）
    变成 Tushare 能识别的标准格式（600519.SH）
    """
    code = code.strip()
    if '.' in code:
        return code  # 如果用户已经输入了后缀，直接返回
    # 逻辑分析：通过首数字判断市场归属
    if code.startswith('6'):
        return code + '.SH'  # 沪市主板/科创板
    elif code.startswith('0') or code.startswith('3'):
        return code + '.SZ'  # 深市主板/创业板
    elif code.startswith('8') or code.startswith('4'):
        return code + '.BJ'  # 北交所
    elif code.startswith('5'):  
        return code + '.SH'  # 沪市基金
    elif code.startswith('1'):  
        return code + '.SZ'  # 深市基金
    else:
        return code
```
* **输入与输出**：输入为字符串（Raw Code），输出为带后缀的字符串（TS Code）。
* **为什么这样做**：交易所之间代码可能重复，必须加后缀区分；且 API 调用强制要求后缀。
* **优化方向**：可以使用正则表达式（Regex）来增强健壮性，防止用户输入非数字字符。
### 模块二：智能接口调度 `fetch_data`
这是脚本的“智慧中心”，解决了资产分类识别的问题。
```
def fetch_data(ts_code, start_date, end_date):
    """尝试多种接口获取数据，因为我们不知道用户搜的是股票还是基金"""
    # 1. 尝试作为 [股票] 获取：调用 pro.daily 接口
    try:
        df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        if not df.empty:
            return df, "股票(Stock)"
    except:
        pass # 如果报错，说明可能不是股票
    # 2. 如果股票为空，尝试作为 [基金/ETF] 获取：调用 pro.fund_daily 接口
    try:
        df = pro.fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        if not df.empty:
            return df, "基金(ETF)"
    except:
        pass
    return pd.DataFrame(), "未知"
```
* **设计意义**：表现为“一键查询”，背后是**多态适配**。本应该由用户指定类型，但为了体验，程序通过“异常捕获+回退（Fallback）”机制自动判断。
* **表现分析**：通过 `df.empty` 判断数据是否存在。  
   3. 技术栈解析与注意事项
* **Pandas**：用于数据清洗和排序（`sort_values`）。注意：Tushare 返回的数据通常是倒序的，必须重新排序。
* **Tushare Pro**：国内主流金融数据源。注意：某些接口（如基金）需要积分权限。
* **JSON 序列化**：使用 `orient='records'`。这对于 AI 最友好，因为它将数据转为“对象数组”格式。
### 4. 类比
想象你去一家**大型综合医院**看病：
1. **挂号处（`normalize_code`）**：你只跟护士说“我肚子疼”，护士根据你的描述，帮你填好单子，写上具体的科室代码。
2. **分诊台（`fetch_data`）**：医生先让你去内科检查（尝试股票接口），如果内科医生说“这不是内科的问题”，你再去外科（尝试基金接口）。
3. **打印报告（`JSON/Prompt`）**：最后医院给你打印一份结构清晰的病历单，并贴心地帮你写好了给专家的咨询简述。
## 5. 算法与数据处理模型
虽然这更多是工程实现，但其数据处理逻辑可以用简单的逻辑映射表示： 设输入集合为 C，目标接口集为 I = \{f\_{stock}, f\_{fund}\}。 算法流程为：
1. 映射函数 M(c) \to c'（代码补全）。
2. 执行判定序列： Result = \begin{cases} f\\_{stock}(c') & \text{if } f\\_{stock}(c') \neq \emptyset \\ f\\_{fund}(c') & \text{else if } f\\_{fund}(c') \neq \emptyset \\ \text{Error} & \text{otherwise} \end{cases}
## 6.完整代码
```
import tushare as ts  
import pandas as pd  
import os  
from datetime import datetime, timedelta  
# 1. 配置 Tushare TokenTOKEN = '' ts.set_token(TOKEN)  
pro = ts.pro_api()  
def normalize_code(code):  
    """  
    自动补全股票/基金后缀  
    5xx, 6xx -> .SH    0xx, 1xx, 3xx -> .SZ    4xx, 8xx -> .BJ    """    code = code.strip()  
    if '.' in code:  
        return code  
    # 股票规则  
    if code.startswith('6'):  
        return code + '.SH'  
    elif code.startswith('0') or code.startswith('3'):  
        return code + '.SZ'  
    elif code.startswith('8') or code.startswith('4'):  
        return code + '.BJ'  
    # 基金/ETF 规则 (新增)  
    elif code.startswith('5'):  # 沪市基金 (如 510050, 561380)        return code + '.SH'  
    elif code.startswith('1'):  # 深市基金 (如 159915)        return code + '.SZ'  
    else:  
        return code  
def fetch_data(ts_code, start_date, end_date):  
    """尝试多种接口获取数据 (股票 或 基金)"""  
    # 1. 尝试作为 [股票] 获取  
    try:  
        df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)  
        if not df.empty:  
            return df, "股票(Stock)"  
    except:  
        pass  
    # 2. 如果股票为空，尝试作为 [基金/ETF] 获取  
    try:  
        # print("尝试获取基金数据...") # 调试用  
        df = pro.fund_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)  
        if not df.empty:  
            return df, "基金(ETF)"  
    except:  
        pass  
    return pd.DataFrame(), "未知"  
def get_stock_data():  
    print("-" * 50)  
    print("通用行情获取工具 (支持 股票 & ETF基金)")  
    print("-" * 50)  
    # 1. 输入代码  
    raw_code = input("请输入代码 (例如 000560 或 561380): ")  
    ts_code = normalize_code(raw_code)  
    # 2. 获取当前时间  
    now = datetime.now()  
    today_str = now.strftime('%Y%m%d')  
    print(f"\n当前识别目标: [{ts_code}]")  
    print("请选择时间范围:")  
    print("1. 仅今天 (Today)")  
    print("2. 本月至今 (This Month)")  
    print("3. 今年至今 (This Year)")  
    print("4. 近三个月 (Last 3 Months)")  
    choice = input("请输入选项 (1-4): ").strip()  
    start_date = ''  
    file_suffix = ''  
    # 3. 计算时间  
    if choice == '1':  
        start_date = today_str  
        file_suffix = 'today'  
    elif choice == '2':  
        start_date = datetime(now.year, now.month, 1).strftime('%Y%m%d')  
        file_suffix = 'month'  
    elif choice == '3':  
        start_date = datetime(now.year, 1, 1).strftime('%Y%m%d')  
        file_suffix = 'year'  
    elif choice == '4':  
        start_date = (now - timedelta(days=90)).strftime('%Y%m%d')  
        file_suffix = '3months'  
    else:  
        start_date = datetime(now.year, now.month, 1).strftime('%Y%m%d')  
        file_suffix = 'month'  
    print(f"\n>>> 正在获取数据 ({start_date} - {today_str})...")  
    # 4. 智能调用接口 (核心修改)  
    df, asset_type = fetch_data(ts_code, start_date, today_str)  
    if df.empty:  
        print("【结果为空】")  
        print(f"未能获取到 {ts_code} 的数据。")  
        print("可能原因: 1.代码错误 2.非交易日 3.未收盘 4.权限不足")  
        return  
    print(f"识别为: [{asset_type}]，成功获取 {len(df)} 条数据。")  
    # 排序  
    df = df.sort_values('trade_date', ascending=True)  
    # 5. 保存文件  
    file_name = f"{ts_code}_{file_suffix}.json"  
    json_str = df.to_json(orient='records', force_ascii=False)  
    with open(file_name, 'w', encoding='utf-8') as f:  
        f.write(json_str)  
    print(f"文件已保存: {os.path.abspath(file_name)}")  
    # 6. 生成 Prompt    print("\n" + "=" * 20 + " 请复制以下内容 " + "=" * 20)  
    print(f"""  
你是一个专业的中国金融投资专家  
这个是{ts_code} ({asset_type}) 的历史行情数据:  
{json_str}  
从短线和长线来看，你看看我要不要买入？然后如果买入什么时候出？  
我的钱有300多，足够买入这个1次  
要不要买入  
除了数据之外，现在你还要搜索关于{ts_code}的所有相关信息做出最后判断  
""")  
    print("=" * 20 + " 复制结束 " + "=" * 20 + "\n")  
if __name__ == "__main__":  
    get_stock_data()
```