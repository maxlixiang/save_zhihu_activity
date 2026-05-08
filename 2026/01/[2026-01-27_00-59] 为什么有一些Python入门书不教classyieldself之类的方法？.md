# 为什么有一些Python入门书不教class，yield，self之类的方法？

---

## 一、必要性
正好问主说的这本书 —— 《Python编程快速上手——让繁琐工作自动化》，也是我当年入门 Python 时，最喜欢看的两本书之一。
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634064924.jpg)
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634065377.webp)
我入门 Python 的知识库
我和问主一样，也不是科班程序员，学 Python 之目的，除个人兴趣外，也是奔着提高工作效率去的。
想当年，我没有问主那么多困惑，顺着大众评价，就认准了上述两本入门书（没有再去拓展其他的入门书籍和视频）。因此，即便看完书，实践了一段时间后，我也不知道 `yield` 的存在。对 `class` 里的 `self` 和 `init` 更是一知半解。
直到工作需要，经常上手，用多了后，这些（`yield、class`）东西才有了点眉目。
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634065754.jpg)
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634066448.webp)
问主的困惑
### 1、[函数式编程](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B&zhida_source=entity)速成
严格来说《Python编程快速上手——让繁琐工作自动化》这本书，是一本 **函数式编程的速成书**。它的主要编写目的，是让读者快速了解 Python 的变量、控制（流程和循环）、函数体系，好让初学者可以快速上手开发一些实用的小工具。
所以、不只是 `class`（含 `self` 和 `init`）、`yield` 被略过了，即使是比较实用的 `lambda`、`map`、`reduce`、`filter`、`sorted` 等内置高级函数，也是能省则省。
问主以为这就完了？远远不是，该书连基本的序列知识（`list、tuple、set、dict`）都是能省则省（ `set` 只字未提）。
很多人觉得神书《Python 编程从入门到实践》比 [《Python 编程快速上手——让繁琐工作自动化》](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E3%80%8APython+%E7%BC%96%E7%A8%8B%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B%E2%80%94%E2%80%94%E8%AE%A9%E7%B9%81%E7%90%90%E5%B7%A5%E4%BD%9C%E8%87%AA%E5%8A%A8%E5%8C%96%E3%80%8B&zhida_source=entity)全，也是误解。《Python 编程从入门到实践》除了蜻蜓点水地提及 `class` 之外，对 `self` 和 `__init__` 压根就没有做深入辨析。而且基础序列同样缺失 `set`，更不用提问主说的 `yield` 了。
### 2、初学者疑惑
`class` 是[面向对象编程](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B&zhida_source=entity)范式，如果真要讨论，那《Python 编程快速上手——让繁琐工作自动化》整本书的篇幅，都不够！
况且这些内容也不符合该书 **速成** 之主旨（初学者面向过程编程范式都没掌握好，就直接引入面向对象，不符合初学者的理解规律）。
至于引入 `yield` 这种处理[生成器函数](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E7%94%9F%E6%88%90%E5%99%A8%E5%87%BD%E6%95%B0&zhida_source=entity)的关键字，就更不可能了。因为，这是处理大数据时，才该考虑节的细节（节约内存）。况且这本书的应用案例中，根本涉及不到这一需求。强制引入，只会让初学者不适。
最后，我个人理解《Python 编程快速上手——让繁琐工作自动化》第一部分介绍的基础知识（前 6 章），都是紧扣第二部分（第 8-16 章）应用的。主打一个**短平快速成**。
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634066698.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2382' height='1984'></svg>)
## 二、yield 概念
既然问主对 `class`、`yield` 有想法了，那我就先从简单一点的 `yield` 开吹。
### 1、官话
Python 的`yield`是一个用于在生成器函数（一种特殊[类](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E7%B1%BB&zhida_source=entity)型的函数，它可以在需要时生成一系列值，而不是一次性生成并存储在内存中）中，产生值的关键字。
也就是说 `yield`可以将值产生给调用方，并在生成器函数的执行中，保持状态。
是不是很绕，初学者听到这话，估计瞬间就能被劝退。
### 2、白话
下面说说我的理解，当代码需要处理大量数据时，`yield`允许生成器在迭代过程中，动态产生值（不需要一次性，将所有的值加载到内存中），从而节省内存空间。
## 三、yield 示例
问主可以读读我的理解，看是不是比官话通俗？
不过，对初学者来说，不论官话、白话，都含有大量“劝退”成分。
如果问主意志力够坚定，硬要刚 `yield`，可以用我的理解，结合如下的示例自己悟。至于能悟多少，那就全赖自身的 Python 基础了。
### 1、无限数据生成
```
def infinite_sequence():
    num = 0
    while True:
        num += 1
inf_seq = infinite_sequence()
for code in inf_seq: # 由于 inf_seq 在无限自增，所以程序根本进行不到这一步
    print(code)
```
比如，上述代码就是个无限生成数据的大坑，按照正常的 `while` 循环来理解，`inf_seq` 就会成为一个自增死循环的容器（变量）。
如果运行这段代码，`inf_seq` 就会**爆体而亡（内存耗尽，被卡死）**。
这时，`yield` 这个神器出现了。
```
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
inf_seq = infinite_sequence()
for _ in range(30):  # 指定迭代次数
    print(next(inf_seq)) # 允许生成器在迭代过程中，动态产生值（不需要一次性，将所有的值加载到内存中），从而节省内存空间
```
有了它，`inf_seq` 再也不用**无脑自增**了（不会因为内存耗尽，而卡死）。它会等着 `for` 遍历中 `range` 指定的迭代数，来动态、优雅地产生值。
是不是很神奇呢？
因此，Python 中 `yield` 就经常被拿来生成**斐波那契**，这种无限序列。
```
def fibonacci():
    code_1, code_2 = 0, 1
    while True:
        yield code_1
        code_1, code_2 = code_2, code_1 + code_2
fib = fibonacci()
for _ in range(100):
    print(next(fib))
```
如果没有`yield`，那**斐波那契**这种变态的无限序列，就会把`fib`这个容器（变量）撑爆。
### 2、读取大文件
这个比较容易理解，就以读取文本文件中的行数来举例吧。
比如，我们要读取的《红楼梦》，是一个 `红楼梦.txt` 的文本，那这个 红楼梦.`txt` 文件的字符行数，一定也是海量的。
如果要直接读取，很可能撑爆内存。
因此，`yield` 就可以大显神威了。
```
def read_long_txt(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
hongloumeng = read_long_txt('hongloumeng.txt')
for _ in range(5):
    print(next(hongloumeng))
```
有了它（按需读取），就再也不用担心内存耗尽了。
## 四、class 中的 init 和 self
至于，`class` 中 `__init__` 和 `self` 辨析，我之前也简单总结过，不过，这些知识对于 Python 基础不够厚的初学者来说，如同嚼蜡。
### 1、**没有 \_\_init\_\_ 方法的 class 和不带 self 变量的 def**
使用 Python 定义 `class` 时，不写 `__init__` 方法可行吗？答案是可以的。
```
class Example：
  def __init__(self, avg): # 去掉 init 也是可以的
```
比如，我们写一个小狗的类，小狗有名字，也会跑。
```
class Dog:
​
   def dog_name(self, name):
       print(f'The dog`s name is {name}')
