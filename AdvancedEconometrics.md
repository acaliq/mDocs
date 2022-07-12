高级计量经济学
> 洪永淼
> 2022-5-6

# 计量经济学导论

现代计量经济学可以分成四个领域：宏观经济学、微观经济学、金融经济学和计量经济学。

现代经济学研究的一般方法：

1. 搜集数据和归纳经验典型特征事实(empirical stylized facts)
2. 构建经济理论或经济模型。
3. 经济模型的经验验证(empirical verification)
4. 应用。

现代经济学的两个重要特征：一是经济理论的数学建模，二是经济现象的实证分析(empirical analysis)。

要成为一门科学，任何理论必须满足两个条件：一是逻辑一致性和理论体系的自洽性(coherency)，二是理论和典型特征事实的一致性。数学和计量经济学就是为了帮助经济学达到这两个条件。

经济学为什么要数学？

1. 数学语言可精炼描述一个理论的要点。
2. 经济学复杂的逻辑分析可通过数学工具得到极大的简化。
3. 数学建模是经济理论经验验证的必由之路。

检验经济理论或经济模型的前提假设是否正确是困难的，但可以通过考察经济理论的推论与观察数据之间是否一致来检验经济理论。计量经济学是利用数理统计学方法对经济理论进行实证检验的一门经济学科。

现代计量经济学建立在两个公理之上：

1. 任何经济系统都可视为服从一定概率法则的随机过程(stochastic process)。
2. 任何经济现象，通常以数据的形式呈现，可视为上述随机数据生成过程(data generating process)的实现(realizations)。

> 上述基本公理的重要内涵是，不能期望用精确的确定性数学模型来描述经济关系。计量经济学的目的就是从观测数据中找出经济系统的概率规律。经济理论通常对概率法则进行某些限制，可以通过检验这些限制的有效性来验证经济理论或经济假说[^econometrica]。

[^econometrica]: 在《计量经济学》(Econometrica)创刊号中，计量经济学学会创始人Fisher说：计量经济学会的主要目标是，促进以定性和定量方法、经验实证和定量方法相结合的经济研究范式的发展，促进在自然科学领域广泛使用的富有建设性的严格思维方式在经济学领域中的应用。但是，经济学的定量研究方法有很多方面，任何单一方面均不能独自存在，必须与计量经济学相结合。因此，计量经济学不是经济统计学，也不能等同于一般的经济理论，尽管这些理论中有一部分具有数量特征；同时，计量经济学也不是数学在经济学中的应用，尽管这些理论中有相当一部分具有数量特征；实践证明，统计学、经济理论、数学这三个要素是真正理解现代经济生活中数量关系的必要条件，但不是充分条件。只有三个要素互相结合，才能发挥各自的威力，才构成了计量经济学。

计量经济学在经济研究中的作用：

1. 检验经济理论是否能够解释历史经济数据，特别是重要的经验典型特征事实。
2. 验证经济理论和经济假说的正确性或有效性。
3. 预测未来经济发展趋势，并提供政策建议。

一个经济系统可由主导它的概率法则来全面地刻画。对于具体的问题，到底是对条件期望】条件方差，还是对整个条件概率分布进行建模，则取决于所研究问题的性质。同时，必须根据经济数据的特点以及各种计量经济学方法与工具的适用范围和条件，以及经济结构的因果关系和逻辑关系，来选择正确的计量经济学模型、方法和工具，并对统计推断结论给予正确的经济学解释。

计量经济学分析的局限性：

1. 作为对现实的简化，经济理论和模型仅能刻画经济系统中最主要的或最重要的因素，然而观测数据却是由多种因素相互作用的结果，其中某些因素是未知的或不可观测的，这些因素在现实中确实存在，但没有包括在模型中，因而模型无法反映或测度它们的影响。
2. 现实经济是一个不可逆或不可重复的系统。
3. 经济结构关系往往具有时变性。
4. 数据质量。

## 一般回归分析和模型设定

统计关系的本质是一种预测关系。
经济关系的本质是一种因果关系。

各阶条件矩的集合是条件概率分布$f_{Y|X}(y|x)$的一个总体刻画(summary characterization)。针对条件矩构建的数学模型称为条件矩计量经济学模型。

一阶条件矩$E(Y|X)$也称为Y对X的回归函数(regression function)。“回归(regression)”一词用于表示Y与X之间存在一定的关系。

**回归函数**(Regression Function): 条件均值$E(Y|X)$称为Y对X的回归函数。

回归分析或条件均值分析是计量经济学中最常见的统计方法，在经济学中有广泛应用。

**引理**
$E[E(Y|X)] = E(Y)$
> 解释：条件均值的均值，是无条件均值。

