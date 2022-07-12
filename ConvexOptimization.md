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
