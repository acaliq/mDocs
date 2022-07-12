概率论与数理统计
> 统计学知识的掌握程度决定着数据分析能力的上限
# Introduction to Statistics and Econometrics
> by Yongmiao Hong

- 微分积分其实就是求最优解
- 线性代数最重要的是在计量经济学里面
- 概率论与数理统计是经济统计方法的理论基础

## General methodology of modern economic research
1. Data collection and summary of empirical stylized facts
   > The so-called stylized facts are often summerized from obsered economic data. For example, Engel Curve(恩格尔曲线), Phillips Curve（菲利普斯曲线）, volatility clustering in finance. 揭示的并非经济规律，而是经济现象。
   > The empirical stylized facts serves as a starting point for economic research. 问题导向
   1. surveys
   2. field studies
   3. experimental economics
   4. Big data

2. Development of Economic Theories/Models
   1. With the empirical stylized facts in mind, economists then develop  an economic theory for model.
   2. This usually calls for specifying an mathematical model of economic theory.
   3. An example is the Euler equation for rational expectations in macroeconomics.
   4. The objective of economic modeling is not merely to explain the stylized facts, but also to understand the economic mechanism.

3. Empirical validation/inference of economic models
   1. A key is to transform **an economic model** into **a testable empirical econometric model**.
      1. 经济模型就是经济理论的数学化。计量模型可用数据进行检验。计量经济学为经济模型及其参数的检验提供方法和手段。 
   2. One often has to assume some functional form, up to some unkown model parameters, or to choose suitable instrumental variables to form a set of moment conditions.
   3. One needs to estimate unkown model parameters and make inferences based on observed data.
   4. Check whether the econometric model is adequate. An adequate model should be at least consistent with the empirical stylized facts.

4. Application
   > After an econometric model passes the empirical evaluation, it can then be used to :
   1. Explain importan empitical stylized facts
   2. Test economic theory and/or hypotheses
   3. Forecast future evolution of the economy
   4. Policy evaluation and other applications

## Roles of Econometrics
- Fundamental Axioms of Econometrics

Modern econometrics is essentially built upon the followingfundamental axsoms:
- Any economy can be viewed as a stochastic process governed by some probability law.
- Economic phenomenon, often summerized in form of data, can be reviewed as a reaization of this stochastic data generatiing process (DGP). 
- Tools and methods of probability and statistics will provide operating principles for econometrics.  For example, model specification （模型设定）, parameter estimation, hypothesis testing, model validation.
- Econometrics is not a simple application of general theory of mathmatical statistics to economic data.
- Among other things, econometrics can play the following roles in economics:
  - Examine how well an economic theory can explain historical economic data (partically the important stylized facts)
  - Test validaty of economic theories and economic hypotheses.