**引理**：重复期望法则(Law of Interated Expectations, LIE)
对给定的可测函数G(X,Y)，假设期望E[G(X,Y)]存在，则$$
E[G(X,Y)] = E{E[G(X,Y)|X]}
$$

为了测度g(X)接近Y的程度，定义一个判定准则，即均方误(mean sqared error, MSE)准则。

**均方误**：假设用函数g(X)来预测Y，则预测量g(X)的均方误定义为$$
MSE(g) = E[Y-g(X)]^2
$$MSE是预测误差的平方的平均值。一个函数的MSE越小，其预测Y的能力越好。

**定理**：MSE最优解
条件均值E(Y|X)是下列问题的最优解$$
E(Y|X) = arg \min\limits_{g \in \Bbb{F}} MSE(g) = arg \min\limits_{g\in \Bbb{F}} E[Y-g(X)]^2
$$其中$\Bbb{F}$是所有可测和平方可积函数的集合(space of all measureable and square-integrable functions)，即$$
\Bbb{F} = \{g: \Bbb{R}^{k+1} \rarr \Bbb{R}| \int g^2(x)f_X(x)dx \lt \infty\}
$$

**定理**：回归等式(Regression Identity)
给定条件均值E(Y|X)，总有$$
Y = E(Y|X) + \epsilon
$$其中$\epsilon$称为回归扰动项(regression disturbance)，满足$$
E(\epsilon|X) = 0
$$

随机变量$\epsilon$通常称为回归扰动项，因为它可视为对回归函数关系$E(Y|X)$的扰动。$\epsilon$代表随机变量Y中没有被条件均值$E(Y|X)$预测或解释的部分，也称为噪声(noise)，而回归函数$E(Y|X)$称为信号(signal)，可以根据回归函数$E(Y|X)$用$X$来预测$Y$。

$E(\epsilon|X)=0$表示回顾扰动项$\epsilon$不包含能够预测$Y$的条件期望的任何有关$X$的系统信息。从$E(\epsilon|X)=0$可以推出$\epsilon$与$X$正交，且与X的任何可测函数$h(X)$均正交，即$E(\epsilon h(X))=0$。这表明，不能用任何形式的函数$h(X)$预测$\epsilon$的条件均值，无论是线性的还是非线性的模型$h(X)$都对$\epsilon$的条件期望没有预测能力[^ hetero]。

[^ hetero]: 需要指出，当$E(\epsilon|X)=0$时，$var(\epsilon|X)$仍有可能是X的函数。如果$var(\epsilon|X)=\sigma^2\gt 0$，则称$\epsilon$为条件同方差(conditional homoskedasticity)。此时，X不能用于预测Y的条件方差，因为$var(Y|X)=var(\epsilon|X)$。但是，如果对于任意的$\sigma^2\gt 0$，均有$var(\epsilon|X)\neq \sigma^2$，此时存在条件异方差(conditional heteroskedasticity)。在这种情况下，可以用X预测Y的波动率。回归分析的计量经济学方法通常会因为是否存在条件异方差而有所不同。比如，在存在条件异方差的情况下，通常的t检验和F检验是无效的。

为什么会出现条件异方差？
一般而言，如果$E(Y|X)$依赖于X，那么很自然地，$var(Y|X)$和更高阶的条件矩也可能依赖于X。事实上，数据生成过程的随机系数也可能导致条件异方差。

如何对条件均值$g_o(X)$进行建模？
在计量经济学中，一个应用广泛的建模方法是将条件均值$E(Y|X)$设定为某种已知的函数形式，但包含少数未知参数。因为简单且容易解释，人们常常用线性函数作为条件均值$g_o(X)$的近似。

