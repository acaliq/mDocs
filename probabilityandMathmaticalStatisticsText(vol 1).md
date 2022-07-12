 概率论与数理统计教程（第三版）
> 茆诗松、程依明、濮晓龙编著
> 为什么要费这么大周章做摘记？为了看到big picture。

摘记这本书为了：厘清概念、理解定理的证明

# 随机事件与概率

概率论与数理统计的**研究对象**是随机现象[^1]。概率论研究随机现象的模型（即概率分布）及其性质；数理统计研究随机现象的数据收集、处理及统计推断。
[^1]: 相同条件输出不同结果。

## 随机事件及其运算

在一定的条件下，并不总是出现相同结果的现象称为**随机现象**。随机现象有两个特点：（1）结果不止一个；（2）哪一个结果出现，人们事先并不知道。  
只有一个结果的现象称为**确定性现象**。  
在相同条件下可以重复的随机现象的观察、记录、实验称为**随机试验**。  
随机现象的一切可能基本结果组成的集合称为**样本空间[^2]**，记为$\Omega = \{\omega\}$，其中$\omega$表示基本结果，又称为**样本点**。  
[^2]: 所有基本结果的集合。

样本点的个数为有限个或可列[^countable]的情况归为一类，称为**离散样本空间**。  
[^countable]: 如果一个集合与正整数集合之间存在一一对应，则这个集合称为可列集。可列就是这个集合可以找到与自然数集的一一对应关系。

样本点个数为不可列无限个的情况归为一类，称为**连续样本空间**。  
随机现象的某些样本点组成的集合称为**随机事件[^3]**，简称**事件**，常用大写字母A,B,C,...表示。  
[^3]: 基本结果的集合。

样本空间$\Omega$中的单个元素组成的子集称为**基本事件**。样本空间$\Omega$的最大子集（即$\Omega$本身）称为**必然事件**。样本空间$\Omega$的最小子集（即空间$\empty$）称为**不可能事件**。  
表示随机现象结果的变量称为**随机变量[^4]**，常用大写字母X,Y,Z表示。  
[^4]: 代表随机事件。

**在同一个随机现象中，不同的设置可获得不同的随机变量，如何设置可按需要进行**。  
**包含关系**：如果属于A的样本点必属于B，则称A被包含在B中，或称B包含A，记为$A\subset B$，或$B\supset A$。用概率论的语言说：事件A发生必然导致事件B发生。  
**相等关系**：如果事件A与事件B满足，属于A的样本点必属于B，而且属于B的样本点必属于A，即$A\subset B$且$B\subset A$，则称事件A与B相等，记为$A=B$。  
**互不相容**：如果A与B没有相同的样本点，则称A与B互不相容。用概率论的语言说：A与B互不相容就是事件A与事件B不可能同时发生。  
**事件A与B的并**：记为$A\cup B$。由事件A与B中所有的样本点（相同的只计入一次）组成的新事件。或用概率论的语言说，事件A与B中至少有一个发生。  
**事件A与B的交**：记为$A\cap B$，或简记为AB。由事件A与B中公共的样本点组成的新事件。或用概率论的语言说，事件A与B同时发生。  
**事件A对B的差**：记为$A-B$。由事件A中而不在B中的样本点组成的新事件。或用概率论的语言说，事件A发生而B不发生。  
**事件A的对立事件**：记为$\bar{A}$，由在$\Omega$中，而不在A中的样本点组成的新事件。或者用概率论的语言说，A不发生，即$\bar{A} = \Omega - A$。  
A与B互为对立事件的充要条件是：$A\cap B = \emptyset$，且$A\cup B= \Omega$。  
需要注意的是：（1）对立事件一定是互不相容事件，即$A\cap \bar{A} = \empty$，但互不相容的事件不一定是对立事件。（2）A-B可以记为$A\bar{B}$。  
**事件的运算性质**：

1. 交换律：$A\cup B = B\cup A, AB=BA$  
2. 结合律：$(A\cup B)\cup C = A\cup (B\cup C)，(AB)C = A(BC)$  
3. 分配律：$(A\cup B)\cap C = AC\cup BC, (A\cap B)\cup C = (A\cup C)\cap (B\cup C)$  
4. 对偶律（德摩根公式）
   1. 事件并的对立等于对立的交：$\overline{A\cup B}=\bar{A}\cap \bar{B}$  
   2. 事件交的对立等于对立的并：$\overline{A\cap B}=\bar{A}\cup \bar{B}$

**定义**：设$\Omega$为一样本空间，$\mathscr{F}$为$\Omega$的某些子集所组成的集合类[^set]。如果$\mathscr{F}$满足：

1. $\Omega \in \mathscr{F}$
2. 若$A\in \mathscr{F}$，则对立事件$\bar{A}\in \mathscr{F}$
3. 若$A_n\in \mathscr{F}, n=1,2,...$，则可列并$\bigcup\limits_{n=1}^{\infty}A_n\in \mathscr{F}$
则称$\mathscr{F}$为一个**事件域**，又称为$\sigma$域或$\sigma$代数。  
[^set]: 即集合的集合，包含事件的容器，是对所有基本事件之可能组合的描绘。事件域的定义是为了定义概率。

**样本空间的分割**：对样本空间$\Omega$，如果有n个事件$D_1,D_2,...,D_n$满足：诸$D_i$互不相容，且$\bigcup\limits_{i=1}^nD_i=\Omega$，则称$D_1,D_2,...,D_n$为样本空间$\Omega$的一组**分割**。也可以是可列个不相容事件$D_1,D_2,...,D_n,...$组成$\Omega$的一个分割。

## 概率的定义及其确定方法

概率是随机事件发生的可能性大小。  
1900年希尔伯特提出要建立概率的公理化定义，以最少的几条本质特性出发去刻画概率的概念。1933年苏联数学家柯尔莫哥洛夫首次提出了概率的公理化定义。  
**定义**：设$\Omega$为一个样本空间，$\mathscr{F}$为$\Omega$的某些子集组成的一个事件域。如果对任一事件$A\in \mathscr{F}$，定义在$\mathscr{F}$上的一个实值函数P(A)满足：

1. 非负性公理：若$A\in \mathscr{F}$，则$P(A)\geq 0$
2. 正则性公理：$P(\Omega) = 1$
3. 可列可加性公理[^addable]：若$A_1,A_2,...,A_n,...$互不相容，则$P(\bigcup\limits_{i=1}^\infty A_i)=\sum\limits_{i=1}^\infty P(A_i)$，则称P(A)为事件A的**概率**，称三元素$(\Omega, \mathscr{F},P)$为**概率空间**。
[^addable]: 互不相容事件并的概率等于有关独立事件概率的和。

排列组合的计数原理：

1. **乘法原理**：如果某件事需经过k个步骤才能完成，做第一步有$m_1$种方法，做第二步有$m_2$种方法，...，做第k步有$m_k$种方法，那么完成这件事共有$m_1\times m_2\times ... \times m_k$种方法。
2. **加法原理**：如果某件事可由k类不同途径之一去完成，在第一类途径中有$m_1$中完成方法，在第二类途径中有$m_2$种完成方法，...，在第k类途径中有$m_k$种完成方法，那么完成这件事共有$m_1+m_2+...+m_k$种方法。

**排列**：从n个不同元素中任取$r(r\leq n)$个元素排成一列（考虑元素先后出现次序），称此为一个排列，此种排列的总数记为$P_n^r = n\times (n-1)\times ...\times(n-r+1)={n!\over (n-r)!}$  
**重复排列**：从n个不同元素中每次取出一个，放回去后再取一个，如此连续取r次所得的排列称为重复排列，此种重复排列数共有$n^r$个。  
**组合**：从n个不同元素中任取$r(r\leq n)$个元素并成一组（不考虑元素间的先后次序），称此为一个组合，此种组合的总数记为$\left ( \begin{matrix}
    n\\r
\end{matrix}\right)$或$C_n^r = {P_n^r\over r!}={n!\over r!(n-r)!}$

- 组合具有性质[^combination]：$C_n^r=C_n^{n-r}$
[^combination]: 取出哪些确定后，剩下哪些也就唯一确定了。

**重复组合[^recom]**：从n个不同元素中每次取出一个，放回后再取下一个，如此连续取r次所得的组合称为重复组合，此种重复组合总数为$C_{n+r-1}^r$。
[^recom]: 转化成放球问题来证明。

**确定概率的频率方法**是在大量重复试验中，用频率的稳定值去获得概率的一种方法，其基本思想是：

1. 与考察事件A有关的随机现象可大量重复进行。
2. 在n次重复试验中，即n(A)为事件A出现的次数，又称n(A)为事件A的**频数**。称$f_n(A) = {n(A)\over n}$为事件A出现的**频率**。
3. 人们的长期实践表明：随着试验重复次数n的增加，频率$f_n(A)$会稳定在某一常数a附近，我们称这个常数为频率的稳定值。这就是我们所求的**概率**。  

**确定概率的古典方法**是在经验事实的基础上，对被考察时间的可能性进行逻辑分析后得出该事件的概率，其基本思想是：

1. 所涉及的随机现象只有有限个样本点，譬如为n个。
2. 每个样本点发生的可能性相等（称为等可能性）。
3. 若事件A含有k个样本点，则事件A的概率为$P(A)={事件A所含样本点的个数\over \Omega 中所有样本点的个数} = {k\over n}$。

**确定概率的几何方法**，其基本思想是：

1. 如果一个随机现象的样本空间$\Omega$充满某个区域，其度量（长度、面积或体积等）大小可用$S_\Omega$表示
2. 任意一点落在度量相同的子区域内（可能位置不同）是等可能的。
3. 若事件A为$\Omega$中的某个子区域，且其度量大小可用$S_A$表示，则事件A的概率为$P(A)={S_A\over S_\Omega}$。这个概率称为几何概率。  

**确定概率的主观方法**：统计界的贝叶斯学派认为：**一个事件的概率是人们根据经验对该事件发生的可能性所给出的个人信念**。这样给出的概率称为**主观概率**。  
> 用主观方法得出的随机事件发生的可能性大小，本质上是对随机事件概率的一种推断和估计。虽然结论的精确性有待事件的检验和修正，但结论的可信性在统计意义上是有价值的。

## 概率的性质

1. $P(\empty) = 0$
2. **有限可加性**：若有限个事件$A_1,A_2,...,A_n$互不相容，则有$P(\bigcup\limits_{i=1}^n A_i)=\sum\limits_{i=1}^n P(A_i)$
3. 对任一事件A，有$P(\bar{A})=1- P(A)$
4. 若$A\supset B$，则$P(A-B)=P(A)-P(B)$
5. 对任意两个事件A,B，有$P(A-B)=P(A)-P(AB)$
6. **加法公式**：对任意两个事件A,B,有$P(A\cup B)=P(A)+P(B)-P(AB)$。对任意n个事件$A_1,A_2,...,A_n$，有$P(\bigcup\limits_{i=1}^n A_i) = \sum\limits_{i=1}^n P(A_i) - \sum\limits_{i\leq i\lt j \leq n} P(A_iA_j)+\sum\limits_{i\leq i\lt j \lt k \leq n} P(A_iA_jA_k)+...+(-1)^{n-1}P(A_1A_2...A_n)$

**推论（半可加性）**：对任意两个事件A,B,有$P(A\cup B) \leq P(A)+P(B)$。对任意n个事件$A_1,A_2,...,A_n$，有$P(\bigcup\limits_{i=1}^nA_i)\leq \sum\limits_{i=1}^nP(A_i)$  

**定义**
（1）对$\mathscr{F}$中任一单调不减[^nondecr]的事件序列$F_!\subset F_2 \subset ... \subset F_n \subset ...$，称可列并$\bigcup\limits_{n=1}^\infty F_n$为$\{F_n\}$的**极限事件**，记为$\lim\limits_{n\rightarrow \infty}F_n=\bigcup\limits_{n=1}^\infty F_n$
[^nondecr]: 包含的样本点越来越多。

（2）对$\mathscr{F}$中任一单调不增的事件序列$E_1\supset E_2 \supset ... \supset E_n \supset ...$，称可列交$\bigcap\limits_{n=1}^\infty E_n$为$\{E_n\}$的**极限事件**，记为$\lim\limits_{n\rightarrow \infty} E_n = \bigcap\limits_{n=1}^\infty E_n$