## Illustrative Examples
Example 1: Keynesian Model, Multiplier and Policy Recommendation
$
\left \{ \begin{array} {c} Y_t = C_t + I_t + G_t \\C_t = \alpha + \beta Y_t + \epsilon_t \end{array} \right.$
> 该例中需要估计边际消费倾向$\beta$

where:
1. $Y_t$ is aggregate income,
2. $C_t$ is private consumption, 
3. $I_t$ is private investment,
4. $G_t$ is governement spending,
5. $\epsilon$ is consumption shock

Example 2: Rational Expectations and Dynamic Asset Pricing Models
Suppose a representative agent has a constant relative risk aversion utility $U = \sum\limits_{t=0}^n\beta^tu(C_t)=\sum\limits_{t=0}^n\beta^t{{C_t^\gamma-1}\over \gamma}$
> 该例中需要估计理性人折现因子$\beta$

where:
1. $\beta \gt 0$ is the agent's time discount factor,
2. $\gamma \geq 0$ is the risk aversion parameter,
3. $\mu (·)$ is the agent's utility function in each time period,
4. $C_t$ is consumption during period t.

The FOC (first order condition) is usually called **the Euler Equation** of the economic system.

Example 3: Production Function and Hypothesis on Constant Return to Scale
Production function: $Y_i = exp(\epsilon_i)F(L_i, K_i)$
> 该例要检验规模报酬收益率
where:
1. $Y_i = $ output of firm i,
1. $L_i = $ labor of firm i,
1. $K_i = $ capital of firm i,
1. $\epsilon_i$ is a shock (e.g., uncertain weather condition if $Y_i$ is an agriculural product) 

- 我们应该了解每一个理论、工具、方法成立的前提条件。

Example 4: Effect of Economic Reforms on Transitional Economy
Extended Cobb-Dauglas production function (after taking a logarithmic operation)
$lnY_{it} = lnA_{it} + \alpha lnL_{it} + \beta lnK_{it} + \gamma Bonus_{it} + \delta Contract_{it} + \epsilon_{it}$,

Where:
1. i is the index for firm $i \in \{1,...,N\}$ and t is the index for year $r \in \{i,...,T\}$,
1. $Bonus_{it}$ is proportion of bonus out of total wage bill, 
1. $Contract_{it}$  is proportion of workers who have signed a fixed-term contract.

Example 5: Efficient Market Hypothesis (EMH) and Predictability of Financial Returns
Weak form of efficient market hypothesis (EMH): It is impossible to predict future stock returns using the history of past stock returns: $E(Y_t|I_{t-1}) = E(Y_{t})$,
Where:
$Y_t$ = asset return at time t,
$I_{t-1} = \{Y_{t-1},...Y_1\}$ is the information set at time t-1.

Example 6: Volatility Clustering and ARCH Models
Volatility is a key instrument for measuring uncertianty and risk in finance. This concept is important to investigate information flows and votatility spillover, financial contagions between financial markets, options pricing, and calculation of Value at Risk.
Volatility can be measured by the conditional variance of asset return $Y_t$ given the information $I_{t-1}$: $\sigma_t^2 \equiv var(Y_t|I_{t-1})$.
A popular votatility model is the AutoRegressive Conditional Hereroskedasticity (AECH) model, originally proposed by Engel (1982). 自回归条件异方差模型

- 知道分布假设错了，为什么还要用？因为我想估计未知数。错了估计还能准吗？挺准的。统计学上叫一致估计，但是估计出来的方差较大。

## Roles of Probability and Statistics
Econometrics is an integration of statistical modeling and inferences of economic observational data with economic theory.
- The object of econometrics is to  infer laws of economic motions of a stochastic economy.
- Theory, methods and tools of econometrics are mathematical statistics in combination with economic theory.
 - Probability theory provides operating rules and understanding of mathmatical statistics.
 - In fact, as perhaps the best mathmatical tool to describe analytic tools for macroeconomics, microeconomics and finance.
 - Probability and statistics together provide a foundation for econometrics. In particular, they provides the concepts, tools and methods of mathmatical statistics which are needed  to understand econometrics.
 Modern Statistics usually:
 - assumes that a mathmatical probability model generates an observed data.
 - assumes that the probability model often contains some unknown parameters.
 - based on the observed data, develop methods to estimate unknown parameters and statistical hypotheses.

# Foundation of Probability Theory

## Random Experiments
Recall fundamental axioms of econometrics:
- Axiom A: An economic system can be viewed as a random experiment governed by some probability law.
- Axiom B: any economic phenomenon (often in form of data) can be viewed as an out-come of this random experiment. The random experiment is called a "data generating process".

Definition 1: **random experiment** 
- A random experiment is a mechanism which has at least two possible outcomes.
- When a random experiment is performed, one and only one outcome will occur, but which outcome to occur is unknown in advance.
- There are two essential elements of a random experiment: 
  - The set of all possible outcomes;
  - The likelihood with which each outcome wil occur.
Definition 2: **sample space**
The possible outcomes of a random experiment are called "basic outcomes", and the set of all basic outcomes constitutes "the sample space", which is denoted by S.
- A sample space S can be countable and uncountable.
- The distinction between a countable sample space and an uncountable sample space dictates the ways in which probabilities will be assigned.
  
Definiton 3: **event**
An event A is a collection of basic outcomes from the sample space S that share certain common features or equivalently obey certain restrictions.
- Conceptually speaking, an event is equivalent to a set.

## Review of Set Theory 
Definition 4: **intersection**
Intersection of A and B, denoted A$\cap$B, is the set of basic outcomes in S that belong to both A and B.

Definition 5: **exclusiveness**
If A and B have no common basic outcomes, they are called mutually exclusive and their intersection is empty set $\empty$, i.e., A$\cap$B = $\empty$, where $\empty$ denotes an empty set that contains nothing.

Definition 6: **Union**
The union of A and B, A$\cup$B, is the set of all basic outcomes in S that belongs to A or B.

Definition 7: **collective exhaustiveness**
Suppose $A_1,A_2,...,A_n$ are $n$ events in the sample space S, where $n$ is any positive integer.
If $\cup_{i=1}^n A_i=S$, then these $n$ events are said to be collevtively exhaustive.

Definition 8: **complement**
The complemenet of A is the set of basic outcomes of a random experiment belongs to S but not to A, denoted as $A^c$.

Definition 9: **Difference**
The difference of A and B, denoted as A - B = $A\cap B^c$, is the set of basic outcomes in S that belong to A but not to B.

Theorem 1: **laws of sets operations**
For any three events A, B, C defined on a sample space S;
- Complementation:
$
(A^c)^c = A \\
\empty ^c = S \\ 
S^c = \empty
$
- Commutativity of union and intersection:
$
A\cup B = B\cup A\\
A\cap B = B\cap A
$
- Associativity of union and intersection:
$
(A\cup B)\cup C = A\cup (B\cup C)\\
(A\cap B)\cap C = A\cap (B\cap C)
$
- Distributivity laws
$
A\cap (B\cup C) = (A\cap B)\cup (A\cap C)\\
A\cup (B\cap C) = (A\cup B)\cap (A\cup C)\\
$
- De Morgan's laws
$
(A\cup B)^c = A^c\cap B^c\\
(A\cap B)^c = A^c\cup B^c
$

- 线性代数的投影projection就是这里的intersection。这里的基本思想是，任何一个event，都可以投影到basis上面去。

## Fundamental Probability Laws
Motivation:
To assign a probability to an event A in S, we shall introduce a probability function, which is a function or a mapping from an event to a real number.

- 计量经济学的任务就是找出真是的概率函数
- 概率的假设建立在独立同分布假设之上
- 概率空间是描述随机试验最好的方法

## Methods of Counting


## Conditional Probability
- 这概念非常重要
- 单单概率论和统计学无法告诉我们因果关系。需要经济理论来推断因果关系。

## Bayes's Theorem
- 贝叶斯定理是条件概率一个特别重要的应用，特别是在机器学习领域。

- 贝叶斯定理代表，利用新到的信息B，更新我感性的概率A。


## Independence
- 独立表示事件B对事件A没有任何预测效力

## Conclusion
- 概率空间$(S, \Bbb B, P)$可以完全描述一个随机试验。对于给定的$S, \Bbb B$可以定义很多的概率函数P。计量经济学就是用观测数据找出随机试验的唯一真实概率函数。
- 统计关系的本质是一种预测关系，不是因果关系。
- independent和不相关是不同概念。

# Random Variables and Univariate Probability Distributions

## Random Variables
- 随机变量其实是个映射到实数轴的函数
- 新的随机变量概率函数推导自原始概率函数
- 引入随机变量最重要的理由，是为了使用数学工具

## Cumulative Distribution Function 
- 

## Discrete Random Variables (DRV)
- 重要的是，除了数学公式以来，这些数学关系背后的经济含义是什么

## Continuous Random Variables
- 为什么要研究连续随机变量？因为这可以让我们应用微积分。
- 连续型随机变量可以被视为离散型随机变量的逼近。

## Functions of a Random Variable
- 有时候我们对随机变量X并不感兴趣，而是对随机变量的函数F(X)感兴趣
- 假设严格单调递增函数，是因为它存在逆函数
- 直觉在数学中起到非常重要的作用，抽象的数学要用直观的图标、经济学例子来理解

## Mathematical Expectations
- 定义数学期望就是为了导出矩


## Moments
- 矩，是个物理概念。经济学和物理学是相通的
- 均值就是期望回报，方差就是风险程度
- 任何一个现代金融理论，都是用概率语言来表述的
- 概率论和统计学在做工具上的储备，经济学家和金融学家则使用这些工具来创造新的模型
- 经济金融数据一般为什么都不服从正态分布？因为计算获得的峰度通常大于等于3

## Quantile
> 这玩意儿有什么重要的？

- 中产阶级的定义:收入范围在 $[{2\over 3}median, 2median]$之间
- 模型风险：现在很多商业决策都根据模型算出来。

##    Moment Generating Function (MGF)
- 记不住的公式就不要去记，要懂得基本原理，知道怎么推导
- 中心极限定理是MGF的一个应用
- 随机变量的概率分布和MGF是一一对应的

## Characteristic Function
- MGF有很多有点，但它对很多分布不存在
- 对所有的函数，特征函数都存在
- 傅里叶变换代表同样一件事可以有两种表达方式，一是space domain，二是frequency domain。
- MGF是拉普拉斯变换，CFT是傅里叶变换
- 书不要读太多，关键是读透读精

## Conclusion
- 第三章将第二章内容数学化

# Important Probability Distribution
## Distrete Probability Distribution
- Bernoulli Distribution
  - It's a binary random variable distribution
  - 一个参数p就可以刻画整个分布
  - 用于利率跳跃模型，美国经济周期非对称性的检验等

- Binomial Distribution
  - 用于质量控制，利率调整测试估计等

- Negative Binomial Distribution


- Poisson Distribution
  - 刻画很多小概率事件，加总在一起会产生显著影响。
  - Poisson distribution的产生，源自binomial distribution应用广但难计算的难题
  - 均值和方差都等于$\lambda$
  - Binomial distribution在n趋于无穷大时，它的矩产生函数趋于Poisson distribution的矩产生函数。
  - 上述命题被称小数定理（LSN）。有人称LSN是离散世界的中心极限定理。
  - 可用于对地震发生次数建模，士兵被马蹄踢到的人数，客服电话接收次数，收银员人数，股票价格跳跃的次数等。

# Continuous Probability Distribution
## Uniform Distribution
- 均匀分布在统计学、计量经济学应用广泛，很重要
## Beta Distribution
- 均匀分布是Beta分布的一个特例

## Normal Distribution
- 概率论中最重要的分布，因为中心极限定理
## Cauchy Distribution and   Stable Distribution
- Tail趋于零的速度特别慢
- 每个阶的moment都不存在
- 日常生活中没什么用
- stable distribution有两个特例，一是正态分布，二是可惜分布

## Lognormal Distribution
- 对该随机变量取对数以后，就成了正态分布
- GDP、Income都被认为服从log正态分布

## Gama and Generalized Gama Distribution
- 两个参数，一个决定形状，一个决定规模
- Gama函数可以描述失业时间

## Chi-Square Distribution
- 重要性和正态分布相当
- 很多统计检验都是Chi-Square

## Exponential and Weibull Distribution
- Exponential distribution 是Gama distribution的一个特例
- Weibull distribution比exponential distribution更灵活更一般

## Double Exponential Distribution


## Conclusion
- 学习上面分布，特别注意每个参数的含义，这个非常重要
- 其次，各个分布之间的关系要搞清楚
- 第三章第四章是对应的，后者引入了数学工具而已

# Multivariate Probability Distributions
## Random Vectors and Joint Probability Distributions
- 通货膨胀率和失业率是各国央行优先控制的目标
- 为什么用向量来研究多个随机变量？因为这样不会漏掉随机变量之间的关系
- 连续的联合分布函数$F_{xy}$就是离散的$P(A\capB)$
- $F_{xy}$中，X和Y之间的关系是我们的重点
- The copula用于刻画股市之间的互相影响

## The Discrete Case

## The Continuous Case

## Marginal Distribution
- 奥地利学派的边际革命，就是为了在经济学引进微积分
- 互相独立，就是不存在统计关系

## Conditional Distributions
- 条件分布其实定义了一种预测关系
- 为什么我们总是把离散和连续分开，并且先讲离散？因为离散很简单和直观，方便理解
- 条件概率用来干嘛？刻画市场分别熊市和牛市时，资产回报率的分布；研究劳动力市场，男女员工各自的工资报酬分布。
- $f_{y|x}(y|x)=f(x,y)\over f_x(x)$ 与$P(A\cap B)\over P(B)$相对应。之所以引入随机变量，就是使之数字化，进而数学化，最后引入数学工具进行定量的分析。

## Independence
- 我们在这里做的，只是使第二章内容可检验、可操作
- 如果X和Y互相独立，那么事件X是否出现的信息对于预测Y是否会出现就没有作用
- 变量之间互相独立，一定要每一个和其他任何一个独立，然后它们之间的任何**组合**都独立，仅仅前者尚不足以保证变量之间的独立性。

## Bivariate Transformation
- Factor Model指的是，要解释的变量特别多。它们受到少量共同因子的影响。通过将前者表示为后者的组合，可以减少变量个数，进行降维。比如，欧元日元汇率、需求供给的关系研究等。
- 有一个学习的好方法是，缺什么补什么；而不是把所有数学都学好了，然后再来解决问题。数学里面学得90%，可能都用不到。
- Multivariate transformation需要变量间的映射一一对应，否则不成立。但是，可以把定义域化成多块，使得每一块上变量间一一对应，进而使用Jacobian Matrix进行变换。
- 看到一个例题，不要就去做计算，要看看这道题想说明什么问题。

## Bivariate Normal Tranformation
- 如果X, Y服从一个联合二元正态分布，那么X, Y分别服从正态分布，X, Y的条件分布服从正态分布，$\rho$刻画了X, Y之间的相关关系。当$\rho$等于0时，X和Y相互独立。
- 两个正态分布变量X, Y组成的联合分布，不一定是联合正态分布

## Expectations and Covariance
- 我（Hong）对Covariance理解比较深刻
- 减掉Mean了，就叫Central。比如，X-E(X)
- $Covriance(X, Y) = E((X-\mu_x)(Y = \mu_y))$测度的是两个变量变化方向的一致程度
- Cov(X, X) = Var(X)
- $\rho_{xy} = {cov(x, y)\over \sigma_x \sigma_y}$
- 期望就是要把目标值（/函数）乘以质量（/密度）函数，即求平均
- 线性关系的$\rho$要么1，要么-1。以此观之，$\rho$测度的是两个变量之间的线性相关关系。
- 线性分析就是协方差covariance分析，就是在分析X, Y的相关性
- 独立/不独立 关系是一种比线性关系更丰富更复杂的关系，他包含线性关系，但不止于线性关系。Correlation测度的只是线性关系。比如，满足$Y = X^2$关系的变量X和Y，Cov(x, y) = 0.

## Joint Moment Generating Function

## Implications of Independence on Expectations
- 独立，意味着不仅线性关系不存在，任何非线性关系也不存在
- 今天的主题只有一个，那就是covariance和correlation
- 经济学统计学很多模型都在研究correlation，怎么估计correlation，所有的系数估计都与covariance方程成比例。
- 广义协方差为零，可以推出变量之间互相独立。广义协方差可以刻画任何线性和非线性关系。
- 数学上有两种函数要特别关注，一是exponential function，二是step function （indicator function）。
- 线性回归分析，其实就是线性相关分析
## Conditional Expectations
- Conditional Mean E(Y|X)是统计学和计量经济学**最关注**的概念，很多建模围绕它进行。因为conditional mean的均方误差最小。
  - 给定X的条件下，Y的均值当然是对Y的建模。
- Conditional Mean也叫做回归方程(Y = E(Y|X) + err）。回归分析就是对条件均值建模。
- 所谓模型就是X的一个函数，用线性回归模型来预测Y就有y=g(x)+err。
  - $E(X\epsilon)$和$E(\epsilon |X)$不同，后者可以推出前者，前者通常不能推出后者。
- 模型设置是否正确的判断（重要！）：
  - 充要条件是：模型剩余项（注意：不是误差项）条件期望为零。
  - 用线性模型来建模，来估计，只有当该模型的线性方程部分等于（数据产生方程式的）条件期望时，才是正确的。
- 金融最大的特点是风险，因为它有各种不确定性。
- 所有金融理论都是关于如何刻画、测度金融风险，如何进行定价。
- riskmetrics, econometrics的metrics，指的是用了量化方法进行研究。
- 经济学理性预期学派用的数学工具就是条件期望。
- $\epsilon$是不可预测那部分的大小
- 为什么叫**回归**？最小二乘法OLS，被用来研究病理，研究发现高个子家族的身高最后会回归平均身高。
- Arch或者Garch模型，是金融计量学的核心模型

## Conclusion
- 第一章：为什么要学概率论？因为经济系统、金融市场充满不确定性，经济学、金融学主要研究人在不确定条件下的决策，至今为止概率论是描述不确定性现象最好的数学工具。
- 第二章：概率理论的基础。用随机试验(S,B,P)来描述不确定现象。计量经济学就是对概率建模。一个模型其实是一个family of probability function。所谓模型，一般都有参数，一个参数对应一个概率分布，不同参数对应不同分布。我们假设，真实世界中，只有一个真实的概率分布。我们的目的就是用观测数据，将真实的概率分布找出来。
- 第三章：随机变量和概率分布。随机变量是一个映射，将事件映射为数据，以利用微积分等数学工具来研究概率现象。应用就是求期望、矩、分位数，矩产生函数。
- 第四章：接续第三章。重要的概率分布：伯努利、泊松分布、正态分布、Gama分布、Chi方分布等等。
- 第五章：多元概率分布。联合概率分布函数。广义联合矩产生函数。
- 希望概率论能给大家树立一种世界观。能让我们更好地看待这个充满不确定性的世界。

# Introduction to Sampling Theory
- 离散分布中，最重要的是泊松分布
- 学习分布的时候，不要只将注意力放到数学上，而要看他们应用到哪些经济学领域。
- Bivariate Transformation有助于推导统计学部分的t，F分布
- t, F分布，都假设了总体的数据服从正态分布。但通常总体数据不是正态分布，此时就考察大样本条件下，数据趋于的极限分布。
- **两个经典估计方法**：极大似然估计(MLS)，矩估计(GMN)。另**一个经典估计方法**，普通最小二乘法(OLS)，因为一般教材都有。
  - 这次我需要把各种分布，以及估计方法之间的练习和区别搞清楚。
- 预测关系和因果关系，的关系。
- 大数据、机器学习和统计学，是目前的研究前沿。
  
## Introduction to Statistics
- **统计推断**包括**估计**和**假设检验**，以及**样本外预测**。
- 统计推断就是用一个样本的数据，来推断总体的性质。

## Population and Random Sample
- 做**随机试验**，就是从随机样本产生数据集的过程
- 时间序列数据的局限，只有一个样本点。但我们还是要假设，理论上随机样本可以产生不同的样本点。
- 统计分析，就是用观测数据集来推断总体分布函数。
- 很多应用里，假设函数形式已知，要求的是参数。这就是**参数建模**。
- statistic 统计量

## Sampling Distribution of Sample Mean
- 在推导sample mean的期望时，只要求idential distribution
- 但是，在推导sample mean的方差时,不仅要求idential distribution，还要求independence
- reproductive property of normal distribution: 如果某些随机变量正态分布，那么它们的线性组合仍然服从正态分布。
- 这节课很有所获：之前困惑，为什么抽样以后，随机变量的均值不变，但方差要除以n。其实，抽样后的随机变量是**随机变量的均值**，不是单个的随机变量。从直觉看，求均值以后，原来的均值不变，但波动会变小。

## Sampling Distribution of Sample Variance
- 看到期望expectation这个运算符，就想到大数定理。通过对样本求均值，当样本量趋于无穷时，根据大数定理，样本均值趋于正态分布。
- 样本均值服从正态分布，样本方差服从Chi方分布
- 通过洪永淼教授的讲解，对于统计学的big picture开始有了感觉。这里一直在研究样本的统计量，为之后从样本数据推断总体统计量作准备。有了样本均值和样本方差服从的分布之后，接下来就可以用它们构建求解自己感兴趣的、关于总体的随机变量分布了。

## student's t-Distribution
- 记不住的公式不要去记，但要懂得怎么推导。
- student's t distribution在经典统计学中，占有中心地位。
  - 因为在经典统计学中，我们通常假设随机变量服从独立同分布IID，这样${\bar{X_n}-\mu}\over \sigma/\sqrt n$就服从$N(0,1)$。
  - 但是，上面的$\mu, \sigma$都是未知数，从而表达式不是统计量，因而无法计算。
  - 用样本方差$S_n$代替$\sigma$，我们得到${\bar{X_n}-\mu}\over s_n/\sqrt n$。该式服从$t_{n-1}$分布。
- 统计偏差就是抽样偏差，由于样本是总体的子集，而引起的偏差。
- 显著性水平其实是指犯一种错误的可能性，即**拒真**错误概率，也称为第一类错误。除此之外，还有第二类错误，即**取伪**错误。第一类和第二类错误存在零和博弈关系。
- p value指的是，随机变量服从假定分布的情下，取预定范围内的值的概率大小。p value是统计学最重要的概念之一。
- 从t分布的表达式可以看出，如果样本量非常大，那么t统计量就会趋于无穷大，这样任何显著性水平都能达到。
- 
## Snedecor's F-distribution
- 比较两个随机变量的方差之比时，会用到F检验。
- t distribution和F distribution在linear regression中用的最多。
- t其实跟一阶距的检验相联系；F则跟二阶拒的检验相联系。

## Sufficient Statistics
- 充分统计量，用一个统计量从数据中提取所有与估计参数有关的信息。
- 当随机变量**服从正态分布**，那么该随机变量的样本均值和样本房方差是总体均值和总体方差的充分统计量。
- 充分统计量是Data reduction的一种形式。big Data里的high dimensional reduction（降维）也是Data reduction的一种形式，也可视为sufficient statistics的一种推广。

## Conclusion
- 抽样理论，局部推导整体
- 两个重要统计量：样本均值、样本方差
- t distribution, F distribution
- 第六章有三个基本思想：一是抽样理论，从局部推导总体；二是充分统计量，如何用一个统计量从数据集中将有关参数的信息都提取出来，同时含有最少的冗余信息；三是抽样分布，这涉及统计估计和推断，犯第一类和第二类错误的概率。

# Convergences and Limit Theorems

## Introduction
- 经济变量通常是厚尾(heavy tail)分布，不满足正态分布
- 第七章提供基本概念、方法、工具，为利用渐进理论（大样本理论）分析作准备。
- Asymptotic theory for econometricians, by Halbert White 计量经济学圣经

## Limits and Order of Magnitude: A Review
- order of magnitude告诉我们收敛的速率多块。
- 
## Motivation for Convergence Concepts
- 因为$\bar{X_n}$是随机变量，不是数列，所以它并适用极限理论。
- 为了应用极限理论，需要对统计理论的收敛定义进行改造。

## Convergence in Quadratic Mean and $L_p$ Convergence

## Convergence in Probability
- 依概率收敛。随着样本容量的增大，两个随机变量之间出现大距离的概率趋于0。
- **概率极限**的概念，$p(|z_n-b| \lt \epislon) = 0$。
- 一致估计就是依概率收敛。
  - 欧拉的无穷分析真是重要。
- Markov inequality在计量经济学中的应用特别广。切比雪夫不等式是马尔科夫不等式的一个特例。
- 大数定理要发挥作用，moment必须有限，IID条件必须满足。
- 大数定理说的就是，样本量增大，统计量依概率收敛于总体统计量。
- 
# Convergence and Limit Theorems
 ## Almost Sure Convergence
 - 几乎处处收敛
 - almost sure convergence比较强，概率必须等于1；convergence in probability没有那么强，概率趋于1就可以了，而趋于1则不必对于每个n概率都等于1。前者是对整个序列${Z_n}$来说的，而后者只是对于某个$Z_n$来说。前者可以推导出后者，后者不能推出前者。
 - almost sure convergence是一个比较难，但又比较重要的概念。
- convergence in $L_p$, convergence in probability, almost sure convergence 测度的都是随机变量$Z_n和Z$之间的距离是不是靠得很近(closedness)。
   
## Convergence in Distribution
- 依分布收敛。讲分布函数之间的距离。
- 为何依分布收敛有用？因为它能简化统计推断。做统计推断通常要知道统计量$T_n$的分布，然后根据阀值求得显著性。但是，经济数据通常不满足IID正态分布假设，从而不能用t和F分布。这时，根据n趋于无穷，$F_n(Z)$趋于$F_(Z)$的性质，而后者又是已知的，就可以大大简化计算。
- 第七章一共介绍了四个收敛概念：convergence in Mean Square, convergence in probability, almost sure convergence and convergence in distribution。其中前三个说的都是两个随机变量可以任意地靠近，最后一个说的是两个部分无限靠近。

## Central Limit Theorems
- 计量经济学一定要有**直觉思维**。直觉思维说得通了，然后再去找假设，看看在满足什么假设条件下，你的直觉可以成立。
- 对于技术性很强的假设，一定要去理解它的含义，即这么假设的目的。
- Slusky Theorem在渐进分析里面用得很多。
- Delta Method是概率论领域的泰勒展开。
- 渐进分析或大样本分析有三个基本工具：一是泰勒展开，二是大样本分析，三是中心极限定理。有了这三个工具，就可以进行任何的渐进分析，统计分布分析。

# Parameter Estimation and Evaluation

## Population and Distribution Model
- 统计推断两大任务：估计未知参数，假设检验。
- 三个最重要的参数估计方法：一是MLE，极大似然估计，假设分布形式已知，要估计的是参数。二是MME，矩估计方法，用矩而非整个分布信息进行估计；GMM，广义矩估计方法。三是OLS，普通最小二乘，对条件期望进行建模。

## Maximum Likelihood Estimation
- 我们假定模型设定正确，然后才讨论MLE。
- MLE的意义：选择一个参数值$\hat{\theta}$，让观测值出现的概率最大。
- 一致估计：就是当n趋于无穷的时候，估计量是否收敛于其真实值。

## Asymptotic Properties of MLE
- /asimp`totik/a. 渐进的
- 对于假设条件，要理解为什么要这么假设，它们用在哪里。
- 为什么要自己推导定理？推导的每一步都代表解题思路，如果能推导出来，就说明你对这个定理理解了。
- 自己手动推导对理解定理很有帮助。
- 但这节课内容我没听懂，非常琐碎。

## Method of Moments and Generalized Method of Moments
- 简称：MME, GMM
- 通常MLE比MME更有效，因为MLE以概率密度函数为基础，MME以矩提供的信息为基础，前者包含更多信息。但前者往往计算更复杂，或根本不知道其密度函数，而只要矩存在，后者就可以发挥作用。
- 应用中，Moment Condition是从经济学，而不是统计学来的。
- GMM其实就是，当方程组数目大于未知数，或者原方程组无解的时候，通过向量投影求线性方程组的最优解。

## Asymptotic Properties of GMM
- 证明方法和MLE几乎一样。

## Mean Squared Error Criterion
- 均方误差用来衡量估计量的好坏。
- MSE可以分解为precision和accuracy，精确度和准确度，accuracy测度有没有系统偏差。
- MAE平均绝对值估计量也是估计标准之一。最好估计量是根据选定的估计标准来说的。

## Best Unbiased Estimators
- 有约束的最优化问题，可以用拉格朗日方法。
- $MSE(\hat{\sigma}^2) \lt MSE(S_n^2)$。前者用有偏，换来了误差的大幅减小，从而成为更有效的估计量。所以，unbiased并不一定好于biased的估计量。
- 机器学习或者统计学习，之所以精度比较高，就是用有偏估计代替无偏估计，进而降低方差。换句话说，用precision换accuracy。
- Lagrange Method和Cramer-Rao是两种评价估计参数的方法。

## Cramer-Rao Lower Bound
- Cramer-Rao Lower Bound用到Cauchy-Schwartz inequality，可以证明通过它得到的参数估计是方差最小的。
- Cramer-Rao Lower Bound没有用到IID这个假设。在IID假设之下，其变为Corolary？

- 计量经济学常用估计方法：MLE，MME，GMM/2SLS, OLS, Quasi-MLE，其中MLE最好。
- 判断估计量好坏的准则：MSE，MAE。
- 判断是否最优参数估计：LM拉格朗日方法，Cramer-Rao Lower Bound两者约束条件不同。前者只要知道参数的方差即可，后者要求知道联合分布函数。

# Hypothesis Testing

## Introduction to Hypothesis Testing
- Hypothesis应该被翻译为**假说**，Assumption可以翻译为 **假设**
- Null Hypothesis **原假说**， Alternative Hypothesis **备择假说**。两个假说的集合互斥且互补。
- 这一讲给我帮助很大。之前有一个误区，认为假设检验不太可靠，为啥未低于5%的显著性水平就被接受。这是因为，比如统计量${X-u_0}\over {\sigma/\sqrt{n}}$，在假设$EX=u_0$成立时，在n趋于无穷大时，统计量才趋于0。如果原假设不成立，那么该统计量将趋于无穷。从这个分别来看，设置一个较大的数字M，在统计量超过它时，说原假设不成立是合理的；在n很大时，而统计量没有超过M时，接受原假设也是合理的。关键在n很大时，原假设和备择假设有**天壤之别**。
- **显著性水平**：level of the test，即犯第一类错误的概率上限。
- size of the test，即犯第一类错误的概率。
- 洪永淼教授解释，为什么machine learning比统计模型预测能力更强。因为machine learning是一种非参数方法，它是model free的，能够更好地揭示数据关系。经济模型和统计模型之间则有差异，统计模型假设模型正确地刻画了总体分布，需要预测的是参数，当这个假设不成立，预测能力就弱，至少线性模型就不具有预测效力。
- 

## Neyman-Person Lemma
- Neyman-Person Lemma说的是，likelihood ratio test 是 most powerful uniformly test。vice versa
- 直觉上看，likelihood ratio: $f(x^n, \theta_1)\over f(x^n, \theta_0)$，如果值大于1，那么说明在观测数据$x^n$下，备择假设出现的概率大于原假设出现的概率。这时候应该选择备择假设，反之选择原假设。

## Wald Test
- 假设检验三个最重要的基本方法：Wald Test沃德检验, Lagrangian Multiplier (LM) Test拉格朗日乘子法, Likelihood Ratio Test似然比检测
- 洪永淼教授在将沃德检验的时候，思路很清楚：为了检验$H_0: g(\theta) = 0$，因为$\theta$未知，所以用其一致估计量$\hat{\theta}$来替代。这样就看$g(\hat{\theta})$是否趋于0，这就要求$g(\hat{\theta})$的抽样分布，因此必须 构造$g(\hat{\theta})$的quadratic form。这个二次方程式的渐进分布是Chi-Square分布。
- Wald Test没有假设IID。

## Lagrangian Multiplier (LM) Test
- 拉格朗日乘子法和沃德检验的基本思想是一样的
- 构造统计检验量的思路套路值得学习

## Likelihood Ratio Test
- 似然比测试和拉格朗日乘子法是等价的
- 如果沃德测试的$\theta$用的是MLE估计值，那它和上面两种测试方法也是等价的
- 沃德测试和朗格朗日乘子法构造二次项形式来构造统计检验量，进而进行测试。似然比测试不构造统计量，用的是$I(\theta_0)+H(\theta_0) = 0$，它要求information matrix正确，即要求模型设定必须正确。前两个测试方法没有模型设定必须正确这个要求。

## Illustrative Examples
- Wald Test 检测的是 $\bar{X_n}$是不是趋于$\mu$
- Lagrangian Multiplier 检测的也是$\bar{X_n}$是不是趋于$\mu$
- 在假说正确的情况下，Wald Test 检测和Lagrangian Multiplier 检测渐进等价。

# Big Data, Machine Learning and Statistics
## Introduction
- 讨论大数据、机器学习的出现对统计学的影响

## Empirical Studies and Statistical Inference
- 概率法则，就是概率密度函数。统计推断假设数据产生过程DGP服从概率法则，数学概率模型是已知的，未知的是参数。
- 常用模型：
  - classical linear regression models;
  - probit or logit models in discreete choices;
  - Cox's (1960) proportional hazard models in survival or duration analysis.
- 宏观经济学大多数数据都不大，金融学比较大。
- 数据缺陷：
  - 共线性或近似共线性
  - 条件异方差和误差项的自相关
  - 截断数据
  - 观测数据缺失
  - endogeneity
  - curse of dimentionality
- 统计模型的关键假设：
  - 随机性
  - 模型唯一
  - 模型设定正确
  - 对总体的抽样推断
  - 有代表性的抽样
  - 统计显著性

## Important Features of Big Data
- 大数据特点：
  - volume大：样本容量大的数据叫tall big data，样本容量少于未知数的叫fat big data
  - 数据产生频率高，甚至实时：叫high big data
  - variety种类多：文本数据 textural regression，区间数据，时间序列数据，影像数据
  - veracity信息密度少：
  - 所谓的data reduction就是降维，通过构建统计量提炼原高维数据的信息。
  - 机器学习的产生就是分析大数据的需求，人做不了，就求助于机器计算。

## Big Data Analysis and Statistics
- 描述性统计：GDP，GNP，CPI，PPI这些就是描述性统计。
- 推断统计应用在经济学领域，就是计量经济学。
- 有了大数据，描述性统计的这些经济统计指数可以做到实时产生，使宏观经济数据高频化。这样宏观经济变量和金融市场变量的互动可以更好地刻画。
- 投资者情绪指数，从传媒、社交、报纸的文本中来分析。经济主体的幸福感，也从文本来。将文本变量带入回归，就可以构建文本回归。
- 统计显著性和经济显著性不同：只要样本容量足够大，任何统计变量都具有统计显著性，但未必有经济显著性。人工智能领域feature就是variable。feature importance探讨的是某个变量到底是不是真的重要。
- 抽样推断原理仍然适用：大数据分析、机器学习也假设数据产生是个随机过程。机器学习最重要的任务是，用今天的数据预测明天的数据，所以机器学习用到的数据并非全样本，仍然属于抽样统计。
- 充分性原理和降维：在big fat data中，数据数少于未知数个数。利用机器学习LASSO方法，可以找出系数不等于零的变量，扔掉等于零的变量，从而降低数据维度（data reduction）。
- 模型多样性和模型不确定性：为了robust，对多个模型做model averging。为了处理模型不稳定，用random forest随机深林算法。 
- 相关和因果关系：只要有强相关性就可以做很好的预测，不一定要知道因果关系。在经济学中是需要因果关系的，因为要成为科学就要求分析因果。例如，政策评估计量经济学。
- 机器学习可表示为一个数学优化问题，通过计算机自动实施。机器学习预测比较准确，但这种预测并不是基于经济因果关系，而是通过挖掘数据的特征和变量之间的统计关系实现。
- 统计学的虚拟事实（Counterfactuals）估计方法可以用来预测因果关系。因为机器学习的预测比较准，所以可以虚拟发生与未发生的政策效应，这样用来模拟自然科学的可控实验！
- 频谱分析与识别经济周期：谱密度函数可以用于研究经济周期与经济波动，是宏观经济“心电图”。
- 随机集（random set）概率论与区间数据建模：可用于宏观经济区间管理。