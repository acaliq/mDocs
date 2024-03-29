凸优化
> 凌青
> 2022-5-7

- 我搞这个摘录是为了让自己容易理解，
- 不是把原文摘抄得准确、完整，
- 也不是为了存档留作纪念。
  
# Chapter 1

## Lecture 1

优化/数学规划
Optimization/Mathematical Programming
凸优化是优化的一种，是一类比较简单的优化问题。
优化和数学规划是同义词。

**优化**，是从一个可行解的集合中，找出最优的元素。

## Lecture 2

优化问题分类：

1. 线性规划/非线性规划

$$f(\alpha x+ \beta y) = \alpha f(x) + \beta f(y)$$

线性规划问题的解，都是在边上或顶点上。

2. 凸规划/非凸规划

$$f(\alpha x+ \beta y) \leq \alpha f(x) + \beta f(y)$$

任何一个线性规划问题都是凸规划问题。

3. 光滑/非光滑

光滑：函数在每个点都是可微的。

4. 连续/离散

离散问题通常是非凸规划问题。

5. 单目标/多目标

多目标：帕累托曲线，在帕累托曲线上的任意一点，无法在降低一个目标值的同时，降低另一个目标值。

对于一个优化问题，如果能将其**构造成**凸优化问题，那就相当于解决了问题的90%。

主要内容：

1. 凸集、凸函数、凸优化
2. 凸优化
3. 若干凸优化的算法

拉格朗日：
通过一个**拉格朗日乘子**，将约束条件纳入目标。

**动态优化**(Dynamic Programming)，是Bellman发明的用来解决优化问题一个算法。（从后往前解决优化问题）

博弈论，纳什均衡。

单纯形法，内点法是解决复杂线性规划问题最成功的算法。

## Lecture 3

优化问题的一般形式：
$$
min  f_0(X)
$$$$
s.t. f_i(X) \leq b_i, i=1,2,...
X=[x_1,x_2,...,x_n]^T
$$

凸规划/非凸规划

# Chapter 2: Convex Sets

## Lecture 4

**仿射集** Affine Sets
> 一个集合c是仿射集，若$\forall  X_1,  X_2 \in c$，则连接$ X_1$和$ X_2$的直线也在集合内。

设$X_1,...,X_k \in c, \theta_1,...,\theta_k \in R$。如果$\theta_1+...+\theta_k = 1$，那么仿射组合$\theta_1X_1+...+\theta_kX_k \in c$

任意线性方程组的解集是仿射集。
任意仿射集可以写成线性方程组的解集。

任意集合c，如何构造尽可能小的仿射集？
关于c的仿射包 $\Bbb{aff} c = \{\theta_1 x_1+...+\theta_k | \forall x_1,...,x+k \in c, \forall \theta_1+...+\theta_k = 1 \}$

**凸集** Convex Set
> 一个集合是凸集，当任意两点之间的线段仍然在c内。
c为凸集$\lrArr$若$\forall x_1, x_2 \in c, \forall \theta \in [0,1]$， 有$\theta x_1 + (1-\theta)x_2 \in c$。

$x_1, x_2,...,x_k$的**凸组合**是$x_1\theta_1+ x_2\theta_2+...+x_k\theta_k$。如果$\theta_1,...,\theta_k \in R$，$\theta_1+...+\theta_k = 1, \theta_1,...,\theta_k \in [0,1] $。

c为凸集$\lrArr$任意元素凸组合$\in c$.

**凸包** $c \in R^n$
$\Bbb{Conv} \quad C = \{\theta_1x_1+...+\theta_kx_k| \forall x_1...x_k\in c, \forall \theta_1...\theta_k \in [0,1], \theta_1+...+\theta_k = 1\}$

从一个非凸的集合构造出一个凸集，这个集合的名字叫凸包。

**锥** Cone，**凸锥** Convex Cone
c是锥$\lrArr \forall x \in c, \theta\geq 0$有$\theta x\in c$
c是凸锥$\lrArr \forall x_1,x_2 \in c, \theta_1,\theta_2\geq 0$有$x_1\theta_1 + x_2\theta_2 \in c$