**定义**：对$\mathscr{F}$上的一个概率P,
（1）若它对$\mathscr{F}$中任一单调不减的事件序列$\{F_n\}$均成立$\lim\limits_{n\rightarrow \infty}P(F_n)=P(\lim\limits_{n\rightarrow \infty}F_n)$[^9]，则称概率P是**下连续**的。
（2）若它对$\mathscr{F}$中任一单调不增的事件序列$\{E_n\}$均成立$\lim\limits_{n\rightarrow \infty}P(E_n)=P(\lim\limits_{n\rightarrow \infty}E_n)$，则称概率P是**上连续**的。
[^9]: 概率的极限等于极限的概率。

**概率的连续性**：若P为事件域$\mathscr{F}$上的概率，则P既是下连续的，又是上连续的。

若P是$\mathscr{F}$上满足$P(\Omega)=1$的非负集合函数，则它具有可列可加性的充要条件是：

1. 它是有限可加的
2. 它是下连续的

## 条件概率

条件概率是概率论中的一个既重要又实用的概念。
所谓条件概率，是指在某事件B发生的条件下，另一事件A发生的概率，记为P(A|B)，它与P(A)是不同的两类概率。

**定义**：设A与B是样本空间$\Omega$中的两个事件，若$P(B)\gt 0$，则称$P(A|B)={P(AB)\over P(B)}$为“在B发生下A的条件概率”，简称**条件概率**[^conp]。
[^conp]: 这意味着，计算条件概率P(A|B)是在样本空间$\Omega$缩小为$\Omega_B=B$下进行的。这个解释make sense。从定义出发，B发生这个限定条件就是在缩小样本空间。所以，条件概率就是新样本空间上的概率！

条件概率是概率，即若设$P(B)\gt 0$，则

1. $P(A|B)\geq 0, A\in \mathscr{F}$
2. $P(\Omega|B)=1$[^regular]
3. 若$\mathscr{F}$中的$A_1,A_2,...,A_n,...$互不相容，则$P(\bigcup\limits_{n=1}^\infty A_n|B)=\sum\limits_{n=1}^\infty P(A_n|B)$
[^regular]: 这个规则叫正则，即regular，意即“规则的”。

**乘法公式**

1. 若$P(B)\gt 0$，则$P(AB)=P(B)P(A|B)$
2. 若$P(A_1A_2...A_{n-1})\gt 0$，则$P(A_1A_2...A_n)=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)···P(A_n|A_1A_2...A_{n-1})$

**全概率公式**
设$B_1,B_2,...,B_n$为样本空间$\Omega$的一个分割，即$B_1,B_2,...,B_n$互不相容，且$\bigcup\limits_{i=1}^\infty B_i = \Omega$，如果$P(B_i)\gt 0, i = 1,2,...,n$，则对任一事件A有$P(A)=\sum\limits_{i=1}^n P(B_i)P(A|B_i)$

- 证明：因为$A=A\Omega=A(\bigcup\limits_{i=1}^n B_i) = \bigcup\limits_{i=1}^n (AB_i)$，且$AB_1,AB_2,...,AB_n$互不相容，所以由可加性得$P(A)=P(\bigcup\limits_{i=1}^n (AB_i))=\sum\limits_{i=1}^n P(AB_i)$，再将$P(AB_i)=P(B_i)P(A|B_i)， i=1,2,...,n$，代入上市即得全概率公式。[^wholep]
[^wholep]: 全概率公式的核心思想是，把整个事件A的概率化为各$AB_i$之和($\sum B_i = \Omega$)。所以，全概率公式定义在整个样本空间的一个分割之上。按照这个思路容易构建出全概率公式。

**贝叶斯公式**
设$B_1,B_2,...,B_n$是样本空间$\Omega$的一个分割，即$B_1,B_2,...,B_n$互不相容，且$\bigcup\limits_{i=1}^n B_i=\Omega$，如果$P(A)\gt 0, P(B_i)\gt 0, i=1,2,...,n$，则
$$P(B_i|A)={p(B_i)P(A|B_i)\over \sum\limits_{j=1}^n P(B_j)P(A|B_j)}, i=1,2,...,n.$$

- 证明：由条件概率的定义$P(B_i|A)={P(AB_i)\over P(A)}$.
- 对该式分子用乘法公式，分母用全概率公式，$P(AB_i)=P(B_i)P(A|B_i), P(A)=\sum\limits_{j=1}^n P(B_j)P(A|B_j)$，
- 即得$P(B_i|A)={p(B_i)P(A|B_i)\over \sum\limits_{j=1}^n P(B_j)P(A|B_j)}$

在贝叶斯公式中，如果称$P(B_i)$为$B_i$的**先验概率**，称$P(B_i|A)$为$B_i$的**后验概率**，则贝叶斯公式是专门用于计算后验概率的，也就是通过A的发生这个新信息，来对$B_i$的概率作出的修正[^Bayes]。
[^Bayes] 这个解释具有重要的理论意义，它是统计学习的理论基础。贝叶斯公式的分子是$AB_i$的条件概率表达式；分布是A基于分割$\{B_i\}$的全概率公式。

## 独立性

独立性是概率论中又一个重要概念，利用独立性可以简化概率的计算。
两个事件之间的独立性是指：一个事件的发生不影响另一个事件的发生，即$P(AB)=P(A)P(B)$。

**定义**：如果$P(AB)=P(A)P(B)$成立，则称时间A与B**互相独立**，简称A与B独立。否则称A与B不独立或相依。
若事件A与B独立，则A与$\bar{B}$独立，$\bar{A}$与B独立，$\bar{A}$与$\bar{B}$独立。

