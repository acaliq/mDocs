 概率论与数理统计教程（第三版）
> 茆诗松、程依明、濮晓龙编著
> 为什么要费这么大周章做摘记？为了看到big picture。

摘记这本书为了：厘清概念、理解定理的证明

# 统计量及其分布

在概率论中，**概率分布通常被假定为已知的**，一切计算及推理均基于这个已知的分布进行。  
统计学是一门研究如何有效地收集和分析**受到随机因素影响的数据**的学科。

## 总体和样本

在一个统计问题中，研究对象的全体称为**总体**，构成总体的每个成员称为**个体**。  
**总体就是一个分布**，其数量指标就是服从这个分布的随机变量。**从“总体中抽样”和“从某个分布中抽样”是同一个意思**。  
为了了解总体的分布，从总体中随机地抽取n个个体，记其指标值为$x_1,x_2,...,x_n$，则$x_1,x_2,...,x_n$称为总体的一个**样本**，n称为**样本容量**，或简称**样本量**，样本中的个体称为**样本**。  
样本既是随机变量，又是一组数值。  
没有具体数值，只有一个范围的样本，称为**分组样本**，它是一种**不完全样本**。
**简单随机抽样**要求：

1. 样本具有**代表性**，即要求总体中每一个个体都有同等机会被选入样本，这便意味着**每一个样品$x_i$与总体X有相同的分布**。
2. 样本要有**独立性**，即要求样本中每一样品的取值不影响其他样品的取值，这意味着$x_1,x_2,...,x_n$**相互独立**。  

用简单随机抽样方法得到的样本称为**简单随机样本**，也简称**样本**。于是，样本$x_1,x_2,...,x_n$可以看成是相互独立的具有同一分布的随机变量，又称为i.i.d.样本，其共同分布即为总体分布。  
设总体X具有分布函数$F(x),x_1,x_2,...,x_n$为取自该总体的容量为n的样本，则样本**联合分布函数**为$$
F(x_1,x_2,...,x_n)=\prod\limits_{i=1}^n F(x_i)
$$对无限总体，代表性与独立性容易实现，关键在于排除有意或无意的人为干扰。对有限总体，只要总体所含个体数很大，特别是与样本量相比很大，则独立性也可基本得到满足。

## 样本数据的整理与显示