**凸锥组合**：$\theta_1x_1+...+\theta_kx_k,\theta_1...\theta_k\geq 0$
**凸锥包**：$x_1,...,x_k \in c$, $\{ \theta_1x_1+...+\theta_kx_k| x_1...x_k \in c, \theta_1...\theta_k \geq 0 \}$
> 凸锥包是包含有关点集的最小的锥。

## Lecture 5

> 上节课讲了仿射集、凸集、凸锥；仿射组合、凸组合、凸锥组合；仿射包、凸包、凸锥包这9个概念。其中，组合的概念最关键。
> 对于K个点$x_1, x_2,...,x_k \in C$，
> 选取$\theta_1,...,\theta_k \in R$，
> 构造组合$\theta_1x_1+...+\theta_kx_k$。
> 如果$\theta_1+...+\theta_k = 1$，该组合叫仿射组合，
> 如果$\theta_1+...+\theta_k = 1$，$\theta_1,...,\theta_k \geq 0$，该组合叫凸组合，
> 如果$\theta_1,...,\theta_k \geq 0$，该组合叫凸锥组合。

空集属于{仿射集、凸集、凸锥集}

几种重要的凸集：

1. $R^n$空间及其子空间，仿射集、凸集、凸锥
2. 任意直线，仿射集、不一定是凸集
3. 任意线段，凸集、不一定是仿射集和凸锥

超平面与半空间
**超平面**（Hyperplane）：$\{x| a^Tx=b\}, x,a \in R^n, b\in R, a\neq 0$
> 超平面将整个空间分成两个部分，每个部分被称为半空间。

球和椭球
**球**：$B(x_c,r) = \{x| ||x-x_c|| \leq r\} = \{x| \sqrt{(x-x_c)^T(x-x_c)} \leq r\}$
球是凸集。
**椭球**：$\epsilon (x_c,P) = \{x| (x-x_c)^TP^{-1}(x-x_c) \leq 1\}, x\in R^n, P\in S^n_{++}$
P是对称正定矩阵。P矩阵描述的是椭球的半轴长，这个半轴长由矩阵P的奇异值来描述。（这就是矩阵奇异值的几何含义）
当$P=r^2I_n$，椭球就变成球了。

## Lecture 6

**多面体**Polyhedron
$P = \{x| a_j^Tx \leq b_j, j=1,...m; a_jTx = d_j, j=1,...,p\}$
上边的集合是半空间和超平面的交集。
多面体是凸集。

**单纯性**Simplex
$R^n$空间中选择$v_0...v_k$共k+1个点。$v_1-v_0,...,v_k-v_0$线性无关。则与上述点相关的单纯形为$c = \Bbb{conv} \{\theta_0v_0+...+\theta_kv_k\}, \theta\geq 0 I^T, \theta = 1$
> 单纯型就是点集之上构建成的凸包。

**命题**：Simplex是Polyhedron的一种

- 证明：

**对称矩阵集合**$s^n = \{x\in R^{n\times n}| x=x^T\}$
**对称半正定矩阵集合**$s^n_+ = \{x\in R^{n\times n}|x=x^T,x \succeq 0\}$[^succeq]
**对称正定矩阵集合**$s^n_{++} = \{x\in R^{n\times n}| x= x^T, x \succ 0\}$

[^succeq]: $\succeq$这个符号表示，符号之前矩阵中的奇异值大于等于0；$\succ$这个符号表示，符号之前矩阵中的奇异值大于0。

## Lecture 7

已经讲过的几类凸集：球、椭球、多面体、单纯型

**凸运算**：哪些操作可以保证一个集合的凸性

**交集**：若$S_1,S_2$为凸，则$S_1\cup S_2$为凸。

推广：若$S_a$为凸集，$\forall a \in A$则$\bigcap\limits_{a\in A}S_a$为凸集。

**仿射函数**：$f:R^n\rightarrow R^m$是仿射的，当$f(x)=Ax+b, A\in R^{m\times n}, b\in R^m$。