**仿射函数**(Affine Functions)
记$X=(1,X_1,X_2,...,X_k)', \beta = (\beta_0,\beta_1,...,\beta_k)'$。则仿射函数族定义为$$
\Bbb{A} = \{g:\Bbb{R}^{k+1}\rarr \Bbb{R}| g(X) = \beta_0 + \sum\limits_{j=1}^k \beta_jX_j, \beta_j \in \Bbb{R}\}\\
= \{g:\Bbb{R}^{k+1}\rarr g(X) = X'\beta\}
$$这里，对参数向量$\beta$的值没有限制。对于这族函数，函数形式已知，分别是解释变量$X$和参数$\beta$的线性函数。
> 仿射函数类$\Bbb{A}$的重要特征是$g(X) = X'\beta$，即$g(X)$同时是$X$和$\beta$的线性函数。

因变量是$\beta$的线性函数，但不一定是解释变量的线性函数的模型，被称为**线性回归模型**。相应地，**非线性回归模型**是指$g_o(X)$是参数$\beta$的非线性函数。

当将$g(X)$的函数集合从所有可测且平方可积的函数集合限制为仿射函数集合时，问题变为求参数向量$\beta^*$以使仿射函数$g(X)=X'\beta$的MSE最小化$$
\min\limits_{g\in \Bbb{A}} E[Y-g(X)]^2 = \min\limits_{\beta\in \Bbb{R}^{k+1}}E(Y-X'\beta)^2
$$最优解$g^*(X) = X'\beta^*$称为Y的最优线性最小二乘预测(best linear least squares predictor)，而最优参数值$\beta^*$称为最优最小二乘近似系数向量(best least squares approximation coefficient vector)。

**定理**：最优线性最小二乘预测(Best Linear Least squares Prediction)
假设$E(Y^2)\lt \infty$，且$(k+1)\times (k+1)$矩阵$E(XX')$是非奇异的。则以下优化问题$$
\min\limits_{g\in \Bbb{A}} E[Y-g(X)]^2 = \min\limits_{\beta\in \Bbb{R}^{k+1}}E(Y-X'\beta)^2
$$的解，即最优线性最小二乘预测值为$$
g^*(X) = X'\beta
$$其中最优系数向量为$$
\beta^* = [E(XX')]^{-1}E(XY)
$$
> 在$\beta = (\beta_0, \beta_1)', X = (1, X_1)'$，则最优斜率和截距系数分别为$\beta_1^*= {cov(Y,X_1\over var(X_1))}$和$\beta_0^* = E(Y) - \beta_1^*E(X_1)$。因此，$\beta_1^*$反映了可由协方差cov(Y,X_1)刻画的$Y$和$X_1$之间的线性相依关系即相关性，但它不能反映$cov(Y,X_1)$无法度量的$Y$和$X_1$之间的非线性相依关系。因此，线性回归本质上是相关分析(correlation analysis)。

**线性回归模型**(Linear Regression Model): 方程$$
Y = X'\beta + u, \beta \in \Bbb{R}^{k+1}
$$称为Y对X的线性回归模型，其中u是回归模型误差(regression model error)。如果k=1，称为二元线性回归模型(bivariate linear regression model)或直线回归模型(straight linear gression model)。如果$k>1$，则称为多远线性回归模型(multiple linear regression model)。
> 线性模型可能不包括真是的回归函数$g_o(X)\equiv E(Y|X)$。但是，即使$g_o(X)$不是X的线性函数，从而线性回归模型$Y=X'\beta + u$存在设定错误，该模型仍然可能具有一定的预测能力。

**定理**
令$$
Y = X'\beta + u
$$并令$\beta^*= [E(XX')]^{-1}E(XY)$为最优线性最小二乘近似系数。则$$
\beta = \beta^*
$$当且仅当以下正交条件成立$$
E(Xu) = 0
$$
> 该定理意味着，无论$E(Y|X)$是X的线性函数还是非线性函数，线性回归模型$Y=X'\beta + u$的正交条件$E(Xu) = 0$总会成立，当且仅当$\beta = \beta^*$时。

当X包含截距项时，正交条件$E(Xu) = 0$意味着$E(u)=0$。而当$E(u)=0$时，有$E(Xu) = cov(X,u)$。因此，正交条件与X和u不相关是等价的。这说明，u中不包含任何可用X的线性函数来预测的成分。需要强调的是，条件$E(Xu)=0$与$E(u|X)=0$是完全不同的。后者可推出前者，但反之不成立。

**条件均值模型的正确设定**
线性回归模型$$
Y = X'\beta + u, \beta \in \Bbb{R}^{k+1}
$$是条件均值$E(Y|X)$的正确设定，如果存在某个参数值$\beta^o \in \Bbb{R}^{k+1}$，有$$
E(Y|X) = X'\beta^o
$$另一方面，如果对于任意的参数值$\beta \in \Bbb{R}^{k+1}$ $$
E(Y|X) \neq X'\beta
$$则线性回归模型是对$E(Y|X)$的错误设定(misspecified)。

由条件均值模型设定正确的定义，可以看到，线性回归模型设定正确的条件是，存在某一参数值$\beta^o$，使线性回归模型残差项$u = Y - X'\beta^o$满足下列条件$$
E(u|X) = 0
$$

当条件均值模型设定正确时，回归模型误差项u与真实回归扰动项$\epsilon = Y-E(Y|X)$两者之间有下述关系定理。
**定理**
如果线性回归模型$$
Y = X'\beta + u
$$是对条件均值$E(Y|X)$的正确设定，则

1. 存在一个参数$\beta^o$和一个随机变量$\epsilon$，有$Y = X'\beta^o + \epsilon$，其中$E(\epsilon|X) = 0$
2. $\beta^*= \beta^o$

> 该定理(1)表明，如果$E(Y|X)$的模型设定正确，则存在一个参数值$\beta^o$，使$E(Y|X) = X'\beta^o$。在这种情况下，回归模型误差项$u = Y-X'\beta$在参数$\beta$取$\beta^o$值时将等于真实的回归扰动项$\epsilon = Y-E(Y|X)$。(2)说明，如果线性回归模型设定正确，则条件均值$E(Y|X)$与最优线性最小二乘预测$g^*(X) = X'\beta$是一样的，同时，最优线性最小二乘近似系数$\beta^*$可以解释为X对Y的期望边际效应。

当正交条件$E(Xu)=0$成立，但$E(u|X)\neq 0$时，真实回归函数$$
E(Y|X) = X'\beta + E(u|X) \neq X'\beta
$$模型误差项u中存在某些与X有关的系统信息，可用以改善X对Y的条件均值的预测能力，但被现有线性回归模型忽略了。

**非参数建模**
由于假设函数形式是已知的，参数模型总是存在误设的可能性。在计量经济学中，有一种建模方法不对$E(Y|X)$进行任何参数形式的函数设定，而是让数据本身揭示经济变量之间真实的函数关系。这种方法被称为非参数方法(non-parametric approach)，它在大样本条件下不存在模型设定错误的问题。
非参数建模的基本思想……
非参数方法对数据生成过程的假设限制很少，因此没有模型设定错误的问题。但因为非参数方法需要估计很多未知参数，为了得到精确的估计，往往需要大量的数据。并且，很难对系数进行经济解释。

# 经典线性回归模型

上一章的$\beta^*$取决于总体均值，但是总体分布未知，故无法求得总体均值。此时，总是通过大数定律，以样本均值替代总体均值来计算最优估计。这就是本章要讲授的内容。

当我们在推导定理和性质的时候，总是从定义和假设开始。

经典线性回归模型是经典统计模型的计量经济学版本。基于统计学的经典假设（IID normal），即线性回归模型的随机误差项$\epsilon$服从独立同分布的正态分布，那么就可以对线性回归模型的系数进行t，F估计。

因为包含自变量越多，$R^2$越大，所以$R^2$不是一个用来选择模型的好标准。

选择模型的标准：goodness of fit and model complexity

1. AIC = $\ln (S^2) + {2K\over n}$
2. BIC = $\ln (S^2) + {K\ln (n)\over n}$
3. $\bar{R} = 1-{1-{{n-1}\over {n-k}}R^2}$

之所以要用到二次型（quadratic form），是为了将向量变为标量，以计算用于在分布中定位的阀值（critical value）。

经典回归模型假设3.5（误差项服从正态分布），是为了适用t-test和F-test。

广义最小二乘GLS
> 基本思想：异方差导致OLS不可用，那就通过转换将异方差去掉。这样新的模型就可以继续适用OLS模型。

# 独立同分布样本的线性回归模型

本章与上章的区别是：本章放弃了样本服从正态分布这个假设。
经济数据通常是厚尾分布，不服从正态分布，不能假设$\epsilon|X$服从正态分布。

在上章关于样本服从正态分布的假设下，样本数量（n>1）不是问题。放弃样本服从正态分布后，只有在大样本情况下，才能利用渐进分布进行推断和统计。

Asimptotic Theory就是大样本理论，当n趋于无穷时的理论。

做渐进分析（Asimptotic Theory）所需的三个工具：  

1. 大数定理
2. 中心极限定理
3. Delta Method （泰勒展开）

这门课的特点，就是以经典线性回归模型的那些假设为基础，逐渐放松这些假设，最后建立现代计量经济学理论框架。从第四章开始，到第五、六、七章，都是在重复同样的故事，即用渐进分析替代（放松）原假设。

现代计量经济学理论就是比经典线性回归模型采用更一般化的假设，这样就可以在实际中应用了。

证明定理过程中，需要什么条件，就将之提出为假设。

如果存在独立同方差，在大样本情况下，经典回归模型仍然适用。

Robust statistic 是指在条件异方差，仍然适用的统计量。

第四章的主要结论：

1. conditional homoskedasticity时，在大样本条件下，classical linear regression model 仍然适用。
2. conditional heteroskedasticity时，需要大样本条件并且将统计量处以正确的渐进方差协方差矩阵，classical linear regression model 才适用。

在两个假设检验方法之中，只要有可能就选择那个限制条件更多的，因为它利用了更多更严格的假设信息，分布预测会更精确；而较一般化的检验方法，在样本量不够大时，精确度较差，因为它包含了各种各样的情况。。

# 非独立样本的线性回归模型

本章将换掉LLN和CLT，以适用Time Series Data，但分析方法和上一章一样。

如果$Y_t$取决于$Y_{t-1}$，该模型就叫**动态**模型，也叫**自回归**模型。auto means it depends on it's previous information,

从IID到时间序列数据，考察$\epsilon$是否自相关，非常重要。

时间序列数据可视为一组随机变量，每个随机变量只有一个实现值。所以，为了进行统计分析，必须对这些随机变量施加一些限制。一是stationarity，二是ergodicity，三是央差？

假设时间序列数据是stationary和ergodic之后，可得$\{X_t\epsilon_t\}$是MDS。MDS可导出$E(X_t\epsilon_t|I_{t-1}) = 0$，以及$Cov(X_t\epsilon_t,X-{t-j}\epsilon_{t-j}), \forall j \neq 0$。

因为时间序列数据的一阶矩和二阶矩是时间t的函数，所以当t趋于无穷，矩也趋于无穷。为了做计量分析，常常定义新的随机变量$X_t = Y_t - \hat{m}_t$，其中Y是最初的时间序列随机变量，m是trend，两者差就消除了时间因素。

White Noise的得名源自谱密度函数spetrum density function。谱密度函数是一类傅立叶变换，同白光的光谱频率函数一样。各频率函数叠加后是白光，所以经济学上对应的取名是白噪声。

本课程关注的是stationary time series，如果要做宏观经济和金融学有关数据，需要专门再学non-stationary有关时间序列数据的计量模型。

时间序列数据的一个特点是序列数据之间有很强的相关性，这意味着数据的方差比较小，这又意味着数据包含的信息少。即便在大样本条件下，这样的数据包含信息少，推断统计就可能有问题。

第五章发展的5个假设，将第四章的5个假设作为特例包含了进来。

计量经济学很容易，如果不知道分布就用数据，如果不知道期望就用样本均值，大数定理、中心极限定理派上用场。

在静态模型中，如果$\epsilon$不是MDS，那么Variance-Covariance Matrices就不能用；在动态模型中，如果$\epsilon$不是MDS，那么不仅Variance-Covariance Matrices不能用，而且用OLS估计的$\beta_1$系数都不是consistent的。这就是我们要检查序列相关性的原因。

三大检验：Wald test， LM test，Likehood Ratio test。Wald test针对unrestricted model，LM test针对restricted model，似然比同时针对两者。

# 第六章 Linear Regression Models under Conditional Heteroskedasdicity and Autoregression

什么时候用long run variance-covariance matrix？
当数据不是MDS的时候。IID隐含MDS，所以IID也是MDS。MDS表示$\Gamma(j) = 0, \forall j\neq 0$。

# 第七章 Instrumental Variables Regression

本章要放松的一个条件是$E(\epsilon_t| X_t) = 0$

什么叫内生，什么叫外生？其实，就是看$E(\epsilon_t| X_t) = 0$这个条件有没有满足。

用2SLS可以解决测量误差、变量缺失和测度两个同时起作用的相关线性模型等问题。

# 第八章 
第8章是第7章的一般化。2SLS有其局限性，第8章的GMM方法解决之。
3个重要的统计估计方法：OLS、MME、MLE。在计量经济学中，MME被拓展为GMM。
证明asymptotic distribution的一般方法：
1. take FOC
2. Taylor Expansion
3. $\sqrt(n)(\beta_0 - \hat{\beta)}$ by CLT, LLN, Slusky Thearom

Comment:证明渐进分布只需掌握3个理论工具，即大数定理、中心极限定理、泰勒展开。学习证明过程，是为了清楚假设用在哪，为何要这些假设条件。

# 第九章
指数分布在生存分析的地位，就像IID Normal在线性回归分析中的地位。泊松分布在离散数据分析中的地位，就像正态分布在连续数据分析中的地位。
MLE是专门用来估计probability model的方法。它要求知道整个连续的概率分布函数。也就是说，在需要对整个分布建模而非仅对conditional mean建模时，需要用到MLE。
评价参数efficiency的两个标准：一是OLS的Gauss-Markov least squares，二是MLE的Ramer-tao lower bound。前者不用density function，后者要用。
OLS与conditional mean有关，ARCH与GARCH与condition variance covariance有关，MLE与density function有关。
QMLE在明知模型假设的density function错误的情况下使用。因为魔性的conditional mean是正确的，故可consistly估计模型的参数。    