# MarkDown

- [MarkDown](#markdown)
  - [Print Markdown to HTML](#print-markdown-to-html)
  - [Headings](#headings)
  - [Paragraphs](#paragraphs)
  - [Line Breaks](#line-breaks)
  - [Emphasis](#emphasis)
  - [Blockquotes](#blockquotes)
  - [Lists](#lists)
    - [Ordered Lists](#ordered-lists)
    - [Unordered Lists](#unordered-lists)
    - [Adding Elements in Lists](#adding-elements-in-lists)
  - [Code](#code)
  - [Horizontal Rules 水平线](#horizontal-rules-水平线)
  - [Links](#links)
  - [Images](#images)
  - [Escaping Characters](#escaping-characters)
  - [HTML](#html)
- [数学公式](#数学公式)
  - [行内公式](#行内公式)
  - [行间公式](#行间公式)
  - [希腊字母](#希腊字母)
  - [偏导数符号](#偏导数符号)
  - [卡方](#卡方)
  - [箭头上标](#箭头上标)
  - [任意](#任意)
  - [上标与下标](#上标与下标)
  - [括号](#括号)
    - [小括号与方括号](#小括号与方括号)
    - [大括号](#大括号)
    - [尖括号](#尖括号)
  - [取整](#取整)
    - [上取整](#上取整)
    - [下取整](#下取整)
  - [求和与积分](#求和与积分)
    - [求和](#求和)
    - [极限](#极限)
    - [积分](#积分)
  - [连乘](#连乘)
  - [其他](#其他)
  - [分式与根式](#分式与根式)
    - [分式](#分式)
    - [连分数](#连分数)
  - [根式](#根式)
  - [分类表达式](#分类表达式)
  - [多行表达式](#多行表达式)
  - [方程组](#方程组)
  - [特殊函数与符号](#特殊函数与符号)
    - [三角函数](#三角函数)
    - [比较运算符](#比较运算符)
    - [集合关系与运算](#集合关系与运算)
  - [排列](#排列)
  - [箭头](#箭头)
  - [逻辑运算符](#逻辑运算符)
  - [操作符](#操作符)
  - [等于](#等于)
  - [范围](#范围)
  - [模运算](#模运算)
  - [点](#点)
  - [顶部符号](#顶部符号)
  - [表格](#表格)
  - [矩阵](#矩阵)
  - [括号](#括号-1)
  - [元素省略](#元素省略)
  - [增广矩阵](#增广矩阵)
  - [公式标记与引用](#公式标记与引用)
  - [字体](#字体)
    - [黑板粗体字](#黑板粗体字)
    - [黑体字](#黑体字)

## Print Markdown to HTML

- Commands Markdown: Print current document to HTML and Markdown: Print documents to HTML (batch mode)

## Headings

1. To create a heading, add number signs (#) in front of a word or phrase.

    > # Heading Level 1

    > ## Heading Level 2

    > ### Heading Level 3

    > #### Heading Level 4

    > ##### Heading Level 5

    > ###### Heading Level 6

2. Alternate Syntax. On the line below the text, add any number of == characters for heading level 1 or -- characters for heading level 2.
3. You should also put blank lines before and after a heading for compatibility.

## Paragraphs

1. To create paragraphs, use a blank line to separate one or more lines of text.

## Line Breaks

1. To create a line break or new line (<br>), end a line with two or more spaces, and then type return.

## Emphasis

> You can add emphasis by making text bold or italic.

1. Bold

    > To bold text, add two **asterisks** or **underscores** before and after a word or phrase. To bold the middle of a word for emphasis, add two asterisks without spaces around the letters.

2. Italic

    > To italicize text, add one *asterisk* or *underscore* before and after a word or phrase.
    > To italicize the middle of a word for emphasis, add one as*ter*isk without spaces around the letters.

3. Bold and Italic

    > To emphasize text with bold and italics at the same time, add ***three asterisks*** or _**underscores**_ before and after a word or phrase. To bold and italicize the middle of a word for emphasis, add three as***ter***isks without spaces around the letters.

## Blockquotes

1. To create a blockquote, add a > in front of a paragraph.

    > Blockquote like this

2. Blockquotes with Multiple Paragraphs, add a > on the blank lines between the paragraphs.

    > Blockquotes with Multiple Paragraphs like this
    >
    > and this

3. Nested Blockquotes,  add a >> in front of the paragraph you want to nest.

    > Nested Blockquotes like this
    >
    >> and this

## Lists

> You can organize items into ordered and unordered lists.

### Ordered Lists

> To create an ordered list, add line items with numbers followed by periods.

> The numbers don’t have to be in numerical order, but the list should start with the number one.

      1. First item
      2. Second item
      3. Third item
      4. Fourth item

### Unordered Lists

> To create an unordered list, add dashes (-), asterisks (*), or plus signs (+) in front of line items.
> Indent one or more items to create a nested list.
> If you need to start an unordered list item with a number followed by a period, you can use a backslash (\) to escape the period.

- unordered list like this

- this

- and this

- 1985\. still and this

### Adding Elements in Lists

> To add another element in a list while preserving the continuity of the list, indent the element four spaces or one tab, as shown in the following examples.

- This is the first list item.
- Here's the second list item.

    I need to add another paragraph below the second list item.

- And here's the third list item.

## Code

1. To denote a word or phrase as code, enclose it in backticks (`).
    > `code`  
2. Escape one or more backticks by enclosing the word or phrase in double backticks (``).
    > ``Use `code` in your Markdown file.``  
3. Code Blocks
    > To create code blocks, indent every line of the block by at least four spaces or one tab.

    <html>
      <head>
      </head>
    </html>

## Horizontal Rules 水平线

> To create a horizontal rule, use three or more asterisks (***), dashes (---), or underscores (___) on a line by themselves.

> ***

> ---

> _________________

## Links

1. To create a link, enclose the link text in brackets and then follow it immediately with the URL in parentheses.

    > My favorite search engine is [Goole](https://www.google.com).

2. To add a title  for a link, enclose it in parentheses after the URL.

    > My favorite search engine is [Google](https://www.google.com "这玩意儿比baidu好多了").

3. To quickly turn a URL or email address into a link, enclose it in angle brackets.

> <https://www.markdownguide.org>  
> <fake@example.com>

## Images

1. To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses.
2. You can optionally add a title after the URL in the parentheses.

> ![Mountains are beautiful](image/mountains.jpg "这玩意儿是俺加的")

## Escaping Characters

1. To display a literal character that would otherwise be used to format text in a Markdown document, add a backslash (\) in front of the character.

> \* Without the backslash, this would be a bullet in an unordered list.

## HTML

1. Many Markdown applications allow you to use HTML tags in Markdown-formatted text.

2. To use HTML, place the tags in the text of your Markdown-formatted file.

> This **word** is bold. This <em>word</em> is italic.

# 数学公式

## 行内公式

$\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.$

## 行间公式

$$\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.$$

## 希腊字母

A α $\alpha$  
B β \beta  
Γ γ \gamma  
Δ δ \delta
E ϵ \epsilon
Z ζ \zeta
H η \eta
Θ θ \theta
I ι \iota
K κ \kappa
Λ λ \lambda
M μ \mu
N ν \nu
Ξ ξ \xi
O ο \omicron
Π π \pi
P ρ \rho
Σ σ \sigma
T τ \tau
Υ υ \upsilon
Φ ϕ \phi
X χ \chi
Ψ ψ \psi
Ω ω \omega

## 偏导数符号

$\partial$  \partial

## 卡方

$\chi$ \chi

## 箭头上标

$X \stackrel{F}{\rightarrow} Y$

## 任意

$\forall$

## 上标与下标

- 上标和下标分别使用^ 与_ ，例如$x_i^2$。
- 默认情况下，上、下标符号仅仅对下一个组起作用。一个组即单个字符或者使用{..} 包裹起来的内容。如$10^10$和$10^{10}$

## 括号

### 小括号与方括号

- 使用原始的( ) ，[ ] 即可，如$[2+3](4+4)$
- 使用\left(或\right)使符号大小与邻近的公式相适应（该语句适用于所有括号类型），如$\left(\frac{x}{y}\right)$

### 大括号

- 由于大括号{} 被用于分组，因此需要使用\{和\}表示大括号，也可以使用\lbrace 和\rbrace来表示。如$\{a*b\}:a∗b$ 或$\lbrace a*b\rbrace :a*b$ 表示。

### 尖括号

区分于小于号和大于号，使用\langle 和\rangle 表示左尖括号和右尖括号。如$\langle x \rangle$

## 取整

### 上取整

使用\lceil 和 \rceil 表示。 如，$\lceil x \rceil$

### 下取整

使用\lfloor 和 \rfloor 表示。如，$\lfloor x \rfloor$

## 求和与积分

### 求和

> \sum 用来表示求和符号，其下标表示求和下限，上标表示上限。如: $\sum_{r=1}^n$

### 极限

$\lim\limits_{x\rightarrow\infty}{f(x)}$

### 积分

1. \int 用来表示积分符号，同样地，其上下标表示积分的上下限。如，$\int_{r=1}^\infty$
2. 多重积分同样使用 int ，通过 i 的数量表示积分导数：  
$\iint$  
$\iiint$

## 连乘

$\prod {a+b}$  
$\prod_{i=1}^{K}$  

## 其他

$\prod$

$\bigcup$

$\bigcap$

$arg\,\max_{c_k}$

$arg\,\min_{c_k}$

$\mathop {argmin}_{c_k}$

$\mathop {argmax}_{c_k}$

$\max_{c_k}$

$\min_{c_k}$

## 分式与根式

### 分式

- 一、使用$\frac ab$，\frac作用于其后的两个组a和b。如果你的分子或分母不是单个字符，用{..}来分组，比如$\frac {a+c+1}{b+c+2}$。
- 二、使用\over来分隔一个组的前后两部分，如${a+1}\over{b+1}$
  
### 连分数

- 书写连分数表达式时，用\cfrac代替\frac或者\over两者效果对比如下：

> \frac 表示如下：
 $$x=a_0 + \frac {1^2}{a_1 + \frac {2^2}{a_2 + \frac {3^2}{a_3 + \frac {4^2}{a_4 + ...}}}}$$

> \cfrac 表示如下：
$$x=a_0 + \cfrac {1^2}{a_1 + \cfrac {2^2}{a_2 + \cfrac {3^2}{a_3 + \cfrac {4^2}{a_4 + ...}}}}$$

## 根式

- 根式使用\sqrt 来表示。如，开4次方：$\sqrt[4]{\frac xy}$ ，开平方：$\sqrt {a+b}$

## 分类表达式

- 定义函数的时候经常需要分情况给出表达式，使用\begin{cases}…\end{cases} 。其中：
    > 使用\\\ 来分类，  
    > 使用&指示需要对齐的位置，  
    > 使用\\+空格 表示空格。
$$
f(n)
\begin{cases}
\cfrac n2, &if\ n\ is\ even\\
3n + 1, &if\  n\ is\ odd
\end{cases}
$$

$$
L(Y,f(X)) =
\begin{cases}
0, & \text{Y = f(X)}  \\
1, & \text{Y $\neq$ f(X)}
\end{cases}
$$

- 如果想分类之间的垂直间隔变大，可以使用\\[2ex] 代替\\ 来分隔不同的情况。(3ex,4ex 也可以用，1ex 相当于原始距离）。如下所示：

$$
L(Y,f(X)) =
\begin{cases}
0, & \text{Y = f(X)} \\[5ex]
1, & \text{Y $\neq$ f(X)}
\end{cases}
$$

## 多行表达式

- 将一行公式分多行进行显示。

$$
\begin{equation}\begin{split}
a&=b+c-d\\
&\quad+e-f\\
&=g+h\\
&=i
\end{split}\end{equation}
$$

>其中begin{equation} 表示方程开始，end{equation} 表示结束
> begin{split} 表示多行公式开始，end{split} 表示结束
> 公式中用\\\表示回车到下一行，& 表示对齐的位置。

## 方程组

- 使用\begin{array}...\end{array} 与\left \{ 与\right. 配合表示方程组:

$$
\left \{
\begin{array}{c}
a_1x+b_1y+c_1z=d_1 \\
a_2x+b_2y+c_2z=d_2 \\
a_3x+b_3y+c_3z=d_3
\end{array}
\right.
$$

- 注意：通常MathJax通过内部策略自己管理公式内部的空间，因此a…b 与a…….b （.表示空格）都会显示为ab 。可以通过在ab 间加入\ ,增加些许间隙，\; 增加较宽的间隙，\quad 与\qquad 会增加更大的间隙。

## 特殊函数与符号

### 三角函数

$\sin x$  
$\arctan x$

### 比较运算符

- 小于($\lt$ )
- 大于($\gt$)
- 小于等于($\le$)
- 大于等于($\ge$)
- 不等于($\ne$)
- 可以在这些运算符前面加上$\not$，如$\not\lt$
- $$

### 集合关系与运算

并集($\cup$)  
交集($\cap$)  
差集($\setminus$)  
子集($\subset$)  
子集($\subseteq$)  
非子集($\subsetneq$)  
父集($\supset$)  
属于($\in$)  
不属于($\notin$)  
空集($\emptyset$)  
空($\varnothing$)  

## 排列  

- $\binom{n+1}{2k}$
- ${n+1 \choose 2k}$

## 箭头  

$(\to )$  
$(\rightarrow )$  
$(\leftarrow )$  
$(\Rightarrow )$  
$(\Leftarrow )$  
$(\mapsto )$  

## 逻辑运算符

$(\land )$  
$(\lor )$  
$(\lnot )$  
$(\forall )$  
$(\exists )$  
$(\top )$  
$(\bot )$  
$(\vdash )$  
$(\vDash )$  

## 操作符

$(\star )$  
$(\ast )$  
$(\oplus )$  
$(\circ )$  
$(\bullet )$

## 等于

$(\approx)$  
$(\sim)$  
$(\equiv)$  
$(\prec)$  
$(\preceq)$
$(\succ)$
$(\succeq)$

## 范围

$(\infty )$  
$(\aleph_o )$  
$(\nabla )$  
$(\Im )$  
$(\Re )$

## 模运算

- $(\pmod )$  

> 如$a \equiv b \pmod n$

## 点

- $(\ldots )$  
- $(\cdots )$
- $(\cdot )$

> 其区别是点的位置不同，\ldots 位置稍低，\cdots 位置居中
> 如，
$$
a_1+a_2+\ldots+a_n \\
a_1+a_2+\cdots+a_n
$$

##

- 帽子命令：$\hat{x}$

- 帽子命令：$\tilde{x}$

- 倒尖帽子命令1：$\check{x}$

- 倒尖帽子命令2：$\breve{x}$

- 声调帽子命令：$\grave{x}$

- 声调帽子命令：$\acute{x}$

- 大帽子命令：$\widehat{abcdefg}$
​

## 顶部符号

- 对于单字符，$\hat x$
- 多字符可以使用, $\widehat {xy}$
- 类似的还有, $(\overline x )$
- 矢量$(\vec x)$
- 向量$(\overrightarrow {xy} )$
- $(\dot x )$
- $(\ddot x )$
- $(\dot {\dot x})$

## 表格

- 使用\begin{array}{列样式}…\end{array} 来创建表格
- 列样式可以是clr 表示居中，左，右对齐
- 还可以使用| 表示一条竖线
- 表格中各行使用\\ 分隔
- 各列使用& 分隔
- 使用\hline 在本行前加入一条直线

$$
\begin{array}{c|lcr}
n & \text{Left} & \text{Center} & \text{Right} \\
\hline
1 & 0.24 & 1 & 125 \\
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i \\
\end{array}
$$

## 矩阵

- 使用\begin{matrix}…\end{matrix} 来表示矩阵
- 在\begin 与\end 之间加入矩阵中的元素即可
- 矩阵的行之间使用\\\ 分隔
- 列之间使用& 分隔

$$
\begin{matrix}
1 & x & x^2 \\
1 & y & y^2 \\
1 & z & z^2 \\
\end{matrix}
$$

## 括号

- 使用\left 与\right 配合表示括号符号
- 也可以使用特殊的matrix , 即替换\begin{matrix}…\end{matrix} 中matrix 为pmatrix ，bmatrix ，Bmatrix ，vmatrix , Vmatrix

    > pmatrix$\begin{pmatrix}1 & 2 \\ 3 & 4\\ \end{pmatrix}$  
    > bmatrix$\begin{bmatrix}1 & 2 \\ 3 & 4\\ \end{bmatrix}$
    > Bmatrix$\begin{Bmatrix}1 & 2 \\ 3 & 4\\ \end{Bmatrix}$
    > vmatrix$\begin{vmatrix}1 & 2 \\ 3 & 4\\ \end{vmatrix}$
    > Vmatrix$\begin{Vmatrix}1 & 2 \\ 3 & 4\\ \end{Vmatrix}$

## 元素省略

- 可以使用$\cdots$，$\ddots$，$\vdots$ 来省略矩阵中的元素，如：

$$
\begin{pmatrix}
1&a_1&a_1^2&\cdots&a_1^n\\
1&a_2&a_2^2&\cdots&a_2^n\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&a_m&a_m^2&\cdots&a_m^n\\
\end{pmatrix}
$$

## 增广矩阵

- 增广矩阵需要使用\begin{array} ... \end{array} 来实现

$$
\left[  \begin{array}  {c c | c} %这里的c表示数组中元素对齐方式：c居中、r右对齐、l左对齐，竖线表示2、3列间插入竖线
1 & 2 & 3 \\
\hline %插入横线，如果去掉\hline就是增广矩阵
4 & 5 & 6
\end{array}  \right]
$$

## 公式标记与引用

- 使用\tag{yourtag} 来标记公式，如果想在之后引用该公式，则还需要加上\label{yourlabel} 在\tag 之后

$$
a = x^2 - y^3 \tag{1}\label{1}
$$

- 如果不需要被引用，只使用\tag{yourtag}

$$
x+y=z\tag{1.1}
$$

- \tab{yourtab} 中的内容用于显示公式后面的标记
- 公式之间通过\label{} 设置的内容来引用
- 为了引用公式，可以使用\eqref{yourlabel}
    > $$a + y^3 \stackrel{\eqref{1}}= x^2$$
- 或者使用\ref{yourlabel} 不带括号引用
    > $$a + y^3 \stackrel{\ref{111}}= x^2$$

## 字体

### 黑板粗体字

- 此字体经常用来表示代表实数、整数、有理数、复数的大写字母
    > $\mathbb ABCDEF$
    > $\Bbb ABCDEF$

### 黑体字

> $\mathbf ABCDEFGHIJKLMNOPQRSTUVWXYZ$
> $\mathbf abcdefghijklmnopqrstuvwxyz$

 打印机字体

> $\mathtt ABCDEFGHIJKLMNOPQRSTUVWXYZ$

脚注[^1]
[^1]:Markdown是一种纯文本标记语言

注释：
文档的注释可以通过多种形式实现，推荐使用 <!-- 被注释掉的文字 --> 方式。