- 若$S\in R^n$为凸，$f:R^n\rArr R^m$仿射，则$f(s) = \{f(x)|x\in S\}$为凸。
- 仿射逆映射也保持凸集的凸性。
- 所谓仿射就是线性的映射。

**缩放**和**移位**是保持凸性的：$\alpha S = \{\alpha x| x\in S\}, S+\alpha =\{x+\alpha|x\in S\}$

> 当矩阵把你搞晕了，就把矩阵想象成标量（标量是一维矩阵）。

## Lecture 8

**透视函数**(Perspective function):
$P: R^{n+1}\rarr R^n, dom P = R^n\times R_{++}$  
$P(z,t) = {a\over t}, z\in R^n, t\in R_{++}$

- 所谓透视就是降维

> 透视函数讲的是，将n维向量z和1个正数t降维，即将t除以前n维的component后，将t去掉。
> 几何上是，将n+1维的凸集，透过原点投射到$x_{n+1}=-1$这条直线上，所得到的的集合仍是凸集。

考虑$R^{n+1}$向线段，$x=(\tild{x},x_{n+1}), y=(\tild{y},y_{n+1}),\tild{x}\in R^n, x_{n+1}\in R_{++},\tild{y}\in R^n, y_{n+1}\in R_{++},$，对于$\theta \geq 0$，线段为$\theta x+ (1-\theta)y$  
要求证明线段经过透视函数变换后仍然是线段。
证明：$x\stackrel{P}{\rarr} P(x),y\stackrel{P}{\rarr} P(y)$
$P(\thetax+(1-\theta)y) = {\theta \tild{x}+(1-\theta)\tild{y}\over \theta x_{n+1} + (1-\theta)y_{n+1}} = {\theta x_{n+1}\over \thetax_{n+1}+(1-\theta)y_{n+1}}{\tild{x}\over x_{n+1}} + {(1-\theta)y_{n+1}\over {\theta x_{n+1}}+(1-\theta)y_{n+1}}{\tild{y}\over y_{n+1}}$
> 上式表达了一个线段到另一个线段的一一映射。
> 透视函数的逆映射，也能保证凸性。

**线性分数函数**:
$g: R^n\rarr R^{n+1}$为仿射映射。
$g(x) = \begin{matrix} A\\ c^T \end{matrix}x + \begin{matrix}b\\ d \end{matrix},A\in R^{m\times n}, b\in R^m, c \in R^n, d\in R$
$P: R^{m+1}\rarr R^m$
$f: R^n\rarr R^m = P·g$
$f(x) = {Ax+b\over c^Tx+d}, dom f = \{x|c^Tx + d \geq 0\}$
> 线性分数函数是个重要的函数，它自身是一个非线性函数，一个凸集经过线性分数函数变换后，仍然是凸集。

## lecture 9 凸函数的扩展

$f:R^n\rarr R$为凸，$dom f = c \subseteq R^n$
$\tilde{f} = \begin{cases}
    f(x) & x \in dom f\\
    +\infty  & x \notin dom f
\end{cases} $
$\tilde{f}: R^n \rarr R, dom \tilde{f} = R^n$
> 经过这样扩展定义域的一个函数，仍然是凸函数

示性函数仍然是凸函数。
$I_C(x) = \begin{cases}
    +\infty & x \notin c
    0 x \in c
\end{cases}$

**一阶条件**
设$f:R^n\rarr R$可微，即梯度Df在 dom f上均存在，则f为凸等价于：
1. dom f为凸
2. $f(y) \geq f(x) + Df^T(x)(y-x), \forall x,y \in dom f$
> 所谓一阶条件，即如果一个函数的一阶导数存在，那么凸函数有上述等价的定义。
> 和经典凸函数定义相比，经验定义从上面理解凸性，而一阶条件从下面（切线）去理解这个事情。
> 这是凸函数最重要的性质，因为这个不等式与优化问题密切相关。

# lecture 10 凸函数的四个定义