**定义**：设A,B,C是三个事件，如果有$$\left \{ \begin{array}{l}
    P(AB)=P(A)P(B)，\\
    P(AC)=P(A)P(C)，\\
    P(BC)=P(B)P(C)，
\end{array} \right .$$
则称A,B,C**两两独立**。若还有$P(ABC)=P(A)P(B)P(C)$，则称A,B,C**相互独立**。

**定义**：设有n个事件$A_1,A_2,...,A_n$，对任意的$1\leq i \lt j\lt k\lt ...\leq n$，如果以下等式均成立$$
\left \{ \begin{array}{l}
    P(A_iA_j)=P(A_i)P(A_j)，\\
    P(A_iA_jA_k)=P(A_i)P(A_j)P(A_k)，\\
    ......\\
    P(A_1A_2···A_n)=P(A_1)P(A_2)···P(A_n)，
\end{array} \right.
$$
则称此n个事件$A_1,A_2,...,A_n$相互独立。

**定义**
设有两个试验$E_1$和$E_2$，假如试验$E_1$的任一结果（事件）与试验$E_2$的任一结果（事件）都是相互独立的，则称**这两个试验相互独立**。
类似地，可以定义试验$E_1,...,E_n$相互独立。如果这n个独立试验还是相同的，则称其为**n重独立重复试验**。如果在n重独立重复试验中，每次试验的可能结果为两个：$A或\bar{A}$，则称这种试验为**n重伯努利(Bernoulli)试验[^Bernoulli]**。
[^Bernoulli]: 三个条件：独立、重复、2个结果。

# 随机变量及其分布

为了进行定量的数学处理，必须把随机现象的结果数量化。这就是引进随机变量的原因。

## 随机变量及其分布

**定义**：定义在样本空间$\Omega$上的实值函数$X=X(\omega)$称为**随机变量**，常用大写字母X,Y,Z等表示随机变量，其取值用小写字母x,y,z等表示。
假如一个随机变量可能取有限个或可列个值，则称其为**离散随机变量**。假如一个随机变量的可能取值充满数轴上的一个区间（a，b）,则称其为**连续随机变量**，其中，a可以是$-\infty$，b可以是$\infty$
> 这个定义表明：随机变量X是样本点$\omega$的一个函数。
> 与微积分中的变量不同，概率论中的随机变量X是一种“**随机取值的变量且伴随一个分布**”。以离散随机变量为例，我们不仅要知道X可能取哪些值，而且还要知道它取这些值的概率各是多少，这就需要分布的概念。有没有分布式是区分一般变量与随机变量的主要标志。

**定义**：设X是一个随机变量，对任意实数x，称$$F(x)=P(X\leq x)$$
为随机变量X的**分布函数**。且称X服从$F(x)$，记为$X\sim F(x)$.有时也可用$F_X(x)$以表明是X的分布函数。

**定理**
任一分布函数$F(x)$都具有如下三条基本性质：

1. 单调性 $F(x)$是定义在整个实数轴$(-\infty, \infty)$上的单调非减函数，即对任意的$x_1\lt x_2$，有$F(x_1)\leq F(x_2)$
2. 有界性 对任意的x，有$0 \leq F(x) \leq 1$，且$$F(-\infty) = \lim\limits_{x\rightarrow -\infty} F(x) = 0\\
F(\infty) = \lim\limits_{x\rightarrow \infty} F(x) = 1.
$$
3. 右连续性 $F(x)$是x的右连续函数，即对任意的$x_0$，有$$\lim\limits_{x\rightarrow x_0+0} F(x) = F(x_0)$$即$$F(x_0+0)=F(x_0)$$[^distribution]
[^distribution]: 以上三条基本性质是分布函数必须具有的性质，还可以证明：满足这三条基本性质的函数必定是某个随机变量的分布函数。从而**这三条基本性质称为判别某个函数是否能成为分布函数的充要条件**。

**定义**：设X是一个离散随机变量，如果X的所有可能取值是$x_1,x_2,...,x_n,...$，则称X去$x_i$的概率$$p_i=p(x_i)=P(X=x_i), i=1,2,...,n,...$$为X的**概率分布列**或简称为**分布列**，记为$X\sim \{p_i\}$

**分布列的基本性质**

1. 非负性 $p(x_i)\geq 0, i=1,2,...$
2. 正则性 $\sum\limits_{i=1}^\infty = 1$

> 以上两条基本性质是分布列必须具有的性质，也是判别某个数列能否称为分布列的充要条件。

**定义**：设随机变量X的分布函数为$F(x)$，如果存在实数轴上的一个非负可积函数$p(x)$，使得对任意实数x有$$F(x)=\int_{-\infty}^x p(t)dt$$则称$p(x)$为X的**概率密度函数**，简称为**密度函数**或**密度**。同时称X为**连续随机变量**，称$F(x)$为**连续分布函数**。

**密度函数的基本性质**

1. 非负性 $p(x)\geq 0$  
2. 正则性 $\int_{-\infty}^\infty p(x)dx =1$（含有p(x)的可积性）

## 随机变量的数学期望

随机变量的重要特征数：数学期望，就是**均值**。

**定义**
设离散随机变量X的分布列为$$p(x_i)=P(X=x_i),i=1,2,...,n,...$$
如果$\sum\limits_{i=1}^\infty|x_i|p(x_i)\lt \infty$，则称$E(X)=\sum\limits_{i=1}^\infty x_ip(x_i)$为随机变量X的**数学期望**，或称为该分布的数学期望，简称**期望**或**均值**。

**定义**：设连续随机变量X的密度函数为p(x)。如果$$\int_{-\infty}^\infty |x|p(x)dx \lt \infty$$则称$E(X)=\int_{-\infty}^\infty xp(x)dx$为X的**数学期望**，或称为该分布p(x)的数学期望，简称**期望**或**均值**。
> 数学期望的理论意义是深刻的，它是**消除随机性的主要手段**。
> 数学期望在实际中应用广泛，$E(X)$常作为X的分布的代表（一种统计指标）参与同类指标的比较。

**定理**
若随机变量X的分布用分布列$p(x_i)$或用密度函数p(x)表示，则X的某一函数$g(X)$的数学期望为
$$E[g(X)] = \left \{ \begin{array}{c}
    \sum\limits_i g(x_i)p(x_i)，在离散场合\\
    \int_{-\infty}^\infty g(x)p(x)dx，在连续场合
\end{array} \right.$$

若c是常数，则$E(c)=c$。
对任意常数a，有$E(aX)=aE(X)$。
对任意的两个函数$g_1(x)$和$g_2(x)$，有$E[g_1(x)\plusmn g_2(X)]=E[g_1(X)]\plusmn E[g_2(X)]$

## 随机变量的方差与标准差

随机变量X的数学期望$E(X)$是分布的一种位置特征数，它刻画了X的取值总在$E(X)$周围波动。但这个位置特征数无法反映出随机变量取值的“波动大小”。方差与标准差正是度量此种波动大小的最重要的两个特征数。

**定义**：若随机变量$X^2$的数学期望$E(X^2)$存在，则称偏差平方$(X-E(X))^2$的数学期望$E(X-E(X))^2$为随机变量X（或相应分布）的**方差[^var]**，记为$$Var(X)=E(X-E(X))^2=\left \{ \begin{array}{c}
    \sum\limits_i (x_i-E(X))^2p(x_i)，在离散场合\\
    \int_{-\infty}^\infty (x-E(X))^2p(x)dx，在连续场合
\end{array} \right.$$
称方差的平方根$\sqrt{Var(X)}$为随机变量X（或相应分布）的**标准差**，记为$\sigma (X)$，或$\sigma_X$。
[^var] 方差就是偏差的平方。方差与标准差之间的差别主要在量纲上，由于标准差与所讨论的随机变量、数学期望有相同的量纲，其加减$E(X)\plusmn k\sigma(X)$是有意义的（k为正实数），所以实际中，人们比较乐意选用标准差。

**方差的性质**

1. $Var(X)=E(X^2)-[E(X)]^2$
2. 常数的方差为0，即$Var(c)=0$，其中c是常数。
3. 若a,b是常数，则$Var(aX+b)=a^2Var(X)$

**切比雪夫(Chebyshev)不等式**
设随机变量X的数学期望和方差都存在，则对任意常数$\epsilon \gt 0$，有$$P(|X-E(X)|\geq \epsilon)\leq {Var(X)\over \epsilon^2}$$或$$P(|X-E(X)|\lt \epsilon)\geq 1-{Var(X)\over \epsilon^2}$$

- 证明：设X是一个连续随机变量，其密度函数为p(x)，记为$E(X)=a$，我们有$P(|X-a|\geq \epsilon) = \int\limits_{\{x:|x-a|\geq \epsilon\}} p(x)dx \leq \int\limits_{\{x:|x-a|\geq \epsilon\}} {(x-a)^2\over \epsilon^2}p(x)dx \leq {1\over \epsilon^2}\int\limits_{-\infty}^\infty (x-a)^2p(x)dx = {Var(X)\over \epsilon^2}$

> 在概率论中，事件$\{|X-E(X)|\geq \epsilon\}$称为**大偏差**，其概率$P(|X-E(X)|\geq \epsilon)$称为**大偏差发生概率**。切比雪夫不等式给出大偏差发生概率的上界，这个上界与方差成正比，方差愈大上届也愈大。

**定理**
若随机变量X的方差存在，则$Var(X)=0$的充要条件是X几乎处处为某个常数a，即P(X=a)=1

## 常用离散分布

随机变量有千千万万个，但常用分布并不是很多，熟悉这些常用分布对认识其他分布会很有帮助。

**二项分布**
如果记X为n重伯努利试验中成功（记为事件A）的次数，则X的可能取值为0,1,...,n.记p为每次试验中A发生的概率，即P(A)=p，则$P(\bar{A})=1-p$。因为n重伯努利试验的基本结果可以记为$$\omega = (\omega_1,\omega_2,...,\omega_n)$$其中$\omega_i$或者为$A$，或者为$\bar{A}$。这样的$\omega$共有$2^n$个，这$2^n$个样本点$\omega$组成了样本空间$\Omega$。  
若某个样本点$\omega = (\omega_1,\omega_2,...,\omega_n) \in \{X=k\}$，意味着$\omega_1,\omega_2,...,\omega_n$中有k个A，n-k个$\bar{A}$，所以由独立性知，$P(\omega) = p^k(1-p)^{n-k}$，而事件{X=k}中这样的$\omega$共有$C_n^k$个，所以X的分布列为$P(X=k)=C_n^k p^k(1-p)^{n-k}，k=0,1,...,n$。这个分布称为**二项分布**，记为$X\sim b(n, p)$
> 二项概率$C_n^k p^k(1-p)^k$恰好是n次二项式$(p+(1-p))^n$的展开式中的第$k+1$项，这正是其名称的由来。

**二点分布**
n=1时的二项分布$b(1, p)$称为**二点分布**，或称**0-1分布**，或称**伯努利分布**，其分布列为$P(X=x)=p^x(1-p)^{1-x}, x=0,1$或记为$$
\begin{array}{c|lcr}
X & 0 & 1\\
\hline
P & 1-p & p\\
\end{array}
$$
> 二项分布b(n, p)与二点分布b(1, p)之间的联系：服从二项分布的随机变量总可分解为n个独立同为二点分布的随机变量之和。

**二项分布的数学期望和方差**
设随机变量$X\sim b(n, p)$，则
$$E(X) = \sum\limits_{k=0}^n kC_n^k p^k(1-p)^{n-k}=np\sum\limits_{k=1}^n C_{n-1}^{k-1}p^{k-1}(1-p)^{(n-1)(k-1)}=np[p+(1-p)]^{n-1}=np$$又因为
$$
E(X^2)=\sum\limits_{k=0}^n k^2 C_n^k p^k(1-p)^{n-k} = \sum\limits_{k=1}^n (k-1+1) kC_n^k p^k(1-p)^{n-k} =\\
 \sum\limits_{k=1}^n k(k-1) C_n^k p^k(1-p)^{n-k} + \sum\limits_{k=1}^n kC_n^k p^k (1-p)^{n-k} = \sum\limits_{k=2}^n k(k-1)C_n^k p^k(1-p)^{n-k} + np=\\
  n(n-1)p^2 \sum\limits_{k=2}^n C_{n-2}^{k-2} p^{k-2}(1-p)^{(n-2)-(k-2)}+np = n(n-1)p^2 + np
$$由此得X的方差为$Var(X) = E(X^2)-(E(X))^2 = n(n-1)p^2 +np -(np)^2 = np(1-p)$

**泊松分布**
泊松分布的概率分布列是$P(X=k)={\lambda^k\over k!}e^{-\lambda}, k= 0,1,2,...$，其中参数$\lambda \gt 0$，记为$X\sim P(\lambda)$
> 泊松分布式一种常用的离散分布，常与单位时间（或单位面积、单位产品等）上的计数过程联系。

**泊松分布的数学期望和方差**
设随机变量$X\sim P(\lambda)$，则
$$E(X)=\sum\limits_{k=0}^\infty k{\lambda^k\over k!}e^{-\lambda}=\lambda e^{\lambda}\sum\limits_{k=1}^\infty {\lambda^{k-1}\over (k-1)!}=\lambda e^{-\lambda}e^{\lambda}=\lambda$$
又因为
$$
E(X^2)=\sum\limits_{k=0}^\infty k^2{\lambda^k\over k!}e^{-\lambda}=\sum\limits_{k=1}^\infty k{\lambda^k\over (k-1)!}e^{-\lambda}\\
=\sum\limits_{k=1}^\infty [(k-1)+1]{\lambda^k\over (k-1)!}e^{-\lambda}=\lambda^2e^{-\lambda}\sum\limits_{k=2}^\infty {\lambda^{k-2}\over (k-2)!}+ \lambda e^{-\lambda}\sum\limits_{k=1}^\infty {\lambda^{k-1}\over (k-1)!}=\lambda^2 + \lambda
$$
由此得X的方差为$Var(X)=E(X^2)-(E(X))^2 = \lambda^2 + \lambda -\lambda^2 = \lambda$
> 泊松分布$P(\lambda)$中的参数$\lambda$既是数学期望又是方差。

泊松分布有一个非常实用的特性，即可以用泊松分布作为二项分布的一种近似。
**泊松定理**
在n重伯努利试验中，记事件A在一次试验中发生的概率为$p_n$(与试验次数n有关)，如果当$n\rightarrow \infty$时，有$np_n\rightarrow \lambda$，则
$$
\lim\limits_{n\rightarrow \infty} C_n^k p_n^k(1-p_n)^{n-k}={\lambda^k\over k!}e^{-\lambda}
$$

**超几何分布**
从一个有限总体中进行不放回抽样常会遇到超几何分布。超几何分布是一种常用的离散分布，它在抽样理论中占有重要地位。  
设有N件产品，其中有M件不合格。若从中不放回地随机抽取n件，则其中含有**不合格品的件数服从超几何分布**，记为$X\sim h(n,N,M)$。超几何分布的概率分布列为
$$
P(X=k)={C_M^k C_{N-M}^{n-k}\over C_N^n}, k= 0,1,2,...,r
$$其中$r=min\{M, n\}$，且$M\leq N, n\leq N$，n,N,M均为正整数。

**超几何分布的期望和方差**
若$X\sim h(n,N,M)$，则X的数学期望为
$$
E(X) = \sum\limits_{k=0}^r k {C_M^kC_{N-M}^{n-k}\over C_N^n}=n{M\over N}\sum\limits_{k=1}^r {C_{M-1}^{k-1}C_{N-M}^{n-k}\over C_{N-1}^{n-1}}=n{M\over N}
$$又因为
$$
E(X^2)=\sum\limits_{k=0}^r k^2 {C_M^kC_{N-M}^{n-k}\over C_N^n}=\sum\limits_{k=2}^r k(k-1){C_M^kC_{N-M}^{n-k}\over C_N^n}+n{M\over N}={M(M-1)\over C_N^n}\sum\limits_{k=2}^r C_{M-2}^{k-2}C_{N-M}^{n-k}+n{M\over N} = {M(M-1)\over C_N^n}C_{N-2}^{n-2}+n{M\over N}={M(M-1)n(n-1)\over N(N-1)}+n{M\over N}
$$
由此可得X的方差为$Var(X)=E(X^2)-[E(X)]^2 = {nM(N-M)(N-n)\over N^2(N-1)}$

**几何分布**
在伯努利试验序列中，记每次试验中事件A发生的概率为p，如果X为**事件A首次出现时的试验次数**，则X的可能取值为1,2,...,称X服从**几何分布**，记为$X\sim Ge(p)$，其分布列为$P(X=k)=(1-p)^{k-1}p, k= 1,2,...$

**几何分布的数学期望和方差**
设随机变量X服从几何分布$Ge(p)$，令$q=1-p$，利用逐项微分可得X的数学期望为
$$
E(X)=\sum\limits_{k=1}^\infty kpq^{k-1}=p\sum\limits_{k=1}^\infty kq^{k-1} = p\sum\limits_{k=1}^\infty {dq^k\over dq}=p{d\over dq}(\sum\limits_{k=0}^\infty q^k)= p{d\over dq}({1\over {1-q}})=p{1\over (1-q)^2}={1\over p}
$$
又因为
$$
E(X^2)=\sum\limits_{k=1}^\infty k^2pq^{k-1}=p[\sum\limits_{k=1}^\infty k(k-1)q^{k-1}+\sum\limits_{k=1}^\infty lq^{k-1}]=pq\sum\limits_{k=1}^\infty k(k-1)q^{k-2} + {1\over p}\\
=pq\sum\limits+{k=1}^\infty {d^2\over dq^2}q^k + {1\over p}=pq{d^2\over dq^2}(\sum\limits_{k=0}^\infty q^k)+{1\over p}={2q\over p^2}+{1\over p}
$$由此得X的方差为
$Var(X) = E(X^2)-[E(X)]^2 = {2q\over p^2} + {1\over p} - {1\over p^2} = {{1-p}\over p^2}$

**定理**：几何分布的无记忆性
设$X\sim Ge(p)$，则对任意正整数m与n有$P(X\gt m+n|X \gt m) = P(X\gt n)$
> 这个定理表明：在前m次试验中A没有出现的条件下，在接下去的n次试验中A仍未出现的概率只与n有关，而与以前的m次试验无关，似乎忘记了前m次试验结果，这就是无记忆性。

**负二项分布（帕斯卡分布）**
在伯努利试验序列中，记每次试验中事件A发生的概率为p，如果X为**事件A第r次出现时的试验次数**，则X的可能取值为$r,r+1,...,r+m,...$称X服从负二项分布或帕斯卡分布，其分布列为
$$
P(X=k)=C_{k-1}^{r-1}p^r(1-p)^{k-r}, k=r,r+1,...
$$记为$X\sim Nb(r,p)$。当r=1时，即为几何分布。

## 常用连续分布

**正态分布**
正态分布，也称高斯分布，是概率论与数理统计中最重要的一个分布。
中心极限定理表明：一个随机变量如果是由大量微小的、独立的随机因素叠加而成，那么这个变量一般都可以认为服从正态分布。因此很多随机变量可以用正态分布描述或近似描述。
若随机变量X的密度函数为
$$
p(x)={1\over \sqrt{2\pi}\sigma}e^{(x-\mu)^2\over 2\sigma^2}, -\infty \lt x \lt \infty
$$
则称X服从**正态分布**，称X为**正态变量**，记作$X\sim N(\mu, \sigma^2)$。其中参数$-\infty \lt \mu \lt \infty, \sigma \gt 0$
正态分布$N(\mu, \sigma^2)$的分布函数为$F(x)={1\over \sqrt{2\pi} \sigma}\int_{-\infty}^x e^{-(t-\mu)^2\over 2\sigma^2}dt$
> 正态密度函数的位置由参数$\mu$所确定，称$\mu$为**位置参数**。正态密度函数的尺度由参数$\sigma$所确定，称$\sigma$为**尺度参数**。

**标准正态分布**
称$\mu = 0, \sigma =1$时的正态分布N(0,1)为标准正态分布。
通常记标准正态变量为U，记标准正态分布的密度函数为$\phi(u)$，分布函数为$\Phi(u)$，即：
$$
\phi(u) = {1\over \sqrt{2\pi}}e^{-{u^2\over 2}}, -\infty \lt u \lt \infty,\\
\Phi(u) = {1\over \sqrt{2\pi}}\int_{-\infty}^u e^{-{u^2\over 2}dt}, -\infty \lt u \lt \infty ,
$$
> 标准正态分布的分布函数不含任何未知参数，故其值完全可以算出。

一般正态变量都可以通过一个**线性变换**（标准化）变成标准正态变量。
**定理**
若随机变量$X\sim N(\mu, \sigma^2)$，则$U={(X-\mu)\over \sigma} \sim N(0, 1)$

**正态分布的数学期望和方差**
设随机变量$X\sim N(\mu, \sigma^2)$，由于$U={(X-\mu)\over \sigma} \sim N(0,1)$，所以U的数学期望为
$$
E(U)={1\over \sqrt{2\pi}}\int_{-\infty}^{\infty}ue^{-{u^2\over 2}}du
$$因为被积函数是一个奇函数，所以其积分值等于0，即E(U)=0，又因为$X=\mu + \sigma U$，所以由数学期望的性质得$E(X)=\mu +\sigma\times 0 = \mu$
又因为
$$
Var(U)=E(U^2)={1\over \sqrt{2\pi}}\int_{-\infty}^\infty u^2e^{-{u^2}\over 2}du = {1\over \sqrt{2\pi}}\int_{-\infty}^\infty ud(-e^{-{u^2\over 2}}) \\
= {1\over \sqrt{2\pi}}(-ue^{-{u^2\over 2}}|_{-\infty}^\infty + \int_{-\infty}^\infty e^{-{u^2\over 2}}du) = {1\over \sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-{u^2\over 2}}du = {1\over \sqrt{2\pi}}\sqrt{2\pi}=1
$$由$X = \mu + \sigma U$，所以$Var(X)=Var(\mu + \sigma U) = \sigma^2$

**均匀分布**
若随机变量X的密度函数为$$p(x)= \left \{ \begin{array}{l}
    {1\over (b-a)}, a\lt x \lt b,\\
    0, 其他
\end{array} \right.$$
则称X服从区间(a, b)上的**均匀分布**，记作$X\sim U(a, b)$，其分布函数为$$
F(x) = \left \{ \begin{array}{l}
    0, x\lt a,\\
    {x-a\over b-a}, a\leq x\lt b,\\
    1, x\geq b.
\end{array}
\right.
$$

**均匀分布的数学期望和方差**
设随机变量$X\sim U(a,b)$，则$$
E(X)=\int_{a}^b {x\over b-a}dx = {b^2-a^2\over 2(b-a)}={a+b\over 2}
$$这正是区间(a,b)的中点。
又因为$$
E(X^2)=\int_a^b{x^2\over b-a}dx = {b^3-a^3\over 3(b-a)}={a^2+ab+b^2\over 3}
$$由此可得X的方差为$Var(X)=E(X^2)-[E(X)]^2 = {a^2+ab+b^2\over 3}-{(a+b)^2\over 4}={(b-a)^2\over 12}$

**指数分布**
若随机变量X的密度函数为$$
p(x)= \left \{ \begin{array}{c}
    \lambda e^{-\lambda x}, x\geq 0,\\
    0, x\lt 0.
\end{array} \right.
$$
则称X服从**指数分布[^exp]**，记作$X\sim Exp(\lambda)$，其中参数$\lambda \gt 0$.\
指数分布的分布函数为$$
F(x)= \left \{ \begin{array}{c}
    1-e^{-\lambda x}, x\geq 0,\\
    x, x\lt 0.
\end{array} \right.
$$

[^exp]: 指数分布是一种偏态分布，由于指数分布随机变量只可能取非负实数，所以指数分布常被用作各种“寿命”分布，譬如电子元器件的寿命，动物的寿命、电话的通话时间、随机服务系统中的等待时间等都可假定服从指数分布。

**指数分布的数学期望和方差**
设随机变量$X\sim Exp(\lambda)$，则$$
E(X)=\int_0^\infty x \lambda e^{-\lambda x}dx = \int_0^\infty xd(-e^{-\lambda x})= -xe^{-\lambda x}|_0^\infty + \int_0^\infty e^{-\lambda x}dx = -{1\over \lambda}e^{-\lambda x}|_0^\infty = {1\over \lambda}
$$
在指数分布中，有时记$\theta = {1\over \lambda}$，则$\theta$为指数分布的数学期望。
又因为$$
E(X^2)=\int_0^\infty x^2\lambda e^{-\lambda x}dx = \int_0^\infty x^2d(-e^{-\lambda x})=-x^2e^{-\lambda x}|_0^\infty + 2\int_0^\infty x e^{-\lambda x}dx = {2\over \lambda^2},
$$
由此可得方差为$Var(X)=E(X^2)-[E(X)]^2={2\over \lambda^2}-{1\over \lambda^2}={1\over \lambda^2}$

**定理**：指数分布的无记忆性
如果随机变量$X\sim Exp(\lambda)$，则对任意$s\gt 0, t\gt 0$有$$
P(X\gt s+t| X\gt s) = P(X\gt t)
$$
> 上式可理解为：X是某种产品的使用寿命h，那么已知此产品使用了s(h)没有发生故障，则再使用t(h)而不发生故障的概率与已使用事件s(h)无关，只相当于重新开始使用t(h)的概率。

**伽马分布**
伽马函数如下$$
\Gamma(\alpha) = \int_0^\infty x^{\alpha-1}e^{-x}dx
$$其中参数$\alpha \gt 0$。
伽马函数具有如下性质：

1. $\Gamma(1) = 1, \Gamma({1\over 2})=\sqrt{\pi}$
2. $\Gamma(\alpha+1)=\alpha \Gamma(\alpha)$。当$\alpha$为自然数n时，有$\Gamma(n+1)=n\Gamma(n)=n!$

**伽马分布**
若随机变量X的密度函数为$$
p(x)=\left \{ \begin{array}{l}
    {\lambda^\alpha\over \Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}, x\geq 0,\\
    0, x\lt 0
\end{array} \right.
$$
则称X服从**伽马分布**，记作$X\sim Ga(\alpha, \lambda)$，其中$\alpha \gt 0$为形状参数，$\lambda \gt 0$为尺度参数。$\alpha$越大，p(x)越近似于正态密度函数，但伽马分布总是偏态分布，$\alpha$越小其偏斜程度越严重。

**伽马分布$Ga(\alpha, \lambda)$的数学期望和方差**
伽马分布的数学期望为$$
E(X)={\lambda^\alpha\over \Gamma(\alpha)}\int_0^\infty x^\alpha e^{-\lambda x}dx = {\Gamma(\alpha +1)\over \Gamma(\alpha)}={\alpha\over \lambda}
$$
又因为$$
E(X^2) = {\lambda^\alpha\over \Gamma(\alpha)}\int_0^\infty x^{\alpha +1}e^{-\lambda x}dx = {\Gamma(\alpha + 2)\over \lambda^2\Gamma(\alpha)}={\alpha(\alpha +1)\over \lambda^2}
$$由此可得X的方差$$
Var(X)=E(X^2)-[E(X)]^2 = {\alpha(\alpha +1)\over \lambda^2}-({\alpha \over \lambda})^2={\alpha\over \lambda^2}
$$

**伽马分布的两个特例**

1. $\alpha =1$时的伽马分布就是指数分布，即$Ga(1,\lambda)=Exp(\lambda)$
2. 称$\alpha = {n\over 2}, \lambda={1\over 2}$时的伽马分布是自由度为n的$\chi^2$(卡方)分布，记为$\chi^2(n)$，即$$Ga({n\over 2},{1\over 2})=\chi^2(n)$$其密度函数为$$
p(x)= \left \{ \begin{array}{l}
    {1\over 2^{n\over 2}\Gamma({n\over 2})}e^{-{x\over 2}}x^{{n\over 2}-1}, x\geq 0,\\
    0, x \lt 0
\end{array} \right.
$$

**贝塔分布**
贝塔函数是$B(a,b)=\int_0^1 x^{a -1}(1-x)^{(b-1)}dx$为贝塔函数，其中参数$a\gt 0,b\gt 0$

贝塔函数的性质：

1. B(a,b)=B(b,a)
2. 贝塔函数和伽马函数的关系：$B(a,b)={\Gamma(a)\Gamma(b)\over \Gamma(a+b)}$

**贝塔分布**
若随机变量X的密度函数为$$
p(x)= \left \{ \begin{array}{l}
    {\Gamma(a+b)\over \Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}, 0 \lt x \lt 1,\\
    0, 其他
\end{array} \right.
$$则称X服从贝塔分布，记作$X\sim Be(a,b)$，其中$a\gt 0, b \gt 0$都是形状参数[^beta]。

[^beta]: 因为服从贝塔分布Be(a,b)的随机变量是仅在区间（0，1）取值的，所以不合格品率、机器的维修率、市场的占有率、射击的命中率等各种比率选用贝塔分布作为它们的概率分布是恰当的，只要选择合适的参数a与b即可。

**贝塔分布的数学期望和方差**
贝塔分布的数学期望为$$
E(X)={\Gamma(a+b)\over \Gamma(a)\Gamma(b)}\int_0^1x^a(1-x)^{b-1}dx={\Gamma(a+b)\over \Gamma(a)\Gamma(b)}·{\Gamma(a+1)\Gamma(b)\over \Gamma(a+b+1)}={a\over a+b}
$$又因为$$
E(X^2)={\Gamma(a+b)\over \Gamma(a)\Gamma(b)}\int_0^1 x^{a+1}(1-x)^{b-1}dx={\Gamma(a+b)\over \Gamma(a)\Gamma(b)}·{\Gamma(a+2)\Gamma(b)\over \Gamma(a+b+2)}={a(a+1)\over (a+b)(a+b+1)}
$$由此可得X的方差为
$$
Var(X)={a(a+1)\over (a+b)(a+b+1)}-({a\over a+b})^2 = {ab\over (a+b)^2(a+b+1)}
$$

## 随机变量函数的分布

设$y=g(x)$是定义在$\mathbf{R}$上的一个函数，X是一个随机变量，那么$Y=g(X)$作为X的函数，同样也是一个随机变量。在实际应用中，我们感兴趣的问题是：已知随机变量X的分布，如何求出另一个随机变量$Y=g(X)$的分布。

**离散随机变量函数的分布**
$$
\begin{array}{l|c}
    X & x_1 & x_2& ... & x_n& ...\\
    \hline \\
    P&p(x_1)&p(x_2)&...&p(x_n)&...
\end{array}
$$
显然$Y=g(X)$也是一个离散随机变量，此时Y的分布就可以很简单地表示为$$
\begin{array}{l|c}
    Y & g(x_1) & g(x_2)& ... & g(x_n)& ...\\
    \hline \\
    P&p(x_1)&p(x_2)&...&p(x_n)&...
\end{array}
$$
当$g(x_1),g(x_2),...,g(x_n),...$中有某些值相等时，则把那些相等的值分别合并，并把对应的概率相加即可。

**连续随机变量函数的分布**
离散随机变量的函数仍是一个离散随机变量，但连续随机变量X的函数$Y=g(X)$不一定为连续随机变量。

1. 当$Y=g(X)$为离散随机变量：这种情况下，将Y的可能取值一一列出，再将Y取各种可能值的概率求出即可。
2. 当$g(X)$为严格单调函数时：这种情况有以下定理  

**定理**
设X是连续随机变量，其密度函数为$p_X(x)$。$Y=g(X)$是另一个连续随机变量。若$y=g(x)$严格单调，其反函数$h(y)$有连续导函数，则$Y=g(X)$的密度函数为$$
p_Y(y)=\left \{ \begin{array}{l}
    p_X[h(y)]|h`^(y)|, a \lt y\lt b,\\
    0,其他
\end{array} \right.
$$
其中$a=min\{g(-\infty), g=(\infty)\},b=max\{g(-\infty),g(\infty)\}$。

**定理**
设随机变量X服从正态分布$N(\mu,\sigma^2)$，则当$a\ne 0$时，有$Y=aX+b\sim N(a\mu+b, a^2\sigma^2)$[^linN]。
[^linN] 这个定理表明，正态变量的线性变换仍为正态变量，其数学期望和方差可直接从线性变换求得。

**定理**：对数正态分布  
设随机变量$X\sim N(\mu, \sigma^2)$，则$Y=e^X$的概率密度函数为$$
p_Y(y)=\left \{ \begin{array}{l}
    {1\over \sqrt{2\pi}y\sigma}exp\{-{(\ln y-\mu)^2\over 2\sigma^2}\}, y\gt 0,\\
    0, y\leq 0.
\end{array} \right.
$$
> 这个分布称为**对数正态分布**，记为$LN(\mu, \sigma^2)$，其中$\mu$称为对数均值，$\sigma^2$称为对数方差。

**定理**
设随机变量X服从伽马分布$Ga(\alpha, \lambda)$，则当$k\gt 0$时，有$Y=kX\sim Ga(\alpha, {\lambda\over k})$

**定理**
若随机变量X的分布函数$F_X(x)$为严格单调增的连续函数，其反函数$F_X^{-1}(y)$存在，则$Y=F_X(x)$服从(0,1)上的均匀分布U(0,1)。
> 这个定理表明：均匀分布在连续分布类中占有特殊地位。任一连续随机变量X都可通过其分布函数$F(x)$与均匀分布随机变量U发生关系。

3. 当g(x)为其他形式时：可直接由Y的分布函数$F_Y(y)=P(g(x)\leq y)$出发，按函数$g(x)$的特点作个案处理。

## 分布的其他特征数

数学期望和方差是随机变量最重要的两个特征数（统计量）。此外，还有：
**k阶矩**
设X为随机变量，k为正整数。如果以下的数学期望都存在，则称$\mu_k=E(X^k)$为X的**k阶原点矩**。称$v_k=E(X-E(X))^k$为X的**k阶中心矩[^moment]**。

[^moment]: 矩就是均值。原点矩就是随机变量幂函数的均值，中心矩就是随机变量偏差幂函数的均值。为啥概率论总是跟均值打交道？因为均值是消除不确定性的主要手段。

**变异系数**
设随机变量X的二阶矩存在，则称比值$C_v(X)={\sqrt{Var(X)}\over E(X)}={\sigma(X)\over E(X)}$为X的变异系数。  
因为标准差的量纲与数学期望的量纲是一致的，所以变异系数是一个无量纲的量，从而能更好地比较两个随机变量的波动大小。

**分位数**
设连续随机变量X的分布函数为F(X)，密度函数为p(x)。对任意$p\in (0,1)$，称满足条件$F(x_p)=\int_{-\infty}^{x_p}p(x)dx=p$的$x_p$为此分布的**p分位数**，又称**下侧p分位数**，称满足条件$1-F(x_p^')=\int_{x_{^'}^\infty}p(x)dx=p$的$x_p^'$为此分布的**上侧p分位数**。

**中位数**
设连续随机变量X的分布函数为F(x)，密度函数为p(x)。称p=0.5时的p分位数$x_{0.5}$为此分布的**中位数**，即$x_{0.5}$满足$F(x_{0.5})=\int_{\infty}^{x_{0.5}}p(x)dx = 0.5$

**偏度系数[^skewness]**
设随机变量X的前三阶矩存在，则比值$\beta_s={v_3\over v_2^{3/2}}={E(X-E(X))^3\over [Var(X)]^{3/2}}$称为X（或分布）的**偏度系数**，简称偏度。当$\beta_s\gt 0$时，称该分布为**正偏**，又称**右偏**；当$\beta_s\lt 0$时，称该分布为**负偏**，又称**左偏**。

[^skewness]: 偏度$\beta_s$是描述分布偏离对称性（或歪斜）程度的一个特征数。

**峰度系数[^kurtosis]**
设随机变量X的前四阶矩存在，则$\beta_k={v_4\over v_2^2}-3={E(X-E(X))^4\over [Var(X)]^2}-3$，称为X（或分布）的**峰度系数**，简称**峰度**。

[^kurtosis]: 峰度是描述分布尖峭程度和（或）尾部粗细的一个特征数。减3是为了让正态分布峰度为0。峰度$\beta_k$是相对于正态分布而言的超出量，即峰度$\beta_k$是X的标准化变量与标准正态变量的四阶原点矩之差，并以标准正态分布为基准确定其大小。偏度和峰度都是描述分布形状的特征数，它们的设置都是**以正态分布为基准**，正态分布的偏度和峰度皆为0。

# 多维随机变量及其分布

## 多维随机变量及其联合分布

**定义**
如果$X_1(\omega),X_2(\omega),...,X_n(\omega)$是定义在同一个样本空间$\Omega=\{\omega\}$上的n个随机变量，则称$\mathbf{X}(\omega)=(X_1(\omega),X_2(\omega),...,x_n(\omega))$，为**n维（或n元）随机变量**或**随机变量**。

**定义**
对任意的n个实数$x_1,x_2,...,x_n$，n个事件$\{X_1\leq x_1\},\{X_2\leq x_2\},...,\{X_n\leq x_n\}$同时发生的概率$$
F(x_1,x_2,...,x_n)=P(X_1\leq x_1,X_2\leq x_2,...,X_n\leq x_n)
$$称为n维随机变量$(X_1,X_2,...,X_n)$的**联合分布函数**。

**定理**
任一二维联合分布函数$F(x,y)$必具有如下四条基本性质：

1. 单调性 $F(x,y)$分别对x或y是单调非减的，即当$x_1\lt x_2$时，有$F(x_1,y)\leq F(x_2, y)$，当$y_1 \lt y_2$时，有$F(x,y_1)\leq F(x,y_2)$.
2. 有界性 对任意的x和y，有$0\leq F(x,y)\leq 1$，且$$F(-\infty, y)=\lim\limits_{x\rightarrow -\infty} F(x,y)=0,\\F(x,-\infty)=\lim\limits_{y\rightarrow -\infty} F(x,y)=0,\\F(\infty,\infty)=\lim\limits_{x,y\rightarrow \infty}F(x,y) = 1$$
3. 右连续性 对每个变量都是右连续的，即$$F(x+0,y)=F(x,y),\\F(x,y+0)=F(x,y)$$
4. 非负性 对任意的$a\lt b, c\lt d$有$$P(a\lt X\leq b, c\lt Y\leq d)=F(b,d)-F(a,d)-F(b,c)+F(a,c)\geq 0$$

**定义**
如果二维随机变量(X,Y)只取有限个或可列个数对$(x_i,y_j)$，则称(X,Y)为**二维离散随机变量**，称$p_{ij}=P(X=x_i,Y=y_i), i,j=1,2,...$为(X,Y)的**联合分布列**

**联合分布列的基本性质**

1. 非负性 $p_{ij}\geq 0$
2. 正则性 $\sum\limits_{i=1}^\infty \sum\limits_{j=1}^\infty p_{ij} = 1$

**定义**
如果存在二元非负函数p(x,y)，使得二维随机变量(X,Y)的分布函数F(x,y)可表示为$F(x,y)=\int_{-\infty}^x\int_{-\infty}^y p(u,v)dvdu$，则称(X,Y)为**二维连续随机变量**，称$p(u,v)$为(X,Y)的**联合密度函数**。  
在F(x,y)偏导数存在的点上有$p(x,y)={\partial^2\over \partial x \partial y}F(x,y)$

**联合密度函数的基本性质**

1. 非负性 $p(x,y)\geq 0$
2. 正则性 $\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}p(x,y)dydx = 1$

**多项分布**
进行n次独立重复试验，如果每次试验有r个互不相容的结果：$A_1,A_2,...,A_r$之一发生，且每次试验中$A_i$发生的概率为$p_i=P(A_i), i = 1,2,...,r$,且$p_1+p_i+...+p_r = 1$，记$X_i$为n次独立重复试验中$A_i$出现的次数，i=1,2,...,r，则$(X_1,X_2,...,X_r)$取值$(n_1,n_2,...,n_r)$的概率，即$A_1$出现$n_1$次，$A_2$出现$n_2$次...$A_r$出现$n_r$次的概率为$P(X_1=n_1,X_2=n_2,...,X_r=n_r)={n!\over {n_1!n_2!...n_r!}p_1^{n_1}p_2^{n_2}...p_r^{n_r}}$，其中$n=n_1+n_2+...+n_r$。
这个联合分布列称为**r项分布**，又称**多项分布**，记为$M(n,p_1,p_2,...p_r)$
> 二项分布是一维随机变量的分布，而在r项分布中，因为$p_1+p_2+...+p_r=1$,且$n_1+n_2+...+n_r=n$，所以r项分布是r-1维随机变量的分布[^dimension]。

[^dimension]: 维度跟自由度相关。

**多维超几何分布**
以下给出多维超几何分布的描述：袋中有N个球，其中有$N_i$个i号球，i=1,2,...,r，且$N=N_1+N_2+...+N_r$。从中任意取出$n(\leq N)$个，若记$X_i$为取出的n个球中i号球的个数，i=1,2,...,r，则$$P(X_1=n_1,X_2=n_2,...,X_r=n_r)={C_{N_1}^{n_1}C_{N_2}^{n_2}...C_{N_r}^{n_r}\over C_N^n}$，其中$n_1+n_2+...+n_r = n, n_i\leq N_i, i= 1,2,...,r$$

**多维均匀分布**
设D为$\mathbf{R^n}$中的一个有界区域，其度量（平面的为面积，空间的为体积等）为$S_D$,如果多维随机变量$(X_1,X_2,...,X_n)$的联合密度函数为$$
p(x_1,x_2,...,x_n)=\left \{ \begin{array}{l}
    {1\over S_D}, (x_1,x_2,...,x_n) \in D,\\
    0, 其他
\end{array}\right.
$$
则称$(X_1,X_2,...,X_n)$服从D上的**多维均匀分布**，记为$(X_1,X_2,...,X_n)\sim U(D)$
> 二维均匀分布所描述的随机现象就是向平面区域D中随机投点，如果该点坐标(X,Y)落在D的子区域G中的概率只与G的面积有关，而与G的位置无关，则由第一章知这是几何概率。现在由二维均匀分布来描述，则$$
P((X,Y)\in G)=\iint\limits_G p(x,y)dxdx = \iint\limits_G {1\over S_D}dxdx = {G的面积\over D的面积}
$$这正是几何概率的计算公式。

**二元正态分布**
如果二维随机变量(X,Y)的联合密度函数为$$
p(x,y)={1\over 2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}exp\{-{1\over 2(1-\rho^2)}[{(x-\mu_1)^2\over \sigma_1^2}-2\rho{(x-\mu_1)(y-\mu_2)\over \sigma_1\sigma_2}+{(y-\mu_2)^2\over \sigma_2^2}]\}, -\infty \lt x, y \lt \infty
$$则称(X,Y)服从**二元正态分布**，记为$(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$。其中五个参数的取值范围分别是$-\infty \lt \mu_1,\mu_2 \lt \infty, \sigma_1,\sigma_2 \gt 0, -1 \leq \rho \leq 1$.

## 边际分布与随机变量的独立性

二维联合分布函数含有丰富的信息，主要有：

1. 每个分量的分布，即边际分布
2. 两个分量之间的关联程度，用协方差和相关系数来描述
3. 给定一个分量时，另一个分量的分布，即条件分布

**边际分布函数**
如果二维随机变量(X,Y)的联合分布函数$F(x,y)$中令$y\rightarrow \infty$，由于$\{Y\lt \infty\}$为必然事件，故可得$$
\lim\limits_{y\rightarrow \infty} F(x,y)=P(X\leq x, Y\lt \infty) = P(X\leq x),
$$
这是由(X,Y)的联合分布函数F(x,y)求得的X的分布函数，被称为X的**边际分布**，记为$F_X(x)=F(x,\infty)$。类似地，在F(x,y)中，令$x\rightarrow \infty$，可得Y的**边际分布**$F_Y(y)=F(\infty,y)$.

**边际分布列**
在二维离散随机变量(X,Y)的联合分布列$\{P(X=x,Y=y)\}$中，对j求和所得的分布列$$\sum\limits_{j=1}^\infty P(X=x_i,Y=y_j)=P(X=x_i), i=1,2,...
$$被称为X的**边际分布列**。类似地，对i求和所得的分布列$$
\sum\limits_{i=1}^\infty P(X=x_i,Y=y_j)=P(Y=y_j), j=1,2,...
$$被称为Y的**边际分布列**。

**边际密度函数**
如果二维连续随机变量(X,Y)的联合密度函数为p(x,y)，因为$$
F_X(x)=F(x,\infty)=\int_{-\infty}^x(\int_{-\infty}^\infty p(u,v)dv)du = \int_{-\infty}^xp_X(u)du,\\
F_Y(x)=F(\infty,y)=\int_{-\infty}^y(\int_{-\infty}^\infty p(u,v)du)dv = \int_{-\infty}^yp_Y(v)dv,
$$其中$p_X(x)$和$p_Y(y)$分别为$$
p_X(x)=\int_{-\infty}^\infty p(x,y)dy,\\
p_Y(y)=\int_{-\infty}^\infty p(x,y)dx.
$$
它们恰好处于密度函数位置，故称上式给出的$p_X(x)$为X的**边际密度函数**，$p_Y(y)$为Y的**边际密度函数**。

当两个随机变量的取值互不影响时，就称它们是相互独立的。
**定义**
设n维随机变量$(X_1,X_2,...,X_n)$的联合分布函数为$F(x_1,x_2,...,x_n)$，$F_i(x_i)$为$X_i$的边际分布函数。如果对任意n个实数$x_1,x_2,...,x_n$，有$$
F(x_1,x_2,...,x_n) = \prod\limits_{i=1}^n F_i(x_i)
$$则称$X_1,X_2,...,X_n$**相互独立**。
在离散随机变量场合，如果对其任意n个取值$x_1,x_2,...,x_n$，有$$
P(X_1=x_1,X_2=x_2,...,X_n=x_n)=\prod\limits_{i=1}^n P(X_i=x_i)$$则称$X_1,X_2,...,X_n$相互独立。

## 多维随机变量函数的分布

设$(X_1,X_2,...,X_n)$为n维随机变量，则$(X_1,X_2,...,X_n)$的函数$Y=g(X_1,X_2,...,X_n)$是一维随机变量。现在的问题是：如何由$(X_1,X_2,...,X_n)$的联合分布，求出Y的分布。

**多维离散随机变量函数的分布**
设$(X_1,X_2,...,X_n)$为n维离散随机变量，则某一函数$Y=g(X_1,X_2,...,X_n)$是一维离散随机变量。当$(X_1,X_2,...,X_n)$所有可能取值较少时，可将Y的值一一列出，然后再合并整理就可得出结果。

**连续场合的卷积公式**
设X与Y是两个相互独立的连续随机变量，其密度函数分别为$p_X(x)$和$p_Y(y)$，则其和$Z=X+Y$的密度函数为$$
p_Z(z)=\int_{-\infty}^\infty p_X(z-y)p_Y(y)dy = \int_{-\infty}^\infty p_X(x)p_Y(z-x)dx
$$
> 卷积公式也可用于X与Y不独立的情况，此时只要将边际分布密度（列）的乘积改写成联合分布密度（列）即可。

$\chi^2(n)$分布中的参数n就体现在：n是独立的标准正态变量的个数，因此人们称这个参数n为自由度。

**变量变换法**
设二维随机变量(X,Y)的联合密度函数为p(x,y)，如果函数$$
\left \{ \begin{array}{l}
    u=g_1(x,y)\\
    v=g_2(x,y)
\end{array}\right.
$$
有连续偏导数，且存在唯一的反函数$$
\left \{ \begin{array}{l}
    x=x(u,v)\\
    y=y(u,v)
\end{array}\right.
$$
其变换的雅克比行列式$$
J={\partial (x,y)\over \partial (u,v)}=\left | \begin{matrix}
    {\partial x\over \partial u} & {\partial x\over \partial v}\\
    {\partial y\over \partial u} & {\partial y\over \partial v}
\end{matrix} \right |
=({\partial (u,v)\over \partial (x,y)})^{-1}
=\left ( \left | \begin{matrix}
    {\partial u\over \partial x} & {\partial u\over \partial y}\\
    {\partial v\over \partial x} & {\partial v\over \partial y}
\end{matrix} \right | \right )^{-1} \ne 0
$$
若$$
\left \{ \begin{array}{l}
    U=g_1(X, Y)\\
    V=g_2(X, Y)
\end{array}\right.
$$
则(U,V)的联合密度函数为$p(u,v)=p(x(u,v),y(u,v))|\mathbf{J}|$
> 这个方法实际上就是二重积分的变量变换法。
> 多元正态变量经线性变换后仍是多元正态变量，这个结论在统计中经常用到。

**增补变量法**

增补变量法实质上是变量变换法的一种应用：为了求出二维连续随机变量(X,Y)的函数$U=g(X,Y)$的密度函数，增补一个新的随机变量$V=h(X,Y)$，一般令V=X或V=Y。先用变量变换法求出(U,V)的联合密度函数p(u,v)，再对p(u,v)关于v积分，从而得出关于U的边际密度函数。

## 多维随机变量的特征数

除了各个分量的期望、方差、标准差之外，还有两个随机变量间的关联程度，即协方差与相关系数，这是一种反映两个随机变量**相依关系**的特征数，要特别注意。

**定理**：多维随机变量函数的数学期望
若二维随机变量$(X,Y)$的分布用联合分布列$P(X=x_i,Y=y_i)$或用联合密度函数$p(x,y)$表示，则$Z=g(X,Y)的数学期望为$$
E(Z)=\left \{ \begin{array}{l}\sum\limits_i\sum\limits_j g(x_i,y_j)P(X=x_i,Y=y_j)，在离散场合，\\
\int_{-\infty}^\infty\int_{-\infty}^\infty g(x,y)p(x,y)dxdy，在连续场合 \end{array} \right.
$$
> 这里所涉及的数学期望假设都存在。

**数学期望与方差的运算性质**

1. 设(X,Y)是二维随机变量，则有$$
E(X+Y)=E(X)+E(Y)
$$
2. 若随机变量X与Y相互独立，则有$$
E(XY)=E(X)E(Y)
$$
3. 若随机变量X与Y相互独立[^666]，则有$$
Var(X\plusmn Y)=Var(X)+Var(Y)
$$

[^666]: 一个随机变量的变化不影响另一个随机变量的变化，这个好理解。

**协方差**
设(X,Y)是一个二维随机变量，若$E[(X-E(X))(Y-E(Y))]$存在，则称此数学期望为X与Y的**协方差[^covariance]**，或称为X与Y的**相关（中心）矩**，并记为$$
Cov(X,Y) = E[(X-E(X))(Y-E(Y))]
$$特别有$\mathbf{Cov(X,X)=Var(X)}$。

[^covariance]: 协方差也是期望，偏差之积的期望。

协方差性质：

1. $Cov(X,Y)=E(XY)-E(X)E(Y)$
2. 若随机变量X与Y相互独立，则$Cov(X,Y) = 0$，反之不然[^indecorr]。

[^indecorr]: 独立必导致不相关，但不相关不一定导致独立。这里的相关仅指是否存在线性关系。

3. 对任意二维随机变量$(X,Y)$，有$Var(X\plusmn Y) = Var(X)+Var(Y)\plusmn 2Cov(X,Y)$
4. 协方差$Cov(X,Y)$的计算与X，Y的次序无关，即$Cov(X,Y)=Cov(Y,X)$
5. 任意随机变量X与常数a的协方差为零，即$Cov(X,a)=0$
6. 对任意常数a,b，有$Cov(aX,bX)=abCov(X,Y)$
7. 设X，Y，Z是任意三个随机变量，则$Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$

> 上述第6、7条规则表明，协方差运算满足线性规则。

**相关系数**
协方差Cov(X,Y)是有量纲的量，为了消除量纲的影响，现对协方差除以相同量纲的量，就得到一个新的概念——相关系数。

**定义**
设$(X,Y)$是一个二维随机变量，且$Var(X)=\sigma_X^2\gt 0, Var(Y)=\sigma_Y^2\gt 0$。则称$$
Corr(X,Y) = {Cov(X,Y)\over \sqrt{Var(X)} \sqrt{Var(Y)}}={Cov(X,Y)\over \sigma_X \sigma_Y}
$$
为X与Y的（线性）**相关系数[^correlation]**。

[^correlation]: 相关系数的一个解释是：它是相应标准化变量的协方差。若记X与Y的数学期望分别为$\mu_X$与$\mu_Y$，其标准化变量为$X^*={X-\mu_X\over \sigma_X}, Y^*={Y-\mu_Y\over \sigma_Y}$，则有$Cov(X^*,Y^*)=Cov({X-\mu_X\over \sigma_X}, {Y-\mu_Y\over \sigma_Y})= {Cov(X,Y)\over \sigma_X \sigma_Y}=Corr(X,Y)$

**引理**： 施瓦茨（Schwarz）不等式
对任意二维随机变量$(X,Y)$，若X与Y的方差都存在，且记$\sigma_X^2=Var(X), \sigma_Y^2 = Var(Y)$，则有$$
[Cov(X,Y)]^2\leq \sigma_X^2 \sigma_Y^2
$$

利用施瓦茨不等式即可得到相关系数的重要性质：

1. $-1\leq Corr(X,Y) \leq 1$，或$|Corr(X,Y)|\leq 1$
2. $Corr(X,Y) = \plusmn 1$的充要条件是X与Y间几乎处处有线性关系[^942]，即存在$a(\ne 0)$与$b$，使得$$
P(Y=aX+b)=1$$

[^942]: 其中当$Corr(X,Y)=1$时，有$a\gt 0$；当$Corr(X,Y)=-1$时，有$a\lt 0$。相关系数$Corr(X,Y)$刻画了X与Y之间的线性关系强弱，因此也常称其为“线性相关系数”。若$Corr(X,Y)=0$，则称X与Y**不相关**。不相关是指X与Y之间没有线性关系，但X与Y之间可能有其他的函数关系，譬如平方关系、对数关系等。

3. 在二维正态分布$N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$场合，不相关和独立是等价的。

**随机向量的数学期望与协方差矩阵**
**定义**
记n维随机向量为$\mathbf{X}=(X_1,X_2,...,X_n)'$，若其每个分量的数学期望都存在，则称$$
E(X)=(E(X_1),E(X_2),...,E(X_n))'
$$为n维随机向量**X**的**数学期望向量**，简称为**X**的 **数学期望**，而称$$
E[(X-E(X))(X-E(X))'] = \left ( \begin{matrix}
    Var(X)&Cov(X_1,X_2)&...&Cov(X_1,X_n)\\
    Cov(X_2,X_1)&Var(X_2)&...&Cov(X_2,X_n)\\
    \vdots & \vdots &&\vdots \\
    Cov(X_n,X_1)&Cov(X_n,X_2)&...&Var(X_n)
\end{matrix} \right )
$$为该随机向量的**方差-协方差矩阵**，简称**协方差阵**，记为Cov(X)。
> n维随机向量的数学期望是各分量的数学期望组成的向量。而其方差就是由各分量的方差与协方差组成的矩阵，其对角线上的元素就是方差，非对角线元素为协方差。

**定理**
n维随机向量的协方差矩阵$Cov(X)=(Cov(X_i,X_j))_{n\times n}$是一个对称的非负定矩阵。

**n元正态分布**
设n维随机变量$\mathbf{X}=(X_1,X_2,...,X_n)'$的协方差矩阵$\mathbf{B}=Cov(\mathbf{X})$是正定的，数学期望向量为$\mathbf{a}=(a_1,a_2,...,a_n)'$。又记$\mathbf{x}=(x_1,x_2,...,x_n)'$，则由密度函数$$
p(x_1,x_2,...,x_n)=p(X)={1\over (2\pi)^{n\over 2}|\mathbf{B}|^{1\over 2}}exp\{-{1\over 2}(\mathbf{x-a})'\mathbf{B}^{-1}(\mathbf{x-a})\}
$$
定义的分布称为n元正态分布[^nN]，记为$\mathbf{X}\sim N(\mathbf{a,B})$。其中$|\mathbf{B}|$表示**B**的行列式，$\mathbf{B}^{-1}$表示**B**的逆阵，$(\mathbf{x-a})'$表示向量$(\mathbf{x-a})$的转置。

[^nN]: n元正态分布是一种最重要的多维分布，在概率论、数理统计和随机过程中都占有重要地位。

## 条件分布与条件期望

对二维随机变量$(X,Y)$而言，所谓随机变量X的条件分布，就是在给定Y取某个值的条件下X的分布。

**离散随机变量的条件分布**
对一切使$P(Y=y_i)=p_{·j}=\sum\limits_{i=1}^\infty p_{ij}\gt 0$的$y_i$，称$$
p_{i|j}=P(X=x_i|Y=y_i)={P(X=x_i,Y=y_i)\over P(Y=y_i)}={P_{ij}\over p_{·j}}, i=1,2,...
$$为给定$Y=y_j$条件下X的**条件分布列**。

给定$Y=y_j$条件下X的**条件分布函数**为$$
F(x|y_i)=\sum\limits_{x_i\leq x}P(X=x_i|Y=y_i)=\sum\limits p_{i|j}
$$

**连续随机变量的条件分布**
因为连续随机变量取某个值的概率为零，即$P(Y=y)=0$，所以无法用条件概率直接计算$P(X\leq x|Y=y)$。

对一切使$p_Y(y)\gt 0$的y，给定$Y=y$条件下X的条件分布函数和条件密度函数分别为$$
F(x|y)=\int_{-\infty}^x {p(u,y)\over p_Y(y)}du,\\
p(x|y)={p(x,y)\over p_Y(y)}.
$$

**连续场合的全概率公式和贝叶斯公式**
由条件分布密度函数，有$$
p(x,y)=p_X(x)p(y|x),\\
p(x,y)=p_Y(y)p(x|y).
$$对$p(x,y)$求边际密度函数，就得全概率公式的密度函数形式：$$
p_Y(y)=\int_{-\infty}^\infty p_X(x)p(y|x)dx,\\
p_X(x)=\int_{-\infty}^\infty p_Y(y)p(x|y)dy.
$$将上面两组式子代入，得贝叶斯公式的密度函数形式：$$
p(x|y)={P_X(x)p(y|x)\over \int_{-\infty}^\infty p_X(x)p(y|x)dx}
$$或$$
p(y|x)={P_Y(y)p(x|y)\over \int_{-\infty}^\infty p_Y(y)p(x|y)dy}
$$
> 虽然由边际分布无法得到联合分布，但**由边际分布和条件分布就可以得到联合分布**。

**条件数学期望**
条件分布的数学期望（若存在）称为**条件期望**，其定义如下：$$
E(X|Y=y)=\left \{ \begin{array}{l}
    \sum\limits_i x_iP(X=x_i| Y=y), (X,Y)为二维离散随机变量\\
    \int_{-\infty}^\infty xp(x|y)dx, (X,Y)为二维连续随机变量
\end{array} \right.$$
$$E(Y|X=x)=\left \{ \begin{array}{l}
    \sum\limits_i y_iP(Y=y_i| X=x), (X,Y)为二维离散随机变量\\
    \int_{-\infty}^\infty yp(y|x)dy, (X,Y)为二维连续随机变量
\end{array} \right.
$$
> 条件期望$E(X|Y=y)$是**y的函数**，对于y的不同取值，条件期望$E(X|Y=y)$的取值也在变化。可以将$E(X|Y=y)$看成$Y=y$时$E(X|Y)$的一个取值。

**定理**：重期望公式
设$(X,Y)$是二维随机变量，且$E(X)$存在，则$$
E(X)=E(E(X|Y))
$$
> 重期望公式是概率论中一个较为深刻的结论，在实际中很有用。

# 大数定律与中心极限定理

## 随机变量序列的两种收敛性

**随机变量序列的收敛性**有多种，其中常用的是：依概率收敛和按分布收敛。大数定律涉及依概率收敛，中心极限定理涉及按分布收敛。这些极限定理不仅是概率论研究的**中心议题**，而且在数理统计中有广泛的应用。
> 重要：随机变量“收敛”是消除不确定的主要工具之二。

**定义**
设$\{X_n\}$为一随机变量序列，X为一随机变量，如果对任意的$\epsilon \gt 0$，有$$
P(|X_n-X|\geq \epsilon)\rightarrow 0 (n\rightarrow \infty),
$$则称序列$\{X_n\}$**依概率收敛于X[^pro]**，记作$X_n\stackrel {P} {\rightarrow} X$。

[^pro]: 依概率收敛的含义是：$X_n$对X的绝对偏差不小于任一给定量的可能性将随着n增大而愈来愈小。或者说，绝对偏差$|X_n-X|$小于任一给定量的可能性将随着n增大而愈来愈接近于1。

**定理**
设$\{X_n\}$，$\{Y_n\}$是两个随机变量序列，a,b是两个常数。如果$$
X_n\stackrel{P}{\rarr}a, Y_n\stackrel{P}{\rarr}b,
$$则有：

1. $X_n\plusmn Y_n \stackrel{P}{\rarr}a\plusmn b$；
2. $X_n\times Y_n \stackrel{P}{\rarr}a\times b$;
3. $X_n\div Y_n \stackrel{P}{\rarr}a\div b(n\ne 0)$.

**定义**
设随机变量$X,X_1,X_2,...$的分布函数分别为$F(x),F_1(x),F_2(x),...$。若对$F(x)$的任一连续点x，都有$$
\lim\limits_{n\rightarrow \infty} F_n(x)=F(x)
$$则称$\{F_n(x)\}$**弱收敛于F(x)**，记作$$
F_n(x) \stackrel{W}{\rarr}F(x)
$$也称相应的随机变量序列$\{X_n\}$**按分布收敛于X**，记作$$
X_n\stackrel{L}{\rarr}X
$$

**定理**
$X_n \stackrel{P}{\rarr}X \Rightarrow X_n \stackrel{L}{\rarr}X$
> 因为随机变量取值的概率取决于其分布，所以随机变量依概率收敛可以推出其依分布收敛。

**定理**
若c为常数，则$X_n \stackrel{P}{\rarr}c$的充要条件是：$X_n\stackrel{L}{\rarr}c$

## 特征函数

设p(x)是随机变量X的密度函数，则p(x)的傅里叶变换是$$
\phi(t) = \int_{-\infty}^\infty e^{itx}p(x)dx,
$$
其中$i=\sqrt{-1}$是虚数单位。由数学期望的概念知，$\phi(t)$恰好是$E(e^{itx})$。这就是**特征函数**，它是处理许多概率论问题的有力工具。它能把寻求独立随机变量和的分布的卷积运算转换成乘法运算，还能把求分布的各阶原点矩转换成微分运算，特别地，它能把寻求随机变量序列的极限分布转换成一般的函数极限问题。

**定义**
设X是一个随机变量，称$$
\phi(t)=E(e^{itX}), -\infty \lt t \lt \infty,
$$为X的**特征函数**。特征函数只依赖于随机变量的分布，分布相同则特征函数也相同，所以我们也常称其为某**分布的特征函数**。

**常用分布的特征函数**

1. 单点分布 $P(X=a)=1$，其特征函数为$$
\phi(t) = e^{ita}
$$
2. 0-1分布 $P(X=x)=p^x(1-p)^{1-x}, x=0,1$，其特征函数为$$
\phi(t) = pe^{it}+q, 其中 q=1-p
$$
3. 泊松分布$P(\lambda)$ $P(X=k)={\lambda^k\over k!}e^{-\lambda}, k =0,1,...$，其特征函数为$$
\phi(t) = \sum\limits_{k=0}^\infty e^{ikt}{\lambda^k\over k!}e^{-\lambda} = e^{-\lambda}e^{\lambda e^{it}}=e^{\lambda (e^{it}-1)}
$$
4. 均匀分布$U(a,b)$ 因为密度函数为$$
p(x)= \left { \begin{array}{l}
{1\over b-a}, a\lt x \lt b,\\
0, 其他
\end{array} \right.
$$
所以其特征函数为$$
\phi(t) = \int_a^b {e^{itx}\over b-a}dx = {e^{ibt}-e^{iat}\over it(b-a)}
$$
5. 标准正态分布$N(0,1)$ 因为密度函数为$$
p(x) = {1\over \sqrt{2\pi}}e^{-{x^2\over 2}}, -\infty \lt x \lt \infty,
$$所以其特征函数为$$
\phi(t) = {1\over \sqrt{2\pi}}\int_{-\infty}^\infty e^{itx}e^{-{x^2\over 2}}dx = {1\over \sqrt{2\pi}}\int_{-\infty}^{\infty} \sum\limits_{n=0}^\infty {(itx)^n\over n!}e^{-{x^2\over 2}}dx = \sum\limits_{n=0}^\infty {(it)^n\over n!}[{1\over \sqrt{2\pi}}\int_{-\infty}^\infty x^ne^{-{x^2\over 2}}dx]
$$上式中方括号内正是标准正态分布的n阶矩$E(X^n)$。当n为奇数时$E(X^n)=0$；当n为偶数时，如$n=2m$时，$$
E(X^n)=E(X^{2m})=(2m-1)!!={(2m)!\over 2^m·m!}
$$代回原式，可得标准正态分布的特征函数$$
\phi(t) = \sum\limits_{m=0}^\infty {(it)^{2m}\over (2m)!}·{(2m)!\over 2^m·m!}= \sum\limits_{m=0}^\infty (-{t^2\over 2})^m){1\over m!}=e^{-{t^2\over 2}}
$$
6. 指数分布$Exp(\lambda)$ 因为密度函数为$$
p(x)= \left \{ \begin{array}{l}
\lambda e^{-\lambda x}, x\geq 0,\\
0, x\lt 0,
\end{array} \right.
$$所以其特征函数为$$
\phi(t) = \int_0^\infty e^{itx}\lambda e^{-\lambda x}dx = \lambda [\int_o^\infty \cos (tx)e^{-\lambda x}dx + i\int_0^\infty \sin (tx)e^{-\lambda x}dx]=\lambda ({\lambda\over \lambda^2 + t^2}+i{t\over \lambda^2 + t^2})=(1-{it\over \lambda})^{-1}
$$
7. 二项分布b(n,p) 设随机变量$Y\sim b(n,p)$，则$Y=X_1+X_2+...+X_n$，其中诸$X_i$是相互独立同分布的随机变量，且$X_i\sim b(1,p)$。因为$\phi_{x_i}(t)=pe^{it}+q$。所以由独立随机变量和的特征函数为特征函数的积，得$$
\phi_Y(t)=(pe^{it}+q)^n
$$
8. 正态分布$N(\mu, \sigma^2)$ 设随机变量$Y\sim N(\mu, \sigma^2)$，则$X=(Y-\mu)/ \sigma \sim N(0,1)$。因为$\phi_X(t) = e^{-{t^2\over 2}}$
所以由$Y=\sigma X+\mu$得$$
\phi_Y(t)=\phi_{\sigma X+\mu}(t)=e^{i\mu t}\phi_X(\sigma t)=exp\{i\mu t -{\sigma^2t^2\over 2}\}
$$
9. 伽马分布$Ga(n, \lambda)$ 设随机变量$Y\sim Ga(n,\lambda)$，则$Y=X_1+X_2+...X_n$，其中$X_i$独立同分布，且$X_i\sim Exp(\lambda)$。可知$$
\phi_{X_i}(t)=(1-{it\over \lambda})^{-1}
$$所以由独立随机变量和的特征函数为特征函数的积，得$$
\phi_Y(t)=(\phi_{X_1})^n=(1-{it\over \lambda})^{-n}
$$进一步，当$\alpha$为任一实数时，我们可得$Ga(\alpha, \lambda)$分布的特征函数为$$
\phi(t) = (1-{it\over \lambda})^{-\alpha}
$$
10. $\chi^2(n)$分布 因为$\chi^2(n)-Ga(n/2, 1/2)$，所以$\chi^2(n)$分布的特征函数为$$
\phi(t)=(1-2it)^{-n/2}
$$

**特征函数的性质**

1. $|\phi(t)|\leq \phi(0) =1$
2. $\phi(-t)=\phi(t)$，其中$\phi(-t)$表示$\phi(t)$的共轭
3. 若$Y=aX+b$，其中a,b是常数，则$$
\phi_Y(t)=e^{ibt}\phi_X(at)
$$
4. 独立随机变量和的特征函数为每个随机变量的特征函数的积，即设X与Y相互独立，则$$
\phi_{X+Y}(t) = \phi_X(t)\phi_Y(t)
$$
5. 若$E(X^l)$存在，则X的特征函数$\phi(t)$可$l$次求导，且对$1\leq k\leq l$，有$$
\phi^{(k)}(0)=i^kE(X^k)
$$

> 上式提供了一条求随机变量的各阶矩的途径，特别可用下式去求数学期望和方差$$
E(X)= {\phi'(0)\over i}, Var(X)=-\phi''(0)+(\phi'(0))^2
$$

**定理**：一致连续性
随机变量X的特征函数$\phi(t)$在$(-\infty, \infty)$上一致连续。

**定理**：非负定性
随机变量X的特征函数$\phi(t)$是非负定的，即对任意正整数n及n个实数$t_1,t_2,...,t_n$和n个复数$z_1,z_2,...,z_n$，有$$
\sum\limits_{k=1}^n\sum\limits_{j=1}^n \phi(t_k-t_1)z_k\bar{z_j}\geq 0
$$

**特征函数唯一决定分布函数**
由特征函数的定义可知，随机变量的分布唯一地决定了它的特征函数。要注意的是：如果两个分布的数学期望、方差及各阶矩都相等，也无法证明此两个分布相等。但**特征函数完全决定了分布**。

**定理**：逆转公式
设$F(x)$和$\phi(t)$分别为随机变量X的分布函数和特征函数，则对$F(x)$的任意两个连续点$x_1\lt x_2$，有$$
F(x_2)-F(x_1) = \lim\limits_{T\rightarrow \infty} {1\over 2\pi} \int_{-T}^T {e^{-itx_1}-e^{-itx_2}\over it}\phi(t)dt
$$

**定理**：唯一性定理
随机变量的分布函数由其特征函数唯一决定。

**定理**
若X为连续随机变量，其密度函数为p(x)，特征函数为$\phi(t)$。如果$\int_{-\infty}^\infty |\phi(t)|dt \lt \infty$，则$$
p(x)= {1\over 2\pi} \int_{-\infty}^\infty e^{-itx}\phi(t)dt
$$该式也称**傅里叶逆变换**，所以**特征函数是密度函数的傅里叶变换**，而**密度函数是特征函数的傅里叶逆变换**：$$
\phi(t)=\int_{-\infty}^\infty e^{itx}p(x)dx,\\
p(x)={1\over 2\pi}\int_{-\infty}^\infty e^{-itx}\phi(t)dt
$$

> 在概率论中，**独立随机变量和的问题占有“中心”地位**，用卷积公式去处理独立随机变量和的问题相当复杂，而引入了特征函数可以很方便地用特征函数来识别独立随机变量和的分布。由此大大简化了处理独立随机变量和的难度。

**定理**
分布函数序列$\{F_n(x)\}$弱收敛于分布函数$F(x)$的充要条件是$\{F_n(x)\}$的特征函数序列$\{\phi_n(t)\}$收敛于$F(x)$的特征函数$\phi(t)$。

## 大数定律

大数定律有多种形式。
**伯努利大数定律**
设$S_n$为n重伯努利试验中事件A发生的次数，p为每次试验中A出现的概率，则对任意的$\epsilon \gt 0$，有$$
\lim\limits_{n\rightarrow \infty}P(|{S_n\over n}-p|\lt \epsilon)=1
$$
> 伯努利大数定律说明：随着n的增大，事件A发生的频率$S_n\over n$与其概率p的偏差$|{S_n\over n}-p|$大于预先给定的精度$\epsilon$的可能性愈来愈小，要多小有多小。这就是频率稳定于概率的含义。
> **伯努利大数定律提供了用频率来确定概率的理论依据**。

**大数定律的一般形式**
设有一随机变量序列$\{X_n\}$，假如它具有形如$\lim\limits_{n\rightarrow \infty}P(|{{1\over n} \sum\limits_{i=1}^n X_i - {1\over n}\sum\limits_{i=1}^n E(X_i)}|\lt \epsilon)=1$的性质，则称该随机变量序列$\{X_n\}$**服从大数定律**。

现在的问题是：随机变量序列$\{X_n\}$在什么条件下服从大数定律？以下给出一些大数定律，它们之间的差别表现在条件上：有的是**相互独立**的随机变量序列，有的是**相依**的随机变量序列，有的是**同分布**的随机变量序列，有的是**不同分布**的随机变量序列等。

**定理**：切比雪夫大数定律
设$\{X_n\}$为一列两两不相关的随机变量序列，若每个$X_i$的方差存在，且有共同的上界，即$Var(X_i)\leq c, i=1,2,...$，则$\{X_n\}$服从大数定律，即对任意的$\epsilon \gt 0$，$\lim\limits_{n\rightarrow \infty}P(|{{1\over n} \sum\limits_{i=1}^n X_i - {1\over n}\sum\limits_{i=1}^n E(X_i)}|\lt \epsilon)=1$成立。

**定理**：马尔科夫大数定律
对随机变量序列$\{X_n\}$，若${1\over n^2}Var(\sum\limits_{i=1}^n X_i)\rightarrow 0$成立,则$\{X_n\}$服从大数定律，即对任意的$\epsilon \gt 0$，$\lim\limits_{n\rightarrow \infty}P(|{{1\over n} \sum\limits_{i=1}^n X_i - {1\over n}\sum\limits_{i=1}^n E(X_i)}|\lt \epsilon)=1$成立。

以上几个大数定律均假设随机变量序列的方差存在，而辛钦大数定律去掉了这一假设，仅设每个随机变量的数学期望存在，同时要求$\{X_n\}$为独立同分布的随机变量序列。
**定理**：辛钦大数定律
设$\{X_n\}$为一独立同分布的随机变量序列，若$X_i$的数学期望存在，则$\{X_i\}$服从大数定律，即对任意的$\epsilon \gt 0$，$\lim\limits_{n\rightarrow \infty}P(|{{1\over n} \sum\limits_{i=1}^n X_i - {1\over n}\sum\limits_{i=1}^n E(X_i)}|\lt \epsilon)=1$成立[^xq]。

[^xq]: 辛钦大数定律提供了求随机变量数学期望$E(X)$的近似值的方法：设想对随机变量X独立重复地观察n次，第k次观察值为$X_k$，则$X_1,X_2,...,X_n$应该是相互独立的，且它们的分布应该与X的分布相同。所以，在$E(X)$存在的条件下，按照辛钦大数定律，当n足够大时，可以把平均值${1\over n}\sum\limits_{i=1}^n X_i$作为$E(X)$的近似值。这种做法的一个优点是，我们可以不必去管X的分布究竟是怎样的，我们的目的只是寻求数学期望的近似值。由辛钦大数定律很容易得出：如果$\{X_n\}$为独立同分布的随机变量序列，且$E(|X_i|^k)$存在，其中k为正整数，则$\{X_m^k\}$服从大数定律。这个结论在数理统计中是很有用的，也就是我们可以将${1\over n}\sum\limits_{i=1}^n X_i^k$作为$E(X_i^k)$的近似值。

## 中心极限定理

**大数定律讨论的是**，在什么条件下，**随机变量序列的算术平均依概率收敛到其均值的算数平均**。
**中心极限定理讨论的是**，在什么条件下，**独立随机变量和$Y_n=\sum\limits_{i=1}^n X_i$的分布函数会收敛于正态分布**。
中心极限定理就是研究随机变量和的极限分布，在什么条件下为正态分布的问题。

**林德伯格-莱维(Lindeberg-Levy)中心极限定理**：独立同分布下的中心极限定理
设$\{X_n\}$是独立同分布的随机变量序列，且$E(X_i)=\mu, Var(X_i)=\sigma^2 \gt 0$存在，若记$$
Y_n^*= {X_1+X_2+...+X_n-n\mu \over \sigma \sqrt{n}}
$$，
则对任意实数y，有$$
\lim\limits_{n\rightarrow \infty} P(Y_n^* \leq y)=\Phi(y) = {1\over \sqrt{2\pi}}\int_{-\infty}^\infty e^{-{t^2\over 2}}dt
$$
> 林德伯格-莱维中心极限定理只假设$\{X_n\}$独立同分布、方差存在，不管原来的分布是什么，只要n充分大，就可以用正态分布去逼近随机变量和的分布，所以这个定理有着广泛的应用。它同时揭示了这样的事实：测量误差近似地服从正态分布。

**棣莫弗-拉夫拉斯(de Moivre-Laplace)中心极限定理**：二项分布的正态近似
设n重伯努利试验中，事件A在每次试验中出现的概率为$p(0\lt p \lt 1)$，记$S_n$为n次试验中事件A出现的次数，且记$$
Y_n^*={S_n-np\over \sqrt{npq}}
$$则对任意实数y，有$$
\lim\limits_{n\rightarrow \infty} P(Y_n^*\leq y)=\Phi(y)={1\over \sqrt{2\pi}}\int_{-\infty}^y e^{-{t^2\over 2}}dt
$$

为使极限分布是正态分布，必须对$Y_n=\sum\limits_{i=1}^n X_i$的各项有一定的要求。譬如若允许从第二项起都等于0，则极限分布显然由$X_1$的分布完全确定，这时就很难得到什么有意思的结果。这就告诉我们，要使中心极限定理成立，在和的**各项中不应有起突出作用的项**，或者说，要求各项在概率意义下“均匀地小”。因此，只要对任意的$\tau \gt 0$，有$$
\lim\limits_{n\rightarrow \infty} {1\over \tau^2 B_n^2} \sum\limits_{i=1}^n \int_{|x-\mu_i|\gt \tau B_n} (x-\mu_i)^2 p_i(x)dx = 0
$$就可以保证$Y_n^*$中各项“均匀地小”。该条件被称为**林德伯格条件**。

**林德伯格中心极限定理**：独立不同分布下的中心极限定理
设独立随机变量序列$\{X_n\}$满足林德伯格条件，则对任意的x，有$$
\lim\limits_{n\rightarrow \infty} P({1\over B_n} \sum\limits_{i=1}^n (X_i-\mu_i)\leq x) = {1\over \sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}dt
$$

林德伯格条件虽然比较一般，但该条件较难验证，下面的李雅普诺夫条件则比较容易验证，因为它只对矩提出要求。
**李雅普诺夫(Lyapunov)中心极限定理**
设$\{X_n\}$为独立随机变量序列，若存在$\delta \gt 0$，满足$$
\lim\limits_{n\rarr \infty} {1\over B_n^{2+\delta}}\sum\limits_{i=1}^n E(|X_i-\mu_i|^{2+\delta})=0
$$则对任意的x，有$$
\lim\limits_{n\rarr \infty} P({1\over B_n} \sum\limits_{i=1}^n (X_i-\mu_i)\leq x) = {1\over \sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}dt
$$其中$\mu_i$与$B_n$如前所述。
