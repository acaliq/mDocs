Linear Algebra
> by Gilbert Strange
 - [The Geometry of Linear Equations 方程组的几何解释](#the-geometry-of-linear-equations-方程组的几何解释)
- [The Geometry of Linear Equations 方程组的几何解释](#the-geometry-of-linear-equations-方程组的几何解释)
- [Elimination with Matrices 矩阵消元](#elimination-with-matrices-矩阵消元)
- [Multiplication and Inverse Matrices 矩阵乘法和逆](#multiplication-and-inverse-matrices-矩阵乘法和逆)
  - [$AB = C$](#ab--c)
  - [How to get Inverses](#how-to-get-inverses)
- [Factorization into A = LU 矩阵的LU分解](#factorization-into-a--lu-矩阵的lu分解)
- [Transposes, Permutations, Spaces $R^n$ 转置、置换、向量空间](#transposes-permutations-spaces-rn-转置置换向量空间)
- [Vector Spaces and Subspaces Column Space of A](#vector-spaces-and-subspaces-column-space-of-a)
- [AX = 0: 主元、通解](#ax--0-主元通解)
- [solvablity and the structure of solutions 可解性和解的结构](#solvablity-and-the-structure-of-solutions-可解性和解的结构)
- [线性相关性、基、维数](#线性相关性基维数)
- [Four fundamental subspace 四个基本子空间](#four-fundamental-subspace-四个基本子空间)
- [矩阵空间](#矩阵空间)
- [图和网络](#图和网络)
- [复习一](#复习一)
- [正交向量和正交子空间](#正交向量和正交子空间)
- [投影](#投影)
- [投影矩阵和最小二乘](#投影矩阵和最小二乘)
- [正交矩阵和正交化](#正交矩阵和正交化)
- [行列式及性质](#行列式及性质)
- [行列式公式及代数余子式](#行列式公式及代数余子式)
- [行列式应用：克拉默法则、逆矩阵、体积](#行列式应用克拉默法则逆矩阵体积)
- [特征值和特征向量](#特征值和特征向量)
- [对角化和矩阵乘幂](#对角化和矩阵乘幂)
- [微分方程和$e^{At}$](#微分方程和eat)
- [马尔科夫矩阵和傅里叶级数](#马尔科夫矩阵和傅里叶级数)
- [对称矩阵](#对称矩阵)
- [复矩阵和快速傅里叶变换](#复矩阵和快速傅里叶变换)
- [正定矩阵](#正定矩阵)
- [相似矩阵和若尔当标准型](#相似矩阵和若尔当标准型)
- [奇异值分解](#奇异值分解)
- [线性变换即对应矩阵](#线性变换即对应矩阵)
- [基变换和图像压缩](#基变换和图像压缩)
- [复习三](#复习三)
- [左右逆和伪逆](#左右逆和伪逆)
- [线性代数的本质](#线性代数的本质)
> 我对线性代数的认识：线性代数的基本问题是解线性方程组（$Ax=b$）。求解的方式是对矩阵进行操作。一是通常情况，进行消元，将矩阵化简为rref，从而确定通解和特解。二是求最优解，通过将b投影到A的列空间，从而求得最优近似解（$A^TA\hat{x} = A^Tb$）。三是求阵幂，利用矩阵的特征向量矩阵分解、相似矩阵、奇异值分解等，将矩阵转化为$M_1\Lambda M_2$这种形式，进而将阵幂问题转化为幂函数问题。
> 关于矩阵操作的感悟：矩阵就是空间变换的数值描述。从这个角度来说，坐标系是次要的（会变），特征向量比较重要（变换前后方向不变）。所以，从特征值、特征向量的角度考虑，对称矩阵具有“好矩阵”的特点：一是特征值为正的实数，二是特征向量互相正交。这两个特点给涉及矩阵的运算带来了很多方便。

# The Geometry of Linear Equations 方程组的几何解释

**The fundamental problem of linear algebra**, which is to solve a system of linear equations (线性方程组).

**Example**   
$
\left \{
\begin{array}{c}
2x - y = 0 \\
-x + 2y = 3
\end{array}
\right.
$

$\left[ \begin{matrix} 2 & -1 \\
 -1 & 2 \end{matrix} \right]$ $\left[ \begin{matrix} x \\ y \end{matrix} \right]$ = $\left[ \begin{matrix} 0 \\ 3 \end{matrix} \right]$  
**AX**    =    **b**

**Row Picture**  
直角坐标系，作图解方程
**Column Picture**  
> x $\left[\begin{matrix} 2 \\ -1 \end{matrix}\right]$ + y$\left[\begin{matrix} -1 \\ 2 \end{matrix} \right]$= $\left[\begin{matrix} 0 \\ 3 \end{matrix}\right]$   
- The left side is a linear combination of the columns.  
- The equation requires the right combination of the left to produce the right.

**big picture**
- Can I solve **AX=b**, for every **b**?
- Do the linear combination of the columns fill the 3 demintional space?
- 根据助教的说法，引入矩阵表示方程组，最终是为了解方程。就像标量方程那样，将ax=b,解为$x=a^{-1}b$。矩阵方程**AX=b**可以转化为$X=A^{-1}b$。那么关键就是求$A^{-1}$

**AX** is a linear combination of the columns of **A**
> 这里的要点是，矩阵乘以向量的列计算方法（区别于行计算的点乘法）
$\left[\begin{matrix}2 & 5\\1 & 3\end{matrix}\right]\left[\begin{matrix}1\\2\end{matrix}\right] = 1\left[\begin{matrix}2\\1\end{matrix}\right] + 2\left[\begin{matrix}5\\3\end{matrix}\right] = \left[\begin{matrix}12\\7\end{matrix}\right]$

> 线性代数的学习进程是：vectors/matrices/subspaces
- if **AX=b**, then $X=A^{-1}b$
  - $A^{-1}$被称为A的逆矩阵，所以矩阵是否可逆很重要。
- **a vector space** is one where you take all combinations out of a bunch of vectors.

# Elimination with Matrices 矩阵消元

$
\left\{ 
\begin{array}{c}
x+2y+z=2\\
3x+8y+z=12\\
4y+z=2
\end{array} 
\right.
$
The Process of Elimination of the Augmented Matrix is:
$
\left[
\begin{matrix}
1&2&1&2\\
3&8&1&12\\
0&4&1&2
\end{matrix}
\right]
\rightarrow
\left[
\begin{matrix}
1&2&1&2\\
0&2&-2&6\\
0&4&1&2
\end{matrix}
\right]
\rightarrow
\left[
\begin{matrix}
1&2&1&2\\
0&2&-2&6\\
0&0&5&-10
\end{matrix}
\right]
$

- The **central idea of linear algebra** is how these matrices work by rows as well as by columns.
- $Matrix \times Column$ = 矩阵各列的线性组合，比如：
> $A \left[ \begin{matrix}3\\4\\5
\end{matrix} \right] = \left[ \begin{matrix} 3\times col1+4\times col2+5\times col3 \end{matrix} \right]$

- $Row \times Matrix$ = 矩阵各行的线性组合，比如：
> $\left[ \begin{matrix} 1&2&7 \end{matrix} \right] A = \left[ \begin{matrix} 1\times row1+2\times row2+7\times row3 \end{matrix} \right]$


$E_{32}E_{21}A = U$

# Multiplication and Inverse Matrices 矩阵乘法和逆
> Matrix multiplication(4 ways!)
> Inverse of $A \quad AB\quad A^T$
> Gauss-Jordan method to find $A^{-1}$

## $AB = C$
1. dot multiply: row of A times column of B
2. **columns of C are linear combinations of columns of A**
3. **rows of c are linear combinations of rows of B**
4. C = $\sum\limits_{n=i}^n (column_i \quad of A)\times(row_i\quad of B)$
> 计算矩阵的4种乘法：1.点乘；2.A列向量的线性组合构成C的列向量；3.B行向量的线性组合构成C的行向量；4.A的列向量分别各自乘以B的对应行向量，它们的和就是C。

## How to get Inverses
$A^{-1}A = I = AA^{-1}$
- Singular, Noninverse
  - If I can find a vector $x$, with $AX = 0$
- Gauss-Jordan (solve 2 euqations once)
  - $[AI] \rightarrow [IA^{-1}]$
  - $E_i[AI] = [I\ddots] \rightarrow E_iA = I \rightarrow E_i = A^{-1}$
  - > 高斯-乔丹求逆矩阵方法：通过行变换将A矩阵变成单位矩阵，左乘的一系列单位变换矩阵相乘的结果就是A的逆矩阵。

# Factorization into A = LU 矩阵的LU分解
> Inverse of $AB$, $A^T$
> Product of elimination matrices
> A = LU (no row exchangees)

- What's the inverse of AB
  - $ABB^{-1}A^{-1} = I$
- What's the transpose of $AA^{-1}$
  - $AA^{-1} = I \rightarrow (A^{-1})^TA^{T} = I$
- How to get matrix A's upper triangle U
  - $E_{32}E_{31}E_{21}A = U \rightarrow A = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U$
  - $L = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$
  - > 在A = LU中，为什么不用$L = E_{32}E_{31}E_{21}$，而用$L=E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$?因为If no row exchanges, multipliers go directly into L.即E的逆以逆序方式相乘，只要把各个$E^{-1}$相应位置的数字加总到L上就可以，E则不行。

- How many operations on $n\times n$ matrix $A$ to get LU?
  - $n^2+(n-1)^2+...+2^2+1^2 = {1\over 6}n(n+1)(2n+1))  \approx {1\over 3}n^3= O(n^3)$

  - **The whole point of calculus** is: Calculus is like sums except it's continuous.
  - > $\int_{x=1}^n x^2dx = {1\over 3}n^3$

# Transposes, Permutations, Spaces $R^n$ 转置、置换、向量空间
> PA = LU 
> Vector Spaces and Subspaces

- **Permutation**(置换矩阵), P is the identity matrix with reordered rows.
  - $P^{-1} = P^T \rightarrow PP^{T} = I$ 置换矩阵的逆就是其转置矩阵
  - permutations就是那些单位矩阵经行交换而得到的矩阵。
  - permutations无论怎么进行行列交换，都是permutations。

- **Transpose**
  - $(A^T)_{ij} = A_{ji}$
  - For **Symmetric Matrix**  $A^T = A$
  - $R^TR$ is always symmetric matrix
    - 证明：$(R^TR)^T =R^TR^{TT } = R^TR$

- **vector spaces**
  - $R^2$ = all 2-dim real vectors
    - subspace: (1)All of $R^2$; (2)A line in $R^2$ that go through the zero vector;(3) Zero vector only.
  - $R^3$ = all column vectors with 3 real components
    - subspace: + a plane that go through the origin.
  - 向量空间就是，向量运算都被包含其中的向量集合，即对向量的线性组合封闭。

- **Column Space** of A: All their columns' combinations form a subspace called C(A).
  - 矩阵的列空间是从更高层面审视线性代数的关键，它有助于从另一个视角看待$AX=b$。

# Vector Spaces and Subspaces Column Space of A
> Column Space of A: Solving $AX = b$
> Nullspace of A

- Vector space requirements:
  - V + W and cV are in the Space.
  - All combinations of cV +dW are in the Space.

- **Column Space** of A
  - C(A): all linear combinations of culumns
    - 每个抽象定义的背后，都有其具体目的
  - Does $AX=b$ have a solution for every $b$?
    - 看列向量张成的空间能否填满整个空间（空间的维数由列向量的维数决定）
  - Does $AX=b$ have a solution for a specific $b$?
    - 看b能否由列向量的线性组合得到，即其是否在列向量张成的空间内: $b \quad in \quad C(A)$。
- **Null Space** of A
  - N(A): it contains all solutions to $AX = 0$

# AX = 0: 主元、通解
> Computing the nullspace (AX=0)
> Pivot variables - free variables
> Special Solutions - rref(A) = R

- Elimination of A will not change the nullspace of A
  - Echelon 阶梯形式 
  - Factorization 分解
  - Entry 元素

- Algorithm to find solutions of $AX = 0$
  - rank of $A$ = # of pivots of $A$ 秩
  - pivot columns & free columns: 列向量个数 = 主元列个数 + 自由列个数
  - the nullspace contains all the combinations of the special solutions 零空间包含的是通解
  
- $R = rref(A)$: reduced row echelon form 简化的行阶梯形式
  - $R = \left[ \begin{matrix} I & F \\ 0 & 0 \end{matrix} \right]$
  - $RX = 0 \rightarrow N_{nullspace} = \left[ \begin{matrix} {-F} \\ I \end{matrix} \right]$
    - 证明：$RN = -F + F = 0$，证毕。
    - 求nullspace就是将A化简到rref，其free columns的线性组合就是nullspace。
    - > **rref(A)以最简的形式，包含解空间（nullspace）有关的信息**。

# solvablity and the structure of solutions 可解性和解的结构
> complete solution of AX = b
> rank r

- **$AX = b$ is solvable** when b is in $C(A)$
  - if a combination of rows of A gives *Zero* row, then same combination of entries of b must give *Zero*.

- **To find complete solution** to $AX = b$
  - Fist of all, reduce A to its $rref(A)$.
  - $x_{perticular}$: set all free variables to 0, then solve $Ax = b$ for pivot variables.
  - $x_{nullspace}$: solve $Ax = 0$
  - $Ax_{perticular} = b, Ax_{nullspace} = 0 \rightarrow A(x_{perticular} + x_{nullspace})x = b$
  - $x = x_{nullspace} + x_{perticular}$

- matrix $A_{m \times n }$ by rank $r$
  - $r \leq m,\quad r \leq n$
  - full column rank $\rightarrow$ r = n < m $\rightarrow$ n(A) = 0$\rightarrow$ x = $x_{perticular}$
  - full row rank $\rightarrow$ r = m < n
    - can solve $Ax = b$ for every $b$, left with *n-r* free variables
  - r = m = n $\rightarrow R = I$

- the whole picture of the solvability of $Ax = b$
  - r = m = n: R = I, 1 solution
  - r = n < m: R = $\left[ \begin{matrix} I \\ F \end{matrix} \right]$, 0 or 1 solution
  - r = m < n: R = $[IF]$, $\infty$ solutions 
  - r < m, r< n: R = $\left[ \begin{matrix} I & F \\ 0 & 0 \end{matrix} \right]$, 0 or $\infty$ solutions
    - > 在增广矩阵中，有没有通解，看r是否小于n；有没有特解，看r是否小于m。


# 线性相关性、基、维数
> Linear indepedence
> spanning a space
> Basis and dimensions

- 该讲是核心章节
- **independence**. Vectors $x_1,x_2,...,x_n$ are independent, if no combinations give $Zero$ vector (except for zero combination).
  - Repeat. when $v_1,v_2,...,v_n$ are columns of A. They are independent if nullspace of A is $zero$ vector. They are dependent if nullspace of A is not $Zero$.

- **Spanning a space**. Vector $v_1,v_2,...,v_l$ span a space means: The space consists of all combinations of those vectors.
- **A basis of a vector space** is a sequence of vectors $v_1, v_2,...,v_l$ with 2 properties:
  - They are independent
  - They span the space 

- **Dimension of a space**, is the number of basis of a space.
  - rank(A) = # pivot columns = dim of C(A)
  - dim(Nullspace) = # free variables = n - r

# Four fundamental subspace 四个基本子空间

- 4 SUBSPACE of $A_{m\times n}$
  - column space C(A) in $R^m$
  - > 列空间维度看列向量有几个分量，它等于行数。
  - nullspace N(A) in $R^n$
  - > 零空间是**通解**组成的空间，维度等于变量个数。
  - row space = all combinations of rows = all combinations of columns of $A^T$ = $C(A)^T$ in $R^n$
  - nullspace of $A^T$ = $N(A^T)$ = left nullspace of A in $R^m$
    - $A^Ty = 0 \rightarrow y^TA = 0$，这就是$N(A^T)$又被称为左零空间的原因

- **dimensions of 4 subspaces** of $A$  
$$
\begin{array}{c|clr} & InSpace & SpaceDimension & SpaceBasis\\
\hline
C(A) & R^m & r & \text{pivot columns}\\
N(A) & R^n & n-r & \text{free columns}\\
C(A^T) & R^n & r & \text{frist r rows of R} \\
N(A^T) & R^m & m-r & \text{free rows}\\
\end{array}
$$

- 对矩阵A进行行变换，行空间不变，但列空间被改变了 $C(R)\not= C(A)$。
  - 因为行变换就是对矩阵的行向量进行线性组合，这样的线性组合都落在线性空间内。

- 如何找$C(A^T)$的基？
  - 按照简化阶梯型方法化简A得rref(A)
  - $E\left[ \begin{matrix}A & I \end{matrix}\right]\rightarrow \left[ \begin{matrix}R&E\end{matrix}\right] \rightarrow EA = R$
  - 上面的E就是$y^TA=0$的左零空间基向量

- A new vector space M
  - all $3\times 3$ matrices
  - subspaces of M are: upper triangle matrices, symmetric matrices, diagonal matrices.

# 矩阵空间
> Bases of new vector spaces
> Rank one matrices
> Small world graphs

- M = all $3\times 3$ matrices
  - 9 basis for M: $\left[ \begin{matrix} 1&0&0\\0&0&0\\0&0&0 \end{matrix} \right]$,$\left[ \begin{matrix} 0&1&0\\0&0&0\\0&0&0 \end{matrix} \right]$...$\left[ \begin{matrix} 0&0&0\\0&0&0\\0&0&1 \end{matrix} \right]$ 
  - Symmetric matrix: dimension = 6
  - upper triangle matrix: dimension = 6
  - dimensions of $S\cap U$ = $M_{symmetric}\cap M_{uppertriangle}$ = 3
  - dimensions of $S + U$ = 9
    - 为什么不用$S \cup U$？因为并集不能构成subspace
  - dim(S) = 6, dim(U) = 6, dim($S\cap U$) = 3, dim(S+U) = 9. $\rightarrow dim(S) + dim(U) = dim(S\cap U) + dim(S+U) = 12$

- Rank 1 matrix A can be put as $A = UV^T$. U, V are vectors
  - 任何一个矩阵可以表示为，若干个rank 1矩阵的组合，即可以表示为若干个$UV^T$的线性组合。
  - $v_1+v_2+v_3+v_4 = 0. A = [1,1,1,1], V = \{v_1,v_2,v_3,v_4\}^T$，Av=0。那么C(A) = 1, N($A^T$) = 0

# 图和网络
> Graphs and Networks
> Incidence Matrix 关联矩阵
> Kirchhoff's law 基尔霍夫电流定理

- This lecture is about the application of Linear Algebra

- **Graphs**: Nodes, Edges
  - loop means linear dependent 图中的**环路**意味着线性相关
  - Graph without loops is called a tree **树**
  - Nullspace tells us what combinations of the columns produce $0$.

- Kirchhoff's law
  - 基尔霍夫电流定律说的是，电路上每个节点电流流入等于流出
  - $A^Ty = 0$，应用基尔霍夫电流定律，就要用到这个表达式。

# 复习一

- $A_{m\times n}B_{n\times p} = C$
  - $\left[ \begin{matrix}a_{11},&a_{12}&...&a_{1n}\\a_{21},&a_{22}&...&a_{2n}\\...,&...&\ddots&...\\a_{p1},&a_{m2}&...&a_{mn}\end{matrix} \right]\times \left[ \begin{matrix}b_{11},&b_{12}&...&b_{1p}\\b_{21},&b_{22}&...&b_{2p}\\...,&...&\ddots&...\\b_{n1},&b_{n2}&...&b_{np}\end{matrix} \right] = \left[ \begin{matrix}c_{11},&c_{12}&...&c_{1p}\\c_{21},&c_{22}&...&c_{2p}\\...,&...&\ddots&...\\c_{m1},&c_{m2}&...&c_{mp}\end{matrix} \right]$
  - 这个矩阵乘法中，A决定C的行，包括行数；B决定C的列，包括列数。
  - 换句话说，考虑C第1列，它由A的各列与B第1列各元素的线性组合而成；C的第1行，它由B的各行与A的第1行各元素的线性组合而成。

# 正交向量和正交子空间
> Orthogonal vectors and subspaces 正交
> nullspace $\bot$ rowspace
> N($AA^T$) = N(A)

- **Orthogonal**: x and y are orthogonal if $x^Ty = 0 \rightarrow ||x||^2 + ||y||^2 = ||x+y||^2$
  - $||x||^2 = x^Tx$ 
  - O vector is orthogonal to any vector

- **subspace S is orthogonal to subspace T** means every vector in S is orthogonal to every vector in T

- **row space is orthogonal to Nullspace of A**
  - 因为行空间由方程式组成，零空间由解空间组成，by定义，它们相乘为0.
  - nullspace and row space are orthogonal complements in $R^n$. complement means nullspace contains all vectors that is orthogonal to row space.
  
- **column space is orthogonal to Nullspace of $A^T$**
  - nullspace and column space are orthogonal complements in $R^m$. 

- 行空间没有nullspace，列空间也没有nullspace，只有矩阵有零空间，因为零空间是使方程组为0的解集。

- **线性代数第一部分研究4个子空间的维数，第二部分研究子空间的正交关系，第三部分研究子空间的基。**

- 本章的重点是：对无解的$Ax=b$求解
  - 比如测量误差的存在，要求多测几次数据。这样，噪音导致方程太多而未知数太少，完美解不存在。
  - $A^TA $:
    - **it's square**
    - **it's symmetric**
    - **it's invertible**
    - **$A^TA $是个重要的矩阵表达式，因为矩阵对称性很重要。**
  - $A^TA\hat{x} = A^Tb$：
    - 上述方程是$AX=b$无解情况下，的最优解
    - N($A^TA$) = N($A$)
    - rank of $A^TA$ = rank of A
    - $A^TA$ is invertibel exactly when A has independent columns

# 投影
> Projections!
> Least Squares
> Projection Matrix

- 这节关于投影的课很重要

- 求向量b在向量a上的投影
  - 令p是向量b在向量a上的投影，则p = xa
  - 根据定义，向量b-xa与向量a垂直
  - 所以$a^T(b-xa) = 0 \rightarrow a^Txa = a^Tb \rightarrow x = {{a^Tb}\over a^Ta}$
  - $p = ax = a{{a^Tb}\over a^Ta} \rightarrow {{aa^T}\over a^Ta}b$，其中将$P={{aa^T}\over a^Ta}$被称为投影矩阵，即把任何一个向量投影到a上所要乘的矩阵
  - C(P) = line through a.
    - 因为p = ax，所以p和a在一条线上，那么p的列空间就是向量a张成的空间。
  - rank(P) = 1，因为p就是1条直线。
  - **投影矩阵$P$ 是对称的：$P^T = P$**
  - **投影两次和投影一次相等：$P^2$ = $P$**

- 为什么要作投影？
  - 解决Ax=b无解的问题，即b不在C(A)中。
  - 在上述情况下，求Ax = p instead，其中p是b在C(A)上的投影。
    - > 这个思路之简洁，之美妙，登峰造极！

- **高维投影**：向量在空间上的投影
  - 求向量b在空间A上的投影p，即$p = A\hat{x}$，关键在find $\hat{x}$
  - **Key**: e = $(b - A\hat{x})$ is perpendicular to plane, that is $A^T(b-A\hat{x}) = 0$
  - 由上式可知e在矩阵$A^T$的nullspace中：e in N($A^T$) , that is $e \bot C(A)$
  - 可得：$A^TA\hat{x} = A^Tb$
    - $\hat{x} = (A^TA)^{-1}A^Tb$
    - $p = A\hat{x} = A (A^TA)^{-1}A^Tb$
      - 如果上式中A不是可逆矩阵，那就不能这样推导：$A (A^TA)^{-1}A^Tb =AA^{-1}{A^T}^{-1}A^Tb = I\times b$
    - **Proj Matrix $P = A (A^TA)^{-1}A^T$**
      - 有 $P^T = P, P^2 = P$

- Least Squares: Fitting by a line
  - b = C + Dt

# 投影矩阵和最小二乘
> Projections
> Least Squares and Best Straight Line
> system 方程组
> fitting 拟合

- Projection Matrix $P = A(A^TA)^{-1}A^T$
  - If b in column space, $Pb = b$
  - If b $\bot$ column space, $Pb = 0$
  - > 投影矩阵P将b投影到列空间中，如果b在列空间，那么P=I；如果b与列空间正交，那么Pb=0
  - **列空间中的向量可以表示为$Ax$，即A的列向量的线性组合(列向量是变换后的空间的基)；行空间中的向量可以表示为$A^Ty$，即A的行向量的线性组合。$C(A)\bot N(A^T)$。**
  - 一个向量b，同时向C(A)和$N(A^T)$投影，通过投影矩阵$P$投影到C(A)的就是p = Pb = $A\hat{x}$，投影到$N(A^T)$的就是e。而且，有$p+e = b,\quad p\times e=0$,
    - 对于投影矩阵P，有$e = (I-P)$

- Least Squares
  - 对于线性方程$y = C + Dt$， 假设有$\left[ \begin{matrix} 1&1\\ 2&2\\2&3 \end{matrix} \right]\left[ \begin{matrix} C\\D \end{matrix} \right] = \left[ \begin{matrix} 1\\ 2\\3 \end{matrix} \right]$ 
  - 那么，我们要做的就是最小化误差$||Ax-b||^2 = ||e||^2$
  - Find $\hat{x} = \left[ \begin{matrix}\hat{C}\\\hat{D} \end{matrix} \right]$, P, **that meet $A^TA\hat{x} = A^Tb$**
    - 吉尔伯特教授称，上面最后一个公式是统计和估计中最重要的公式，只要涉及误差，就会首先想到用它来估计。

- If A has independent columns, then $A^TA$ is invertible
  - Suppose $A^TAx = 0$
  - Then $x^TA^TAx = 0 \rightarrow (Ax)^T(Ax) = 0 \rightarrow Ax=0$
  - Because A has independent columns, x must be in Nullspace, that is $x = 0$.

- columns definitely independent if they are perpendicular unit vectors (orthnormal vectors).标准正交向量

# 正交矩阵和正交化
> Orthogonal Basis $q_1,q_2...q_n$
> Orthogonal Matrix Q
> Gram-Schmitt $A\rightarrow Q$

- **Orthonormal vectors**  $q_i^Tq_j = \left \{ \begin{array}{c} 0,& if \quad q_i \not ={q_j}\\1,& if \quad q_i = q_j \end{array} \right.$
  - 标准正交基，让数值计算变得容易

- $Q = [q_1,q_2...q_n]$
  - $Q^TQ = I$
  - If Q is square, then $Q^TQ=I$ **tells us $Q^T = Q^{-1}$**
  
- 求标准单位正交矩阵Q的**Gram-Schmitt方法**
  - 为什么求Q?它使投影矩阵P的计算变得简单：
  - Proj Matrix $P = Q(Q^TQ)Q^T$ = $\left \{ \begin{array}{c} QQ^T \quad&\text{if Q is not Square} \\I \quad & \text{if Q is square} \end{array} \right.$
  - 对于投影运算：$A^TAx = A^Tb \rightarrow Q^TQ\hat{x} = Q^Tb \rightarrow \hat{x} = Q^Tb \rightarrow \hat{x_i}^T = q_i^Tb$
  - 将独立向量组变为标准单位正交基
    - 首先，从独立变量组$a_1,a_2...a_n$选择第一个变量$a_1$,令$A_1 = a_1$
    - 其次，$A_2 = a_2 - {{A_1^Ta_2}\over{A_1^TA_1}}A_1$
    - 继续构造，$A_3 = a_3 - {{A_1^Ta_3}\over{A_1^TA_1}}A_1- {{A_2^Ta_3}\over{A_2^TA_2}}A_2$。这个构造先去掉$a_3$在$A_1$方向的平行投影向量，然后再去掉其在$A_2$方向的投影向量，剩下的就是与$A_1和A_2$都垂直的向量了。
    - 构造完成，将向量单位化：$A_i = {A_i\over ||A_i||}$

# 行列式及性质
> Determinents det A
> Properties 1,2,3,4-10
> $\plusmn$ signs

- 这堂课开始，开讲这门课的第二部分 
- 我们开始将注意力集中到方阵上，学习行列式的原因是为了求特征值
- 行列式和特征值（eigen value）是线性代数的另外一个重点

- **the determinent** is a number associated with every square matrix
  - 行列式记号:det A or |A|
  - 行列式用一个数字包含了有关其矩阵的最多的信息
  - 行列式为0，意味着其矩阵是奇异矩阵；不为0，则原矩阵可逆

- Properties of the determinent
  1. det I = 1
  2. Exchange 2 rows: reverse sign of det 
     1. 置换矩阵P det P = 1 even, det p = -1 odd
  3. **det behaves like a linear function of each row separately**
     1. $ \left | \begin{matrix} ta & tb\\ c & d \end{matrix} \right | =  \quad t\left | \begin{matrix} a & b\\ c & d \end{matrix} \right |$
     2. $ \left | \begin{matrix} a+a' & b+b'\\ c & d \end{matrix} \right | =  \left | \begin{matrix} a & b\\ c & d \end{matrix} \right | +  \left | \begin{matrix} a' & b'\\ c & d \end{matrix} \right |$
  4. 从以上3条性质，可以推出行列式其他性质
  5. 2 equal rows $\rightarrow$ det = 0
     1. exchange rows $\rightarrow$ same matrix
  6. Subtract $l\times row_i$ from $k\times row_k$. DET doesn't change.
     1. use property 3b
  7. Row of Zeros $\rightarrow$ det = 0
     1. use property 3a
  8. 上面的性质为了引出这条性质：det of upper triangle matrix = product of pivots. 上三角阵的行列式等于其主对角线元素的乘积
     1. use property 1 and 3a
  9. det A = 0, exactly when A is singular
     1.  by elimination, A goes to upper triangle matrix
  10. 最后两个性质很有用：det AB = det A $\times$ det B
      1.  推论：$det A^{-1} = {1\over {det A}}$
      2.  $det [2A] = 2^n det A$. 二的N次方读作 2 to the nth
      3.  注意:$det (A + B) \not ={det A + det B}$
  11. $det A^T = det A$
      1.  A = LU, then to prove $det (LU)^T = det (LU)$
          1.  use property 8
      2.  吉尔伯特教授对这条性质的解释是，与前面的行变换一样，列变换也不改变行列式的数值（绝对值）。

# 行列式公式及代数余子式
> Formula for det A (n! terms)
> Cofactor formula 代数余子式
> Tridiagonal matrices

- Big Formula of det
  - $det A = \sum \plusmn a_{1\alpha}a_{2\beta}...a_{n\omega}$
  - 上式是n！个项的和
  - $\alpha，\beta，...，\omega$ 是$1,2,...,n$的一个组合

- Cofactor of $a_{ij}$ = $c_{ij}$ =$(-1)^{i+j}$ det (n-1 matrix with $row_i$ and $column_j$ erased)
  - cofactor formula: $det A = a_{11}c_{11} + a_{12}c_{12}+ a_{1n}c_{1n}$
  - 这个式子可以用来递归地解决行列式求解问题

# 行列式应用：克拉默法则、逆矩阵、体积
> Formula for $A^{-1}$
> Cramers' law for $x = A^{-1}b$
> |det A| = volume of box

- formula for $A^{-1}$
  - $A^{-1} = {1\over {det A}}C^T$
  - C 是伴随矩阵，C中的每一项$c_{ij}是原矩阵A的代数余子式$
  - 证明：to prove$\rightarrow AC^T = det A \times I$ 
    - 上式展开$AC^T$，将得到一个主对角线是A各行元素与其代数余子式乘积的和的矩阵。证毕。
  - 这个矩阵可以用来检查，A变化引起的$A^{-1}$变化。

- $Ax = b \rightarrow x = A^{-1}b = {1\over det A}C^Tb$
  - **Cramers' law**:
    - $x_1 = {det B_1\over det A_1}$,$x_2 = {det B_2\over det A_2}$,...$x_n = {det B_n\over det A_n}$
    - $B_1$ = [b (n-1)columns of A] = A with column 1 replaced by b
    - $B_j$ = A with column j replaced by b
    - 吉尔伯特教授点评：克拉默法则中看不中用，它用代数表示了方程组的解，这就是它唯一的价值。

- |det A| = volume of box
  - det A 的几何意义：对于$A_{3\times 3}$，det A 等于A的3列/行所决定的box的体积。
# 特征值和特征向量
> Eigenvalues - Eigenvectors
> $det [A-\lambda I] = 0$
> Trace = $\lambda_1,\lambda_2,...,\lambda_n$

- 特征值、特征向量是剩余课程中很大的一个主题

- **eigenvector x**: Ax parallel to x.
  - by parallel, $Ax=\lambda x$。矩阵和特征向量的积与特征向量平行
  - if A is singular, $\lambda = 0$ is eigenvalue.
  - fact: the sum of $\lambda's$ = the sum of values down diagonal. 无论矩阵是不是上三角阵，主对角线上的数字之和都等于其特征值之和。

- what are the x's and $\lambda's$ for projection matrix?
  - Any x in plane: Px = x, $\lambda = 1$
  - Any x perpendicular to plane: Px = 0, $\lambda = 0$

- How to solve Ax = $\lambda x$
  - rewrite $(A-\lambda I)x = 0 \rightarrow (A-\lambda I)$ is singular
  - Hence, 得到特征方程：det $(A-\lambda I) = 0$
  - 解特征方程可以得到$\lambda$值
  - 把特征值代入$(A-\lambda I)x = 0$，得到特征向量
  - Observation：如果矩阵$A+3I$，那么特征向量不变，但所有特征值+3.

- 特征值和特征向量不满足线性规律
  - 即Ax =$\lambda x, By=\alpha y \nrightarrow (A+B)x = (\lambda + \alpha)x$

# 对角化和矩阵乘幂
> Diagonalizing a matrix $S^{-1}AS = \Lambda$
> Powers of A / equation $u_{k+1} = Au_k$

- 这节课讲解为什么求特征值和特征向量

- Suppose n independent eigenvectors of A. Put them in columns of S
  - $AS = A[x_1,x_2,...,x_n] = [\lambda x_1,\lambda x_2,...,\lambda x_n] = [x_1,x_2,...,x_n]\left[ \begin{matrix}\lambda_1&0&\dots &0\\0&\lambda_2&...&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\dots&\lambda_n \end{matrix} \right]= S\Lambda $
  - $AS = S\Lambda \rightarrow S^{-1}AS = \Lambda  \rightarrow A = S\Lambda S^{-1}$
  - 上式提供了一种**分解（可逆）矩阵**的新方法。

- 阵幂$A^k$的特征值和特征向量
  - $A^2x=AAx=A\lambda x=\lambda^2x$,即$A^2$的特征值为$\lambda^2$，特征向量还是x
  - 换种推导方式：$A^2 =S\Lambda S^{-1}S\Lambda S^{-1} = S\Lambda^2 S^{-1}$，因为$\Lambda$是对角矩阵，所以特征向量不变，对角矩阵是原来的平方。
  - 以此类推：$A^k =S\Lambda S^{-1}S\Lambda S^{-1}... = S\Lambda^k S^{-1}$
    - 矩阵的特征向量表示，是计算**阵幂**的一种方法。
    - 这就是**特征值、特征矩阵的作用**。

- A is sure to have n independent vectors (and can be diagonalizing) if all the $\lambda's$ are different non-zero numbers.
  - If there are repeated eigenvalues, we may or may not have n indenpendent vectors.

- Differece Equation (差分方程) $u_{k+1} = Au_{k}$, starts with given vector $u_0$.
  -  $u_k = A^ku_0$
  - write $u_0 = c_1x_1+c_2x_2+...+c_nx_n = Sc$，其中$x_i$是A的特征向量，$u_0$是特征向量的线性组合，S是特征向量矩阵，c是系数向量。
    - 根据特征向量定义$Ax = \lambda x$，根据差分方程$u_k=A^{100}u_0$。为了将两者联系起来，需要将矩阵A右边的$u_0$重构成特征向量矩阵与其它成分乘积的形式，这就是Sc的由来。
    - 因为$x_i$是特征向量，所以$Ax_i=\lambda_ix_i\rightarrow A^{100}x_i=\lambda_i^{100}x_i$
  - $u_{100} = A^{100}u_0=c_1\lambda_1^{100}x_1+c_2\lambda_2^{100}x_2+...+c_n\lambda_n^{100}x_n = \Lambda^{100}Sc$
  - Fibonacci example: $F_0=0,F_1=1,1,2,3,5,8,13... \rightarrow F_{100}?$
    - 写出方程：$F_{k+2} = F_{k+1}+F_{k}$
    - 追加一个方程$F_{k} = F_{k}$
    - 令：$u_k = \left[ \begin{matrix} F_{k+1}\\F_{k} \end{matrix} \right]$，$\rightarrow u_{k+1} = \left[ \begin{matrix} 1&1\\1&0 \end{matrix} \right] \left[ \begin{matrix} F_{k+1}\\F_{k} \end{matrix} \right] = \left[ \begin{matrix} 1&1\\1&0 \end{matrix} \right] u_k$
    - 求解矩阵$A = \left[ \begin{matrix} 1&1\\1&0 \end{matrix} \right]$的特征值和特征向量
    - $\lambda_1 = {1+\sqrt 5\over 2}, \lambda_2 = {1-\sqrt 5\over 2};x_1 = \left[ \begin{matrix} \lambda_1\\1 \end{matrix} \right],x_2 = \left[ \begin{matrix} \lambda_2\\1 \end{matrix} \right]$
    - 因为$u_0 = \left[ \begin{matrix} 1\\0 \end{matrix} \right] = c_1x_1+c_2x_2$，所以只要求得$c_1,c_2$就能算出$u_{100}=c_1\lambda_1^{100}x_1+c_2\lambda_2^{100}x_2$。
    - 吉尔伯特教授点评：对于（差分方程类的）增长问题，关键是确定A的特征值和特征向量，根据特征值就能确定数列是发散还是收敛，以及增长得多快。
    - 毛立云点评：这个假设$u_0 = c_1x_1+c_2x_2+...$也很关键，这是无中生有的，一般人不会这么想。

# 微分方程和$e^{At}$
> Differential Euqations ${du\over dt} = Au$
> Expentional $e^{At}$ of a matrix

- 本讲关于如何解一阶导数常系数线性方程，将其转换成线性方程问题。
- 基本思想是：常系数线性方程的解是指数形式，我们要做的就是确定指数是多少，它的系数又是多少，这就是线性代数问题了。

- 例子
  - > $\left \{ \begin{array}{c} {du_1\over dt}=&-u_1&+2u_2\\{du_2\over dt}=& u_1&-2u_2 \end{array} \right.$
  - $\rightarrow A = \left[ \begin{matrix} -1 & 2\\ 1& -2 \end{matrix} \right]$. Set $u(0) = \left [ \begin{matrix} 1\\0 \end{matrix} \right]$
  - 首先求A的特征值和特征向量，得$\lambda_1 = 0, \lambda_2 = -3;x_1 =\left [ \begin{matrix} 2\\1 \end{matrix} \right] ,x_2 = \left [ \begin{matrix} -1\\1 \end{matrix} \right]$
  - Solution: $u(t) = c_1e^{\lambda_1t}x_1+c_2e^{\lambda_2t}x_2 = c_1·1·\left [ \begin{matrix} 2\\1 \end{matrix} \right]+ c_2·e^{-3t}·\left [ \begin{matrix} -1\\1 \end{matrix} \right]$ 
  - Use $u(0) = \left [ \begin{matrix} 1\\0 \end{matrix} \right]$. At t = 0, $c_1·\left [ \begin{matrix} 2\\1 \end{matrix} \right] + c_2·\left [ \begin{matrix} -1\\1 \end{matrix} \right] = \left [ \begin{matrix} 1\\0 \end{matrix} \right]$. We have $c_1={1\over 3}, c_2={1\over 3}$
  - $u(t) = {1\over 3}x_1+{1\over 3}e^{-3t}x_2$
  - Stability:$u(t) \rightarrow 0$, need $e^{\lambda t}\rightarrow 0$, that is the real part of all $\lambda \lt 0$ 收敛
  - Steady State: $\lambda_1 = 0$ and other $\lambda's$ real part $\lt$ 0 稳定
  - Blow up: any $\lambda's$ real part $\gt 0$ 发散

- 解方程 ${du\over dt} = Au$
  - set u = Sv, S is eigenvector
  - ${du\over dt} = {dSv\over dt} = S{dv\over dt} \rightarrow {dv\over dt} = S^{-1}ASv = \Lambda v$
  - $v(t) = e^{\Lambda t}v(0) \rightarrow u(t) = Se^{\Lambda t}S^{-1}u(0) = e^{At}u(0)$. $e^{At} = Se^{\Lambda t} S^{-1}$

- matrix exponentials
  - $e^{At} = I + At + {(At)^2\over 2} + ... + {(At)^n \over n!} + ...$
  - $= SS^{-1} + S\Lambda S^{-1}t + {S\Lambda^2 S^{-1}t^2\over 2} + ... + {S\Lambda^n S^{-1}t^n \over n!} + ...=Se^{\Lambda t}S^{-1}$
    - 矩阵指数的含义：$e^{\Lambda t} = \left [ \begin{matrix} e^{\lambda_1 t}\\ & e^{\lambda_2 t}\\&& e^{\lambda_3 t}\\&&& \ddots\end{matrix} \right]$
    - 要使$e^{At}$收敛，A的每个特征值的实数部分必须小于0；要使矩阵A的幂阵收敛于0，必须使$|\lambda| \lt 1$。
    - 普通泰勒级数的结论对矩阵级数同样适用。
    - $(I - At)^{-1} = I + At + (At)^2$+ ...

- 如何将二阶微分方程 $y'' + by' + ky = 0$，构造成矩阵形式？
  - 令$u = \left [ \begin{matrix} y'\\y \end{matrix} \right], u' = \left [ \begin{matrix} y''\\y' \end{matrix} \right] =\left [ \begin{matrix} -b & -k\\1 & 0 \end{matrix} \right] \left [ \begin{matrix} y'\\y \end{matrix} \right]$
  - 无论是差分方程，还是微分方程，为了将其转换成线性代数问题，都用到了矩阵构造技巧。也就是加了一个y' = y'的无关痛痒方程，使组成方程组。

# 马尔科夫矩阵和傅里叶级数
> Markov Matrices
> steady state: $\lambda = 1$ in matrix and  $\lambda = 0$ in exponential
> Fourier series projections

- 这节课讲特征值的应用

- Markov Matrices
  - 要求解$u_k = A^ku_o$，其中A是Markov Matrix
  - $A = \left [ \begin{matrix} .1&.01&.3\\.2&.99&.3\\.7&0&.4\end{matrix} \right]$
  - 矩阵A称为马尔科夫矩阵，如果其满足(1)all entries $\geq$ 0;(2)all columns add up to 1.
  - $\lambda = 1$ is an eigenvalue
    - 观察$（A-I）$每列元素的和，必然是0。根据定义A的每列元素和为1，I每列元素和为1，相减得0.这样$A-I$是奇异矩阵。
  - all other $|\lambda_i|\lt$ 1
  - $u_k = A^ku_o = c_1\lambda_1^kx_1 + c_2\lambda^kx_2 + ...$
    - 可以看出，当$\lambda_1 = 1, \lambda_i \lt 1$时，上式达到steady state
  - eigenvalues of A and $A^T$ are the same.
    - $det (A-\lambda I) = det (A - \lambda I) ^T= det (A^T - \lambda I) = 0$

- Projections with orthonormal basis $q_1,q_2,...,q_n$. 
  - For any v = $x_1q_1 + x_2q_2 + ... + x_nq_n$
  - $q_1^Tv = x_1q_1^Tq_1 + 0 + 0 + ... = x_1$
  - $Qx = v \rightarrow x = Q^{-1}v = Q^Tv \rightarrow x_1 = q_1^Tv$

- **Fourier Series**
  - $f(x) = a_0 + a_1\cos x + b_1\sin x + a_2\cos 2x + b_2 \sin 2x + ...$
  - 傅里叶的**基本思想**：用函数代替向量，将一个函数展开到由一组正交基张成的空间上。
  - 傅里叶级数成立的原因是：作为component的每个函数的点积是正交的。
    - 函数点积的含义：$f^T·g = \int f(x)g(x) dx$
    - 对于$\sin x \cos x$这两个周期为$2\pi$的函数，${\sin x}^T·{\cos x} = \int_0^{2\pi}\sin x\cos x dx = 0$
  - 怎么求$a_1$?用$\cos x去点乘f(x)$.

# 对称矩阵
> Symmetric matrix
> Eigenvalues/ Eigenvectors

- 对称矩阵是最重要的矩阵
- **矩阵的特殊性体现在特征值和特征向量上**
- 实对称矩阵的两点事实
  - The Eigenvalues are real
  - **The Eigenvector s are perpendicular**

- Usual case: $A = S\Lambda S^{-1}$
- **Symmetric case: $A = Q\Lambda Q^{-1} = Q\Lambda Q^{T}$**
  - 这个分解很美，因为最后这个表达式一看就是对称的

- Why real eigenvalues?
  - conjugate: $x_1 = a + bi, \bar{x_1} = a - bi$ 共轭
  - $Ax =\lambda x \rightarrow \bar{Ax} = \bar{\lambda x} \rightarrow \bar{x}^T\bar{A}^T = \bar{x}^T\bar{\lambda} \rightarrow \bar{x}^T\bar{A}^Tx = \bar{x}^T\bar{\lambda}x \rightarrow \bar{x}^TAx = \bar{x}^T \bar{\lambda} x$
  - $Ax =\lambda x \rightarrow \bar{x}^TAx = \bar{x}^T\lambda x$
  - Also $\bar{x}x$ is the length of x, and $x \not ={0} $.
  - Hence, $\lambda = \bar{\lambda} \rightarrow \lambda $is real
  
- 什么是好矩阵
  - **1.特征值都是正值；2.特征向量互相垂直。**
  - 对于实数矩阵来说，$A=A^T$的矩阵是好矩阵；
  - 对于复数矩阵来说，$A=\bar{A}^T$的矩阵是好矩阵。
  
- 对称矩阵的本质
  - Every Symmetric matrix is a combination of perpendicular projection matrices **每个对称矩阵都是一组正交基的投影矩阵的线性组合**
  - $A = Q\Lambda Q^{-1} = \left[\begin{matrix}q_1&q_2&...&q_n\end{matrix}\right]\left[\begin{matrix}\lambda_1\\&\lambda_2\\&&...\\&&&\lambda_n\end{matrix}\right]\left[\begin{matrix}q_1^T\\q_2^T\\...\\q_n^T\end{matrix}\right] = \lambda_1q_1q_1^T+\lambda_2q_2q_2^T+ ... +\lambda_nq_nq_n^T$
  - 上式的$q_iq_i^T$是投影矩阵。因为$P={q_iq_i^T\over q_i^Tq_i}$，单位正交基的内积为1
  - 特征值和主元有同样多的正数和负数。这对于判断微分方程是否稳定很有用。
  - 特征值的乘积 = 主元乘积 = det的值

# 复矩阵和快速傅里叶变换
> Complex inner products
> Vectors discrete Fourier
> matrices fast Fourier transform = FFT

- 傅里叶矩阵是最重要的复矩阵

- 快速傅里叶变换将矩阵乘法的运算次数从$n^2减少到n\log_2^n$

- For $z \in C^n$ 复数
  - length of Z is $\sqrt{\bar{z}^Tz} = \sqrt{z^Hz}$
    - $z^H$表示z共轭后在转置，H代表Hermitian
    - 为保证复数距离为正，所以将复数乘法定义为其共轭复数的转置乘以原复数

- For $A \in complex$
  - Symmetric Matrix of $A = \bar{A}^T$, that is $A^H = A = \left[ \begin{matrix} 2&3+i\\3-i&5\end{matrix} \right]$
  - perpendicular $q_1,q_2,...,q_n \rightarrow \bar{q}_i^Tq_j$ = $\left \{ \begin{array}{c} 0,& if \quad i \not ={j}\\1,& if \quad i = j \end{array} \right.$
  - unitary matrix $\bar{Q}^TQ = I$ **酉矩阵**，即复数域的标准正交矩阵

- Fourier Matrix
  - $F_n = \left[\begin{matrix}1&1&1&\dots&1\\1&w&w^2&\dots&w^{n-1}\\1&w^2&w^4&\dots&w^{2(n-1)}\\\vdots&\vdots&\vdots&\ddots&\vdots\\1&w^{n-1}&w^{2(n-1)}&\dots&w^{(n-1)^2} \end{matrix}\right]$  
  - $(F_n)_{ij} = w^{ij}, w^n=1, w=e^{i{2\pi\over n}}= \cos({2\pi \over n})+i\sin({2\pi \over n})$
  - 傅里叶矩阵的关键特性是，它的列向量正交
  - 每个傅里叶矩阵与其2倍矩阵之间有联系，即可将$F_{2n}化简为两个F_n$及其修正项的形式。通过多次化简，最终将其简化为用$F_1$表示。

# 正定矩阵
> Positive Definite Matrix (test)
> Tests for Minumum $x^TAx \gt 0$
> Ellipsoids in $R^n$ 椭圆

- 矩阵正定性的判别方法
  1. 特征值 是否大于0
  2. 行列式 主对角线上各余子式是否大于0
  3. pivots 是否大于0
  4. $x^TAx$ 是否大于0

- 主轴定理
  - 对于正定矩阵A，$x^TAx$是个标量函数
  - 对这个函数进行配方，对于配方后的各项，系数是主元，各项内部的系数是消元时行变换的乘数
  - $x^TAx$取横截面，将得到一个椭圆。椭圆的主轴方向是特征向量的方向，主轴的长度是特征值的大小。

# 相似矩阵和若尔当标准型
> $A^TA$ is positive definite!  
> SIMILAR MATRICES A,B  
> JORDAN FORM: B = $M^{-1}AM$

- **positive definite** means 
  - $x^TAx \gt 0 $(except for x = 0)
  - **正定矩阵源自最小二乘法。**大量的实际科学问题涉及长方形矩阵，近似求解要用到$A^TA$，这就是个正定矩阵。
  - 因为$x^TA^TAx = (Ax)^TAx \gt 0$，所以$A^TA$是正定矩阵, rank(A) = n

- 正定矩阵将此前的课程内容串起来了，相似矩阵是本节课的重点，我们目前已经接近线性代数课程的核心内容奇异值分解了。

- n by n matrices A and B are similar means
  - for some M, $B = M^{-1}AM$
  - 相似矩阵的定义，给出了将一类矩阵归入一个集合的方法，每个集合中最特别的矩阵是对角阵$\Lambda$，它最简洁。
  - 相似矩阵也用来计算阵幂，即$A^n = M^{-1}\Lambda^nM$
  - **相似矩阵最重要的性质：特征值相同**
    - 证明：$Ax = \lambda x, B= M^{-1}AM$
    - 得，$M^{-1}A(MM^{-1})x = \lambda M^{-1}x \rightarrow BM^{-1}x = \lambda M^{-1}x$
    - 所以，$\lambda$也是B的特征值，但特征向量变为$M^{-1}x$

- Bad Case 得到重复特征值的情况
  - (1)One Small Family has: $\left[ \begin{matrix}4&0\\0&4 \end{matrix} \right]$
  - (2)Big Family includes: $\left[ \begin{matrix}4&1\\0&4 \end{matrix} \right]$
  - 上面(1)式的相似矩阵家族只有他自己，因为$M^{-1}cIM = cI$
  - 上面(2)式被称为若尔当标准型，对于那些不能被对角化的矩阵，若尔当标准型矩阵是他们能化简到的最接近对角矩阵的形式。

- Jordan Theorem
  - Every square A is similar to Jordan Matrix J
  - $J = \left[ \begin{matrix} [j_1]\\&[j_2]\\&&\ddots\\&&&[j_d]\end{matrix} \right]$
  - 分块矩阵的个数d，等于矩阵A的不重复的特征值个数

# 奇异值分解
> Singular Value Decomposition = SVD
> $A = U\Sigma V^T$
> $\Sigma diagonal$
> U,V orthogonal

- **奇异值分解**是矩阵最终和最好的分解
- 任意矩阵A可被分解为正交矩阵U对角矩阵$\Lambda$和正交矩阵$V^T$

- 目标：$AV = U\Sigma$
  - 我们要将行向量空间的一个向量$v_1$变换到列向量空间的一个向量$u_1$，即$u_1 = A v_1$。如果加入伸缩因子（scaling factors），使转换矩阵标准化，就是$\sigma_1u_1 = A v_1$。表示成矩阵就是$AV = U\Sigma$。
  - 为此，我们要寻找行空间的一组标准正交基V，以及列空间的一组标准正交基U，使得A作用在（行空间的）标准正交基V上以后，另一边就得到了作用在（列空间）标准正交基U上的一组正交向量，即变成将矩阵A转化成对角矩阵$\Sigma$
    - $\Sigma$是由系数组成的矩阵，必是对角阵。
  - $AV = U\Sigma \rightarrow A = U\Sigma V^{-1} \rightarrow U\Sigma V^{T} $
  - $A^TA = V \Sigma^TU^T U\Sigma V^{T} \rightarrow V \Sigma^T \Sigma V^{T}\rightarrow V \Sigma^2 V^{T}$
    - 因为V是标准正交基，所以上式就是$Q\Lambda Q^T$，那么$\Sigma^2$就是特征值的矩阵，V就是特征向量。根据特征值和特征向量的求解算法，就可以从$A^TA$求出V和$\Lambda$
    - 之所以要用$A^T$去乘A是为了消去两个标准正交基（U、V）中的一个，以先求出另一个。
  - 现在消去V求U：$AA^T = U \Sigma^TV^T V\Sigma U^{T} \rightarrow U \Sigma^T \Sigma U^{T}\rightarrow U \Sigma^2 U^{T}$
  - 求出U、V、和$\Lambda$，A的奇异值分解就得到了。
    - 注意：利用$Av_i = \sigma_iu_i$来确定$\sigma_i$正负号。

- 我们做了什么
  - $v_1,v_2,...,v_r$是行空间的标准正交基，$u_1,u_2,...,u_r$是列空间的标准正交基
  - $v_{r+1},v_{r+2},...,v_m$是行空间的零空间的标准正交基，$u_{r+1},u_{r+2},...,u_n$是列空间的零空间的标准正交基
  - $v_i和u_i$分别是（行空间及其零空间）和（列空间及其零空间）的一组恰当基。
  - 说他们恰当，是指（1）他们被标准正交化（去耦合）了，（2）他们的个数恰好张成整个行空间和列空间。
  - **通过奇异值分解，我们建立了$v_i和u_i$(行空间和列空间的基)之间的关系：$v_i = \sigma_i u_i$。**
  - 这样A乘以每个$v_i$，得到的都是对应于$u_i$方向上的一个向量。

# 线性变换即对应矩阵
> Linear Tranformations
> without coordinates: no matrix
> with coordinates -> matrix

- 线性变换的概念可以独立于矩阵而存在
- 引入坐标系以后，才有数值，以及矩阵

- 线性运算
  - T(v+w) = T(v)+T(w)
  - T(cv) = cT(v)
  - 向量的投影和旋转都是线性变换
  - 向量$\times$矩阵是线性变换

- 我们的目标是理解线性变换，理解的方法是找到线性变换背后的矩阵
  - T(v) = Av
  - information needed to know T(v) for all input
  - 只要确定线性变换对基向量的影响，就可以确定其对所有输入的影响
    - 因为线性代表空间均匀同质，所以才有这条性质

- **coordinates** comes from a basis
  - 坐标系建立在基的基础上
  - contruct matrix A that represent linear transformation $T:R^n\rightarrow b^m$
  - choose $v_1,v_2,...,v_n$ for inputs
  - choose  $w_1,w_2,...,w_m$ for outputs
    - eigen basis leads to diagonal matrix
  - rule to find A
    - given basis: $(v_1,v_2,...,v_n) and (w_1,w_2,...,w_m)$
    - 1st column of A: apply $T(v_1) = a_{11}w_1,+a_{21}w_2+...+a_{m1}w_m$
    - 上式可得：**A(input coordinates) = (output coordinates)**
      - **矩阵的本质：空间的线性变换**
  
- **求导是一种线性变换**
- **矩阵的逆相当于线性变换的逆变换**
- **矩阵的乘积相当于线性变换的乘积，实际上矩阵乘法就源自线性变换的乘法**
  

# 基变换和图像压缩
> Change of basis
> Compression of images
> Tranformation $\leftrightarrow$ matrix

- 矩阵用坐标来描述线性变化

- 图像压缩原理
  - 首先作基变换，从原坐标系换到傅里叶或小波基坐标系上来
  - 然后进行压缩处理，设定一个阀值，低于这个数值的被归零，高于这个数值的才留存数据信息。

- 什么是矩阵 A
  - 对于一组基 $v_1,v_2,...,v_8$
  - Know T completely from $T(v_1),T(v_2),...,T(v_8)$
    - 只要知道线性变换T对基做了什么，就知道T的所有信息了。
  - 因为对于任何向量x有： $x = c_1v_1 + c_2v_2+ ... + c_8v_8$
  - 所以 $T(x) = c_1T(v_1) + c_2T(v_2)+ ... + c_8T(v_8)$
  - 计算T对每个基的作用：$T(v_1) = a_{11}v_1 + a_{21}v_2 + ...a_{81}v_8$,$T(v_2) = a_{12}v_1 + a_{22}v_2 + ...a_{82}v_8$
  - $[A]^T = \left[ \begin{matrix} a_{11}& a_{21}&...\\a_{12}& a_{22}&... \\\vdots& \vdots&\vdots \\a_{18}& a_{28}&...\end{matrix} \right]$ 

# 复习三
- 半正定矩阵：$x^TAx \geq 0$
- **研究矩阵往往从特征值、特征向量开始**
- 正交矩阵仅改变方向，但不改变长度

# 左右逆和伪逆
> 4 subspaces
> Left inverses
> right inverses
> Pseudo-inverses 伪逆

- 左逆矩阵
  - m by n 矩阵，$r= n \lt m$
  - 左逆矩阵 = $(A^TA)^{-1}A^T$
  - 因为$(A^TA)^{-1}A^T \times A = I_{n\times n}$
- 右逆矩阵
  - m by n 矩阵，$r= m \lt n$
  - 右逆矩阵 = $A^T(AA^T)^{-1}$
  - 因为$ A\times A^T(A^TA)^{-1} = I_{n\times n}$
- A乘以左逆矩阵= $A(A^TA)^{-1}A^T$ = 向列向量空间的投影矩阵$P_{col}$
- 右逆矩阵A乘以= $A^T(AA^T)^{-1}A$ = 向行向量空间的投影矩阵$P_{row}$
- 伪逆$A^+$
  - 统计学家最喜欢伪逆
    - 统计学家喜欢最小二乘法，而且他们的数据通常存在线性相关问题或者无解问题。这就需要进行投影，来进行求解。
  - m by n 矩阵，$r\lt m,r \lt n$
  - 如何求伪逆：
    - 首先进行奇异值分解：$A = U\Sigma V^T$
    - 伪逆：$A^+ = V\Sigma^+ U^{T}$
  - 伪逆取消了Nullspace的影响，使解投影到列向量空间。
    - **非满秩矩阵之所以没有逆，是因为nullspace的存在**。因为任何向量乘以0向量都是0，而0再没法映射回去得到原向量。伪逆的**基本思想**就是，不考虑零向量部分，只考虑存在pivot值的空间映射。

# 线性代数的本质
- 线性代数有数值和几何两个方面。数值方面侧重应用工具解决问题，几何方面侧重直观和解决问题的工具的选择。数值计算可以留给计算机，理解几何意义则可以让人更清晰地理解概念，进而找出解决问题的思路。
- **向量**，对于物理学家来说就是有长度和方向的有向线段；对于计算机学家来说，就是一个数列；对于数学家来说只要满足“可加性”和“成比例（一阶齐次）”的一切对象都是向量。
- scalar标量，span张成的空间，Lingering constant剩余常数，linear system of equations线性方程组
- 坐标系的基向量的线性组合可以张成整个坐标系空间，改变基向量的scale和direction同样可以让一个向量到达坐标系任何一处。
  - 坐标系不太重要，可随意选择。
- 线性变换的“变换”只不过是函数的一种比较“花哨”的说法。之所以用变换这个词，旨在强调这种函数映射是可视化的。线性变换的**线性**则强调两点：一是直线变换之后仍是直线，二是原点不变。
- **矩阵**是对两个空间之间进行线性变换的数值描述。
- 线性变换是操纵空间的一种方式。以变换后的空间极坐标构成列的矩阵，为描述这种空间变换提供了一种语言，即**矩阵就是空间变换函数**。矩阵向量乘法是计算这种线性变换作用于特定向量的一种途径。
- 为什么看中线性变换前后的基变换？因为向量(x,y)变换后的新坐标，完全可以由变换前后的基坐标$(i,j)$和$(\hat{i},\hat{j})$计算出来:$\hat{x} = x\hat{i}, \hat{y} = y\hat{j}$，**矩阵的列就是变换后的基向量**。
- **矩阵乘法**的来历：矩阵乘法就是空间的两次相继线性变换，结果就是乘积（product）。相继意味着order matters。先进行哪种空间变换后进行哪种会产生不同效果。和复合函数f(g(x))一样，越靠近变量左边的变换越先进行。
  - 这条对我帮助很大。以前我总是认为矩阵向量乘法是向量对矩阵的作用，现在才知道是**矩阵对向量**进行作用，正常的作用顺序是用矩阵进行左乘。
- **行列式**是线性变换前后，面积（体积）的改变比例。所以，如果行列式为0，意味着要在原空间被压缩到了更低维的空间里。如果行列式值为负，说明有基向量的方向被改变了（空间翻转了）。
- 求解线性方程组$Ax=b$，意味着找到一个向量，经A矩阵变换后，与b重合。
- **逆矩阵**就是空间变换的相反变换，矩阵乘以它的逆就是空间不发生变化，用矩阵描述这种不变就是I。
- **矩阵的秩**就是变换后的空间的维度。为何秩不能大于矩阵的行数或列数？因为函数只能多对一映射，不能一对多。
- **列空间**是所有可能的输出向量$Ax$构成的集合。这个名字源于：矩阵的列告诉我们基向量变换后的位置，而这些变换后的基向量张成的空间就是列空间！
- **零空间**必定在列空间中，因为原点在变换前后保持不变。对满秩变换来说，唯一能在变换后落在原点的，就是零向量自身。但对于非满秩变换，因为空间维度压缩的原因，可以有无数向量被压缩到原点。变换后被压缩到零点的原向量所构成的空间，叫零空间！对于齐次线性方程组$Ax=0$，解集就是零空间。
- 对于矩阵$A_{m\times n}$，**行m是变换后空间维度**，**列数（未知数个数n）是变换前空间维度**。记住矩阵作用的未知数和函数f(x)中的情况一样，都是输入，即来源于变换前空间。
- **点积**：$x^Ty$ = 一个数字。左边$x^T$应该看成一个$1\times n$矩阵，它将n维空间变换成1维空间。这个1维空间就是数轴，矩阵就是将n维向量y变成数轴上的一个数字（其实是个1维向量）。
  - 这条对我的帮助也很大。我之前脑子里一直有线性代数中存在标量和向量两套系统的误解，一直想搞清楚两套系统之间的关系。现在明白了，原来都是一回事，线性空间中只有向量的概念，没有标量的容身之所。所有的标量，都是一维向量。
- **投影**：向量a在向量b的投影 = ${aa^T\over a^Ta}b$。
- **叉积**：两个向量的叉积是这两个向量及其平移所围成的四边形面积，正负号由右手法则决定。
  - 两个向量的叉积=四边形面积= 两个向量组成的行列式。为什么？因为行列式是变换前后的面积缩放比例，而变换前坐标系是直角坐标系，在坐标轴上的两个单位向量所围成的面积就是1。
- **基变换**：向量和数字之间的转化关系就意味着坐标系。如何对另一个空间的一组基应用变换M？首先用矩阵A将本空间的基转化成另一个空间的基，然后在那个空间应用变换M，最后将变换后的向量用逆矩阵$A^{-1}$变回用本空间的基来表示。这个思路就是表达式$A^{-1}MA$，它暗示一种数学上的转移作用。M代表一种变换，外侧两个矩阵代表转移作用。三个矩阵的乘积仍然代表同一种变换，但确是从其他人的角度来看的。
- **特征值**和**特征向量**：$Ax=\lambda x$，特征向量x是经矩阵A变换后仍保持原来方向的向量，特征值是该变量在变换后的伸缩（拉长）因子。
  - 对角矩阵的主对角线元素就是特征值，因为这类矩阵只有基的伸缩、没有旋转！
  - 研究变换（即矩阵）过程中，坐标轴的不是特别重要，因为它们可以任意选取，但特征向量很有意义，因为它们在变换过程中保持方向不变，所有其他部分围绕它们进行旋转！
  - 因此，很多时候我们通过将特征向量作为新的基，来求解问题。比如，$A^{-1}MA$，其中A的列是特征向量代表当前空间的基变换到以特征向量为基的空间，M是要研究的变换，$A^{-1}$是特征向量空间往当前空间的映射。那么该式代表同一变换，但从特征向量空间视角看。这样变换后，矩阵就被对角化了。
    - 这就是将矩阵对角化的思想精髓。比吉尔伯特讲得还好！
  - 对于求阵幂，这个算法意味着，先到特征向量空间完成阵幂计算，然后在换回本空间。
- Formal definition of linearity:
  - Additivity:$L(v+w) =L(v) + L(w)$
  - Scaling:$L(cv) = cL(v)$
  - Linear transformations preserve addition and scalar multiplication
  - 线性的上述性质，使得通过研究变换对基的作用来了解其对空间内任何向量的作用成为可能！
  - 求导运算为什么是线性的：因为$(f(x)+g(x))' = f'(x)+g'(x),(cf(x))' = cf'(x)$。所以吉尔伯特教授用矩阵来求微分方程、差分方程！
  - **标准正交基**：变换后基仍然互相垂直，且长度不变，即空间只是转了角度。
- 毛立云点评
  - You blow my mind!
  - 听了以后确实受益匪浅。之所以线性代数没学好，就是概念不清整的。这个系列的视频，正是我的菜，帮我纠正了好几个错误认识。
  - 另外，此前觉得吉尔伯特讲得很好了，没人可以超越了。听了这个小博主讲的，认识到每个人都有局限性。每个人、每本书都是对知识的一份使用说明书，多看几本可能得到新的视角。