​
   def dog_run(self):
       print(f'Tom run')
​
​
tom = Dog()
tom.dog_name('Tom')
tom.dog_run()
```
运行结果
```
The dog`s name is Tom
Tom run
```
### **2、class def 中的 self 变量**
`dog_run` 方法中的名字被固定成了 `Tom`，如果要把 `dog_name` 方法中的变量 `name`， 用起来，应当怎么办呢？
先来写一段错误代码：
```
class Dog:
​
   def dog_name(self, name):
       print(f'The dog`s name is {name}')
​
   def dog_run(self):
       print(f'{name} run') # 错误，注意name的作用域
​
​
tom = Dog()
tom.dog_name('Tom')
tom.dog_run()
```
报错如下：
```
username@usernamedeMacBookPro1 lab %python -u"/Users/username/Coding/lab/dog_example.py"
The dog`s name is Tom
Traceback (most recent call last):
File "/Users/username/Coding/lab/dog_example.py", line 12, in<module>
  tom.dog_run()
File "/Users/username/Coding/lab/dog_example.py", line 7, in dog_run
  print(f'{name} run') # 错误，注意name的作用域
NameError: name 'name' is not defined
```
可以看到，`tom` 在调用 `dog_run` 方法的时候，出现了 `name` 变量未定义错误。这是为什么呢？
因为 `name` 变量是 `dog_name` 方法的参数，它的**作用域仅限于 `dog_name` 方法内**，**`dog_run` 方法自然不能使用，**
```
class Dog:
​
   def dog_name(self, name):
       print(f'The dog`s name is {name}')
​
   def dog_run(self):
       print(f'{name} run') # 错误，注意name的作用域
```
**`dog_run` 方法要使用 `dog_name` 方法的参数变量 `name`，就必须得把 `name` 的作用域，扩展至 `dog_run` 方法内。**
**用 `self`（约定俗成的单词，当然，也可以使用其他单词）关键字在 `dog_name` 方法内初始化 `name` 变量，让 `name` 变量的作用域扩展至 `dog_run` 方法。**
```
class Dog:
​
   def dog_name(self, name):
       self.name = name # self 初始化变量 name，让 name 的作用域扩展至整个 class 内
       print(f'The dog`s name is {name}')
​
   def dog_run(self):
       print(f'{self.name} run') # self.name就具有了被对象调用的能力
​
​
tom = Dog()
tom.dog_name('Tom')
tom.dog_run()
```
程序运行如下：
```
The dog`s name is Tom
Tom run
```
### **3、sub class def 中的 self 变量**
继续写一个 Dog `class` 的 `sub class` Cat，使用 `self` 初始化 `name` 变量，就可以让 Dog `class` 中 `name` 变量的作用域，扩展至 `sub class` Cat，反之亦然。
比如，`Cat` 叫 `Tony`，那么调用 `Dog` 中的 `dog_run` 方法时，`sub class` 中的 `name` 只要被 `self` 调用，那么这个 `name` 也会被被 `father class` 中的 `dog_run` 读取到，从而显示 Tony 在跑。
```
class Dog:
​
   def dog_name(self, name):
       self.name = name  # self初始化变量name，让name的作用域扩展至class内
       print(f'The dog`s name is {name}')