定义一：
$f:^n \rarr R$为凸，等价于dom f 为凸。
$\forall y \in dom f, 0\leq \theta \leq 1$有$f(\theta x + (1-\theta)y)\leq \theta f(x)+ (1-\theta) f(y)$
> 这个定义最一般，但对于高维用起来不是很方便。
定义二：
$\forall x \in dom f, \forall v, g(t) = f(x+tv)$为凸，$dom g = \{t| x+tv \in dom f\}$
> 这个定义将高维降到一维。
定义三：
若f可微，$\forall x, y \in dom f, f(y) \geq f(x)+ Df^T(x)(y-x)$

> 上节课我们讲了一维的一阶条件：$g:R\rarr R$可微，f为凸等价于$dom f$为凸。$\forall x, y \in dom f$

> 对于高维的证明...

定义四：
**二阶条件**
若$f:R^n\rarr R$二阶可微，则f为凸函数等价于$dom f$为凸：$D^2f(x)\geq 0$, $\forall x \in dom f$

> 二阶微分矩阵角Hessain矩阵。
> 分析一个函数是否是凸函数，用的最多的定义。

# lecture 11

通过二阶条件，讨论指数函数、幂函数、绝对值的幂函数、对数函数的凹凸性。

**负熵**：$f(x) = xlogx,x\in R_{++}$
$(xlogx)^{''}={1\over x}\geq 0$

**范数**：$R^n$空间的范数$P(x), x\in R^n$。范数就是满足以下三个性质的数：
1. $P(ax) = |a|P(x)$
2. $P(x+y) \leq P(x) + P(y)$
3. $P(x) = 0 等价于 x= 0$
> 范数是从向量空间$R^n$到实数空间$R$的函数，是向量的距离概念。
> 范数是个凸函数。

**极大值函数**：
$
f(x) = max\{x_1,x_2,...,x_n\}, x\in R^n.
\forall x,y \in R^n, \forall 0\leq \theta \leq 1
f(\theta x+(1-\theta)y) = max\{\theta x_i + (1-\theta)y_i, i=1,...,n\} \leq \theta max\{x_i, i=1,...n\} + \{(1-\theta)max\{y_i,...,y_n \} \}
 = \theta f(x) + (1-\theta)f(y)$

> 极大值函数是凸函数。极大极小问题或极小极大问题，即极小化一个极大值函数，是计算机领域经常出现的问题。$min max f(x,y)$
> 虽然这是个凸函数，但不可导。为了解决这个问题，用解析函数（log-sum-up）逼近。

**log-sum-up**: $f(x) = log(e^{x_1}+...+e^{x_n}), x\in R^n$,
$max \{x_1,...,x_n\} \leq f(x) \leq max\{x_1,...,x_n\}+log n$

# Lecture 12

证明log-sum-up函数是凸函数。

- 三角不等式：看到范数想到它。
- Cachy-Schwartz不等式：看到平方想到它。

- 算数平均：$f(x) = {x_1·...·x_n\over n}$
- 几何平均：$f(x) = (x_1·...·x_n)^{1\over n}，x\in R^n_{++}$

证明行列式的对数函数log det|A|是凹函数。

接下来讲，凸函数在什么操作下仍然是凸函数：
1. 非负加权和：$f_1,...,f_m$为凸，则对于任意的$m_i\geq 0, \forall i$,有$f=\sum\limits_{i=1}^m{w_if_i}$为凸。
2. 若$f(x,y)$，对任意$y\in A, f(x,y)$均为凸函数。设$w(y)\geq 0,\forall y \in A, g(x) = \int\limits_{y\in A}w(y)f(x,y)dy$为凸。
3. 放射映射后保持凸性。$f:R^n\rarr R, A\in R^{n\times m}, b\in R^n,g(x) = f(Ax+b), dom g = \{x|Ax+b\in dom f\}$.
4. 两个函数的极大值函数为凸。$f_1,f_2$为凸，定义$f(x) = max\{f_1(x),f_2(x)\}, dom f= domf_1\cap dom f_2$
5. 无限个凸函数的极大值为凸。f(x,y)对于x为凸，\forall \in A, g = \sup\limits_{y\in A} f(x,y).

