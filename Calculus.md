普林斯顿微积分读本

- [函数、图像和直线](#函数图像和直线)
  - [函数](#函数)
  - [函数的复合](#函数的复合)
  - [奇函数和偶函数](#奇函数和偶函数)
  - [线性函数的图像](#线性函数的图像)
  - [常见函数及其图像](#常见函数及其图像)
- [三角学回顾](#三角学回顾)
  - [基本知识](#基本知识)
  - [三角恒等式](#三角恒等式)
- [极限导论](#极限导论)
  - [极限：基本思想](#极限基本思想)
  - [左极限与右极限](#左极限与右极限)
  - [何时不存在极限](#何时不存在极限)
  - [三明治定理](#三明治定理)
- [求解多项式的极限问题](#求解多项式的极限问题)
- [连续性和可导性](#连续性和可导性)
  - [连续性](#连续性)
  - [可导性](#可导性)
  - [何时导数不存在](#何时导数不存在)
  - [可导性和连续性](#可导性和连续性)
- [求解微分问题](#求解微分问题)
- [三角函数的极限和导数](#三角函数的极限和导数)
  - [三角函数的极限](#三角函数的极限)
  - [三角函数的导数](#三角函数的导数)
- [隐函数求导和相关变化率](#隐函数求导和相关变化率)
- [指数函数和对数函数](#指数函数和对数函数)
  - [指数函数（exponential function）回顾](#指数函数exponential-function回顾)
  - [对数函数(logarithmic function)回顾](#对数函数logarithmic-function回顾)
  - [e的定义](#e的定义)
  - [对数函数和指数函数求导](#对数函数和指数函数求导)
- [反函数和反三角函数](#反函数和反三角函数)
  - [导数和反函数](#导数和反函数)
  - [求反函数的导数](#求反函数的导数)
  - [反三角函数](#反三角函数)
- [导数(derivative)和图像](#导数derivative和图像)
- [最优化和线性化](#最优化和线性化)
  - [最优化问题：一般方法](#最优化问题一般方法)
  - [线性化问题：一般方法](#线性化问题一般方法)
  - [牛顿法](#牛顿法)
- [洛必达法则](#洛必达法则)
- [积分(integral)](#积分integral)
- [定积分](#定积分)
- [微积分基本定理](#微积分基本定理)
- [求积分的方法](#求积分的方法)
- [反常积分](#反常积分)
- [数列和级数](#数列和级数)
  - [数列](#数列)
  - [级数的收敛与发散](#级数的收敛与发散)
- [泰勒多项式、泰勒级数和幂级数导论](#泰勒多项式泰勒级数和幂级数导论)
- [参数方程和极坐标](#参数方程和极坐标)
- [复数](#复数)
- [微分方程](#微分方程)
  - [可分离变量的一阶微分方程](#可分离变量的一阶微分方程)
  - [一阶线性方程](#一阶线性方程)
  - [常系数微分方程](#常系数微分方程)
# 函数、图像和直线
> 前两章温习**函数的性质**

## 函数
- **函数**是将一个对象转化为另一个对象的规则。起始对象称为**输入**，来自称为**定义域**(domain)的集合。返回对象称为**输出**，来自称为**上域**(codomain)的集合。
  - f(x) = $x^2$中，f是一个函数，f(x)是把规则f应用到变量x之后得到的结果。
- 函数的**值域**(range)是所有实际输出所组成的集合。
- 一个函数必须给每一个有效的输入指定**唯一**的输出。
  - 函数可以是多个自变量到一个应变量的映射，但不可以是一个自变量到多个应变量的映射。
- 上域是**可能**输出的集合，值域是**实际**输出的集合。

## 函数的复合
> 对于f(x) = h(g(x))，称f是g与h的复合。

## 奇函数和偶函数
- 如果对f定义域内的所有x有f(-x) = f(x)，则f是偶函数。
- 如果对f定义域内所有x都有f(-x) = -f(x)，则f是奇函数。
  - 偶函数关于y轴镜面对称，奇函数关于原点$180^0$对称。

## 线性函数的图像
- 形如 f(x) = mx + b的函数叫作线性函数。
  - 如此命名的原因是，它们的图像是直线。

## 常见函数及其图像
- **多项式**(polynomial)
  - p(x) = $a_nx^n + a_{n-1}x^{n-1} + ... + a_2x^2 + a_1x^1 + a_0$
  - 多项式的重要性体现在，它比较好处理。比如泰勒级数就将某个函数的近似求解问题转化为多项式来处理。
  - 多项式中最大的幂指数称为多项式的次数。
  - 次数为2的多项式，称为二次(quadratic)函数。解x = $-b \pm \sqrt{b^2 - 4ac} \over 2a$，可通过配方得到。
- 有理函数
  - $p(x) \over q(x)$，其中p和q为多项式的函数
- 指数函数和对数函数
  - 指数函数，f(x) = $b^x$
  - 对数函数，f(x) = $log_a(x)$
  
# 三角学回顾
> 学习微积分必须要了解三角学，它对于处理周期函数很重要

## 基本知识
- **弧度**，半径为1的圆，其周长是$2\pi$个单位。
  - 用弧度度量的角 = ${\pi \over 180} \times 用角度度量的角$
  - 用弧度表示角的大小是自然的，而把圆分成360度则是人为的。
- $\sin \theta = {对边 \over 斜边}$
- $\cos \theta = {邻边 \over 斜边}$
- $\tan \theta = {对边 \over 邻边}$
- $\csc x = {1 \over \sin x}$
- $\sec x = {1 \over \cos x}$
- $\cot x = {1 \over \tan x}$
- 数学不是死记硬背，但有些内容是值得记忆的，比如下面这张表：
$$
\begin{array}{c|lcr} n & {0} & {\pi\over6} & {\pi\over4} & {\pi\over3} & {\pi\over2} \\
\hline
sin & 0 &{1\over2}&{1\over\sqrt2}&{\sqrt3\over 2}&1  \\
cos & 1 & {\sqrt3\over2}&{1\over\sqrt2}&{1\over 2}& 0 \\
tan & 0 & {1\over\sqrt3}&{1}&{\sqrt3}& - \\
\end{array}
$$
## 三角恒等式
- $\cos^2x + \sin^2x = 1$
  - **毕达哥拉斯定理**(Pythagoras Theorem)
  - 这个定理最重要，其他皆由其推出。
- $1 + \tan^2x = \sec^2x$
- $\cot^2x + 1 = \csc^2x$
- $\sin x = \cos ({{\pi \over 2} - x})$，$\tan x = \cot ({{\pi \over 2} - x})$，$\sec x = \csc ({{\pi \over 2} - x})$
  -  一些函数名以“co”开头，这是“互余(complementary)”的简称。说两个角互为余角，意味着它们的和是$\pi \over 2$。
- $\sin(A+B) = \sin(A)\cos(B) + \cos(A)\sin(B)$
- $\cos(A+B) = \cos(A)\cos(B) - \sin(A)\sin(B)$
  - $\sin 2x = 2\sin x\cos x$
  - $\cos 2x = \cos^2x - \sin^2x = 2\cos^2x - 1 = 1 - 2\sin^2 x$
  - 三角函数的和差化积公式是从图形推导出来的。积化和差公式，则应用和差化积公式推导而来。

# 极限导论
## 极限：基本思想
- 极限表达式 $\lim\limits_{x\rightarrow2}f(x) = 1$，等式左边不是x的函数。它是说，当x接近2时，f(x)接近于1。
  - 这里的要点是，在极限表达式中，变量x只是一个虚拟变量。它是一个暂时的标记，用来表示某个非常接近于2的量。
  - 这里的“=”号表示的并非相等，而是无限趋近。
- **极限定义**:$\lim\limits_{x\rightarrow a}f(x)=L$表示，对于任选的$\epsilon \gt 0$，可以选取$\delta \gt 0$，使得：对于所有满足$0\lt |x-a|\lt \delta$的x，有$|f(x)-L|\lt \epsilon$
## 左极限与右极限
- 极限表达式 $\lim\limits_{x\rightarrow3^-}h(x) = 1$，表示h(x)在3处的左极限。
- 极限表达式$\lim\limits_{x\rightarrow3^+}h(x) = -2$，表示h(x)在3处的右极限。
- 这里的要点是：通常的双侧极限在 x = a 处存在，仅当左极限和右极限在 x = a 处都存在且相等。

## 何时不存在极限
- 左极限不等于右极限或左右极限至少有一个等于$\plusmn \infty$
- 垂直渐近线：“f在 x = a 处有一条垂直渐近线”说的是，$\lim\limits_{x\rightarrow a^-}f(x)和\lim\limits_{x\rightarrow a^+}f(x)至少有一个极限是\infty或-\infty$

## 三明治定理
- **三明治定理**又称**夹逼定理**：如果一个函数f被夹在函数g和h之间，当$x\rightarrow a$时，这两个函数g和h都是收敛于同一个极限L，那么当$x\rightarrow a$时，f也收敛于极限L。
  - 如果对于所有a附近的x都有$g(x)\leq f(x)\leq h(x)$，且$\lim\limits_{x\rightarrow a}g(x) = \lim\limits_{x\rightarrow a}h(x) = L$，则$\lim\limits_{x\rightarrow a}f(x) = L$。
    - 证明：根据$\lim\limits_{x\rightarrow a}g(x)=L和\lim\limits_{x\rightarrow a}h(x)=L$，我们希望证明$\lim\limits_{x\rightarrow a}f(x)=L$
    - 根据极限定义，存在$\delta \gt 0, 使得当0\lt |x-a|\lt \delta$成立时，$0\lt |g(x)-L|\lt \epsilon$成立，即$L-\epsilon \lt g(x) \lt L+\epsilon$
    - 根据，$g(x)\lt f(x) \lt h(x)$，有$L-\epsilon \lt g(x) \lt f(x)$
    - 类似地，我们有$f(x) \lt h(x) \lt L + \epsilon$
    - 所以，有$L-\epsilon \lt g(x) \lt f(x) \lt h(x) \lt L+\epsilon$，证毕。

# 求解多项式的极限问题
> 微分会涉及比率的极限，因此我们的注意力主要集中在这种类型的极限上。
- 极限$\lim\limits_{x\rightarrow a}{p(x)\over q(x)}$，其中p和q都是多项式。根据p、q的值，可将极限分为定式和不定式(p、q同为0或无穷)。
- 如果是定式，则将x的值直接带入求解。
- 如果是不定式，则有下面这些求解技巧：
  - 通过约分化简，比如利用立方差公式$a^3-b^3 = (a-b)(a^2+ab+b^2)$
  - 对于有平方根的极限，分子分母同时乘以共轭表达式。
  - 当$x\rightarrow\infty$时，分子分母同时除以多项式最高次项$a_nx^n$。

# 连续性和可导性
> **连续性**，直觉上要求连续函数的图像必须能一笔画成。
> **可导性**，直觉上要求可导函数的图像不会出现尖角。
    - 出现尖角则斜率不唯一。
## 连续性
- 在一点处连续：如果 $\lim\limits_{x\rightarrow a}f(x) = f(a)$,那么函数f在点 x = a 处连续。
  - 这个定义要求（1）双侧极限$\lim\limits_{x\rightarrow a}f(x)$存在；（2）函数在点 x=a 处有定义，即f(a)存在；（3）以上两个量相等。
- 在一个区间上连续：函数f在[a,b]上连续，如果（1）函数f在点（a,b）中的每一点都连续；（2）函数f在点 x=a 处右连续；（3）函数f在点 x=b 处左连续。
- **介值定理**(intermediate value theorem)：如果f在[a,b]上连续，并且$f(a)\lt 0且f(b)\gt 0$，那么在区间(a,b)上至少有一点c，使得 f(c) = 0
  - 介值定理的重要性在于：证明解的存在。只要构造出一个右边等于零的方程式，并且证明左边表达式可以取到正负值，那么该方程一定有解。
  - 证明：设S是区间[a,b]内，使得$f(x)\leq u$的所有x的集合。根据实数完备性，S的最小上界c一定存在，即c = sup S。我们需要证明f(c) = u
  - 假设$f(c) \gt u$，则根据函数的连续性，存在$\delta \gt 0$，使得$|x-c|\lt \delta$时，$|f(x)-f(c)| \lt f(c)-u$
  - 上式可化简为$f(x)\lt f(c)-(f(c)-u) = u$，因此$c-\delta$是S的一个比C小的上界，这与假设c是S的最小上界矛盾。
  - 类似可证明$f(c)\lt u$也同假设矛盾。
  - 所以，$f(c)=u$。当u=0时，得出介值定理的一种特殊情况。证毕。
- **最大值最小值定理**：如果f在[a,b]上连续，那么f在[a,b]上至少有一个最大值和一个最小值。
  - 优化问题与最大最小值密切相关。
  证明：此定理的证明分两个阶段，先证明闭区间连续函数有界，再证有最值。
  - 利用反证法，先假设无界，然后利用无界的定义构造一数列，然后利用致密性定理即可。
  - 因为f(x)在闭区间[a,b]上有界，由确界原理可得，存在上确界：$\sup_{x\in[a,b]}f(x) = M$
  - 令$S = \{f(x)|x \in (a,b)\}$
  - 如果$M \notin S$，必存在单调递增数列$\{y_n\} \subseteq S \rightarrow M$,使$\lim\limits_{n\rightarrow +\infty}y_n = M$
  - 由值域的定义可得，$\exist x_i \in [a,b]$使得$f(x_i) = y_i (i = 1,2,...,n)$
  - 由于数列${x_n}$有界，由致密性定理可得，存在子列${x_{nk}}\rightarrow x_0 \in [a,b]$
  - 此时，可得$y_{nk} = f(x_{nk})\rightarrow M$,使$\lim\limits_{k\rightarrow +\infty}y_{nk}=M$
  - 由于f(x)在[a,b]上连续，由归结原则可得：$f(x_0) = \lim\limits_{x\rightarrow x_0}f(x)=\lim\limits_{k\rightarrow +\infty}f(x_{nk})= \lim\limits_{k\rightarrow +\infty}y_{nk}= M$，这与$M\notin S$矛盾，证毕。
## 可导性
- 通过(x,f(x))的切线的斜率是x的一个函数。这个函数被称为f的**导数**，记为 $f'$。我们说，对f关于变量x求导，得到函数 $f'$。
  - 导数度量函数输出对于函数输入变化的敏感程度。斜率只是一种直观的示意图。
  - 
- 如果极限 $\lim\limits_{h\rightarrow 0}{f(x+h)-f(x)\over h}$ 存在，则f在x点**可导**。否则f在x点不可导。
- 令$\Delta x = x_新 - x，\Delta y = y_新 - y$，则导数可写为 $f'(x) = \lim\limits_{\Delta x \rightarrow 0}{\Delta y \over \Delta x}$
- 令dx表示“x中十分微小（无穷小）的变化”，则可以用$dy \over dx$ 来代替$f'$
  - 读本科的时候不明白dx，后来读了陶哲轩的实分析才知道，dx几乎就是0的另一个说法，差别就是dx可以作被除数。
  - 量$dy\over dx$是y关于x的导数。
  - $dy \over dx$不是一个分数，它是当$\Delta x \rightarrow 0$时分数$\Delta y \over \Delta x$的极限。
  - $\Delta y$是实际的变化量，dy是当x改变$\Delta x$时，y改变量的线性主部。
  - dy是$\Delta y$的线性近似量，生而不精确。微积分因为可视为一门优化估计量的学问。

## 何时导数不存在
- 左导数：$\lim\limits_{h\rightarrow 0^-}{f(x+h)-f(x) \over h}$
- 右导数：$\lim\limits_{h\rightarrow 0^+}{f(x+h)-f(x) \over h}$
- 如果导数存在，那么左右导数都存在且都等于导数值。
  - 因为导数的定义是在点(x,f(x))处的斜率，以函数在x处有定义为前提，所以在改点有定义不用特别说明。

## 可导性和连续性
- 可导函数必连续，反之不一定成立。
  - 证明：设函数f(x)可导。
  - 则$f(x+h)-f(x)$ = ${f(x+h)-f(x)\over h}\times h$。
  - 根据f(x)可导知，$f(x+h)-f(x)\over h$等于常数C。
  - 所以，$\lim\limits_{h\rightarrow 0}{f(x+h)-f(x)\over h}\times h$ = $\lim\limits_{h\rightarrow 0}C \times h$ = 0，即$\lim\limits_{h\rightarrow 0}{f(x+h)-f(x)} = 0$，证毕。
  
# 求解微分问题
> **函数的微分**（Differential of a function），指对函数的局部变化的一种**线性描述**。微分可以近似地描述当函数自变量的取值作足够小的改变时，函数的值是怎样改变的。  
> 函数f(x)的自变量x有一个微小的改变h时，f(x)的变化可以分解为两个部分：一是线性部分，等于x的改变量乘以函数在x处的斜率，即$f'(x)h$；二是比h更高阶的无穷小，等于f(x)的实际改变量减去其线性部分。*线性部分就是函数在x处的微分**。  
> 数学表达：当x有改变量$\Delta x$时，y改变$\Delta y$。如果$\Delta y$可以表示为$A\Delta x + o(\Delta x)$，其中A是常数，$o(\Delta x)$是$\Delta x$的高阶无穷小，则称**线性主部$A\Delta x$为函数y的微分，记为dy**。
- **乘积法则**，如果 y = uv，则${dy\over dx} = {v{du \over dx}} + {u{dv\over dx}}$。如果y = uvw，则${dy\over dx} = {{du \over dx}vw} + {u{dv\over dx}w} + uv{dw\over dx}$
- **商法则**，如果 $y = {u\over v}$，那么${dy\over dx} = {{v{du\over dx}-u{dv\over dx}}\over v^2}$
- **链式求导法则**，如果y是u的函数，并且u是x的函数，那么${dy\over dx} = {dy\over du}{du \over dx}$

# 三角函数的极限和导数
## 三角函数的极限
- $\lim\limits_{x\rightarrow 0}{\sin x\over x} = 1$
  - 这个公式非常重要，是解决涉及三角函数的微积分问题的关键所在。
- $\lim\limits_{x\rightarrow 0}{\tan x \over x} = 1$
- 上述两个公式的证明，借助了单位圆上三角形的弧长面积公式，比较直观。

## 三角函数的导数
- ${d \over dx} \sin x = \cos x$
- ${d \over dx} \cos x = -\sin x$
- ${d \over dx} \tan x = \sec^2 x$
- ${d \over dx} \sec x = \sec x \tan x$
- ${d \over dx} \csc x = - \csc x \cot x$
- ${d \over dx} \cot x = - \csc^2x$

# 隐函数求导和相关变化率
- 如果方程F(x,y) = 0能确定y是x的函数，那么称这种方式表示的函数是隐函数。用y = f(x)表示的，称显函数。隐函数是相对于显函数来说的。
- 隐函数求导步骤
  - 在原始方程中，对每一项求导并使用链式求导法则、乘积法则以及商法则进行化简；
  - 如果想求$dy\over dx$，可重新整理并作除法来求解；
  - 如果想求斜率或者曲线一个特定点上的切线方程，可先带入x和y的已知值，接着重新整理并求$dy \over dx$，最后用点斜式来求切线方程。
- 量Q的**变化率**是Q关于时间的导数。
  - 如果Q是某个量，那么Q的变化率是$dQ \over dt$

# 指数函数和对数函数
## 指数函数（exponential function）回顾
1. $b^0 = 1$
1. $b^1 = b$
2. $b^xb^y = b^{x+y}$
3. ${b^x \over b^y} = b^{x-y}$
4. $(b^x)^y = b^{xy}$

## 对数函数(logarithmic function)回顾
> 对数$\log_b(y)$是为了得到y，你必须将底数b提升的**幂次**。
1. $\log_b(1) = 0$
2. $\log_b(b) = 1$
3. $\log_b(xy) = \log_b(x) + \log_b(y)$
   1. 证明：$b^{\log_b(x) + \log_b(y)} = b^{\log_b(x)} \times b^{\log_b(y)} = xy = b^{\log_b(xy)}$
   2. 所以 $\log_b(x) + \log_b(y) = \log_b(xy)$
4. $\log_b(x/y) = \log_b(x) - \log_b(y)$
5. $\log_b(x^y) = y\log_b(x)$
6. **换底法则** $\log_b(x) = {\log_c(x) \over \log_c(b)}$，意味着所有不同底数的对数函数其实是互为常数倍的。$\log_b(x) = K \log_c(x)$
   1. 证明：$c^{{\log_c(b)} \times \log_b(x)} = ({c^{{\log_c(b)}})^{\log_b(x)}}= x = c^{\log_c(x)}$
   2. 所以$\log_c(b) \times \log_b(x) = \log_c(x)$

## e的定义
- 自然对数底(natural base)
- $e = \lim\limits_{n\rightarrow \infty}{(1+{1 \over n})^{n}}$
- $e = \lim\limits_{h\rightarrow0}(1+h)^{1\over h}$
- $\lim\limits_{n \rightarrow \infty}{(1+ {x\over n})^n} = e^x$ 
- $\lim\limits_{h \rightarrow 0}{(1+ {xh})^{1\over h}} = e^x$ 
- 上面这些e的公式都是$1^\infty$这种形式。

## 对数函数和指数函数求导
1. ${d \over dx}\ln(x) = {1 \over x}$
   1. 根据幂函数$x^n$的求导规则，无法从幂函数中求得$x^{-1}$这个导数。这是ln被称为自然对数的原因之一。
2. ${d\over dx}\log_b{x} = {1 \over x\ln(b)}$
3. ${d\over dx}(b^x) = {b^x}\ln(b)$
4. ${d\over dx}(e^x) = e^x$
   1. 函数的导数是原函数，这很特殊

# 反函数和反三角函数
## 导数和反函数
- 如果f在其定义域（a,b）上**可导**且满足以下条件中的任意一条：
  - 对于所有的在（a,b）中的x,$f'(x) \gt 0$;
  - 对于所有的在（a,b）中的x,$f'(x) \lt 0$;
  - 对于所有的在（a,b）中的x,$f'(x) \geq 0$且对于有限个数的x,$f'(x) = 0$;
  - 对于所有的在（a,b）中的x,$f'(x) \leq 0$且对于有限个数的x,$f'(x) = 0$;
- 则f有反函数。
> 上面这些条件都为了明确一件事：保证反函数自变量到应变量的映射不会出现一对多的情况。

## 求反函数的导数
- 如果$y = f^{-1}(x)$，则${dy\over dx} = {1\over {f'(y)}}$
- 上式右边的变量是y，如果用x表达所有项，则有：${d\over dx}(f^{-1}(x)) = {1\over {f'(f^{-1}(x))}}$
  - 证明：反函数 $y = f^{-1}(x)$ 也可以写成 x = f(y)，对两边求隐函数导有${dx\over dx} = {d\over dx}f(y)$
  - 令u=f(y)，根据链式法则有${du\over dy}{dy\over dx} = 1$
  - 因为${du\over dy} = f'(y)$，所以${dy\over dx} = {1\over {f'(y)}}$
    >上边证明过程要点是：将反函数写成x = f(y)这个形式。虽然形式与原函数一样，但变量已经是反函数的变量。通过这个表达，将反函数的变量同原函数的函数形式f结合了起来。
> 反函数的导数就是原函数导数的倒数，但要注意导数表达式中的变量是y，不是x。

## 反三角函数
- ${d\over dx}\sin^{-1}(x) = {1\over {\sqrt{1-x^2}}}$，其中$-1 \lt x \lt 1$
  - 证明：因为${d\sin x \over dx} = {\cos x}$，所以${d \over dx}(\sin^{-1}x) = {1\over \cos(y)}$
  - 因为$\cos^2(y) + sin^2(y) = 1$，而$x = sin(y)$，所以$\cos y = \sqrt{1-x^2}$
  - 所以${d\over dx}(sin^{-1}x) = {1\over \sqrt{1-x^2}}$，其中$-1\lt x\lt 1$
- ${d\over dx}\cos^{-1}(x) = -{1\over {\sqrt{1-x^2}}}$，其中$-1 \lt x \lt 1$
- ${d\over dx}{\tan^{-1}(x)} = {1\over {1+x^2}}$

# 导数(derivative)和图像
- 如果当x=a时，f(a)是函数f整个定义域内的最大值，我们就说它是**全局最大值**。
  - 在(closed interval)闭区间[a,b]内求全局最大值和最小值的步骤：
  - （1）找出f'(x)，并列出在(a,b)中f'(x)不存在或f'(x)=0的点。也就是说，列出在开区间(a,b)内所有临界点。
  - （2）把端点x=a和x=b放入上述列表。
  - （3）对于上述列表中的每一个点，将它们代入y=f(x)以求出它们所对应的函数值。
  - （4）找出最大的函数值以及它所对应的x的值，这就是全局最大值。
  - （5）用同样的方法找出最小的函数值和全局最小值。
- 在包含a的某一小段区间内，如果在x=a处，f(a)有最大值，我们就称这点为**局部最大值**。
- 如果函数在x=c处的导数为零或不存在，我们就称x=c为**临界点**(critical point)。
- **极值定理**：假设函数f定义在开区间(a,b)内，并且点c在(a,b)区间内。如果点c为函数的局部最大值或最小值，那么点c一定为该函数的临界点。也就是说，$f'(c)=0$或$f'(c)$不存在。
  - 证明：假设f在x=c有一个局部最小值。
  - 如果f'(c)存在，那么$f'(c) = \lim\limits_{n\rightarrow 0}{f(c+h)-f(c)\over h}$
  - 由于f在c上有一个局部最小值，因而当c+h非常接近c时，$f(c+h)\geq f(c)$，当$h\gt 0$时，量$\lim\limits_{h\rightarrow 0^+}{f(c+h)-f(c)\over h}\geq 0$；当$h\lt 0$时，$\lim\limits_{h\rightarrow 0^-}{f(c+h)-f(c)\over h} \leq 0$。
  - 又因为f'(c)存在，所以左极限等于右极限，所以$f'(c)=0$，证毕。
- **罗尔定理**：假设函数f在闭区间[a,b]内连续，在开区间(a,b)内可导。如果f(a)=f(b)，那么在开区间(a,b)内至少存在一点c，使得f'(c)=0
  - 证明：由最大值最小值定理，有f在[a,b]内有一个全局最大值和一个全局最小值。
  - 如果最大值或最小值中任何一个出现在(a,b)内的某个数c上，那么极值定理告诉我们f'(c)=0
  - 否则，全局最大值和最小值都出现在端点a和b上，这意味着f(x)=f(a)=f(b)，即该函数为常数。证毕。
- **中值定理**(mean value theorem)：假设函数f在闭区间[a,b]内连续，在开区间(a,b)内可导，那么在开区间(a,b)内至少有一点c使得$f'(c) = {f(b)-f(a)\over (b-a)}$
  - 中值定理的几个推论：（1）如果对于在定义域(a,b)内的所有x，都有f'(x)=0，那么函数f在开区间(a,b)内为常数函数。（2）如果对于任意实数x都有f'(x)=g'(x)，那么有f(x)=g(x)+C (C为常数)。（3）如果函数f的导函数始终为正，那么该函数为增函数。也就是说，如果$a\lt b,则有f(a)\lt f(b)$
  - 证明：令$g(x) = f(x)-{f(b)-f(a)\over {b-a}}(x-a)$
  - $g(a) = f(a) - {f(b)-f(a)\over {b-a}}(a-a) = f(a)$且$g(b) = f(b) - {f(b)-f(a)\over {b-a}}(b-a) = f(a)$
  - 因为g(a)=g(b)，应用罗尔定理知，存在常数c，使得$g'(c)=0$，即$0=f'(c)-{f(b)-f(a)\over {b-a}}$，证毕。
- **拐点**(inflection point)：函数改变凹凸性的点。
  - 如果x=c点是函数f的拐点，则有$f''(c)=0$
  - 如果$f''(c)=0$，则c点不一定都是函数f的拐点
  - > 拐点要求$f''$在点c前后改变符号，所以在c点上$f''$必为0，但在c点处$f''$为0却不改变符号的则不是拐点。
- $f'(c)=0$时，有：
  - 如果从左往右通过c点，$f'(x)$符号由正变负，那么c点为局部最大值；
  - 如果从左往右通过c点，$f'(x)$符号由负变正，那么c点为局部最小值；
  - 如果从左往右通过c点，$f'(x)$符号不变，那么c点为水平拐点；
- $f'(c)=0$时，有：
  - 如果$f''(c)\lt 0$，那么x=c为局部最大值；
  - 如果$f''(c)\gt 0$，那么x=c为局部最小值；
  - 如果$f''(c) = 0$，那么需要使用一阶导数方法进行判断。

# 最优化和线性化
> 微积分的两个实际应用：最优化和线性化  
> **最优化**涉及找出各种可能情况中最好的一种  
> **线性化**是一种对难以计算的量找出其估算值的有用技术  

## 最优化问题：一般方法
1. 识别出所有你可能用到的变量。其中之一应该是你想要最大化或最小化的变量Q
2. 试探一下当前情况的极端可能，看变量能最大或最小到多少
3. 写出关联不同变量的各个方程。其中之一应该是关于Q的方程
4. 努力通过这些方程消去其他变量，**使得Q可以表示为只关于一个变量的函数**
5. 对Q关于那个变量求导，然后找出临界点
6. 求出Q在临界点及端点所对应的值，从中选出最大值和最小值。使用一阶或二阶导数的符号表格对临界点进行分类，加以检验
7. 写出所得到的结论
   
## 线性化问题：一般方法
> $df = f'(a)\Delta x$，量df被称为f在x=a处的**微分**。它是对当x从a变化为a+$\Delta x$时f的变化量的**近似**。  
- 估算或近似计算一个难搞定的数的**基本策略**：
  - 写出主要公式：$f(x)\approx L(x) = f(a) + f'(a)(x-a)$
  - 选择一个函数f以及一个数x，使得这个难搞定的数等于f(x)。另外，选取一个接近x的a，并使得f(a)可以容易算得
  - 对f求导，找出f'(x)
  - 在上述方框公式中，用实际的函数分别替代f和f'，用你选定的实际数值替代a
  - 最后，把第二步中的x值代入公式加以计算。另外注意到微分df等于量f'(a)(x-a)
  > 线性估算的基本思路是用容易计算的线性函数替换原函数，用容易计算的近似值替换原自变量值，然后以此估算原函数在原自变量处的值。

## 牛顿法
- **牛顿法**：假设a是对方程f(x)=0的解的一个近似。如果令$b = {a - {f(a)\over f'(a)}}$，则在很多情况下，b是个比a更好的近似。
  - 牛顿法的**基本思想**是，通过使用f在x=a处的线性化来改善估算。
  - 证明：令$f(x) \approx L(x) = f(a) + f'(a)(x-a)$
  - 则$f(b) \approx f(a) + f'(a)(b-a) = 0$
  - $b = {a-{f(a) \over f'(a)}}$，证毕。
- 牛顿法失效的四种情况
  - f'(a)的值接近于0
  - 如果f(x) = 0有不止一个解，可能得到的不是你想要的那个解
  - 近似可能变得越来越糟
  - 你可能陷入一个循环而无法自拔
- 可以通过连续使用牛顿法，得到原函数解的越来越准确的近似值。

# 洛必达法则
- **洛必达法则**：如果$f(a)=g(a)=0，那么\lim\limits_{x\rightarrow a}{f(x)\over g(x)}={f'(x)\over g'(x)}$
- **基本思想**：当f和g可导，且f(a)和g(a)等于0时。对于求解形如$\lim\limits_{x\rightarrow a}{f(x)\over g(x)}$这样的不定式，考虑在x=a处，对它们线性化，以近似求解。  
  - 证明：$f(x) \approx f(a) + f'(a)(x-a)， g(x) \approx g(x) + g'(a)(x-a)$
  - 因为f(a)=0，g(a)=0
  - 所以${f(x) \over g(x)} \approx {f'(a)(x-a)\over {g'(a)(x-a)}}={f'(a)\over g'(a)}$，证毕。
- ${0\over 0}和{\infty\over \infty}$型：直接用洛必达法则求解
- ${\infty - \infty}$型：通分或同时乘以/除以一个共轭表达式，从而转为$0\over 0$型
- $0\times \infty$型：将其中一个取倒数，移到分母
- $f(x)^{g(x)}$型：考虑先取对数，转化为$0\over 0$型求导，然后取指数，转回去。

# 积分(integral)
- **求和符号**：$\sum\limits_{j=1}^n {1\over j^2}$，其中的j只是虚拟变量，是个临时的替代者，我们把它叫作**求和指标**。
- **伸缩级数**：$\sum\limits_{j=a}^b(f(j)-f(j-1))=f(b)-f(a-1)$
  - 伸缩级数的关键是展开式中，前后项互相抵消，最后只留下首项减末项。
  - 伸缩级数之所以重要，是因为求积分的黎曼和会用到

# 定积分
- **定积分**：$\int_a^bf(x)dx={\lim\limits_{mesh\rightarrow 0}\sum\limits_{j=1}^nf(c_j)(x_j-x_{j-1})}$，其中$a=x_0\lt x_1\lt x_2 \lt ... \lt x_{n-1} \lt x_{n} = b$并且对于每一个j=1,...,n都有$c_j$在$[x_{j-1},x_j]$内。
  - $\sum\limits_{j=1}^nf(c_j)(x_j-x_{j-1})$称为**黎曼和**。它给出了定积分的**估算值**。
- 定积分的性质：
  - $\int_b^af(x)dx = -\int_a^bf(x)dx$
  - $\int_a^af(x)dx = 0$
  - $\int_a^bf(x)dx = \int_a^cf(x)dx + \int_c^bf(x)dx$，其中c不一定在[a,b]中
  - 线性齐次性：$\int_a^bCf(x)dx = C\int_a^bf(x)dx$，常数可以移到积分表达式外面
  - 线性可加性：$\int_a^b(f(x)+g(x))dx = \int_a^bf(x)dx + \int_a^bg(x)dx$，和或差的积分等于积分的和或差
  - 可积函数f的平均值：函数f在区间[a,b]内的平均值= ${1\over {b-a}}\int_a^bf(x)dx$
  - 积分的中值定理：如果函数f在区间[a,b]上连续，那么在开区间(a,b)内总有一点c，满足$f(c) = {{1\over {b-a}}\int_a^bf(x)dx}$

# 微积分基本定理
- **微积分第一基本定理**：如果函数f在闭区间[a,b]上是连续的，定义F为$F(x) = \int_a^xf(t)dt, x\in [a,b]$ 则F在开区间(a,b)内是可导函数，而且$F'(x)=f(x)$
  - 简而言之，${d\over dx}\int_a^xf(t)dt = f(x)$
  - 因为F(x)的导数是f(x)，所以F(x)被称为f(x)的**反导数**
    - 证明：$F(x) = \int_a^xf(t)dt, F(x+h) = \int_a^{x+h}f(t)dx$
    - 根据积分中值定理，存在$c\in [x,x+h]$，使得$F(x+h)-F(x)=f(c)\times h$，所以${{F(x+h)-F(x)}\over h} = f(c)$
    - 当$\lim\limits_{h\rightarrow 0}{{F(x+h)-F(x)}\over h} = \lim\limits_{c\rightarrow x}f(c) = f(x)$，证毕。
- **微积分第二基本定理**：如果函数f在闭区间[a,b]上是连续的，F是f的任意一个关于x的反导数，那么有$\int_a^bf(x)dx = F(b)-F(a)$
> 从微积分基本定理可知，积分和求导互为逆运算。
- **求导数公式**
  - ${d\over dx}x^a = ax^{a-1}$
  - ${d\over dx}\ln(x) = {1\over x}$
  - ${d\over dx}e^x = e^x$
  - ${d\over dx}b^x = b^x\ln(b)$
  - ${d\over dx}\sin x = \cos x$
  - ${d\over dx}\cos x = -\sin x$
  - ${d\over dx}\tan x = \sec^2 x$
  - ${d\over dx}\sec x = \sec x \tan x$
  - ${d\over dx}\cot x = -\csc^2 x$
  - ${d\over dx}\csc x = -\csc x \cot x$
  - ${d\over dx}\sin^{-1} x = {1\over \sqrt{1-x^2}}$
  - ${d\over dx}\tan^{-1} = {1\over {1+x^2}}$
  - ${d\over dx}sec^{-1} x = {1\over {|x|\sqrt{x^2-1}}}$
  - ${d\over dx}\sinh x = \cosh x$
  - ${d\over dx}\cosh x = \sinh x$
- **求积分公式**
  - $\int x^adx = {x^{a+1} \over {a+1}} + C$，如果$a\neq -1$
  - $\int {1\over x}dx = \ln |x| + C$
  - $\int e^xdx = e^x + C$
  - $\int b^xdx = {b^x\over \ln b} + C$
  - $\int \cos xdx = \sin x + C$
  - $\int \sin xdx = -\cos x + C$
  - $\int \sec^2 xdx = \tan x + C$
  - $\int \sec x \tan xdx = \sec x + C$
  - $\int \csc^2 xdx = -\cot x + C$
  - $\int \csc x \cot xdx = -\csc x + C$
  - $\int {1\over \sqrt{1-x^2}}dx = \sin^{-1} x + C$
  - $\int {1\over \sqrt{1+x^2}}dx = \tan^{-1} x + C$
  - $\int {1\over {|x|\sqrt{x^2-1}}}dx = \sec^{-1} x + C$
  - $\int \cosh xdx = \sinh x + C$
  - $\int \sinh xdx = \cosh x + C$

# 求积分的方法
- 换元法
  - **换元法**的基本思想是，**逆用求导的链式法则**
  - 设$F'(t) = f(t)$，令t = g(x)
  - 根据链式法则有：$\int F'(g(x))g'(x)dx = F(g(x)) + C$
  - 所以:$\int f(g(x))g'(x)dx = F(g(x)) + C$
  - > 这里的关键是令新变元等，于其导数g'(x)也在其中的函数g(x)
- 分部积分法
  - **分部积分法**的基本思想是，**逆用求导的乘法法则**
  - 根据乘法法则：${d\over dx}(uv) = v{du \over dx} + u{dv\over dx}$
  - 两边同时对x求积分得：$\int u{dv\over dx}dx = \int {d\over dx}(uv)dx - \int v{du\over dx}dx$
  - 因为上式第二项是对函数uv先求导再积分，所以原函数不变
  - 化简得：$\int u{dv\over dx}dx = uv - \int v{du\over dx}dx$，这就是分部积分公式
- **三角换元法**
  - 类型1：$\sqrt{a^2-x^2}$，令$x=a\sin \theta$
  - 类型2：$\sqrt{x^2 + a^2}$，令$x=a\tan \theta$
  - 类型3：$\sqrt{x^2 - a^2}$，令$x=a\sec \theta$

# 反常积分
- 如果积分$\int_a^bf(x)dx$有以下情况，就是反常积分：
  - 函数f在闭区间[a,b]内是无界的：$f(x_i) = \infty$
  - $b = \infty$
  - $a = -\infty$
- 当下面这些极限存在时，积分收敛，否则发散：
  - 当a是破裂点：$\int_a^bf(x)dx = \lim\limits_{\epsilon\rightarrow 0^+}\int_{a+\epsilon}^bf(x)dx$。
  - 当b是破裂点：$\int_a^bf(x)dx = \lim\limits_{\epsilon\rightarrow 0^+}\int_{a}^{b-\epsilon}f(x)dx$
  - $\int_a^\infty f(x)dx = \lim\limits_{N\rightarrow \infty}\int_{a}^{N}f(x)dx$
  - $\int_{-\infty}^b f(x)dx = \lim\limits_{N\rightarrow \infty}\int_{-N}^{b}f(x)dx$
- **比较判别法**：如果函数f和g在x=a点都有垂直渐近线，在其他地方没有破裂点，且区间[a,b]内的所有x都有$0\leq f(x)\leq g(x)$，那么，我们有：$0\leq \int_{a+\epsilon}^bf(x)dx \leq \int_{a+\epsilon}^bg(x)dx$，对于任何$\epsilon \gt 0$成立。现在取极限，如果反常积分$\int_a^bg(x)dx$收敛，则原函数收敛。
- **极限比较判别法**：如果当$x\rightarrow a$时，$f(x)\sim g(x)$，且这两个函数在区间[a,b]上没有其他的瑕点了，那么积分$\int_a^bf(x)dx和\int_a^bg(x)dx$是同时收敛或同时发散的。
  - 当$x\rightarrow a$时，$f(x)\sim g(x)$ 意即 $\lim\limits_{x\rightarrow a}{f(x)\over g(x)} = 1$
- **p判别法**：
  - $\int^\infty$的情况：对于任何有限值$a\gt 0$，积分$\int_a^\infty{1\over x^p}dx$，在$p\gt 1$时是收敛的，在$p\leq 1$时是发散的。
  - $\int_0$ 的情况：对于任何有限值$a\gt 0$，积分$\int_0^a{1\over x^p}dx$，在$p\lt 1$时是收敛的，在$p\geq 1$时是发散的。
- **绝对收敛判别法**：如果$\int_a^b|f(x)|dx$是收敛的，那么$\int_a^bf(x)dx$也是收敛的。
  > 对于所有的$0\lt x \lt 1, |\ln x| \leq {C\over x^a}$。这里的原理是，当$x\rightarrow 0^+$时对数函数缓慢趋于$-\infty$。对于任何$a\gt 0$，幂函数$x^a$在$x\rightarrow 0$时，趋于$\infty$的速度都要比对数函数快。

# 数列和级数
> 研究级数是为了引出幂级数  
> 研究幂级数是为了介绍泰勒级数  
> 搞出泰勒级数是为了（通过幂级数）近似表示复杂函数
## 数列
- **数列**，是一列有序的数(order matters)，可能有有限项，也可能有无穷项，后者称**无穷数列**。
  - $\{a_n\} = a_1,a_2,a_3,...$
- 令数列的第n项为$a_n$，如果极限$\lim\limits_{n\rightarrow \infty}a_n = L$存在，则数列$\{a_n\}$收敛，否则发散。
- **等比数列**：取常数r，并考虑从n=0开始取值的数列$a_n=r^n$。这是个等比数列，且有以下规则：
$$
\lim\limits_{n\rightarrow \infty}r^n =
\begin{cases}
=0, & \text{如果$-1\lt r \lt 1$}\\  
=1, & \text{如果$r=1$}\\  
=\infty, & \text{如果$r\gt 1$}\\  
{不存在}, & \text{如果$r \leq {-1}$}  
\end{cases}
$$
- **另一个数列**：令k为任意常数，数列第n项为$a_n = {(1+{k\over n})^n}$，则$\lim\limits_{n\rightarrow \infty}(1+{k\over n})^n = e^k$
## 级数的收敛与发散
- **级数**就是数列的和，即将数列$a_n$的各项都加起来。
  - $\sum\limits_{n=1}^\infty a_n = a_1+a_2+a_3+...$
- 无穷级数的值：$\sum\limits_{n=1}^\infty a_n = {\lim\limits_{N\rightarrow \infty}\sum\limits_{n=1}^Na_n}$。如果右边的极限不存在，则左边的级数发散。
- **几何级数**(等比级数): $\sum\limits_{n=0}^\infty r^n = 1+r+r^2+r^3+...$
  - 如果$-1\lt r \lt 1$，$\sum\limits_{n=0}^\infty r^n = {1\over {1-r}}$；如果$r\geq 1或r \leq -1$，级数发散。
- **第n项判别法**：若$\lim\limits_{n\rightarrow \infty}a_n \neq 0$，或极限不存在，则级数$\sum\limits_{n=1}^\infty a_n$发散。
  - 任何时候都要首先考虑第n项判别法！
- **比式判别法**：若$L = \lim\limits_{n\rightarrow \infty}|{a_{n+1}\over a_n}|$，则$n=\sum\limits_{n=1}^\infty a_n$在$L\lt 1$时绝对收敛，在$L \gt 1$时发散；但当$L=1$或极限不存在时，比式判别法无效。
  - 若级数中包含阶乘，则用比式判别法。
- **根式判别法**：若$L=\lim\limits_{n\rightarrow \infty}|a_n|^{1\over n}$，则$n=\sum\limits_{n=1}^\infty a_n$在$L\lt 1$时绝对收敛，在$L\gt 1$时发散；但当$L=1$或极限不存在时，比式判别法无效。
  - 当级数通项的指数为特殊的关于n的函数时，用根式判别法。
- **积分判别法**：若对连续递减函数f有$a_n=f(n)$，则$\sum\limits_{n=N}^\infty a_n$与$\int_N^\infty f(x)dx$同时收敛或同时发散。
  - 当级数同时含有$1\over n$和$\ln (n)$时，可用积分判别法。
- **交错级数判别法**：若级数$\sum\limits_{n=1}^\infty a_n$是交错的，且各项的绝对值递减趋于0，则级数收敛。也就是说，$a_n$正负交错，$|a_n|$递减，且$\lim\limits_{n\rightarrow \infty}|a_n|=0$，则级数收敛。
  - 证明：设交错级数$\{a_n\}$的奇数项为正，偶数项为负。考虑奇数数列和$A_{0},A_{2},A_{4},...$，因为$a_{0}\gt |a_{1}| \gt a_{2}$，必有$A_{0}\gt A_{2}\gt A_{4} ...$。类似地，有$A_{1} \lt A_{3} \lt A_{5} ...$。所以，$A_N$必收敛于$[A_0,A_1]$中。
- **比较判别法、极限比较判别法和p判别法**：同反常积分有关判别法。
  - 当其他判别法不能使用时，对正项级数应用这些判别法。

# 泰勒多项式、泰勒级数和幂级数导论
- **泰勒近似定理**：若f在x=a光滑，则在所有次数为N或更低的多项式中，当x在a附近时，最近似于f(x)的是$P_N(x) = f(a) + f'(a)(x-a) + {f''(a)\over {2!}}(x-a)^2+ ...+{{f^{N}(a)}\over {N!}}(x-a)^N$，用求和号表示为$P_N(x) = \sum\limits_{n=0}^N{f^{(n)}(a)\over n!}(x-a)^n$
  - 我们称多项式$p_N$为f(x)在x=a处的**N阶泰勒多项式**。
  - $P_N$的重要性质是，对所有n=0,1,2...N，$P_N^{(n)}(a) = f^{(n)}(a)$，即当x=a时，$P_N$的所有N阶导及以下的导数值都与f的对应值相等，但是$P_N$的所有更高阶导数处处为0。函数$P_N$利用了f在x=a处直到N阶导数的所有信息。
  - 之所以每项有指数n和阶乘n!，是为了满足上面这条性质。
- **泰勒定理**：关于x=a的N阶余项$R_N(x)={f^{N+1}(c)\over{(N+1)!}}(x-a)^{N+1}$，其中c是介于x与a之间的一个数。
  - 由于$f(x) = P_N(x) + R_N(x)$，所以$f(x)=\sum\limits_{n=0}^N{f^{(n)}(a)\over {n!}}(x-a)^n + {f^{(N+1)}\over (N+1)!}(x-a)^{N+1}$
  - 当$N=0, f(x) = P_0(x)+R_0(x)=f(a)+f'(c)(x-a)$，所以泰勒定理是中值定理的扩展。
  - 当$N=1, f(x)= f(a) + f'(a)(x-a) + {f''(c)\over {2!}}(x-a)^2 = L(x) + R_1(x)$，其中L(x)是f关于x=a的线性化部分。
- **麦克劳林级数**：是f关于x=0的泰勒级数的另一个名字，即 $f(x) = \sum\limits_{n=0}^\infty {f^{(n)}(0)\over {n!}}x^n$
- 泰勒级数的收敛性：函数f(x)等于它的泰勒级数，若想证明一个函数在某些数x处等于它的泰勒级数，可尝试证明当$N\rightarrow \infty时R_N(x)\rightarrow 0$
- 常见麦克劳林级数：
  - $e^x = \sum\limits_{n=0}^\infty {x^n\over {n!}} = 1+x+{x^2\over{2!}} + {x^3\over {3!}}+...$
  - $\sin x = \sum\limits_{n=0}^\infty {{(-1)^nx^{2n+1}}\over {(2n+1)!}} = x - {x^3\over {3!}} + {x^5\over {5!}} - {x^7\over {7!}} + ...$
  - $\cos x = \sum\limits_{n=0}^\infty {(-1)^nx^{2n}\over {(2n)!}} = 1 - {x^2\over {2!}} + {x^4\over {4!}} - {x^6\over {6!}} + ...$
  - ${1\over {1-x}} = \sum\limits_{n=0}^\infty x^n = 1+x+x^2+x^3+...$
  - $\ln (1+n) = \sum\limits_{n=1}^\infty {-{(-1)^nx^n}\over n} = x-{x^2\over 2}+{x^3\over 3}-{x^4\over 4}+ ...$
  - $\ln (1-n) = \sum\limits_{n=1}^\infty {-{x^n}\over n} = -x-{x^2\over 2}-{x^3\over 3}-{x^4\over 4}- ...$
  - 利用幂级数和泰勒级数求导：因为f(x)关于x=a的泰勒级数的第n项系数公式为$a_n={f^{(n)}(a)\over {n!}}$，所以$f^{(n)}(a) = n!\times a_n$

# 参数方程和极坐标
- **参数方程**：x和y不直接相关而是通过一个公共参数相联系
  - 例如，$x=3\cos t$和$y=3\sin t$。若选定t的值，则可通过将t值代入上面的方程求得相应的x和y值。变量t被称为参数，上述方程被称为参数方程。
- 参数方程的导数：${dy\over dx} = {{dy/dt}\over {dx/dt}}$
- **极坐标**：极坐标下的点表示为$(r,\theta)$，笛卡尔坐标和极坐标的关系为$x=r\cos \theta, y=r\sin \theta$
- **面积公式**：$\int_{\theta_0}^{\theta^1}{1\over 2}r^2d\theta$

# 复数
- **虚数**：一个数是虚数，意思是它的平方是一个负数。虚数的唯一形式是yi，其中y是不为0的实数。
- **复数**：形如x+yi的数即复数，x称为实部，y称为虚部。
- **欧拉恒等式**：$e^{i\theta} = \cos (\theta) + i\sin (\theta)$
  - 证明：$e^{i\theta} = 1+(i\theta)+{(i\theta)^2\over 2!}+{(i\theta)^3\over 3!}+{(i\theta)^4\over 4!}+{(i\theta)^5\over 5!}+{(i\theta)^6\over 6!}+{(i\theta)^7\over 7!}+...=1+{i\theta}-{\theta^2\over 2!}-i{\theta^3\over 3!}+{\theta^4\over 4!}+i{\theta^5\over 5!}-{\theta^6\over 6!}-i{\theta^7\over 7!}+...$
  - 又因为上式的实部$1-{\theta^2\over 2!}+{\theta^4\over 4!}-{\theta^6\over 6!}+...=\cos \theta$，虚部$\theta - {\theta^3\over 3!}+{\theta^5\over 5!}-{\theta^7\over 7!}+...=\sin \theta$
  - 所以$e^{i\theta} = \cos \theta + i\sin \theta$
- 若(x,y)和$(r,\theta)$为相同的点，则$x+yi= re^{i\theta}$
  - $e^{i\theta}$关于$\theta$是周期的，且周期为$2\pi$。
  - 在复平面上，$e^{i\theta}$绕着原点，以1为半径，作逆时针圆周运动。
- 为何要用**极坐标形式**：极坐标形式比较容易进行乘法和取幂运算。比如 $3e^{i\pi/4}\times 2e^{-i(3\pi/8)} = 6e^{i(\pi/4-3\pi/8)}$，而$(3e^{i\pi/4})^{200} = 3^{200}e^{i(\pi/4)\times {200}}$
- $e^{i\theta}$是一类极坐标形式，因为它等于$\cos \theta + \sin \theta i$。令$x=r\cos \theta, y=r\sin \theta i$，则$x + yi = re^{i\theta}$

# 微分方程
> 微分方程就是包含导数的方程，它们对于描述现实世界中量的变化非常有用。  
> 一个微分方程的阶就是其所包含的最高阶导数的阶。  
> 微分方程问题很难求解，基本上是**不可能求解**的。有以下三种简单类型有解。
## 可分离变量的一阶微分方程
- 如果能够把一阶微分方程中所有关于y的部分（包括dy）放在一边，所有关于x的部分（包括dx）放在另一边，则该微分方程被称为是**可分离变量的**。
- 对于可分离变量的一阶微分方程，先将变量分离至等号两边，然后积分求解即可。
  
## 一阶线性方程
- 形如 ${dy\over dx}+p(x)y = q(x)$，其中p和q是关于x的函数。这样的方程称为**一阶线性微分方程**。
- **一阶线性微分方程**指的是，$y$和$dy/dx$的幂次都是1.
- 求解一阶线性微分方程的步骤：
  - 将包含y的部分放在左边，包含x的部分放在右边，然后两边除以dy/dx的系数，得到一个标准的一阶线性微分方程：${dy\over dx}+p(x)y = q(x)$
  - 两边都乘以积分因子：$f(x) = e^{\int p(x)dx}$
  - 左边变为：${d\over dx}(f(x)y)$，其中f(x)是积分因子。
  - 两边积分，并在右边加上常数项C
  - 除以积分因子，解出y
- 为什么积分因子起作用？
  - 因为加上积分因子以后，左式配成符合导数乘积法则的形式。$dy\over dx$就是对y求偏导的结果，$p(x)y$就是对积分因子求偏导后的结果。所以根据链式法则，积分因子为$e^{\int p(x)dx}$。
  - 将积分因子$e^{\int p(x)dx}$乘以方程${dy\over dx}+p(x)y = q(x)$两边
  - 得到$e^{\int p(x)dx}{dy\over dx} + e^{\int p(x)dx}p(x)y = 关于x的部分$
  - 根据求导的乘积法则，上式变成：${d\over dx}(e^{\int p(x)dx}y) = 关于x的部分$
  - 两边积分可得解。

## 常系数微分方程
- **常系数微分方程**是形如$a_n{d^ny\over dx^n}+...+a_2{d^2y\over dx^2} + a_1{dy\over dx} + a_0y = f(x)$这样的方程式，其中f(x)是关于x的函数，$a_n,...,a_1,a_0$是常实数。
- 形如${dy\over dx}-3y = 0$这样的方程（右边没有关于x的部分），称为**齐次的**。
- 解**一阶齐次方程** ${dy\over dx}+ay = 0$的解为：$y=Ae^{-ax}$，其中A是常数。
- 解**二阶其次方程**$a{d^2y\over dx^2}+b{dy\over dx} + cy =0$
  - 首先写出特征二次方程：$at^2+bt+c=0$，并解t
  - 若有两个不同实根$\alpha和\beta$，解为$y = Ae^{\alpha x} + Be^{\beta x}$
  - 若只有一个双重实根$\alpha$，解为：$y = Ae^{\alpha x} + Bxe^{\alpha x}$
  - 若有两个复根，它们是共轭的，即形如$\alpha \plusmn i\beta$，解为：$y = e^{\alpha x}(A\cos(\beta x)+B\sin(\beta x))$
- 为什么特征二次方程适用？
  - 将$y=e^{\alpha x}$代入方程$ay''+by'+cy=0$，得$a\alpha ^2e^{\alpha x}+b\alpha e^{\alpha x} + ce^{\alpha x} = (a\alpha ^2+b\alpha +c)e^ {\alpha x}$
  - 所以，如果$\alpha$为特征二次式$at^2+bt+c$的一个根，则有$a\alpha^2+b\alpha +c = 0$。上述等式，暗示了$ay''+by'+c=0$，即$y=e^{\alpha x}$解出了微分方程。
  - 如果二次方程的两个解是共轭复根，则解为$y = Ae^{(\alpha +i\beta)}x+Be^{(\alpha -i\beta x)} = e^{\alpha x}(Ae^{i\beta x}+Be^{-i\beta x})$，由欧拉公式得$y = e^{\alpha x}(A(\cos(\beta x)+i\sin(\beta x))+B(\cos(\beta x)-i\sin(\beta x)))=e^{\alpha x}((A+B)cos(\beta x)+(A-B)i\sin(\beta x))$
  - 如果特征二次方程只有一个根$\alpha$，将$y = xe^{\alpha x}$带入微分方程$ay''+by'+c=0$，得$ay''+by'+cy=(a\alpha^2+b\alpha+c)xe^{\alpha x}+(2a\alpha + b)e^{\alpha x}$。如果$\alpha$是$at^2+bt+c$的双重根，则不仅$a\alpha^2+b\alpha+c=0$，而且$2a\alpha + b = 0$，由此可推出双重根解。
- 求**特解**：对于非齐次方程，要猜一个特解（记为$y_p$），并代入原方程求解。
  - 如果f是一个次数为n的多项式，则$y_p$=次数为n的一般多项式
  - 如果f是指数$e^{kx}$的倍数，则$y_p = Ce^{kx}$
  - 如果f是$\cos(kx)$的倍数+$\sin(kx)$的倍数，则$y_p = C\cos(kx)+D\sin(kx)$
  - 注意：$y_p和y_h$可能会发生冲突（形式相同），这时候要将$y_p$乘以x或$x^2$。
- 求解非齐次方程步骤总结：
  - 先将方程整理成正确的形式，一阶形式方程化简为${dy\over dx}+ay = f(x)$，二阶形式化简为$a{d^2y\over dx^2} + b{dy\over dx}+cy = f(x)$
  - 求解相应的齐次方程，${dy\over dx}+ay = 0$和${d^2y\over dx^2} + b{dy\over dx}+cy = 0$，并将齐次方程的解记为$y_h$
  - 写出特解$y_p$的形式，并代入原方程，令系数相等来求待定常数
  - 最后解为:$y = y_h+y_p$