​
   def dog_run(self):
       print(f'{self.name} run')  # self.name就具有了被对象调用的能力
​
​
class Cat(Dog):
​
   def cat_name(self, name):
       self.name = name
​
​
tom = Cat()
tom.cat_name('Tony')
tom.dog_run()
```
程序运行效果：
```
Tony run
```
### 4、作用域
因此，`class` 内 `__init__` 函数，所携带的参数（变量），就能被 `self` 初始化后，扩展作用域至整个 `class`，这样的初始化形式，特别适合**初始化 `class` 内，被多个方法反复调用的参数（变量）**。
```
class Dog:
    def __init__(self, name, age):
        self.name = name # self.name 被 show_name、show choose 反复调用
        self.age = age # self.age 被 show_name、show choose 反复调用
    def show_name(self):
        print(f'我的小狗叫 {self.name}, 今年已经 {self.age} 岁了')
    def show_choose(self, number):
        number = int(input())
        if number == 1:
            print(f'我的小狗叫 {self.name}')
        elif number == 2:
            print(f'我的小狗 {self.age} 岁了')
        else:
            print('您的输入有误！')
if __name__ == '__main__':
    dog = Dog('Toy', 3)
    dog.show_name()
    dog.show_choose(2)
```
运行效果
```
我的小狗叫 Toy, 今年已经 3 岁了
2
我的小狗 3 岁了
```
可以看到 `show_name` 和 `show_choose` ，都需要调用变量 `name` 和 `age`，所以，在 `__init__` 方法中直接用 `self` 参数，让 `name` 和 `age` 的作用域扩展至整个 `class`。而 `show_choose` 方法中的 `number` 变量，就只能被 `show_choose` 自己调用（不用 `self` 关键字初始化的变量，作用域只限本地）。
若 `show choose` 方法内的 `number` 变量，要被其他 `def` 调用，就必须用 `self` 初始化。
```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_name(self):
        print(f'我的小狗叫 {self.name}, 今年已经 {self.age} 岁了')
    def show_choose(self, number):
        self.namber = number # self 参数让 number 作用域扩展至整个 class 内
        self.number = int(input())
        if self.number == 1:
            print(f'我的小狗叫 {self.name}')
        elif self.number == 2:
            print(f'我的小狗 {self.age} 岁了')
        else:
            print('您的输入有误！')
    def add(self, code):
        sum_code = self.number + code
        print(sum_code)
if __name__ == '__main__':
    dog = Dog('Toy', 3)
    dog.show_name()
    dog.show_choose(2)
    dog.add(3)
```
运行效果
```
我的小狗叫 Toy, 今年已经 3 岁了
2
我的小狗 3 岁了
5
```
思维过程大概如下图：
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634067556.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2244' height='1396'></svg>)
## 五、总结
综上，是不是感觉《Python 编程快速上手——让繁琐工作自动化》用来入门，比较友好了？
### 1、题外话
Python 零基础的入门书籍，我更推荐 《Python 编程从入门到实践》、《Python编程快速上手——让繁琐工作自动化》。
理由是，这两本书的知识体系，并非填鸭式罗列。而是充分照顾了零基础读者的学习逻辑。
### 2、感慨
反观某些大而全 Python 入门教材，不仅填鸭式罗列知识点，还经常跳跃式推进。
比如，在函数入门章节，堆砌 `lambda`、`yield`、`map`、`reduce`、`filter`、`sorted` ，在函数入门章节后，高论[装饰器](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E8%A3%85%E9%A5%B0%E5%99%A8&zhida_source=entity)。
再比如，在类、对象、[实例](https://zhida.zhihu.com/search?content_id=681981762&content_type=Answer&match_order=1&q=%E5%AE%9E%E4%BE%8B&zhida_source=entity)的辨析都没讲明白的情况下，突入并发、并行、异步等概念！
### 3、比喻
最后再作一个类似开车般的比喻。
`yield`、`class` （含 `self 、__init__`）等知识，就好比开手动挡汽车，坡启时的离合器半联动。只要入了 Python 的门，这些东西基本一用就会。
《Python编程快速上手——让繁琐工作自动化》就好比告诉新手司机，踩离合挂档起步的开车教学。至于坡启什么的，在学会开车后，多去坡上练几把，自然就会了（找到离合器半联动的踩踏脚感）。
既然是入门后多用就会的东西，何必在入门前徒增烦恼？
![](%5B2026-01-27_00-59%5D%20%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E4%B8%80%E4%BA%9BPython%E5%85%A5%E9%97%A8%E4%B9%A6%E4%B8%8D%E6%95%99classyieldself%E4%B9%8B%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F_%E5%9B%BE%E7%89%87/_1775634068140.jpg)
![](data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='2632' height='2092'></svg>)
想要把车开到特技效果，啃这本书即可