设$x_1,x_2,...,x_n$是取自总体分布函数为$F(x)$的样本，若将观测值由小到大进行排列，记为$x_{(1)},x_{(2)},...,x_{(n)}$，则$x_{(1)},x_{(2)},...,x_{(n)}$称为**有序样本**，用有序样本定义如下函数$$
F_n(x)= \left \{ \begin{array}{l}
    0, 当x\lt x_{(1)},\\
    {k/n}, 当x_{(k)}\leq x \lt x_{(k+1)}, k=1,2,...,n-1,\\
    1, 当x\geq x_{(n)},
\end{array}  \right.
$$则$F_n(x)$是一非减右连续函数，且满足$$
F_n(-\infty) = 0和F_n(\infty)=1
$$由此可见，$F_n(x)$是一个分布函数，称$F_n(x)$为该样本的**经验分布函数**。

**格利文科(Glivenko)定理**
设$x_1,x_2,...,x_n$是取自总体分布函数为$F(x)$的样本，$F_n(x)$是其经验分布函数，当$n\rarr \infty$时，有$$
P(\sup\limits_{-\infty\lt x \lt \infty} |F_n(x)-F(x)|\rarr 0)=1
$$
> 格利文科定理表明，当n相当大时，经验分布函数是总体分布函数$F(x)$的一个良好的近似。**经验统计学中一切统计推断都以样本为依据，其理由就在于此**。

## 统计量及其分布

当人们需要从样本获得对总体各种参数的认识时，更有效的加工方法是构造样本的函数，不同的样本函数反映总体的不同特征。  

**定义**
设$x_1,x_2,...,x_n$为取自总体的样本，若样本函数$T=T(x_1,x_2,...,x_n)$中不含有任何未知参数，则称T为**统计量**。统计量的分布称为**抽样分布**[^statistic]。

[^statistic]: 必须指出，尽管统计量不依赖于未知参数，但它的分布是依赖于未知参数的。不含未知数的样本函数，就是统计量。

**定义**
设$x_1,x_2,...,x_n$为取自某总体的样本，其算术平均值称为**样本均值**，一般用$\bar{x}$表示，即$$
\bar{x} = {x_1+x_2+...+x_n\over n}={1\over n}\sum\limits_{i=1}^n x_i
$$在分组样本场合，样本均值的近似公式为$$
\bar{x} = {x_1f_1+x_2f_2+...+x_nf_n\over n}  \quad (n=\sum\limits_{i=1}^k f_i)
$$其中k为组数，$x_i$为第i组的组中值，$f_i$为第i组的频数。

**样本均值的性质**：

1. 若把样本中的数据与样本均值之差称为偏差，则样本所有偏差之和为0，即$\sum\limits_{i=1}^n (x_i-\bar{x})=0$
2. 数据观测值与样本均值的偏差平方和最小，即在形如$\sum (x_i-c)^2$的函数中，$\sum (x_i-\bar{x})^2$最小，其中c为任意给定常数。

**定理**
设$x_1,x_2,...,x_n$是来自某个总体的样本，$\bar{x}$为样本均值。

1. 若总体分布为$N(\mu, \sigma^2)$，则$\bar{x}$的**精确分布**为$N(\mu, \sigma^2/n)$；
2. 若总体分布未知或不是正态分布，$E(x)=\mu, Var(x)=\sigma^2$存在，则n较大时$\bar{x}$的**渐近分布**为$N(\mu, \sigma^2/n)$，常记为$\bar{x} \sim N(\mu , \sigma^2/n)$。这里渐进分布是指n较大时的近似分布。

**定义**
设$x_1,x_2,...,x_n$为取自某总体的样本，则它关于样本均值$\bar{x}$的平均偏差平方和$$
s_n^2 = {1\over n}\sum\limits_{i=1}^n (x_i-\bar{x})^2
$$称为**样本方差**。其算术根$s_n = \sqrt{s_n^2}$称为**样本标准差**。  
> 相对样本方差而言，样本标准差通常更有实际意义，因为它与样本均值具有相同的度量单位。在n不大时，常用$$
s^2 = {1\over n-1} \sum\limits_{i-1}^n (x_u-\bar{x})^2
$$作为样本方差（也称**无偏方差**），其算术根$s=\sqrt{s^2}$也称为样本标准差。
> 在实际中$s^2比s_n^2$更常用，以后讲样本方差通常指$s^2$。  

**定理**
设总体X具有二阶矩，即$E(X)=\mu, Var(X)=\sigma^2 \lt \infty, x_1,x_2,...,x_n$为从该总体得到的样本，$\bar{x}和s^2$分别是样本均值和样本方差，则$$
E(\bar{x})=\mu, Var(\bar{x})=\sigma^2/n,\\
E(s^2)=\sigma^2
$$
> 该定理表明，样本均值的期望与总体均值相同，而样本均值的方差是总体方差的$1/n$。

**定义**
设$x_1,x_2,...,x_n$是样本，k为正整数，则统计量$$
a_k ={1\over n}\sum\limits_{i=1}^n x_i^k
$$称为**样本k阶原点矩**，特别，样本一阶原点矩就是样本均值。统计量$$
b_k = {1\over n}\sum\limits_{i=1}^n (x_i-\bar{x})^k
$$称为**样本k阶中心距**。特别，样本二阶中心矩就是样本方差。  

当总体关于分布中心对称时，我们用$\bar{x}$和s刻画样本特征很有代表性，而当其不对称时，只用$\bar{x}, s$就显得很不够。为此，需要一些刻画分布形状的统计量。  

**定义**
设$x_1,x_2,...,x_n$是样本，则称统计量$$
\hat{\beta}_s = {b_3\over b_2^{3/2}}
$$为**样本偏度**
> 样本偏度$\hat{\beta_s}$反映了样本数据与对称性的偏离程度和偏离方向。

**定义**
设$x_1,x_2,...,x_n$是样本，则称统计量$$
\hat{\beta_k}={b_4\over b_2^2}-3
$$为**样本峰度**
> 样本峰度$\hat{\beta_k}$是反映总体分布密度曲线在其峰值附近的陡峭程度和尾部粗细的统计量。  

**定义**
设$x_1,x_2,...,x_n$是取自总体X的样本，$x_{(i)}$称为样本的**第i个次序统计量**，它的取值是将样本观测值由小到大排列后得到的第i个观测值。其中$x_{(1)}=min\{x_1,x_2,...,x_n\}$称为样本的最小次序统计量，$x_{(n)}=max\{x_1,x_2,...,x_n\}$称为该样本的最大次序统计量。$(x_{(1)},x_{(2)},...,x_{(n)})$称为该样本的次序统计量。  

**定理**
设总体X的密度函数为$p(x)$，分布函数为$F(x),x_1,x_2,...,x_n$为样本，则第k个次序统计量$x_{(k)}$的密度函数为$$
p_k(x) = {n!\over (k-1)!(n-k)!}(F(x))^{k-1}(1-F(x))^{n-k}p(x)
$$

**定理**
次序统计量$(x_{(i)}, x_{(j)})(i\lt j)$的联合分布密度函数为$$
p_{ij}(y,z)= {n!\over (i-1)!(j-i-1)!(n-j)!}[F(y)]^{i-1}[F(z)-F(y)]^{j-i-1}[1-F(z)]^{n-j}p(y)p(z), y\leq z
$$

**样本中位数**$m_P{0.5}$也是一个很常见的统计量，它也是次序统计量的函数，通常定义为：$$
m_{0.5} = \left \{ \begin{array}{l}
    x_{({n+1\over 2})},& n为奇数\\
    {1\over 2}(x_{({n\over 2})}+x_{({n\over 2}+1)}),& n为偶数
\end{array} \right.
$$

**定理**
设总体密度函数为$p(x), x_p$为其p分位数，$p(x)$在$x_p$处连续且$p(x_p)\gt 0$，则当$m\rarr \infty$时样本p分位数$m_p$的渐进分布为$$
m_p \stackrel{·}{\sim} N(x_p, {p(1-p)\over n·p^2(x_p)})
$$特别，对样本中位数，当$n\rarr \infty$时近似地有$$
m_{0.5} \stackrel{·}{\sim} N(x_{0.5}, {1\over 4n·p^2(x_{0.5})})
$$

## 三大抽样分布

有很多统计推断是基于正态分布的假设，以标准正态变量为基石而构造的三个著名统计量在实际中有广泛的应用，这是因为这三个统计量不仅有明确背景，而且其抽样分布的密度函数有显式表达式，他们被称为统计中的“三大抽样分布”。

**$\chi^2分布（卡方分布）$**
设$X_1,X_2,...,X_n$独立同分布于标准正态分布$N(0,1)$，则$\chi^2 = X_1^2+X_2^2+...+X_n^2$[^kafang]的分布称为自由度为n的$\chi^2$分布，记为$\chi^2 \sim \chi^2(n)$

[^kafang]: 这个样本的函数的分布，被称为卡方分布，也就是样本的平方和。

$\chi^2$分布有用的一个重要原因是下面的定理。
**定理**
设$x_1,x_2,...,x_n$是来自正态总体$N(\mu,\sigma^2)$的样本，其样本均值和样本方差分别为$$
\bar{x} = {1\over n}\sum\limits_{i=1}^n x_i和s^2 = {1\over n-1}\sum\limits_{i=1}^n (x_i-\bar{x})^2
$$则有

1. $\bar{x}与s^2$相互独立
2. $\bar{x}\sim N(\mu, \sigma^2/n)$
3. ${(n-1)s^2\over \sigma^2}\sim \chi^2(n-1)$

**F分布**
设随机变量$X_1\sim \chi^2(m), X_2\sim \chi^2(n)$，$X_1$与$X_2$独立，则称$F={X_1/m\over X_2/n}$的分布是自由度为m与n的F分布，记为$F\sim F(m,n)$，其中m称为分子自由度，n称为分母自由度[^fdis]。

[^fdis]: F分布就是样本平方和之商的分布。

**推论**
设$x_1,x_2,...,x_m$是来自$N(\mu_1, \sigma_1^2)$的样本，$y_1,y_2,...,y_n$是来自$N(\mu_2,\sigma_2^2)$的样本，且此两样本相互独立，记$$
s_x^2 = {1\over m-1}\sum\limits_{i=1}^m (x_i-\bar{x})^2, s_y^2={1\over n-1}\sum\limits_{i=1}^n (y_i-\bar{y})^2
$$其中$$
\bar{x} = {1\over m}\sum\limits_{i=1}^m x_i, \bar{y} = {1\over n}\sum\limits_{i=1}^n y_i
$$则有$$
F={s_x^2/\sigma_1^2\over s_y^2/\sigma_2^2}\sim F(m-1, n-1)
$$特别，若$\sigma_1^2=\sigma_2^2$，则$F={s_x^2/s_y^2}\sim F(m-1, n-1)$

**t分布**
设随机变量$X_1$与$X_2$独立且$X_1\sim N(0,1), X_2\sim \chi^2(n)$，则称$t= {X_1\over \sqrt{X_2/n}}$的分布为自由度为n的t分布，记为$t\sim t(n)$[^tdis]。  

1. 自由度为1的t分布就是标准柯西分布，它的均值不存在。
2. $n\gt 1$时，t分布的数学期望存在且为0
3. $n\gt 2$时，t分布的方差存在，且为n/(n-2)
4. 当自由读较大$(n\geq 30)$时，t分布可以用$N(0,1)$分布近似

[^tdis]: t分布是统计学中的一类重要分布，它与标准正态分布的**微小差别**是由英国统计学家戈塞特(Gosset)发现的。t分布的发现在统计学上具有划时代的意义，打破了正态分布一统天下的局面，开创了**小样本统计推断**的新纪元。的确，t分布只有在样本量小于30时起显著作用。

**推论**
设$x_1,x_2,...,x_n$是来自正态分布$N(\mu,\sigma^2)$的一个样本，$\bar{x}$与$s^2$分别是该样子的样本均值与样本方差，则有$$
t={\sqrt{n}(\bar{x}-\mu)\over s} \sim t(n-1)
$$

**推论**
设$\sigma_1^2=\sigma_2^2=\sigma^2$，并记$$
s_w^2={(m-1)s_x^2+(n-1)s_y^2\over m+n-2}={\sum\limits_{i=1}^m (x_i-\bar{x})^2+\sum\limits_{i=1}^n (y_i-\bar{y})^2\over m+n-2}
$$则$$
{(\bar{x}-\bar{y})-(\mu_1-\mu_2)\over s_w\sqrt{{1\over m}+{1\over n}}}\sim t(m+n-2)
$$

## 充分统计量

构造统计量就是对样本进行加工，去粗取精，简化样本，便于统计推断。但在加工过程中是否会丢失样本中关于感兴趣问题的信息？如果某个统计量包含了样本中关于感兴趣问题的所有信息，则这个统计量对将来的统计推断会非常有用，这就是**充分统计量**的直观含义，它是费希尔于1922年正式提出的。

对于分布函数$F_{\theta}(X|T=t)$，如果条件"T=t"的出现，使得从样本联合分布$F_\theta(X)$到条件分布$F_{\theta}(X|T=t)$，有关$\theta$的信息消失了。这说明有关$\theta$的信息都含在统计量T之中。当已知统计量T的取值之后，也就知道了样本中关于$\theta$的所有信息，就这就统计量具有充分性的含义。

**定义**
设$x_1,x_2,...,x_n$是来自某个总体的样本，总体分布函数为$F(x;\theta)$，统计量$T=T(x_1,x_2,...,x_n)$称为$\theta$的**充分统计量**，如果在给定T的取值后，$x_1,x_2,...,x_n$的条件分布列与$\theta$无关。  

统计学中的一个**基本原则**：在充分统计量存在的场合，任何统计推断都可以基于充分统计量进行，这可以简化统计推断的程序，通常将该原则称为**充分性原则**。  
判断一个统计量是否充分的一个简单办法是下面的**因子分解定理**。

**概率函数**
$f(x)$称为随机变量X的概率函数：在连续场合，$f(x)$表示X的概率密度函数；在离散场合，$f(x)$表示X的概率分布列。

**定理**
该总体概率函数为$f(x;\theta), x_1,x_2,...,x_n$为样本，则$T=T(x_1,x_2,...,x_n)$（T可以是一维的，也可以是多维的）为充分统计量的充分必要条件是：存在两个函数$g(t,\theta)和h(x_1,x_2,...,x_n)$使得对任意的$\theta$和任一组观测值$x_1,x_2,...,x_n$，有$$
f(x_1,x_2,...,x_n)=g(T(x_1,x_2,...,x_n), \theta)h(x_1,x_2,...,x_n)
$$其中$g(t,\theta)$是通过统计量T的取值而依赖于样本的。

正态总体下，常用的$(\bar{x}, s^2)$是$\theta = (\mu, \sigma^2)$的充分统计量。

**定理**
若统计量T是充分统计量，存在某个函数$h(·)$，使得T可以表示为$t=h(s)$，则统计量S也是充分统计量。

## 参数估计

引进统计量的目的在于对感兴趣的问题进行统计推断，而在实际中，我们感兴趣的问题多是与分布族中的未知参数有关的。  
参数指以下三类未知数：

1. 分布中所含的未知参数$\theta$。如二点分布b(1,p)中的概率p，正态分布$N(\mu, \sigma^2)$中的$\mu和\sigma$
2. 分布中所含的未知参数$\theta$的函数。如服从正态分布$N(\mu, \sigma^2)$的变量X不超过某给定值a的概率$P(X\leq a)-\Phi({a-\mu\over \sigma})$是未知参数$\mu, \sigma$的函数。
3. 分布的各种特征数也都是未知参数。如均值E(X)，方差Var(X)，分布中位数等。  
一般场合，常用$\theta$表示参数，参数$\theta$所有可能取值组成的集合称为**参数空间**，常用$\Theta$表示。参数估计问题就是根据样本构造适当的统计量对上述各种未知参数作出估计。

## 点估计的概念与无偏性

**定义**
设$x_1,x_2,...,x_n$是来自总体的一个样本，用于估计未知参数$\theta$的统计量$\hat{\theta} = \hat{\theta}(x_1,x_2,...,x_n)$称为$\theta$的估计量，或称为$\theta$的**点估计**，简称**估计**。  
**定义**
设$\hat{\theta} = \hat{\theta}(x_1,x_2,...,x_n)$是$\theta$的一个估计，$\theta$的参数空间为$\Theta$，若对任意的$\theta \in \Theta$，有$$
E_\theta(\hat{\theta})=\theta
$$则称$\hat{\theta}$是$\theta$的**无偏估计**[^unbias]，否则称为**有偏估计**。

[^unbias]: 无偏性表示，把这些偏差平均起来其值为0。而若估计不具有无偏性，则无论使用多少次，其平均也会与参数真值有一定的距离，这个距离就是**系统误差**。

并不是所有的参数都存在无偏估计，当参数存在无偏估计时，称该参数是**可估的**，否则称为**不可估的**。

当参数可估时，其无偏估计可以有很多，如何在无偏估计中进行选择？直观的想法是希望该估计围绕参数真值的波动越小越好，波动大小可以用方差来衡量，因为人们常用无偏估计的方差的大小作为度量无偏估计优劣的标准，这就是**有效性**。  
**定义**
设$\hat{\theta_1},\hat{\theta_2}$是$\theta$的两个无偏估计，如果对任意的$\theta\in \Theta$有$$
Var(\hat{\theta_1})\leq Var(\hat{\theta_2})
$$且至少有一个$\theta\in \Theta$使得上述不等号严格成立，则称$\hat{\theta_1}比\hat{\theta_2}$有效。

## 矩估计及相合性

1900年皮尔逊提出了一个替换原理，后来人们称此方法为**矩法**。  
替换原理指[^substi]：  
1. 用样本矩去替换总体矩，这里的矩可以是原点矩也可以是中心矩。  
2. 用样本矩的函数去替换相应的总体矩的函数。  

[^substi]: 矩法估计的统计思想（替换原理）十分简单明确，众人都能接受，使用场合甚广。它的实质是用经验分布函数去替换总体分布，其理论基础是格利文科定理。  

**概率函数已知时未知参数的矩估计**：
设总体具有已知的概率函数$p(x; \theta_1,\theta_2,...,\theta_k)$，$(\theta_1,\theta_2,...,\theta_k)\in \Theta$是未知参数或参数向量，$x_1,x_2,...,x_n$是样本。假定总体的k阶原点矩$\mu_k$存在，则对所有的j，$0\lt j \lt k, \mu_j$都存在，若假设$\theta_1,\theta_2,...,\theta_k$能够表示成$\mu_1,\mu_2,...,\mu_k$的函数$\theta_j=\theta_j(\mu_1,\mu_2,...,\mu_k)$，则可给出诸$\theta_j$的矩估计：$$
\hat{\theta_j}=\theta_j(a_1,a_2,...,a_k), j=1,2,...,k
$$其中$a_1,a_2,...,a_k$是前k阶样本原点矩$a_j={1\over n}\sum\limits_{i=1}^n x_i^j$。进一步，如果要估计$\theta_1,\theta_2...,\theta_k$的函数$\eta = g(\theta_1,\theta_2,...,\theta_k)$，则可直接得到$\eta$的矩估计$$
\hat{\eta} = g(\hat{\theta_1},\hat{\theta_2},...,\hat{\theta_k})
$$当k=1时，通常可以由样本均值出发对未知参数进行估计；如果k=2，可以由一阶、二阶原点矩（或二阶中心矩）出发估计未知参数。

**一致性**
设$\theta\in \Theta$为未知参数，$\hat{\theta_n}=\hat{\theta_n}(x_1,x_2,...,x_n)$是$\theta$的一个估计量，n是样本容量，若对任何一个$\epsilon \gt 0$，有$$
\lim\limits_{n\rarr \infty} P(|\hat{\theta_n}-\theta|\geq \epsilon) = 0
$$则称$\hat{\theta_n}$为参数$\theta$的**一致估计**[^consistency]。

[^consistency]: 一致性被认为是对估计的一个最基本要求。

**定理**
设$\hat{\theta_n}=\hat{\theta_n}(x_1,x_2,...,x_n)$是$\theta$的一个估计量，若$$
\lim\limits_{n\rarr \infty} E(\hat{\theta})=\theta, \quad \lim\limits_{n\rarr \infty} Var(\hat{\theta_n})=0,
$$则$\hat{\theta_n}$是$\theta$的一致估计。

**定理**
若$\hat{\theta_{n1}},\hat{\theta_{n2}},...,\hat{\theta_{nk}}$分别是$\theta_1,\theta_2,...,\theta_k$的一致估计，$\eta =g(\theta_1,\theta_1,...,\theta_k)$，是$\theta_1,\theta_2,...,\theta_k$的连续函数，则$\hat{\eta_n} =g(\hat{\theta_{n1}},\hat{\theta_{n2}},...,\hat{\theta_{nk}}$)是$\eta$的一致估计。

## 最大似然估计与EM算法

求最大似然估计的**基本思路**：对离散总体，设有样本观测值$x_1,x_2,...,x_n$，我们写出**该观测值出现的概率**。它一般依赖于某个或某些参数，用$\theta$表示，将该概率看成$\theta$的函数，用$L(\theta)$表示，又称似然函数，即$$
L(\theta) = P(X_1=x_1, X_2=x_2, ..., X_n=x_n; \theta),
$$求最大似然估计就是找$\theta$的估计值$\hat{\theta} = \hat{\theta}(x_1,x_2,...,x_n)$使得上式的$L(\theta)$达到最大值。  
对连续总体，样本观测值$x_1,x_2,...,x_n$出现的概率总是为0，但我们可用联合概率密度函数来表示随机变量在观测值附近出现的可能性大小，也将其称为**似然函数**。  

**定义**
设总体的概率函数为$p(x;\theta), \theta\in \Theta$，其中$\theta$是一个未知参数或几个未知参数组成的参数向量，$\Theta$是参数空间，$x_1,x_2,...,x_n$是来自该总体的样本，将样本的联合概率函数看成$\theta$的函数，用$L(\theta; x_1,x_2,...,x_n)$表示，简记为$L(\theta)$,$$
L(\theta) = L(\theta;x_1,x_2,...,x_n)=p(x_1,\theta)p(x_2,\theta)···p(x_n;\theta),
$$$L(\theta)$称为样本的**似然函数**。如果某统计量$\hat{\theta}=\hat{\theta}(x_1,x_2,...,x_n)$满足$$
L(\hat{\theta})=\max\limits_{\theta\in \Theta} L(\theta),
$$则称$\hat{\theta}$是$\theta$的**最大似然估计**，简记为MLE[^mle]。

[^mle]: 最大似然估计有一个简单有用的性质：如果$\hat{\theta}$是$\theta$的最大似然估计，则对任一函数$g(\theta), g(\hat{\theta})$是其最大似然估计。该性质称为最大似然估计的**不变性**。

**EM**算法
MLE是一种非常有效的参数估计方法，但当分布中有多余或数据为截尾或缺失时，其MLE的求取是比较困难的。EM算法的出发点是，把求MLE的过程分为两步，第一步求期望，以便把多余的部分去掉，第二步求极大值。  

最大似然估计有一个良好的性质：它通常具有渐进正态性。
**定义**
参数$\theta$的一致估计$\hat{\theta_n}$称为渐进正态的，若存在趋于0的非负常数序列$\sigma_n(\theta)$，使得$\hat{\theta_n}-\theta\over \sigma_n(\theta)$依分布收敛于标准正态分布。这时也称$\hat{\theta_n}$服从**渐进正态分布**$N(\theta,\sigma_n^2(\theta))$，记为$\hat{\theta_n}\sim AN(\theta, \sigma_n^2(\theta))。\sigma_n^2(\theta)$称为$\hat{\theta_n}$的**渐进方差**。

**定理**
设总体X有密度函数$p(x;\theta), \theta\in \Theta, \Theta$为非退化区间，假定：

1. 对任意的x，偏导数${\partial \ln p\over \partial \theta},{\partial^2 \ln p\over \partial^2 \theta},{\partial^3 \ln p\over \partial^3 \theta} $对所有$\theta \in \Theta$都存在；
2. $\forall \theta\in \Theta$，有$$
{\left |\partial p\over \partial \theta \right |}\lt F_1(x), {\left |\partial^2 p\over \partial^2 \theta \right |}\lt F_2(x), {\left |\partial^3 p\over \partial^3 \theta \right|}\lt F_3(x),
$$其中函数$F_1(x),F_2(x),F_3(x)$满足$$
\int_{-\infty}^\infty F_1(x)dx \lt \infty, \int_{-\infty}^{\infty} F_2(x)dx \lt \infty,\\
\sup\limits_{\theta\in \Theta} \int_{-\infty}^\infty F_3(x)p(x;\theta)dx \lt \infty
$$
3. $\forall \theta \in \Theta, 0\lt I(\theta)\equiv \int_{-\infty}^\infty ({\partial \ln p\over \partial \theta})^2p(x;\theta)dx\lt \infty$
若$x_1,x_2,...,x_n$是来自该总体的样本，则存在未知参数$\theta$的最大似然估计$\hat{\theta_n}=\hat{\theta_n}(x_1,x_2,...,x_n)$，且$\hat{\theta_n}$具有一致性和渐进正态性，$\hat{\theta_n}\sim AN(\theta,{1\over nI(\theta)})$。

> 该定理表明，最大似然估计通常是渐进正态的，且其渐进方差$\sigma_n^2(\theta) = (nI(\theta))^{-1}$有一个统一的形式，其中$I(\theta)$称为**费希尔信息量**。

## 最小方差无偏估计

一致性和渐进正态性是在**大样本**场合下评价估计好坏的两个重要标准。在样本量不是很大时，人们更加倾向于使用一些基于**小样本**的评价标准，此时，对无偏估计常使用方差，对有偏估计常使用均方误差。

**均方误差**
$MSE(\hat{\theta})=E(\hat{\theta}-\theta)^2$是评价点估计的最一般的标准。  
注意到$$
MSE(\hat{\theta})=E[(\hat{\theta}-E(\hat{\theta}))+(E(\hat{\theta})-\theta)]^2=E(\hat{\theta}-E(\hat{\theta}))^2+(E(\hat{\theta})-\theta)^2 +2E[(\hat{\theta}-E(\hat{\theta}))(E(\hat{\theta})-\theta)]=Var(\hat{\theta})+(E(\hat{\theta})-\theta)^2
$$由此，**均方误差由点估计的方差与偏差$|E(\hat{\theta})-\theta|$的平方两部分组成**。
> 如果$\hat{\theta}$是$\theta$的无偏估计，则$MSE(\theta)=Var(\hat{\theta})$，此时用均方误差评价点估计与用方差是完全一样的，这也说明了用方差考察无偏估计有效性是合理的。当$\hat{\theta}$不是$\theta$的无偏估计时，就要看其均方误差$MSE(\theta)$，即不仅要看其方差大小，还要看其偏差大小。在均方误差的含义下，有些有偏估计优于无偏估计[^mse]。

[^mse]: 机器学习就是以有偏为代价，通过降低方差，增加预测准确度。

**定义**
设有样本$x_1,x_2,...,x_n$，对待估参数$\theta$，设有一个估计类，称$\hat{\theta}(x_1,x_2,...,x_n)$是该估计类中$\theta$的**一致最小均方误差估计**，如果对该估计类中另外任意一个$\theta$的估计$\tilde{\theta}$，在参数空间$\Theta$上都有$$
MSE_{\theta}\hat{\theta} \leq MSE_{\theta}\tilde{\theta}
$$
> 一致最小均方误差估计通常是在一个确定的估计类中进行的，若不对估计加以限制，则一致最小均方误差估计是不存在的。既然**一致最小均方误差估计一般都不存在**，对估计提一些合理要求，如无偏性就是一个最常见的合理要求。

**定义**
对参数估计问题，设$\hat{\theta}$是$\theta$的一个无偏估计，如果对另外任意一个$\theta$的无偏估计$\tilde{\theta}$，在参数空间$\Theta$上都有$$
Var_{\theta}(\hat{\theta}) \leq Var_\theta(\tilde{\theta})
$$则称$\hat{\theta}$是$\theta$的**一致最小方差无偏估计**，简记为UMVUE。

**定理**
设$X=(x_1,x_2,...,x_n)$是来自某总体的一个样本,$\hat{\theta}=\hat{\theta}(X)$是$\theta$的一个无偏估计，$Var(\hat{\theta})\lt \infty$。则$\hat{\theta}$是$\theta$的UMVUE的充要条件是，对任意一个满足$E(\phi(X))$=0和$Var(\phi(X))\lt \infty$的$\phi(X)$，都有$$
Cov_{\theta}(\hat{\theta},\phi)=0, \forall \theta \in \Theta
$$
> 该定理表明：$\theta$的UMVUE必与任一零的无偏估计不相关，反之亦然，这是UMVUE的重要特征。

较好的那个无偏估计是充分统计量的函数，这不是偶然的。事实上，若充分统计量和UMVUE存在，则UMVUE一定可以表示为充分统计量的函数。

**定理**
设总体概率函数是$p(x;\theta), x_1,x_2,...,x_n$是其样本，$T=T(x_1,x_2,...,x_n)$是$\theta$的充分统计量，则对$\theta$的任一无偏估计$\hat{\theta}=\hat{\theta}(x_1,x_2,...,x_n)$，令$\tilde{\theta}=E(\hat{\theta}|T)$，则$\tilde{\theta}$也是$\theta$的无偏估计，且$$
Var(\tilde{\theta})\leq Var(\hat{\theta})
$$
> 该定理说明，如果无偏估计不是充分统计量的函数，则将之对充分统计量求条件期望可以得到一个新的无偏估计，该估计的方差比原来的方差要小，从而降低了无偏估计的方差。换言之，考虑$\theta$的估计问题只需要在基于充分统计量的函数中进行即可，该说法对所有的统计推断问题都成立，这便是所谓的**充分性原则**

最大似然估计的渐进方差主要由费希尔信息量$I(\theta)$决定。
**定义**
设总体的概率函数$p(x;\theta),\theta\in \Theta$满足下列条件：

1. 参数空间$Theta$是直线上的一个开区间
2. 支撑$S=\{x:p(x;\theta)\gt 0\}$与$\theta$无关
3. 导数${\partial\over \partial \theta}p(x;\theta)$对一切$\theta\in \Theta$都存在
4. 对$p(x;\theta)$，积分与微分运算可交换次序，即$$
{\partial\over \partial \theta}\int_{-\infty}^\infty p(x;\theta)dx = \int_{-\infty}^\infty p(x;\theta)dx
$$
5. 期望$E[{\partial\over \partial \theta}\ln p(x;\theta)]^2$存在，则称$$
I(\theta)=E[{\partial\over \partial \theta}\ln p(x;\theta)]^2
$$为总体分布的**费希尔信息量**。

> 费希尔信息量是统计学中一个**基本概念**，很多的统计结果都与费希尔信息量有关。如最大似然估计的渐进方差，无偏估计的方差的下界等都与费希尔信息量$I(\theta)$有关。$I(\theta)$的种种性质表示，**“$I(\theta)$越大”可被解释为总体分布中包含未知参数$\theta$的信息越多**。

**定理**：克拉默-拉奥不等式
设总体分布$p(x;\theta)$满足费希尔信息量定义的条件，$x_1,x_2,...,x_n$是来自该总体的样本，$T=T(x_1,x_2,...,x_n)$是$g(\theta)$的任一个无偏估计，$g'(\theta)={\partial g(\theta)\over \partial \theta}$存在，且对$\Theta$中一切$\theta$，对$$
g(\theta) = \int_{-\infty}^\infty ···\int_{-\infty}^\infty T(x_1,x_2,...,x_n)\prod\limits_{i=1}^n p(x_i;\theta)dx_1···dx_n
$$的微商可在积分号下进行，即$$
g'(\theta) = \int_{-\infty}^\infty ···\int_{-\infty}^\infty T(x_1,x_2,...,x_n){\partial\over \partial \theta}\prod\limits_{i=1}^n p(x_i;\theta)dx_1···dx_n\\
=g(\theta) = \int_{-\infty}^\infty ···\int_{-\infty}^\infty T[x_1,x_2,...,x_n]({\partial\over \partial \theta}\ln \prod\limits_{i=1}^n p(x_i;\theta))\prod\limits_{i=1}^n p(x_i;\theta)dx_1···dx_n
$$对离散总体，则将上述积分改为求和号后，等式仍然成立。则有$$
Var(T)\geq [g'(\theta)]^2/(nI(\theta))
$$上式称为**克拉默-拉奥(C-R)不等式**， $[g'(\theta)]^2/(nI(\theta))$称为$g(\theta)$的无偏估计的方差的**C-R下界**，简称$g(\theta)$的C-R下界。特别，对$\theta$的无偏估计$\hat{\theta}$，有$Var(\hat{\theta})\geq (nI(\theta))^{-1}$

## 贝叶斯估计

在统计学中有两大学派：频率学派（也称经典学派）和贝叶斯学派。  
根据样本信息对总体分布或总体的特征数进行推断，这是经典学派对统计推断的规定，这种推断用到两种信息：**总体信息**和**样本信息**。  
贝叶斯学派认为，除了以上两种信息外，还应该使用第三种信息：**先验信息**。  
**总体信息**即总体分布或总体所属分布族提供的信息。  
**样本信息**即抽取样本所得观测值提供的信息。  
**先验信息**即抽样（试验）之前有关统计问题的一些信息。一般来说，先验信息来源于经验和历史资料。  

贝叶斯学派的**基本观点**是：任一未知量$\theta$都可看作随机变量，可用一个概率分布去描述，这个分布称为先验分布；在获得样本之后，**总体分布、样本与先验分布通过贝叶斯公式结合起来**，得到一个关于未知量$\theta$的新分布——后验分布；任何关于$\theta$的统计推断都应该基于$\theta$的后验分布进行。  

贝叶斯学派的一些**具体想法**：

1. 总体依赖于参数$\theta$的概率函数在经典统计中记为$p(x;\theta)$，它表示参数空间$\Theta$中不同的$\theta$对应不同的分布。在贝叶斯统计中应记为$p(x|\theta)$，它表示在随机变量$\theta$取某个给定值时总体的**条件概率函数**。
2. 根据参数$\theta$的先验信息确定**先验分布$\pi(\theta)$**。
3. 从贝叶斯观点看，样本$X=(x_1,x_2,...,x_n)$的产生要分两步进行。首先**设想**从先验分布$\pi(\theta)$产生一个个体$\theta_0$.这一步是老天爷做的。第二步从$p(X|\theta_0)$中产生一组样本。这时样本$X=(x_1,x_2,...,x_n)$的**联合条件概率函数**为$$
p(X|\theta_0)=p(x_1,x_2,...,x_n|\theta_0)=\prod\limits_{i=1}^n p(x_i|\theta_0)
$$这个分布综合了总体信息和样本信息。
4. 由于$\theta_0$是设想出来的，仍然是未知的，它是按先验分布$\pi(\theta)$产生的。为把先验信息综合进取，不能只考虑$\theta_0$，对$\theta$的其他值发生的可能性也要加以考虑，故要用$\pi(\theta)$进行综合。这样一个样本X和参数$\theta$的**联合分布**为$$
h(X,\theta) = p(X|\theta)\pi(\theta)
$$这个联合分布把总体信息、样本信息和先验信息三种可用信息都综合进去了。
5. 我们的目的是要对未知参数$\theta$作统计推断。在没有样本信息时，我们只能依据先验分布对$\theta$作出推断。在有了样本观测值$X=(x_1,x_2,...,x_n)$之后，我们应依据$h(X,\theta)$对$\theta$作出推断。若把$h(X,\theta)$作如下分解：$$
h(X,\theta)=\pi(\theta|X)m(X)
$$其中$m(X)$是X的边际概率函数$$
m(X)=\int_\Theta h(X,\theta)d\theta = \int_\Theta p(X|\theta)\pi(\theta)d\theta
$$它与$\theta$无关，或者说$m(X)$中不含$\theta$的任何信息。因此能用来对$\theta$作出推断的仅是条件分布$\pi(\theta|X)$，它的计算公式是$$
\pi(\theta|X) = {h(X,\theta)\over m(X)}= {p(X|\theta)\pi(\theta)\over \int_{\Theta}p(X|\theta)\pi(\theta)d\theta}
$$这个条件分布称为$\theta$的**后验分布**，它集中了总体、样本和先验中有关$\theta$的一切信息。上式就是用密度函数表示的贝叶斯公式，它也是用总体和样本对先验分布$\pi(\theta)$作调整的结果，它要比$\pi(\theta)$更接近$\theta$的真实情况。

由后验分布$\pi(\theta|X)$估计$\theta$有三种常用的方法：

1. 使用后验分布的密度函数最大值点作为$\theta$的点估计的**最大后验估计**
2. 使用后验分布的中位数作为$\theta$的点估计的**后验中位数估计**
3. 使用后验分布的均值作为$\theta$的点估计的**后验期望估计**

> 用得最多的是后验期望估计，它一般也简称为**贝叶斯估计**，记为$\hat{\theta_B}$

从贝叶斯公式可以看出，整个贝叶斯统计推断只要先验分布确定后就没有理论上的困难。共轭先验分布是最常用的先验分布。
**定义**
设$\theta$是总体分布$p(x;\theta)$中的参数，$\pi(\theta)$是其先验分布，若对任意来自$p(x;\theta)$的样本观测值得到的后验分布$\pi(\theta|X)$与$\pi(\theta)$属于同一个分布族，则称该分布族是$\theta$的**共轭先验分布（族）**。

## 区间估计

参数的点估计给出了一个具体的数值，便于计算和使用，但其精度如何，点估计本身不能回答，需要由其分布来反映。实际中，度量一个点估计的精度的最直观的方法就是给出未知参数的一个区间，这便产生区间估计的概念。  
设$\theta$是总体的一个参数，$x_1,x_2,...,x_n$是样本，**所谓区间估计**就是要找两个统计量$\hat{\theta_L}=\hat{\theta_L}(x_1,x_2,...,x_n)$和$\hat{\theta_U}=\hat{\theta_U}(x_1,x_2,...,x_n)$，使得$\hat{\theta_L}\lt \hat{\theta_U}$，在得到样本观测值之后，就把$\theta$估计在区间$[\hat{\theta_L},\hat{\theta_U}]$内。由于样本的随机性，区间$[\hat{\theta_L},\hat{\theta_U}]$盖住未知参数$\theta$的可能性并不确定，人们通常要求区间$[\hat{\theta_L},\hat{\theta_U}]$盖住$\theta$的概率$P(\hat{\theta_L}\leq \theta \leq \hat{\theta_U})$尽可能大，但这必然导致区间长度增大，为了解决此矛盾，把区间$[\hat{\theta_L},\hat{\theta_U}]$盖住$\theta$的概率事先给定，这就引入了置信区间的概念。

**定义**
设$\theta$是总体的一个参数，其参数空间为$\Theta, x_1,x_2,...,x_n$是来自该总体的样本，对给定的一个$\alpha(0\lt \alpha \lt 1)$，假设有两个统计量$\hat{\theta_L}=\hat{\theta_L}(x_1,x_2,...,x_n)$和$\hat{\theta_U}=\hat{\theta_U}(x_1,x_2,...,x_n)$，若对任意的$\theta\in \Theta$，有$$
P_\theta(\hat{\theta_L}\leq \theta \leq \hat{\theta_U}) \geq 1-\alpha,
$$则称随机区间$[\hat{\theta_L},\hat{\theta_U}]$为$\theta$的**置信水平为$1-\alpha$的置信区间**，或简称$[\hat{\theta_L},\hat{\theta_U}]$是$\theta$的$1-\alpha$**置信区间**，$\hat{\theta_L}$和$\hat{\theta_U}$分别称为$\theta$的（双侧）**置信下限**和**置信上限**。

**定义**
如对给定$\alpha(0\lt \alpha \lt 1)$，对任意的$\theta \in \Theta$，有$$
P_\theta(\hat{\theta_L}\leq \theta \leq \hat{\theta_U}) = 1-\alpha
$$则称$[\hat{\theta_L},\hat{\theta_U}]$为$\theta$的$1-\alpha$**同等置信区间**。

**定义**
设$\hat{\theta_L}=\hat{\theta_L}(x_1,x_2,...,x_n)$是统计量，对给定的$\alpha \in (0,1)$和任意的$\theta\in \Theta$，有$$
P_\theta(\hat{\theta_L}\leq \theta)\geq 1-\alpha, \forall \theta \in \Theta,
$$则称$\hat{\theta_L}$为$\theta$的置信水平为$1-\alpha$的（单侧）**置信下限**。假如等号对一切$\theta\in \Theta$成立，则称$\hat{\theta_L}$为$\theta$的$1-\alpha$**同等置信下限**。

**定义**
设$\hat{\theta_U}=\hat{\theta_U}(x_1,x_2,...,x_n)$是统计量，对给定的$\alpha\in (0,1)$和任意的$\theta\in \Theta$，有$$
P_\theta(\hat{\theta_U}\geq \theta)\geq 1-\alpha, \forall \theta \in \Theta,
$$则称$\hat{\theta_U}$为$\theta$的置信水平为$1-\alpha$的（单侧）**置信上限**。假如等号对一切$\theta\in \Theta$成立，则称$\hat{\theta_U}$为$\theta$的$1-\alpha$**同等置信上限**。

构造位置参数$\theta$的置信区间的最常用方法是**枢轴量法**：
1. 设法构造一个样本和$\theta$的函数$G=G(x_1,x_2,...,x_n,\theta)$使得G的分布不依赖于未知参数。一般称具有这种性质的G为**枢轴量**。
2. 适当地选择两个常数c,d，使得对给定的$\alpha(0\lt \alpha \lt 1)$，有$$
P(c\leq G \leq d) = 1-\alpha.
$$在离散场合，上式等号改为大于等于。
3. 假如能将$c\leq G \leq d$进行不等式等价变形化为$\hat{\theta_L}\leq \theta \leq \hat{\theta_U}$，则有$$
P_\theta(\hat{\theta_L}\leq \theta \leq \hat{\theta_U})=1-\alpha,
$$这表明$[\hat{\theta_L},\hat{\theta_U}]$是$\theta$的$1-\alpha$同等置信区间。

> 这种构造置信区间的关键在于构造枢轴量G，故把这种方法称为**枢轴量法**。

**单个正态总体参数的置信区间**

1. $\sigma$已知时$\mu$的置信区间
由于$\mu$的点估计为$\bar{x}$，其分布为$N(\mu,\sigma^2/n)$，因此枢轴量可选为$G={\bar{x}-\mu\over \sigma/\sqrt{n}}\sim N(0,1)$，c和d应满足$P(c\leq G\leq d)=\Phi(d)-\Phi(c)=1-\alpha$，经过不等式变形可得$P_mu(\bar{x}-d\sigma/\sqrt{n} \leq \mu \leq \bar{x}-c\sigma/\sqrt{n})=1-\alpha$，该区间长度为$(d-c)\sigma/\sqrt{n}$。由于标准正态分布为单峰对称的，在$\Phi(d)-\Phi(c)=1-\alpha$的条件下，当$d=-c=u_{1-\alpha/2}$时，d-c达到最小，由此给出了$\mu$的$1-\alpha$同等置信区间为$$
[\bar{x}-n_{1-\alpha/2}\sigma/\sqrt{n}, \bar{x}+n_{1-\alpha/2}\sigma/\sqrt{n}]
$$
2. $\sigma$未知时$\mu$的置信区间
这时可用t统计量，因为$t={\sqrt{n}(\bar{x}-\mu)\over s}\sim t(n-1)$，因此t可以用来作为枢轴量。可得到$\mu$的$1-\alpha$置信区间为$$
[\bar{x}-t_{1-\alpha/2}(n-1)s/\sqrt{n},\bar{x}+t_{1-\alpha/2}(n-1)s/\sqrt{n}]
$$其中$s^2={1\over n-1}\sum\limits_{i=1}^n (x_i-\bar{x})^2$是$\sigma^2$的无偏估计。
3. $\sigma^2$的置信区间
枢轴量不难给出。已知，$\sigma^2$可用样本方差$s^2$估计。而${(n-1)s^2\over \sigma^2}\sim \chi^2(n-1)$，由于$\chi^2$分布是偏态分布，寻找平均长度最短区间很难实现，一般都改为寻找等尾置信区间：把$\alpha$平分为两部分，在$\chi^2$分布两侧各截面积为$\alpha/2$的部分，即采用$\chi^2$的两个分数位$\chi^2_{\alpha/2}(n-1)$和$\chi^2_{1-\alpha/2}(n-1)$，它们满足$$
P(\chi^2_{\alpha/2}\leq {(n-1)s^2\over \sigma^2} \leq \chi^2_{1-\alpha/2})=1-\alpha
$$由此给出$\sigma^2$的$1-\alpha$置信区间为$$
[(n-1)s^2/\chi^2_{1-\alpha/2}(n-1), (n-1)s^2/\chi^2_{\alpha/2}(n-1)]
$$
4. 大样本置信区间
在有些场合，寻找枢轴量分布及其分布比较困难。在样本量充分大时，可用渐近分布来构造近似的置信区间，一个典型的例子是关于比例P的置信区间。  
设$x_1,x_2,...,x_n$是来自二点分布$b(1,p)$的样本，现要求p的$1-\alpha$置信区间。由中心极限定理知，样本均值$\bar{x}$的渐近分布为$N(p,{p(1-p)\over n})$，因此有$$
u={\bar{x}-p\over \sqrt{p(1-p)/n}}\stackrel{·}{\sim}N(0,1)
$$这个u可作为近似枢轴量，对给定$\alpha$，利用标准正态分布的$1-\alpha/2$分位数$u_{1-\alpha/2}$可得$$
p(|{\bar{x}-p\over \sqrt{p(1-p)/n}}|\leq u_{1-\alpha/2}) \simeq 1-\alpha,
$$括号里的事件等价于$$
(\bar{x}-p)^2 \leq u^2_{1-\alpha/2}p(1-p)/n,
$$记$\lambda=u^2_{1-\alpha/2}$，上述不等式可化为$$
(1+{\lambda/over n})p^2-(2\bar{x}+{\lambda\over n})p + \bar{x}^2 \leq 0,
$$左侧p的二次三项式的判别式$$
(2\bar{x}+{\lambda}\over n)^2-4(1+{\lambda\over n})\bar{x}^2 ={4\bar{x}(1-\bar{x})\over n}\lambda + {\lambda^2\over n^2} \gt 0,
$$故此二次三项式的图形是开口向上并与x轴有两个交点的曲线。记两个交点的横坐标为$\hat{p}_L$和$\hat{p}_U$，则有$$
P(\hat{p}_L\leq p\leq \hat{p}_U) = 1-\alpha.
$$这里$\hat{p}_L$和$\hat{p}_U$是该二次三项式的两个根，可以表示为$$
{1\over 1+{\lambda\over n}}(\bar{x}+{\lambda\over 2n}\plusmn \sqrt{{\bar{x}(1-\bar{x})\over n}\lambda + \lambda^2\over 4n^2}).
$$由于n比较大，在实用中通常略去$\lambda/n$项，于是可将置信区间近似为$$
[\bar{x}-u_{1-\alpha/2}\sqrt{\bar{x}(1-\bar{x})\over n}, \bar{x}+u_{1-\alpha/2}\sqrt{\bar{x}(1-\bar{x})\over n}]
$$

**两个正态总体下的置信区间**
设$x_1,x_2,...,x_m$是来自$N(\mu_1,\sigma_1^2)$的样本，$y_1,y_2,...,y_b$是来自$N(\mu_2, \sigma_2^2)$的样本，且两个样本相互独立。$\bar{x}$和$\bar{y}$分别是它们的样本均值，$s_x^2={1\over m-1}\sum\limits_{i=1}^m(x_i-\bar{x})^2$和$s_y^2={1\over n-1}\sum\limits_{i=1}^n(y_i-\bar{y})^2$分别是它们的样本方差。
一. $\mu_1-\mu_2$的置信区间

   1. $\sigma_1^2$和$\sigma_2^2$已知时
    此时有$\bar{x}-\bar{y}\sim N(\mu_1-\mu_2, {\sigma_1^2\over m}+{\sigma_2^2\over n})$，取枢轴量为$$
    u = {\bar{x}-\bar{y}-(\mu_1-\mu_2)\over \sqrt{{\sigma_1^2\over m}+{\sigma_2^2\over n}}}\sim N(0,1),
    $$可得$\mu_1-\mu_2$的$1-\alpha$置信区间为$$
    \bar{x}-\bar{y}\plusmn u_{1-\alpha/2}\sqrt{{\sigma_1^2\over m}+{\sigma_2^2\over n}}
    $$

    2. $\sigma_1^2=\sigma_2^2=\sigma^2$
    此时有$$
    \bar{x}-\bar{y}\sim N(\mu_1-\mu_2, ({1\over m}+{1\over n}){\sigma^2}), \\
    {(m-1)s_x^2+(n-1)s_y^2\over \sigma^2}\sim \chi^2 (m+n-2),
    $$由于$\bar{x},\bar{y},s_x^2,s_y^2$相互独立，故可构造如下服从t分布$t(m+n-2)$的枢轴量$$
    t= \sqrt{{mn(m+n-2)\over m+n}}{\bar{x}-\bar{y}-(\mu_1-\mu_2)\over \sqrt{(m-1)s_x^2+(n-1)s_y^2}}\sim t(m+n-2).
    $$记$s_w^2 = {(m-1)s_x^2 + (n-1)s_y^2\over m+n-2}$，则$\mu_1-\mu_2$的$1-\alpha$置信区间为$$
    \bar{x}-\bar{y}\plusmn \sqrt{m+n\over mn} s_w t_{1-\alpha/2}(m+n-2)
    $$

    3. ${\sigma_2^2\over \sigma_1^2} = c$已知时
    注意到$$
    \bar{x}-\bar{y}\sim N(\mu_1-\mu_2, {\sigma_1^2\over m}+{\sigma_2^2\over n}) = N(\mu_1-\mu_2, \sigma_1^2({1\over m}+{c\over n})),\\
    {(m-1)s_x^2+(n-1)s_y^2/c \over \sigma_1^2}={(m-1)s_x^2\over \sigma_1^2}+{(n-1)s_y^2\over \sigma_2^2}\sim \chi^2(m+n-2),
    $$由于$\bar{x},\bar{y},s_x^2,s_y^2$相互独立，仍可构造如下服从t分布$t(m+n-2)$的枢轴量$$
    t= {\bar{x}-\bar{y}-(\mu_1-\mu_2)\over \sqrt{(m-1)s_x^2+(n-1)s_y^2/c}}\sqrt{mn(m+n-2)\over mc+n}\sim t(m+n-2),
    $$记$s_w^2 = {(m-1)s_x^2+(n-1)s_y^2/c\over m+n-2}$，则$\mu_1-\mu_2$的$1-\alpha$置信区间为$$
    \bar{x}-\bar{y}\plusmn \sqrt{mc+n\over mn} s_wt_{1-\alpha/2}(m+n-2)
    $$
    4. 当m和n很大时的近似置信区间
    若对$\sigma_1,\sigma_2$没有什么信息，当m,n都很大时，由中心极限定理知$$
    {\bar{x}-\bar{y}-(\mu_1-\mu_2)\over \sqrt{{s_x^2\over m}+{s_y^2\over n}}}\stackrel{·}{\sim} N(0,1).
    $$由此可给出$\mu_1-\mu_2$的$1-\alpha$近似置信区间为$$
    \bar{x}-\bar{y}\plusmn u_{1-\alpha/2}\sqrt{{s_x^2\over m}+{s_y^2\over n}}.
    $$
    5. 一般情况下的近似置信区间
    若对$\sigma_1,\sigma_2$没有什么信息，当m,n也不很大，求$\mu_1-\mu_2$的精确置信区间是历史上注明的贝伦斯-费希尔(Behrens-Fisher)问题。这里介绍一种近似方法：令$s_0^2=s_x^2/m + s_y^2/n$，取近似枢轴量$$
    T=[\bar{x}-\bar{y}-(\mu_1-\mu_2)]/s_0,
    $$此时T不服从N(0,1)，但近似服从自由度为$l$的$t$分布，其中$l$由公式$$
    l={s_0^4\over {{s_x^4\over m^2(m-1)}+{{s_y^4}\over n^2(n-1)}}}
    $$决定，$l$一般不是整数，可以取与之最接近的整数代替之。于是，近似地有$T\sim t(l)$，从而可得$\mu_1-\mu_2$的$1-\alpha$近似置信区间为$$
    \bar{x}-\bar{y}\plusmn s_0t_{1-\alpha/2}(l)
    $$

二. $\sigma_1^2/\sigma_2^2$的置信区间
    1. 由于$(m-1)s_x^2/\sigma_1^2\sim \chi^2(m-1),(n-1)s_y^2/\sigma_2^2\sim \chi^2(n-1)$，且$s_x^2$和$s_y^2$相互独立，故可仿照F变量构造如下枢轴量：$$
    F={s_x^2/\sigma_1^2\over s_y^2/\sigma_2^2}\sim F(m-1,n-1),
    $$对给定的置信水平$1-\alpha$，由$$
    P(F_{\alpha/2}(m-1,n-1)\leq {s_x^2\over s_y^2}·{\sigma_2^2\over \sigma_1^2}\leq F_{1-\alpha/2}(m-1,n-1))=1-\alpha,
    $$经不等式变形即给出$\sigma_1^2/\sigma_2^2$的如下的$1-\alpha$置信区间：$$
    [{s_x^2\over s_y^2}·{1\over F_{1-\alpha/2}(m-1, n-1)}, {s_x^2\over s_y^2}·{1\over F_{\alpha/2}(m-1, n-1)}]
    $$

# 假设检验

统计推断的另一个主要内容是假设检验(hypothesis test)。

## 假设检验的基本思想与概念

非空不相交的参数集合称作**统计假设**，简称**假设**。  
通过样本对一个假设作出对或不对的具体判断规则称为该假设的一个**检验**或**检验规则**。  
若假设可用一个参数的集合表示，该假设检验问题称为**参数假设检验问题**，否则称为**非参数假设检验问题**。  

**假设检验的基本步骤**

1. 建立假设
设有来自某一个参数分布族$\{F(x,\theta)|\theta\in\Theta\}$的样本$x_1,x_2,...,x_n$，其中$\Theta$为参数空间，设$\Theta_0\subset \Theta$，且$\Theta_0\ne \empty$，则命题$H_0:\theta\in \Theta_0$称为一个假设或**原假设**或**零假设(null hypotheis)**，若有另一个$\Theta_1(\Theta_1\subset \Theta, \Theta_1\Theta_0=\empty)$，常见的一种情况是$\Theta_1=\Theta-\Theta_0$，则命题$H_1:\theta\in \Theta_1$称为$H_0$的**对立假设**或**备择假设(alternative hypothesis)**。于是，我们感兴趣的一对假设就是$$
H_0:\theta\in \Theta_0 \quad vs \quad H_1:\theta\in \Theta_1
$$如果$\Theta_0$只含一个点，则称之为**简单(simple)原假设**，否则称为**复合（composite）原假设**。
2. 选择检验统计量，给出拒绝域形式
**假设检验**是指这样一个法则：当有了具体的样本后，按该法则就可决定是接受$H_0$还是拒绝$H_0$，即检验就等价于把样本空间划分成两个互不相交的部分$W$和$\bar{W}$，当样本属于$W$时，拒绝$H_0$；否则接受$H_0$。称$W$为该检验的**拒绝域**，而$\bar{W}$为**接受域**。  
由样本对原假设进行检验总是通过一个统计量完成的，该统计量称为**检验统计量**。  

> 通常我们将注意力放在拒绝域上。正如数学上不能用一个例子去证明一个结论一样，用一个样本不能证明一个命题成立，但可以用以推翻一个命题。

3. 选择显著性水平
当$\theta\in \Theta_0$时，样本由于随机性却落入了拒绝域$W$，这时因拒绝$H_0$而产生的错误称为**第一类错误(type I error)**；当$\theta\in \Theta_1$时，样本却落入了接受域$\bar{W}$，因为接受了$H_0$而产生的的错误称为**第二类错误(type II error)**。  

**定义**
设检验问题$$
H_0:\theta \in \Theta_0 \quad vs \quad H_1:\theta\in \Theta_1
$$的拒绝域为$W$，则样本观测值X落在拒绝域W内的概率称为该检验的**势函数(power function)**，记为$$
g(\theta)=P_\theta(X\in W), \theta\in \Theta = \Theta_0 \cup \Theta_1
$$显然，势函数$g(\theta)$是定义在参数空间$\Theta$上的一个函数。当$\theta\in \Theta_0$时，$g(\theta)=1-\beta(\theta)$。  
在给定样本量的情况下，$\alpha(\theta)$和$\beta(\theta)$中一个减小必导致另一个增大。既然不能同时控制一个检验犯第一类、第二类错误的概率，在此背景下，只能采取折中方案。通常的做法是仅限制犯第一类错误的概率，这就是费希尔的显著性检验。  

**定义**
对检验问题$H_0:\theta\in \Theta_0 \quad vs \quad H_1:\theta\in \Theta_1$，如果一个检验满足对任意的$\theta\in \Theta_0$，都有$$
g(\theta)\leq \alpha
$$则称该检验是**显著性水平为$\alpha$的显著性检验**，简称**水平为$\alpha$的检验**[^obv]。  

[^obv]: 提出显著性检验的概念就是要控制犯第一类错误的概率$\alpha$，但也不能使得$\alpha$过小（会导致$\beta$过大），在适当控制$\alpha$中制约$\beta$。最常用的选择是$\alpha=0.05$，有时也选择$\alpha=0.10$或$\alpha=0.01$。

4. 给出拒绝域
确定显著性水平后，就可以定出检验的拒绝域$W$。
5. 作出判断
有了明确的拒绝域后，根据样本观测值就可以作出拒绝或接受原假设的判断。

**定义**
在一个假设检验问题中，利用样本观测值能够作出拒绝原假设的最小显著性水平称为**检验的p值**。

## 正态总体参数假设检验

一、 单个正态总体均值的检验
设$x_1,x_2,...,x_n$是来自$N(\mu, \sigma^2)$的样本，考虑如下三种关于$\mu$的检验问题：$$
I  \quad H_0:\mu\leq \mu_0 \quad vs \quad H_1:\mu\gt \mu_0,\\
II \quad H_0:\mu\geq \mu_0 \quad vs \quad H_1:\mu\lt \mu_0,\\
III \quad H_0:\mu = \mu_0 \quad vs \quad H_1:\mu\ne \mu_0
$$其中$\mu_0$是已知常数。

1. $\sigma=\sigma_0$已知时的u检验
对于单侧检验问题$I$，由于$\mu$的点估计是$\bar{x}$，且$\bar{x}\sim N(\mu, \sigma_0^2/n)$ ，故选用检验统计量$$
u={\bar{x}-\mu_0\over \sigma_0/\sqrt{n}}
$$是恰当的。直觉告诉我们：当样本均值$\bar{x}$不超过设定均值$\mu_0$时，应倾向于接受原假设；当样本均值$\bar{x}$超过$\mu_0$时，应倾向于拒绝原假设。可以，在有随机性存在的场合，如果$\bar{x}$比$\mu_0$大一点就拒绝原假设似乎不当，只有当$\bar{x}$比$\mu_0$大到一定程度时拒绝原假设才是恰当的。这就存在一个临界值c，拒绝域为$$
W_I = \{(x_1,x_2,...,x_n): u\geq c\},
$$常简记为$\{u\geq c\}$。若要求检验的显著性水平为$\alpha$，则c满足$$
p_{\mu_0}(u\geq c)=\alpha.
$$由于在$\mu=\mu_0$时，$u=N(0,1)$，故$c=u_{1-\alpha}$，最后的拒绝域为$$
W_I = \{u\geq u_{1-\alpha}\}
$$

2. $\sigma$未知时的t检验
对检验问题$I$，由于$\sigma$未知，一个自然的想法是将其替换成样本标准差s，这就形成了t检验统计量$$
t={\sqrt{n}(\bar{x}-\mu_0)\over s}.
$$
在$\mu=\mu_0$时，$t\sim t(n-1)$，从而检验问题$I的拒绝域为$$
W_I = \{t\geq t_{1-\alpha}(n-1)\}
$$

二、两个正态总体均值差的检验
设$x_1,x_2,...,x_n$是来自$N(\mu_1, \sigma_1^2)$的样本，$y_1,y_2,...,y_n$是来自另一个正态总体$N(\mu_2, \sigma_2^2)$的样本，两个样本相互独立。考虑如下三类检验问题：$$
I \quad H_0:\mu_1-\mu_2\leq 0 \quad vs \quad H_1:\mu_1- \mu_2\geq 0,\\
II  \quad H_0:\mu_1- \mu_2\geq 0 \quad vs \quad H_1:\mu_1- \mu_2 \leq 0,\\
III \quad H_0:\mu_1-\mu_2 = 0 \quad vs \quad H_1:\mu_1-\mu_2 \ne 0.
$$

1. $\sigma_1, \sigma_2$已知时的两样本u检验
此时$\mu_1-\mu_2$的点估计$\bar{x}-\bar{y}$的分布完全已知，$$
\bar{x}-\bar{y}\sim N(\mu_1-\mu_2, {\sigma_1^2\over m}+{\sigma_2^2\over n}).
$$由此可采用u检验方法，检验统计量为$$
u={\bar{x}-\bar{y}\over \sqrt{{\sigma_1^2\over m}+{\sigma_2^2\over n}}}
$$在$\mu_1=\mu_2$时，$u\sim N(0,1)$。检验的拒绝域取决于备择假设的具体内容。对于$I$类检验问题，检验的拒绝域与p值分别为$$
W_I = \{u\geq u_{1-\alpha}\}, P_I=1-\Phi(u_0),
$$其中$u_0={\bar{x}-\bar{y}\over \sqrt{{\sigma_1^2\over m}+{\sigma_2^2\over n}}}$是由样本计算得到的检验统计量的值。

2. $\sigma_1=\sigma_2=\sigma$但未知时的两样本t检验
在$\sigma_1^2=\sigma_2^2=\sigma^2$但未知时，首先$$
\bar{x}-\bar{y}\sim N(\mu_1-\mu_2, ({1\over m}+{1\over n})\sigma^2),
$$其次，由于$$
{1\over \sigma^2}\sum\limits_{i=1}^m (x_i-\bar{x})^2\sim \chi^2(m-1), {1\over \sigma^2}\sum\limits_{i=1}^n (y_i-\bar{y})^2\sim \chi^2(n-1),
$$故${1\over \sigma^2}(\sum(x_i-\bar{x})^2+\sum(y_i-\bar{y})^2)\sim \chi^2(m+n-2)$，记$$
s_w^2 = {1\over m+n-2}[\sum\limits_{i=1}^m (x_i-\bar{x})^2+\sum\limits_{i=1}^n (y_i-\bar{y})^2],
$$于是有$$
t = {(\bar{x}-\bar{y})-(\mu_1-\mu_2)\over s_w\sqrt{{1\over m}+{1\over n}}}\sim t(m+n-2).
$$当$\mu_1=\mu_2$时，检验统计量为$$
t={\bar{x}-\bar{y}\over s_w\sqrt{{1\over m}+{1\over n}}}.
$$对检验问题$I$，检验的拒绝域与p值分别为$$
W_I=\{t\geq t_{1-\alpha}(m+n-2)\}, p_I=P(t\geq t_0),
$$其中$t_0={\bar{x}-\bar{y}\over s_w\sqrt{{1\over m}+{1\over n}}}$是由样本计算得到的检验统计量的值，t是服从自由度是n+m-2的t分布的随机变量。

三. 正态总体方差的检验

1. 单个正态总体方差的$\chi^2$检验
设$x_1,x_2,...,x_n$是来自$N(\mu, \sigma^2)$的样本，对方差亦可考虑如下三个检验问题：$$
I  \quad H_0:\sigma^2\leq \sigma_0^2  \quad vs \quad  H_1:\sigma^2\gt \sigma_0^2,\\
II  \quad H_0:\sigma^2\geq \sigma_0^2  \quad vs \quad  H_1:\sigma^2\lt \sigma_0^2,\\
III  \quad H_0:\sigma^2= \sigma_0^2  \quad vs \quad H_1:\sigma^2\ne \sigma_0^2,
$$其中$\sigma_0^2$是已知常数。此处通常假定$\mu$未知，它们采用的检验统计量是相同的，均为$\chi^2=(n-1)s^2/\sigma_0^2$
在$\sigma^2=\sigma_0^2$时，$\chi^2\sim \chi^2(n-1)$，于是，若取显著性水平为$\alpha$，则对应三个检验问题的显著性水平为$\alpha$的检验的拒绝域依次为$$
W_I = \{\chi^2\geq \chi^2_{1-\alpha}(n-1)\},\\
W_{II} = \{\chi^2\leq \chi^2_{\alpha}(n-1)\},\\
W_{III} = \{\chi^2\leq \chi^2_{\alpha/2}(n-1)或\chi^2\geq \chi^2_{1-\alpha/2}(n-1)\}.
$$
2. 两个正态总体方差比的F检验
设$x_1,x_2,...,x_m$是来自$N(\mu_1,\sigma_1^2)$的样本，$y_1,y_2,...,y_n$是来自$N(\mu_2,\sigma_2^2)$的样本。考虑如下三个假设检验问题：$$
I  H_0:\sigma_1^2\leq \sigma_2^2  vs  H_1:\sigma_1^2\gt \sigma_2^2,\\
II  H_0:\sigma_1^2\geq \sigma_2^2  vs  H_1:\sigma_1^2\lt \sigma_2^2,\\
III  H_0:\sigma_1^2= \sigma_2^2  vs  H_1:\sigma_1^2\ne \sigma_2^2,
$$此处$\mu_1,\mu_2$均未知，记$s_x^2,s_y^2$分别是由$x_1,x_2,...,x_m$算得的$\sigma_1^2$的无偏估计和由$y_1,y_2,...,y_n$算得的$\sigma_2^2$的无偏估计（两个都是样本方差），则可建立如下的检验统计量:$$
F={s_x^2\over s_y^2}.
$$当$\sigma_1^2=\sigma_2^2$时，$F\sim F(m-1,n-1)$，由此给出三个检验问题对应的拒绝域依次为$$
W_I=\{F\geq F_{1-\alpha}(m-1, n-1)\},\\
W_{II}=\{F\leq F_{\alpha}(m-1, n-1)\},\\
W_{III}=\{F\leq F_{\alpha/2}(m-1, n-1)或F\geq F_{1-\alpha/2}(m-1, n-1)\}.
$$

## 其他分布参数的假设检验

**指数分布参数的假设检验**
指数分布是一类重要的分布，有广泛的应用。设$x_1,x_2,...,x_n$是来自指数分布$Exp(1/\theta)$的样本，$\theta$为其均值，现考虑关于$\theta$的如下检验问题：$$
I \quad H_0:\theta\leq \theta_0  \quad vs \quad H_1:\theta\gt \theta_0.
$$为寻找检验统计量，考察参数$\theta$的充分统计量$\bar{x}$。在$\theta=\theta_0$时，$n\bar{x}=\sum\limits_{i=1}^n x_i\sim Ga(n, 1/\theta_0)$，由伽马分布性质可知$$
\chi^2={2n\bar{x}\over \theta_0}\sim \chi^2(2n),
$$于是可用$\chi^2$作为检验统计量并利用$\chi^2(2n)$的分位数建立检验的拒绝域，对检验问题$I$，拒绝域形式为$W_I=\{\chi^2\geq \chi^2_{1-\alpha}(2n)\}$.

**比率p的检验**
比率p可看作某事件发生的概率，即可看作二点分布$b(1,p)$中的参数。做n次独立试验，以x记该事件发生的次数，则$x\sim b(n,p)$。可以根据x检验关于p的一些假设。先考虑单边假设检验问题：$$
I \quad H_0: p\leq p_0  \quad vs \quad H_1: p\gt p_0.
$$直观上，一个显然的检验方法是取如下的拒绝域$W=\{x\geq c\}$，由于x只取整数值，故c可限制在非负整数中。然后，一般情况下对给定的$\alpha$，不一定能正好取到一个c，使得$$
P(x\geq c;p_0)=\sum\limits_{i=c}^n C_n^i P_0^i(1-p_0)^{n-i}=\alpha,
$$能恰巧使得上式成立的c值是罕见的。这是在对离散总体作假设检验中普遍会遇到的问题。在这种情况下，较常见的是找一个$c_0$，使得$$
\sum\limits_{i=c_0}^n C_n^i p_0^i (1-p_0)^{n-i}\gt \alpha \gt \sum\limits_{i=c_0+1}^n C_n^i p_0^i (1-p_0)^{n-i}.
$$于是，可取$c=c_0+1$，此时相当于把显著性水平由$\alpha$降低到$\sum\limits_{i=c_0+1}^n C_n^i p_0^i (1-p_0)^{n-i}$。
事实上，在离散场合使用p值作检验较为简单，这时可以不用找$c_0$，而只需根据观测值$x=x_0$计算检验的p值，即$$
p=P(x\geq x_0),
$$并将之与事先给定的显著性水平比较大小即可，其中x为服从$b(n,p_0)$分布的随机变量。

**大样本检验**
在实际使用中，如果样本量较大，经常采用渐进正态分布构造检验统计量，获得大样本检验。  
一般思路如下：设$x_1,x_2,...,x_n$是来自正态总体分布$F(x;\theta)$的样本，又设该总体均值为$\theta$，方差为$\theta$的函数，记为$\sigma^2(\theta)$。现在要对下列三类假设检验问题：$$
I \quad H_0: \theta\leq \theta_0 \quad vs \quad H_1: \theta \gt \theta_0.\\
II \quad H_0: \theta\geq \theta_0 \quad vs \quad H_1: \theta \lt \theta_0.\\
III \quad H_0: \theta= \theta_0 \quad vs \quad H_1: \theta \ne \theta_0. 
$$寻找大样本检验方法。在样本容量n充分大时，利用中心极限定理知$\bar{x\stackrel{·}{\sim}N(\theta,\sigma^2(\theta)/n)}$，故在$\theta=\theta_0$时，可采用如下检验统计量：$$
u={\sqrt{n}(\bar{x}-\theta_0)\over \sqrt{\sigma^2(\hat{\theta})}}\stackrel{·}{\sim}N(0,1),
$$其中$\hat{\theta}$为$\theta$的MLE，并由此可近似地确定拒绝域。对应上述三类检验问题的拒绝域依次为$$
W_I = \{u\geq u_{1-\alpha}\},\\
W_{II} = \{u\leq u_{\alpha}\},\\
W_{III} = \{|u|\geq u_{1-\alpha/2}\}.\\
$$

## 似然比检验与分布拟合检验

类似于估计中存在着多种估计一样，在假设检验中也有多种检验方法。似然比检验是一种应用较为广泛的检验方法，在假设检验中的地位犹如MLE在点估计中的地位。  
**定义**
设$x_1,x_2,...,x_n$为来自密度函数为$p(x;\theta),\theta \in \Theta$的总体的样本，考虑如下检测问题：$$
H_0: \theta \in \Theta_0  vs  H_1:\theta \in \Theta_1 = \Theta-\Theta_0
$$令$$
\Lambda(x_1,x_2,...,x_n)={\sup\limits_{\theta\in \Theta} p(x_1,x_2,...,x_n;\theta)\over \sup\limits_{\theta\in \Theta_0} p(x_1,x_2,...,x_n;\theta)},
$$则我们称统计量$\Lambda((x_1,x_2,...,x_n)$为假设检验的**似然比(likelihood ratio)**，有时也称之为**广义似然比**。  

统计量$\Lambda((x_1,x_2,...,x_n)$也可以写成$$
\Lambda(x_1,x_2,...,x_n)={p(x_1,x_2,...,x_n;\hat{\theta})\over p(x_1,x_2,...,x_n;\hat{\theta_0})},
$$其中$\hat{\theta}$表示在全参数空间$\Theta$上$\theta$的最大似然估计，$\hat{\theta_0}$表示在子参数空间$\Theta_0$上$\theta$的最大似然估计。也就是说，$\Lambda(x_1,x_2,...,x_n)$的分子表示没有假设时的似然函数最大值，分母表示在原假设成立条件下的似然函数最大值。不难看出，如果$\Lambda(x_1,x_2,...,x_n)$的值很大，则说明$\theta\in \Theta_0$的可能性要比$\theta\in \Theta_1$的可能性小，于是，我们有理由认为$H_0$不成立。这样，我们有如下的似然比检验  

**定义**
当采用似然比统计量$
\Lambda(x_1,x_2,...,x_n)={p(x_1,x_2,...,x_n;\hat{\theta})\over p(x_1,x_2,...,x_n;\hat{\theta_0})}
$作为检验问题的检验统计量，且取其拒绝域为$W=\{\Lambda(x_1,x_2,...,x_n)\geq c\}$，其中临界值c满足$$
P_\theta(\Lambda(x_1,x_2,...,x_n)\geq c)\leq \alpha, \forall \theta \in \Theta_0,
$$则称此显著性水平$\alpha$的**似然比检验(likelihood ratio test)**，简记为LRT。
> 似然比检验是寻找检验统计量的一种思路，它有很好的的统计思想。似然比检验有一个统一的检验统计量，遗憾的是该似然比检验统计量在一般场合至今尚无统一的精确分布形式，但在很一般的条件下有一个统一的渐进分布（对数似然比检验统计量的2倍近似服从$\chi^2$分布，其自由度为其独立参数个数），这为似然比检验的广泛使用奠定了基础。

**分类数据的$\chi^2$拟合优度检验**
此前的检验问题都是在总体分布形式已知的前提下对分布的参数建立假设并进行检验，属于假设检验问题。下面对总体分布形式建立假设并进行检验，这一类检验问题统称为**分布的拟合检验**，是一类非参数检验问题。  
根据某项指标，总体被分成r类：$A_1,A_2,...,A_r$。此时我们最关心的是关于各类元素在总体中所占的比率的假设$$
H_0: A_i 所占的比率是P_{i0}, i=1,2,...,r,
$$其中$p_{i0}$已知，满足$\sum\limits_{i=1}^r p_{i0}=1$。记$x_1,x_2,...,x_n$为从此总体抽出的样本，且以$n_i$记这n个样本中属于$A_i$的样本个数。由于当$H_0$成立时，在n个样本中属于$A_i$类的“理论个数”或“期望个数”为$np_{i0}$，而我们实际观测到的值为$n_i$，故当$H_0$成立时，$n_i$与$np_{i0}$应相差不大。于是K.皮尔逊提出用统计量$$
\chi^2 = \sum\limits_{i=1}^r {(n_i-np_{i0})^2\over np_{i0}}
$$来衡量“理论个数”与实际个数间的差异。  
为了控制上述检验的第一类错误，必须知道此检验统计量在原假设成立下的分布，为此，K.皮尔逊证明了如下定理：
**定理**
在前述各项假定下，在$H_0$成立时，对上式的统计检验量有$$
\chi^2\stackrel{L}{\rarr} \chi^2(r-1).
$$ 根据该定理，对于假设$H_0: A_i 所占的比率是P_{i0}, i=1,2,...,r,$，可以采取如下的显著性水平近似为$\alpha$的显著性检验：检验统计量为$\chi^2 = \sum\limits_{i=1}^r {(n_i-np_{i0})^2\over np_{i0}}$，拒绝域为$$
W=\{\chi^2\geq \chi^2_{1-\alpha}(r-1)\}.
$$该检验方法称为皮尔逊$\chi^2$拟合优度检验。

**分布的$\chi^2$拟合优度检验**
设$x_1,x_2,...,x_n$是来自总体$F(x)$的样本，有时，需要检验的原假设是$$
H_0: F(x)=F_0(x),
$$其中$F_0(x)$称为理论分布，它可以是一个完全已知的分布，也可以是一个仅依赖于有限个实参数且分布形式已知的分布函数。这个分布检验问题就是检验观测数据是否与理论分布相符合。在样本容量较大时，这类问题可以用$\chi^2$拟合优度检验来解决。  

1. 总体X为离散分布
设总体X为取有限或可列个值$a_1,a_2,...$的离散随机变量，我们把相邻的某些$a_i$合并为一类，使得$a_1,a_2,...$被分为有限个类$A_1,A_2,...,A_r$，并使得样本观测值$x_1,x_2,...,x_n$落入每一个$A_i$内的个数$n_i$不小于5。记$P(X\in A_i)=p_i(i=1,2,...,r)$，那么，假设$H_0$:总体分布$F(x)=F_0(x)$就转化为如下假设：$$
H_0: A_i所占的比例为p_i(i=0,1,...r)。
$$
这样，离散分布的拟合检验与前述分类数据的检验问题就完全一样了。

2. 总体X为连续分布
设总体X为连续随机变量，分布函数为$F_0(x)$，这种情况略为复杂一些。一般采用下列方法：选$r-1$个实数$a_1\lt a_2\lt ... \lt a_{r-1}$，将实数族分为r个区间$$
(-\infty,a_1], (a_1, a_2], ..., (a_{r-1}, \infty),  
$$当观测值落入第i个区间内，就把它看作属于第i类，因此，这r个区间就相当于r个类。在$H_0$为真时，记$$
p_i = P(a_{i-1}\lt X \leq a_i)= F_0(a_i)-F_0(a_{i-1}), i=1,2,...,r,
$$其中$a_0=-\infty, a_r=\infty$,以$n_i$表示样本的观测值$x_1,x_2,...,x_n$落入区间$(a_{i-1},a_i]$内的个数$(i=1,2,...,r)$，接下来的做法就与总体只取有限个值的情况一样了。  

**列联表的独立性检验**
按两个或多个特征分类的频数数据，称为**交叉分类数据**。它们一般以表格的形式给出，称为**列联表**。  
列联表分析的基本问题是，考察属性之间有无关联，即判别两个属性是否独立。在$r\times c$列联表中，若以$p_{i·}, p_{·j}和p_{ij}$分别表示总体中的个体仅属于$A_i$，仅属于$B_j$，和同时属于$A_i与B_i$的概率，可得一个二维离散分布表。那么"A ,B两属性独立"的假设可以表述为$$
H_0: p_{ij}=p_{i·}p_{·j}, i=1,2,...,r, j=1,2,...,c.
$$这就变为此前诸$p_{ij}$不完全已知时的分布拟合检验。这里诸$p_{ij}$共有rc个参数，在原假设$H_0$成立时，这rc个参数$p_{ij}$由r+c个参数$p_{1·},...,p_{r·}$和$p_{·1},...,p_{·c}$决定。在这后r+c个参数中存在两个约束条件：$\sum\limits_{i=1}^r p_{i·}=1, \sum\limits_{i=1}^c p_{·j}=1$，所以，此时$p_{ij}$实际上由r+c-2个独立参数所确定。据此，检验统计量为$$
\chi^2 = \sum\limits_{i=1}^r\sum\limits_{j=1}^c {(n_{ij}-n\hat{p_{ij}})^2\over n\hat{p_{ij}}}
$$在原假设$H_0$成立时，上式近似服从自由度为$rc-(r+c-2)-1 = (r-1)(c-1)$的$\chi^2$分布。其中诸$\hat{p_{ij}}$是在$H_0$成立下得到的$p_{ij}$的最大似然估计，其表达式为$$
\hat{p_{ij}}=\hat{p_{i·}}\hat{p_{·j}}={n_{i·}\over n}·{n_{·j}\over n}
$$对给定的显著性水平$\alpha(0\lt \alpha \lt 1)$，检验的拒绝域为$W=\{\chi^2\geq \chi^2_{1-\alpha}((r-1)(c-1))\}$.

## 正态性检验

判断总体分布是否为正态分布的检验方法称为正态性检验。

1. 正态概率纸  
正态概率纸是一种特殊的坐标纸，横坐标等间隔，纵坐标按标准正态分布函数值给出。利用样本数据在概率纸上描点，用**目测**方法看这些点是否在一条直线附近，若是则认为改数据来自总体为正态分布。

2. W检验  
W检验用于$8\leq n \leq 50$时。  
设$x_1,x_2,...,x_n$是来自正态总体$N(\mu, \sigma^2)$的样本，$x_{(1)} \leq x_{(2)} \leq ... \leq x_{(n)}$为其次序统计量，W统计量定义为$$
W = {[\sum\limits_{i=1}^n (a_i-\bar{a})(x_{(i)}-\bar{x}]^2\over \sum\limits_{i=1}^n (a_i-\bar{a})^2\sum\limits_{i=1}^n (x_i-\bar{x})^2}
$$其中系数$a_1,a_2,...,a_n$在样本容量为n时有特定的值，可查表获得。对于假设$H_0$：总体分布为$N(\mu, \sigma^2)$，其检验的拒绝域具有形式$\{W\leq W_\alpha\}$，其中$\alpha$分位数$W_\alpha$可查表获得。  

3. EP检验  
EP检验即爱泼斯-普利(Epps-Pulley)检验$(n\geq 8)$。  
EP检验对多种备择假设有较高的效率，其出发点是利用样本的特征函数与正态分布的特征函数的差的模的平方产生的一个加权积分得到的。  
设$x_1,x_2,...,x_n$是来自正态总体$N(\mu, \sigma^2)$的样本，EP检验统计量定义为$$
T_{EP}= 1+ {n\over \sqrt{3}}+ {2\over n}\sum\limits_{i=2}^n\sum\limits_{j=1}^{i-1}exp\{{-(x_j-x_i)^2\over 2s_n^2}\}-\sqrt{2}\sum\limits_{i=1}^n exp\{{-(x_i-\bar{x})^2\over 4s_n^2}\},
$$其中$\bar{x},s_n^2$就是前述的样本均值和（除以n的）样本方差。  
上式通常需要编程计算，其拒绝域为$\{T_{EP}\geq T_{1-\alpha,EP}(n)\}, T_{1-\alpha, EP}(n)$是样本容量为n时EP检验统计量（在原假设下的分布）的$1-\alpha$分位数。  

## 非参数检验  

**统计学的基本问题**是利用观测到的样本推断总体。在统计推断中，对研究的总体常常要做一些假定，最常见的假定是假定总体分布为正态。这样的假定是比较强的。由于实际的总体与假定的总体往往会有差距，那么，这种做法将可能引起推断结果的错误。这个问题促使人们去研究在总体分布假定比较弱的前提下，如何进行统计推断。非参数检验正是这样的一个领域。  

1. 游程检验  
所有的统计推断方法要求数据随机取自同一个总体，对数据是否符合随机选取的检验就是**游程检验**。  
设$x_1,x_2,...x_n$为依时间顺序连续得到的一组样本观测值序列。记样本中位数为$m_e$，把序列中小于$m_e$的那些$x_i$换成0，大于或等于$m_e$的那些$x_i$换成1。这样就得到一个由0和1组成的序列。把以0为界的一连串的1称1游程，以1为界的一连串的0称为0游程，统称为**游程**。设序列中0和1的个数分别为$n_1$和$n_2$，其和为样本量n。设R表示序列的总游程数，则R的最小值是2，最大值是n。若游程总数R的值过大或过小，可以认为样本数据受到了某些非随机因素的干扰，它不符合随机抽取的原则。因此，对于原假设$$
H_0: 样本序列符合随机抽取的原则
$$该检验的拒绝域应具有形式$\{R\leq c_1\}\cup \{R\geq c_2\}$，其中临界值$c_1$和$c_2$要根据$H_0$为真时R的分布确定。  

2. 符号检验  
符号检验是一类重要的非参数检验，主要用来对总体p分位数$x_p$进行检验。对任一连续总体X，其p分位数$x_p(0\lt p \lt1)$是存在且唯一的。  
设$x_1,x_2,...,x_n$是来自总体X的样本，欲检验$$
H_0: x_p\leq x_0 \quad vs \quad H_1: x_p \gt x_0,
$$其中$F(x_p)=p$，$x_0$是某个给定常数。记符号函数$$
y_i=\left \{ \begin{array}{l}
    1, x_i\gt x_0,\\
    0, x_i\leq x_0,
\end{array} \right.
$$记$\theta=P(y_i=1)=P(x_i-x_0\gt 0)$，则$y_1,y_2,...,y_n$可以看作是来自二点分布$b(1,\theta)$的样本，从而$S^+=\sum\limits_{i=1}^n y_i\sim b(n,\theta)$，在$H_0$为真时，有$$
\theta=P(y_i=1)=P(x_i-x_0\gt 0)\leq P(x_i-x_p\gt 0)=1-P(x_i-x_p\leq 0)=1-F(x_p)=1-p.
$$反之，若$\theta\leq 1-p$，则$\theta=P(x_i-x_0\gt 0)\leq P(x_i-x_p)\gt 0 = 1-p$，从而$x_p\leq x_0$，亦即$H_0$为真。所以，检验问题等价于$$
H_0:\theta\leq 1-p \quad vs \quad H_1: \theta\gt 1-p.
$$
上述检验问题是二项分布参数的检验问题，该检验问题的统计量是$S^+=\sum\limits_{i=1}^n y_i$，拒绝域形式为$$
W=\{S^+\geq c\}, c=\inf\limits_k \{k:\sum\limits_{i=k}^n C_n^i p_0^i (1-p_0)^{n-i}\leq \alpha\},
$$不难看出，$S^+=\sum\limits_{i=1}^n y_i$就是差值$$
x_1-x_0, x_2-x_0, ..., x_n-x_0
$中取正号的个数。  
上述统计量$S^+=\sum\limits_{i=1}^n y_i$称**符号统计量**。利用符号统计量做的检验称**符号检验**。

3. 秩和检验  
符号检验有一个不足：只利用了观测值和中心位置之差的正负号，而没有考虑到这些差的绝对值大小。秩检验方法是建立在秩及秩统计量基础上的非参数方法。  
**定义**
设$x_1,x_2,...,x_n$是来自连续分布$F(x)$的简单随机样本，$x_{(1)}\leq x_{(2)}\leq ... \leq x_{(n)}$是其观测值的有序样本，则观测值$x_i$在有序样本中的序号r称为$x_i$的秩，记为$R_i=r$。  
**定义**
设$x_1,x_2,...,x_n$是来自连续总体的样本，$R_i$是$x_i$的秩，则$R=(R_1,R_2,...,R_n)$称为$(x_1,x_2,...,x_n)$的**秩统计量**。由R导出的统计量，也称为秩统计量。基于秩统计量的检验方法称为**秩检验**。  
**定义**
设$x_1,x_2,...,x_n$是样本，记$R_i$为$|x_i|$在$(|x_1|,|x_2|,...,|x_n|)$中的秩，记$$
I(x_i\gt 0) = \left \{ \begin{array}{l}
    1, x_i\gt 0,\\
    0, x_i\leq 0.
\end{array} \right.
$$则称$$
W^+ = \sum\limits_{i=1}^n R_iI(x_i\gt 0)
$$为**符号秩和统计量**。用这个统计量所作的检验称为**符号秩和检验**。

# 方差分析与回归分析

## 方差分析

前几章讨论的都是一个总体或两个总体的统计分析问题，在实际工作中还经常碰到多个总体均值的比较问题，处理这类问题通常采用方差分析方法。  

1. 单因子方差分析的统计模型  
在单因子试验中，记因子为A，设其有r个水平，记为$A_1,A_2,...,A_r$，在每一水平下考察的指标可以看成一个总体，现有r个水平，假定：
(1)每一总体均为正态总体，记为$N(\mu_i, \sigma_i^2), i = 1,2,...,r.$
(2)各总体的方差相同，记为$\sigma_1^2=\sigma_2^2=...=\sigma_r^2=\sigma^2$.
(3)从每一总体中抽取的样本是相互独立的，即所有的试验结果$y_{ij}$都相互独立。  
这三个假定都可以用统计方法进行验证。譬如，利用正态性检验验证（1），利用方差齐次性检验验证（2），实验结果$y_{ij}$的独立性可由随机化实现，这里的随机化是指所有试验按随机次序进行。  
我们要做的工作是比较各水平下的均值是否相同，即要对如下的一个假设进行检验：$$
H_0: \mu_1=\mu_2=...=\mu_r,
$$其备择假设为$$
H_1: \mu_1=\mu_2=...=\mu_r不全相等。
$$如果$H_0$成立，因子A的r个水平均值相同，称因子A的r个水平间没有显著差异，简称因子A**不显著**；反之，当$H_0$不成立时，因子A的水平均值不全相同，称因子A**显著**[^obeq]。

[^obeq]: 显著就是不相等，不显著就是相等。

为对假设进行检验，需要从每一水平下的总体抽取样本，设从第i个水平下的总体获得m个试验结果，用$y_{ij}$表示第i个总体的第j次重复试验结果，共得如下$r\times m$个试验结果：$$
y_{ij}, i=1,2,...,r, j=1,2,...,m,
$$其中r为水平数，m为重复数，i为水平编号，j为重复序号。  
水平$A_i$下的试验结果$y_{ij}$与该水平下的指标均值$\mu_i$总是有差距的，即$\epsilon_{ij}=y_{ij}-\mu_i, \epsilon_{ij}$称为随机误差，于是又$$
y_{ij}=\mu_i + \epsilon_{ij}.
$$上式称为试验结果$y_{ij}$的**数据结构式**。把三个假定用于数据结构式就可以写出单因子方差分析的统计模型：$$
\left \{ \begin{array}{l}
    y_{ij} = \mu_i + \epsilon_{ij}, i= 1,2,...,r, j=1,2,...,m,\\
    诸\epsilon_{ij}相互独立，且都服从N(0,\sigma^2).
\end{array} \right.
$$为了能更好地描述数据，常在方差分析中引入总均值与水平效应的概念。诸$\mu_i$的平均（所有试验结果的均值的平均）$$
\mu = {1\over r}(\mu_1+\mu_2+...+ \mu_r)={1\over r}\sum\limits_{r=1}^r \mu_i
$$称为**总均值**，也称**一般平均**。第i个水平下的均值$\mu_i$与总均值$\mu$的差$$
a_i=\mu_i-\mu, i=1,2,...,r
$$称为因子A的第i个水平的**主效应**，简称为$A_i$的**水平效应**。
容易看出$$
\sum\limits_{i=1}^r a_i = 0, \\
\mu_i = \mu + a_i,
$$这表明第i个总体的均值是由总均值与该水平的效应叠加而成的，从而单因子方差分析的统计模型可以改写为$$
\left \{ \begin{array}{l}
    y_{ij} = \mu + a_i + \epsilon_{ij}, i= 1,2,...,r, j=1,2,...,m,\\
    \sum\limits_{i=1}^r a_i = 0,\\
    诸\epsilon_{ij}相互独立，且都服从N(0,\sigma^2).
\end{array} \right.
$$假设可改写为$$
H_0: a_1 = a_2 = ... =a_r=0,
$$备择假设为$$
H_0: a_1 , a_2 , ... , a_r 不全为0.
$$

2. 平方和分解  
对两个正态总体均值间有无差异可用t检验，但对三个及以上正态总体均值间有无差异再用t检验就行不通了。费希尔等人另辟思路，改用数据的平方和及其分解导出F分布来进行显著性检验。  
在单因子方差分析中，将试验数据列成下表形式$$
\begin{array}{cccc}
    因子水平&试验数据&和&均值\\
    \hline
    A_1&y_{11}y_{12}...y_{1m}&T_1&\bar{y_{1·}}\\
    A_2&y_{21}y_{22}...y_{2m}&T_2&\bar{y_{2·}}\\
    \vdots&\vdots\vdots\quad\vdots&\vdots&\vdots&\\
    A_r&y_{r1}y_{r2}...y_{rm}&T_r&\bar{y_{r·}}\\
\end{array}
$$

最后两列的和与均值的含义如下：$$
T_i=\sum\limits_{j=1}^m y_{ij}, \bar{y_{i·}}={T_i\over m}, i=1,2,...,r,\\
T=\sum\limits_{i=1}^r T_i, \bar{y} = {T\over r·m}={T\over n},\\
n=r·m=总试验次数。
$$数据$y_{ij}$与总均值$\bar{y}$间的偏差可用$y_{ij}-\bar{y}$表示，它可以分解为两个偏差之和$$
y_{ij}-\bar{y} = (y_{ij}-\bar{y_{i·}})+(\bar{y_{i·}}-\bar{y}).
$$记$$
\bar{\epsilon_{i·}}={1\over m}\sum\limits_{j=1}^m \epsilon_{ij},\\
\bar{\epsilon} = {1\over r}\sum\limits_{i=1}^r \bar{\epsilon_{i·}}={1\over n}\sum\limits_{i=1}^r\sum\limits_{j=1}^m \epsilon_{ij}
$$由于$$
y_{ij}-\bar{y_{i·}} = (\mu_i+\epsilon_{ij})-(\mu_i + \bar{\epsilon_{i·}}) = \epsilon_{ij}-\bar{\epsilon_{i·}},
$$所以$y_{ij}-\bar{y_{i·}}$仅反映组内数据与组内均值的随机误差，称为**组内偏差**。而$$
y_{i·}-\bar{y} = (\mu_i+\epsilon_{i·})-(\mu + \bar{\epsilon}) = a_i + \epsilon_{i·}-\bar{\epsilon},
$$$\bar{y_{i·}}-\bar{y}$除了反映随机误差外，还反映了第i个水平效应，称为**组间偏差**。  
在统计学中，把k个数据$y_1,y_2,...,y_k$分别对其均值$\bar{y}=(y_1+y_2+...+y_k)/k$的偏差平方和$$
Q = (y_1-\bar{y})^2 + (y_2-\bar{y})^2 + ... + (y_k-\bar{y})^2 = \sum\limits_{i=1}^k (y_i-\bar{y})^2
$$称为k个数据的**偏差平方和**，有时简称**平方和**。常用来度量若干个数据分散的程度，是用来度量若干个数据间差异（即波动）大小的一个重要统计量。  
在构成偏差平方和Q的k个偏差$y_1-\bar{y}, y_2-\bar{y},...,y_k-\bar{y}$间有一个恒等式$$
\sum\limits_{i=1}^k (y_i-\bar{y}) = 0,
$$这说明在Q中独立的偏差只有k-1个。在统计学中把平方和中独立偏差个数称为该平方和的**自由度**，常记为f，如Q的自由度为$f_Q=k-1$。  
各$y_{ij}$间总的差异大小可用**总偏差平方和**$S_T$表示$$
S_T=\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\bar{y}), f_T = n-1,
$$仅由随机误差引起的数据间的差异可以用**组内偏差平方和**表示，也称为**误差偏差平方和**，记为$S_e$，即$$
S_e=\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\bar{y_{i·}}), f_e = r(m-1)=n-r.
$$由于组间差异除了随机误差外，还反映了效应间的差异，故效应不同引起的数据差异可用**组间偏差平方和**表示，也称为**因子A的偏差平方和**，记为$S_A$，即$$
S_A=m\sum\limits_{i=1}^r (\bar{y_{i·}}-\bar{y})^2, f_A = r-1.
$$

**定理**
总平方和$S_T$可以分解为因子平方和$S_A$与误差平方和$S_e$之和，其自由度也有相应分解公式，具体为$$
S_T=S_A+S_e, f_T=f_A+f_e,
$$称为**总平方和分解式**。

3. 检验方法  
偏差平方和Q的大小与数据个数（或自由度）有关，一般说来，数据越多，其偏差平方和越大。为了便于在诸偏差平方和间进行比较，统计上引入了**均方**的概念，定义为$$
MS={Q\over f_Q}，
$$其意味平均每个自由度上有多少平方和。
要对因子均方和$S_A$与误差平方和$S_e$进行比较，用其均方$$
MS_A = {S_A\over f_A}, MS_e = {S_e\over f_e}
$$进行比较更为合理，因为均方排除了自由度不同所产生的干扰。故用$$
F={MS_A\over MS_e}={S_A/f_A\over S_e/f_e}
$$作为检验$H_0$的统计量。

**定理**
在单因子方差分析模型中，有
(1)$S_e/\sigma^2\sim \chi^2(n-r)$，从而$E(S_e)=(n-r)\sigma^2$
(2)$E(S_A)=(r-1)\sigma^2+m\sum\limits_{i=1}^r a_i^2$，进一步，若$H_0$成立，则有$S_A/\sigma^2\sim \chi^2(r-1)$
(3)$S_A$与$S_e$独立。
若该定理成立，则$F={MS_A\over MS_e}={S_A/f_A\over S_e/f_e}$定义的检验统计量F服从自由度为$f_A$和$f_e$的F分布，考虑到统计量F的值越大越倾向于拒绝原假设，故该检验的拒绝域为$$
W=\{F\geq F_{1-\alpha} (f_A,f_e)\}
$$

4. 参数估计
**点估计**
由模型$W=\{F\geq F_{1-\alpha} (f_A,f_e)\}$知，诸$y_{ij}$互相独立，且$y_{ij}\sim N(\mu+a_i, \sigma^2)$，因此可使用最大似然法求出总均值$\mu$\各水平效应$a_i$和误差方差$\sigma^2$的估计。
先写出似然函数$$
L(\mu, a_1,a_2,...,a_r,\sigma^2) = \prod\limits_{i=1}^r \prod\limits_{j=1}^m \{{1\over \sqrt{2\pi \sigma^2}}exp\{-{(y_{ij}-\mu-a_i)^2\over 2\sigma^2}\}\},
$$其对数似然函数为$$
l(\mu,a_1,a_2,...,a_r,\sigma^2) = -{n\over 2}\ln(2\pi\sigma^2)-{1\over 2\sigma^2} - {1\over 2\sigma^2}\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\mu-a_i)^2,
$$求偏导，得似然方程为$$
\left \{ \begin{array}{l}
    {\partial l\over \partial \mu} = {1\over \sigma^2}\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\mu-a_i)=0,\\
    {\partial l\over \partial a_i} = {1\over \sigma^2}\sum\limits_{j=1}^m (y_{ij}-\mu-a_i) = 0, i=1,2,...,r,\\
    {\partial l\over \partial \sigma^2} = -{n\over 2\sigma^2}+{1\over 2\sigma^4}\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\mu-a_i)^2=0.
\end{array} \right.
$$考虑到约束条件$\sum\limits_{i=1}^r a_i = 0$，可求出前述各参数的最大似然估计为$$
\hat{\mu} = \bar{y},\\
\hat{a_i} = \bar{y_{i·}} - \bar{y}, i = 1,2,...,r,\\
\hat{\sigma}_M^2 = {1\over n}\sum\limits_{i=1}^r\sum\limits_{j=1}^m (y_{ij}-\bar{y_{i·}})^2 = {S_e\over n}.
$$由最大似然估计的不变性，各水平均值$\mu_i$的最大似然估计为$$
\hat{\mu_i} = \bar{y_{i·}},
$$由于$\hat{\sigma}_M^2$不是$\sigma^2$的无偏估计，实用中通常采用如下误差方差的无偏估计$$
\hat{\sigma}^2 = MS_e
$$

**置信区间**
水平均值$\mu_i$的置信区间，由上一个定理知，$\bar{y_i}\sim N(\mu_i, \sigma^2/m), S_e/\sigma^2 \sim \chi^2(f_e)$，且两者独立，故$$
{\sqrt{m}(\bar{y_{i·}}-\mu_i)\over \sqrt{S_e/f_e}}\sim t(f_e)
$$
由此给出$A_i$的水平均值$\mu_i$的$1-\alpha$置信区间为$$
[\bar{y_{i·}}\plusmn t_{1-\alpha/2}(f_e)\hat{\sigma}/\sqrt{m}]
$$
其中$\hat{\sigma}^2$为$\hat{\sigma}^2 = MS_e$

5. 重复数不等情形  
有时，每个水平下重复试验次数不全相等。这种情况下进行方差分析与重复数相等情况下的方差分析极为相似。

## 多重比较

**水平均值差的置信区间**
如果方差分析的结果是因子A显著，则等于说有充分理由认为因子A各水平的效应不全相同，但这并不是说她们中一定没有相同的。就指定的一对水平$A_i$与$A_j$，我们可通过求$\mu_i-\mu_j$的区间估计来进行比较较，方法如下：$$
\bar{y_{i·}}-\bar{y_{j·}}\sim N(\mu_i-\mu_j, ({1\over m_i}+{1\over m_j})\sigma^2),
$$而根据之前定理$S_e/\sigma^2\sim \chi^2(f_e)$，且两者独立，故$$
{(\bar{y_{i·}}-\bar{y_{j·}})-(\mu_i-\mu_j)\over \sqrt{({1\over m_i}+{1\over m_j}){S_e\over f_e}}}\sim t(f_e).
$$由此给出$\mu_i-\mu_j$的置信水平为$1-\alpha$的置信区间为$$
[\bar{y_{i·}}-\bar{y_{j·}}\plusmn \sqrt{({1\over m_i}+{1\over m_j})}\hat{\sigma}·t_{1-{\alpha\over 2}}(f_e)],
$$其中$\hat{\sigma}^2 = S_e/f_e$是$\sigma^2$的无偏估计。根据置信区间与双侧假设检验间的对应关系知，上式给出的置信区间就是两正态均值差的检验问题：$$
H_0: \mu_i-\mu_j = 0 \quad vs \quad H_1: \mu_i - \mu_j \ne 0
$$的接受域$\bar{W}$。若该置信区间含有0，则可认为$\mu_i$与$\mu_j$间无显著差异；否则认为有显著差异。
**多重比较问题**
这里遇到一个新问题，对每一组(i,j)，上述置信区间给出的置信水平都是$1-\alpha$，但对多个这样的区间，要求其同时成立，其联合置信水平就不再是$1-\alpha$了。如，设$E_1,E_2,...,E_k$是k个随机事件，且有$P(E_i)=1-\alpha, i=1,2,...,k$,则其同时发生的概率$$
P(\bigcap\limits_{i=1}^k E_i) = 1-P(\bigcup\limits_{i=1}^k \bar{E_i})\geq 1- \sum\limits_{i=1}^k P(\bar{E_i}) = 1-k\alpha,
$$说明他们同时发生的概率可能比$1-\alpha$小很多。为了使其同时发生的概率不低于$1-\alpha$，可采用多重比较来解决。  
在方差分析中，如果经过F检验拒绝原假设，表明因子A是显著的，即r个水平对应的水平均值不全相等，此时我们还需要进一步确认哪些水平均值间是确有差异的。在r(r>2)个水平均值中，同时比较任意两个水平均值间有无明显差异的问题称为**多重比较**，多重比较即要以显著性水平$\alpha$**同时**检验如下r(r-1)/2个假设：$$
H_0^{ij}： \mu_i-\mu_j, 1\leq i\lt j \leq r.
$$
直观地看，当$H_0^{ij}$成立时，$|\bar{y_{i·}}-\bar{y_{·j}}|$不应过大，过大就应拒绝$H_0^{ij}$，故在同时考察$C_r^2$个假设$H_0^{ij}$时，诸$H_0^{ij}$中至少有一个不成立就构成多重比较的拒绝域。因此，关于上述假设的拒绝域应有如下形式$$
W=\bigcup\limits_{1\leq i \lt j \leq r}\{|\bar{y_{i·}}-\bar{y_{j·}}|\geq c_{ij}\},
$$诸临界值$c_{ij}$应在假设成立的时候由$P(W)=\alpha$确定。
下面根据重复度是否相等分别介绍临界值的确定。
**重复数相等场合的T法**
...
**重复数不相等场合的S法**
...

## 方差齐性检验  

在单因子试验中r个水平的指标可以用r个正态分布$N(\mu_i,\sigma_i^2)(i=1,2,...,r)$表示，在进行方差分析时要求r个方差相等，这称为**方差齐性**，但方差齐性不一定自然具有。理论研究表明，当正态性假定不满足时，对均值相等的F检验影响较小，即F检验对正态性的偏离具有一定的稳健性，而F检验对方差齐性的偏离较为敏感，所以r个方差的齐性检验就显得十分必要。  
所谓**方差齐性检验**是对如下一对假设作出检验：$$
H_0:\sigma_1^2=\sigma_2^2=...=\sigma_r^2 \quad vs \quad H_1:诸\sigma_i^2不全相等
$$

1. 哈特利检验：仅适用于样本量相等的场合
当各水平下试验重复次数相等时，即$$
m_1=m_2=...=m_r=m,
$$哈特利提出检验方差相等的检验统计量$$
H={\max\{s_1^2,s_2^2,...,s_r^2\}\over \min\{s_1^2,s_2,...,s_r\}}
$$它是r个样本方差的最大值与最小值之比。这个统计量的分布尚无明显的表达式，但在诸方差相等条件下，可通过**随机模拟方法**获得H分布的分位数，该分布依赖于水平数r和样本方差的自由度$f=m-1$，因此该分布可记为$H(r,f)$。
直观上看，当$H_0$成立，即诸方差相等$(\sigma_1^2=\sigma_2^2=...=\sigma_r^2)$时，H的值应接近于1，H越大，诸方差的差异就越大。这是应拒绝假设中的$H_0$。由此可知，对给定的显著性水平$\alpha$，检验$H_0$的拒绝域为$$
W=\{H\geq H_{1-\alpha}(r,f)\},
$$其中$H_{1-\alpha}(r,f)$为分布的$1-\alpha$分位数。
2. 巴特利特检验：可用于样本量相等或不等的场合，但是每个样本量不得低于5
在单因子方差分析中有r个样本，设第i个样本方差为$$
s_i^2={1\over m_i-1}\sum\limits_{j=1}^{m_i}(y_{ij}-\bar{y_{i·}})^2 = {Q_i\over f_i}, i=1,2,...,r
$$其中$m_i$为第i个样本容量（即试验重复次数），$Q_i=\sum\limits_{j=1}^{m_i}(y_{ij}-\bar{y_{i·}})^2与f_i=m_i-1$为该样本的偏差平方和及自由度。由于误差均方$$
MS_e = {1\over f_e}\sum\limits_{i=1}^r Q_i = \sum\limits_{i=1}^{r} {f_i\over f_e}s_i^2,
$$它是r个样本方差$s_1^2,s_2^2,...,s_r^2$的（加权）算术平均数。而相应的r个样本方差的集合平均数记为$GMS_e$，它是$$
GMS_e = [(s_1^2)^{f_1}(s_2^2)^{f_2}···(s_r^2)^{f_r}]^{1/f_e},
$$其中$f_e=f_1+f_2+...+f_r=\sum\limits_{i=1}^r (m_i-1)=n-r$。
由于几何平均数总不会超过算术平均数，故有$$
GMS_e \leq MS_e,
$$其中等号成立当且仅当诸$s_i^2$彼此相等，若诸$s_i^2$间的差异越大，则此两个平均值相差也越大。由此可见，当诸总体方差相等时，其样本方差间不应相差较大，从而此值$MS_e/GMS_e$接近于1.反之，在比值$MS_e/GMS_e$较大时，就意味着诸样本方差差异较大，从而反映诸总体方差差异较大。这个结论对此比值的对数也成立。从而检验的拒绝域可以表示为$$
W=\{\ln(MS_e/GMS_e)\gt d\}.
$$巴特利证明了：在大样本场合，$\ln(MS_e/GMS_e)$的某个函数近似服从自由度为r-1的$\chi^2$分布。具体是$$
B={f_e\over C}(\ln MS_e-\ln GMS_e) \stackrel{·}{\sim} \chi^2 (r-1),
$$其中$$
C=1+{1\over 3(r-1)}(\sum\limits_{i=1}^r {1\over f_i}-{1\over f_e}),
$$且C通常会大于1.
根据上述结论，可取$$
B={1\over C}(f_e\ln MS_e - \sum\limits_{i=1}^rf_i\ln s_i^2)
$$作为统计检验量，对给定的显著性水平$\alpha$，检验的拒绝域为$$
W=\{B \geq \chi_{1-\alpha}^2(r-1)\}
$$由于这里的$\chi^2$分布是近似分布，使用上述检验通常要求诸样本量$m_i$均不小于5。  
3. 修正的巴特利特检验：在样本量较小或较大、相等或不等场合均可使用
针对样本量低于5时不能使用巴特利特检验的而确定，博克斯提出修正的巴特利特检验统计量$$
B'={f_2BC\over f_1(A-BC)},
$$
其中B与C如巴特利特检验所示，且$$
f_1=r-1, f_2={r+1\over (C-1)^2}, A={f_2\over 2-C+2/f_2}.
$$在原假设$H_0: \sigma_1^2=\sigma_2^2=...=\sigma_r^2$成立下，博克斯还证明了统计量$B'$的近似分布是自由度为$f_1和f_2$的F分布，对给定的显著性水平$\alpha$，该检验的拒绝域为$$
W=\{B'\geq F_{1-\alpha}(f_1,f_2)\},
$$其中$f_2$的值可能不是整数，这时可通过对F分布的分位数表施行内插法得到近似分位数。

## 一元线性回归

回归分析处理的是变量与变量间的关系。变量间常见的关系有两类：一类称为**确定性关系**，这些变量间的关系是完全确定的，可以用函数$y=f(x)$来表示，x给定后，y的值就唯一确定了。另一类称为**相关关系**，变量间有关系，但不能用函数来表示。变量间的相关关系不能用完全确定的函数形式表示，但在**平均意义下**有一定的定量关系表达式，寻找这种定量关系表达式就是**回归分析**的主要任务。  
回归分析便是研究变量间相关关系的一门学科。它通过对客观事物中变量的大量观察或试验获得的数据，去寻找隐藏在数据背后的相关关系，给出它们的表达形式——**回归函数的估计**。  
**一元线性回归模型**
设y与x间有相关关系，称x为**自变量**，y为**因变量**，在知道x取值后，y的取值并不是确定的，它是一个随机变量，因此有一个分布，这个分布是在知道x的取值后Y的条件密度函数$p(y|x)$。我们关心的是y的均值$E(Y|x)$，它是x的函数，这个函数是确定性的：$$
f(x)=E(Y|x)=\int_{-\infty}^\infty yp(y|x)dy.
$$这便是y关于x的回归函数——条件期望，也就是我们要寻找的相关关系的表达式。  
除了x与y均为随机变量这类回归问题，还有第二类回归问题，其自变量x是可控变量，只有y 是随机变量，它们之间的相关关系可用下式表示：$$
y=f(x)_\epsilon,
$$其中$\epsilon$是随机误差，一般假设$\epsilon\sim N(0,\sigma^2)$。由于$\epsilon$的随机性，导致y是随机变量。这里研究第二类回归问题。  
设线性相关关系$y=\beta_0+\beta_1x+\epsilon$是与关于x的一元线性回归的数据结构式。这里总假定x为一般变量，是非**随机变量**，其值可以精确测量或严格控制，$\beta_0,\beta_1$为未知参数，$\beta_1$是直线的斜率，表示x每增加一个单位引起$E(y)$的增加量。$\epsilon$是随机误差，通常假定$$
E(\epsilon)=0, Var(\epsilon)=\sigma^2,
$$在对未知参数作区间估计或假设检验时，还需要假定误差服从正态分布，即$$
y\sim N(\beta_0+\beta_1x, \sigma^2).
$$由于$\beta_0,\beta_1$均未知，需要从收集到的数据$(x_i,y_i)(i=1,2,...,n)$出发进行估计。在收集数据时，一般要求观测独立地进行，即假定$y_1,y_2,...,y_n$相互独立。综合上述假定，可以给出最简单、最常用的一元线性回归的统计模型：$$
\left \{ \begin{array}{l}
    y_i = \beta_0 + \beta_1x_i + \epsilon_i, i= 1,2,...,n,\\
    各\epsilon_i独立同分布，其分布为N(0,\sigma^2)
\end{array} \right.
$$由数据$(x_i,y_i)(i=1,2,...,n)$可以获得$\beta_0,\beta_1$的估计$\hat{\beta_0},\hat{\beta_1}$，称$$
\hat{y} = \hat{\beta_0}+\hat{\beta_1}x
$$为y关于x的**经验回归函数**，简称**回归方程**，其图形称为**回归直线**。给定$x=x_0$后，称$\hat{y} = \hat{\beta_0}+\hat{\beta_1}x_0$为**回归值或拟合值、预测值**。

**回归系数的最小二乘估计**
一般采用最小二乘方法估计回归方程中的$\beta_0,\beta_1$。令$$
Q(\beta_0,\beta_1) = \sum\limits_{i=1}^n (y_i-\beta_0-\beta_1x_i)^2,
$$
$\hat{\beta_0},\hat{\beta_1}$应该满足$$
Q(\hat{\beta_0},\hat{\beta_1})=\min\limits_{\beta_0,\beta_1} Q(\beta_0, \beta_1),
$$这样得到的$\hat{\beta_0},\hat{\beta_1}$称为$\beta_0,\beta_1$的**最小二乘估计**，记为LSE。  
由于$Q\geq 0$，且对$\beta_0,\beta_1$的导数存在，因此最小二乘估计可以通过求偏导数并命其为0而得到$$
\left \{ \begin{array}{l}
    {\partial Q\over \partial \beta_0} = -2\sum\limits_{i=1}^n (y_i-\beta_0-\beta_1x_i) = 0,\\
    {\partial Q\over \partial \beta_1} = -2\sum\limits_{i=1}^n (y_i-\beta_0-\beta_1x_i)x_i = 0.
\end{array} \right.
$$这组方程称为**正规方程组**，经过整理，可得$$
\left \{ \begin{array}{l}
n\beta_0+n\bar{x}\beta_1 = n\bar{y},\\
n\bar{x}\beta_0+\sum x_i^2\beta_1 = \sum x_iy_i,
\end{array} \right.
$$记$$
\bar{x} = {1\over n}\sum x_i, \bar{y} ={1\over n}\sum y_i,\\
l_{xy} = \sum (x_i-\bar{x})(y_i-\bar{y}) = \sum x_iy_i-n\bar{x}·\bar{y} = \sum x_iy_i-{1\over n}\sum x_i\sum y_i,\\
l_{xy} = \sum (x_i-\bar{x})^2 = \sum x_i^2 - n\bar{x}^2 = \sum x_i^2 - {1\over n}(\sum x_i)^2,\\
l_{xy} = \sum (y_i-\bar{y})^2 = \sum y_i^2 -n\bar{y}^2 = \sum y_i^2 - {1\over n}(\sum y_i)^2
$$解得$$
\left \{ \begin{array}{l}
\bar{\beta_1}={l_{xy}\over l_{xx}},\\
\bar{\beta_0} = \bar{y}-\hat{\beta_1}\bar{x},
\end{array} \right.
$$这就是参数的最小二乘估计。

**定理**
在模型$y_i = \beta_0 + \beta_1x_i + \epsilon_i, i= 1,2,...,n, $各$\epsilon_i$独立同分布，其分布为$N(0,\sigma^2)$下，有：
(1) $\hat{\beta_0}\sim N(\beta_0, ({1\over n}+{\bar{x}^2\over l_{xx}})\sigma^2), \hat{\beta_1}\sim N(\beta_1, {\sigma^2\over l_{xx}})$
(2) $Cov(\hat{\beta_0},\hat{\beta_1}) = -{\hat{x}\over l_P{xx}}\sigma^2$
(3) 对给定的$x_0,\hat{y_0}=\hat{\beta_0}+\hat{\beta_1}x_0\sim N(\beta_0+\beta_1x_0, ({1\over n}+{(x_0-\bar{x})^2\over l_{xx}})\sigma^2)$
该定理说明：

1. $\hat{\beta_0},\hat{\beta_1}$分别是$\beta_0,\beta_1$的无偏估计
2. $\hat{y_0}$是$E(y_0)=\beta_0+\beta_1x_0$的无偏估计
3. 除$\bar{x}=0$外，$\hat{\beta_0}和\hat{\beta_1}$是相关的
4. 要提高$\hat{\beta_0},\hat{\beta_1}$的估计精度（即降低他们的方差）就要求n大，$l_{xx}$大（即要求$x_1,x_2,...,x_n$较分散）

**回归方程的显著性检验**
建立回归方程的目的是寻找**y的均值随x变化**的规律，即找出回归方程$E(y)=\beta_0+\beta_1x$。如果$\beta_1=0$，那么不管x如何变化，E(y)不随x的变化作线性变化，那么这时求得的一元线性回归方程就没有意义，或称回归方程**不显著**。如果$\beta_1\neq 0$，那么当x变化时，E(y)随x的变化作线性变化，那么这时求得的回归方程就有意义，或称回归方程是**显著**的。  
对回归方程是否有意义作判断就是要对如下的检验问题作出判断：$$
H_0: \beta_1 = 0 \quad vs \quad H_1: \beta_1 \neq 0,
$$
拒绝$H_0$表示回归方程是显著的。  
在一元线性回归中有三种等价的检验方法：

1. F检验
采用方差分析的思想，从数据出发研究各$y_i$不同的原因。称$\hat{y_i}=\hat{\beta_0}+\hat{\beta_1}x_i$为$x_i$处的**回归值**，又称$y_i-\hat{y_i}$为$x_i$处的**残差**。
根据总的波动用**总偏差平方和**$$
S_T = \sum (y_i-\bar{y})^2 = l_{xx}
$$表示。引起各$y_i$不同的原因主要有两类因素：其一是$H_0$可能不真，即$\beta_1\neq 0$，从而$E(y)=\beta_0+\beta_1 x$随x的变化而变化，即在每一个x的观测值处的回归值不同，其波动用**回归平方和**$$
S_R = \sum (\hat{y}-\bar{y})^2
$$表示。其二是其他一切因素，包括随机误差、x对E(y)的非线性影响等，这样在得到回归值以后，y的观测值与回归值之间还有差距，这可用**残差平方和**$$
S_e = \sum (y_i - \hat{y_i})^2
$$表示。  
为对上述诸平方和实施方差分析，要证明重要的平方和分解式。注意到$\hat{\beta_0},\hat{\beta_1}$满足正规方程组，因此$$
\sum (y_i-\hat{\beta_0}-\hat{\beta_1}x_i) = 0 \Rightarrow \sum (y_i-\hat{y_i}) = 0, \\
\sum (y_i-\hat{\beta_0}-\hat{\beta_1}x_i)x_i = 0 \Rightarrow \sum (y_i-\hat{y_i})x_i = 0.
$$利用$\hat{y_i} = \hat{\beta_0}+\hat{\beta_1}x_i = \bar{y}+\hat{\beta_1}(x_i-\bar{x})$，可得$$
\sum (y_i-\hat{y_i})(\hat{y_i}-\bar{y}) = \sum [y_i-\hat{y_i}](\hat{\beta_1}(x_i-\bar{x})) = \hat{\beta_1}[\sum (y_i-\hat{y_i})x_i - \sum (y_i-\hat{y_i})\bar{x}] = 0,
$$从而$$
S_r = \sum (y_i-\bar{y})^2 = \sum (y_i - \hat{y_i}+\hat{y_i}-\bar{y})^2 = \sum  (y_i-\bar{y_i})^2 +\sum  (\hat{y_i}-\bar{y})^2,  
$$即$$
S_T = S_R + S_e,
$$上式就是一元线性回归场合下的**平方和分解式**。

**定理**
设$y_i = \beta_0 + \beta_1x_i + \epsilon_i$，其中$\epsilon_1,\epsilon_2,...,\epsilon_n$相互独立，且$$
E(\epsilon_i) = 0, Var(\epsilon_i)= \sigma^2, i=1,2,...,n,
$$有$$
E(S_R) = \sigma^2 + \beta_1^2l_{xx},\\
E(S_e) = (n-2)\sigma^2,
$$上式说明$\hat{\sigma}^2=S_e/(n-2)$是$\sigma^2$的无偏估计。

有关$S_R和S_e$的分布，有如下定理
**定理**
设$y_1,y_2,...,y_n$相互独立，且$y_i\sim N(\beta_0+\beta_1x_i, \sigma^2), i=1,2,...,n$，则有
1. $S_e/\sigma^2 \sim \chi^2(n-2)$\\
2. 若$H_0$成立，则有$S_R/\sigma^2\sim \chi^2(1)$\\
3. $S_R$与$S_e$，$\bar{y}$独立（或$\hat{\beta_1}$与$S_e,\bar{y}$独立）

2. t检验
对$H_0:\beta_1=0$的检验也可基于t分布进行。由于$\hat{\beta_1}\sim N(\beta_1, {\sigma^2\over l_{xx}}), {S_e\over \sigma^2}\sim \chi^2(n-2)$，且与$\hat{\beta_1}$相互独立，因此在$H_0$为真时，有$$
t = {\hat{\beta_1}\over \hat{\sigma/\sqrt{l_{xx}}}} \sim t(n-2),
$$其中$\hat{\sigma} = \sqrt{S_e/(n-2)}$，由于$\sigma_{\hat{\beta_1}} = {\sigma\over \sqrt{l_{xx}}}$，因此称$\sigma_{\hat{\beta_1}} = {\sigma\over \sqrt{l_{xx}}}$为$\hat{beta_1}$的标准误，即$\hat{beta_1}$的标准差的估计。t统计量可用来检验假设$H_0$。对给定的显著性水平$\alpha$，拒绝域为$$
W=\{|t|\gt t_{1-\alpha/2}(n-2)\}.
$$注意$t^2=F$，因此t检验与F检验是等同的。

3. 相关系数检验
考察一元线性回归方程能否反映两个随机变量x与y间的线性相关关系时，它的显著性检验还可通过对二维总体相关系数$\rho$的检验进行。它的一对假设是$$
H_0: \rho = 0 \quad vs \quad H_1: \rho \neq 0.
$$
所用的检验统计量为样本相关系数$$
r = {\sum (x_i-\bar{x})(y_i-\bar{y})\over \sqrt{\sum (x_i-\bar{x})^2(y_i-\bar{y})^2}}={l_{xy}\over \sqrt{l_{xx}l_{yy}}}
$$其中$(x_i, y_i)(i= 1,2,...,n)$是容量为n的二维样本。
根据样本相关系数有关性质，检验中原假设$H_0: \rho = 0$的拒绝域为$W= \{|r|\geq c\}$，其中临界值c可由$H_0:\rho = 0$成立时，样本相关系数的分布定出，该分布与自由度n-2有关。  
对给定的显著性水平$\alpha$，由$P(W)=P(|r|\geq c)=\alpha$知，临界值c应是$H_0: \rho = 0$成立下$|r|$的分布的$1-\alpha$分位数，故可记为$c=r_{1-\alpha}(n-2)$。可用F分布来确定临界值c。  
由样本相关系数的定义可以得到统计量r与F之间的关系$$
r^2 = {l_{xy}^2\over l_{xx}l_{yy}} = {S_R/S_T} = {S_R\over S_R+S_e} = {S_R/S_e\over S_R/S_e+1},
$$而$$
F={MS_R\over MS_e} = {S_R\over S_e/(n-2)}= {(n-2)S_R\over S_e}
$$两者综合，可得$$
r^2 = {F\over F+(n-2)}
$$这表明，|r|是F的严格单调增函数，故可以从F分布的$1-\alpha$分位数$F_{1-\alpha}(1,n-2)$得到|r|的$1-\alpha$分位数为$$
c=r_{1-\alpha}(n-2)=\sqrt{F_{1-\alpha}(1,n-2)\over F_{1-\alpha}(1,n-2)+n-2}
$$

> 上述三个检验在考察一元线性回归时是等价的，但在多元线性回归场合，经推广F检验仍可用，另外两个就无法使用了。

4. 估计与预测
当回归方程经过检验是显著的后，可用来作估计和预测。这是两个不同的问题：

- 当$x=x_0$时，寻求均值$E(y_0)=\beta_0+\beta_1x_0$的点估计与区间估计（注意这里的$E(y_0)$是常量），这是**估计问题**。
- 当$x=x_0$时，$y_0$的观测值在什么范围内？由于$y_0$是随机变量，一般只求一个区间，使$y_0$落在一区间的概率为$1-\alpha$，即要求$\delta$，使$P(|y_0-\hat{y_0}|\leq \delta) = 1-\alpha$，称区间$[\hat{y_0}-\delta, \hat{y_0}+\delta]$为$y_0$的概率为$1-\alpha$的预测区间，这是**预测问题**。

**$E(y_0)$的估计**
在$x=x_0$时，其对应的因变量$y_0$是一个随机变量，有一个分布。我们经常需要对该分布的均值给出估计。该分部的均值$E(y_0)=\beta_0+\beta_1x_0$，因此一个直观的估计应为$$
\hat{E}(y_0) = \hat{\beta_0}+\hat{\beta_1}x_0
$$这个估计简记为$\hat{y_0}$，由于$\hat{\beta_0},\hat{\beta_1}$分别是$\beta_0, \beta_1$的无偏估计，因此$\hat{y_0}$也是$E(y_0)$的无偏估计。
为得到$E(y_0)$的区间估计，需要知道$\hat{y_0}$的分布。由最小二乘估计性质定理得$$
\hat{y_0} = \hat{\beta_0}+\hat{\beta_1}x_0 \sim N(\beta_0+\beta_1x_0, ({1\over n}+{(x_0-\bar{x})^2\over l_{xx}})\sigma^2),
$$由方差和分解定理知，$S_e/\sigma^2\sim \chi^2(n-2)$，且与$\hat{y_0}=\bar{y} + \hat{\beta_1}(x_0-\bar{x})$相互独立，记$$
\hat{\sigma}^2 = {S_e\over n-2},
$$则$$
{(\hat{y_0}-E(y_0))/\sqrt{{1\over n}+{(x_0-\bar{x})^2}\sigma}\over \sqrt{{S_e\over \sigma^2}/(n-2)}}={\hat{y_0}-E(y_0)\over \hat{\sigma}\sqrt{{1\over n}+{(x_0+\bar{x})^2\over l_{xx}}}}\sim t(n-2).
$$于是$E(y_0)$的$1-\alpha$的置信区间是$$
[\hat{y_0}-\delta_0, \hat{y_0}+\delta_0]
$$其中$$
\delta_0 = t_{1-\alpha/2}(n-2)\hat{\sigma}\sqrt{{1\over n}+{(x_0-\bar{x})^2\over l_{xx}}}
$$

**$y_0$的预测区间**
对于$y_0 = E(y_0)+\epsilon$，由于通常假定$\epsilon\sim N(0,\sigma^2)$，因此$y_0$的最可能取值仍然为$\hat{y_0}$，于是可以使用以$\hat{y_0}$为中心的一个区间$$
[\hat{y_0}-\delta, \hat{y_0}+\delta]
$$作为$y_0$的取值范围，为确定$\delta$的值，需要如下的结果：由于$y_0$与$\hat{y_0}$独立，故$$
y_0-\hat{y_0}\sim N(0,(1+{1\over n}+{(x_0-\bar{x})^2\over l_{xx}})\sigma^2).
$$因此有$$
{y_0-\hat{y_0}\over \hat{\sigma}\sqrt{1+{1\over n}+{(x_0-\bar{x})^2\over l_{xx}}}}\sim t(n-2),
$$上述预测区间与$E(y_0)$的置信区间的差别就在于根号里多个1，这个差别导致预测区间要比置信区间宽很多。

## 一元非线性回归

有时回归函数并非是自变量的线性函数，若通过变换可以将之化为线性函数，从而可用一元线性回归方法对其分析，这是**处理非线性问题**的一种常用方法。  
首先描出数据的散点图，判断两个变量之间可能的函数关系。  
对非线性函数，参数估计最常用的方法是“线性化”方法，即通过某种变换，将方程化为一元线性方程的形式。  
**曲线回归方程的比较**
通常采用如下两个指标进行曲线方程选择：

1. 决定系数$R^2$。类似于一元线性回归方程中相关系数，**决定系数**定义为$$
R^2 = 1- {\sum (y_i-\hat{y_i})^2\over \sum (y_i-\bar{y})^2}
$$$R^2$越大，说明残差越小，回归曲线拟合越好，$R^2$从总体上给出一个拟合好坏程度的度量。
2. 剩余标准差s。类似于一元线性回归中标准差的估计公式，此剩余标准差可用平均残差平方和来获得，即$$
s=\sqrt{\sum (y_i = \hat{y_i})^2\over n-2}
$$s为诸观测点$y_i$与由曲线给出的拟合值$\hat{y_i}$间的平均偏离程度的度量，s越小，方程越好。  
在观测数据给定后，不同的曲线选择不会影响$\sum\limits_{i=1}^n (y_i-\bar{y})^2$的取值，但会影响到残差平方和$\sum\limits_{i=1}^n (y_i-\bar{y_i})^2$的取值。因此，对选择的曲线而言，决定系数和剩余标准差都取决于残差平方和，从而两种选择准则是一致的，只是从两个不同侧面作出评价。
