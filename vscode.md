# 1. Visual Stido Code 权威指南


## 1.1. 如何学习Visual Studio Code

### 1.1.1. 学会搜索
学会使用Stack Overflow和Google是成为一名优秀程序员的必要条件。

### 1.1.2. 知其然知其所以然
Visual Studio Code是基于Electron开发框架开发的，而Electron是基于HTML、CSS、JavaScript等Web技术栈开发的。

## 1.2. Visual Studio Code简介
Visual Studio Code是一款免费且开源的现代化轻量级代码编辑器。

## 1.3. 核心组件

### 1.3.1. Electron
原名Atom Shell，是GitHub开发的恶一个开源框架，以Node.js作为运行时（runtime），以Chromium作为渲染引擎，使开发者可以适用HTML、CSS和JavaScript这样的前端技术栈来开发跨平台桌面GUI应用程序。

### 1.3.2. Monaco Editor
一个基于浏览器的代码编辑器。

### 1.3.3. TypeScript
是JavaScript的严格超集，其设计目标是开发大型应用。

### 1.3.4. Language Server Protocal (LSP)
一种编辑器和语言服务器之间的协议，可以让编辑器支持各种编程语言，提供了诸如自动补全、定义跳转、代码格式化等与编程语言相关的功能。

### 1.3.5. Debug Adapter Protocal (DAP)
一种让编辑器支持各种编程语言的Debugger的协议，抽象了开发工具和调试工具之间的通信。

### 1.3.6. Xterm.js
集成终端（Integrated Terminal）基于被广泛使用的开源项目Xterm.js开发而来。

## 1.4. 安装与配置

### 1.4.1. 启动
在终端中输入code， 即可启动vscode

## 1.5. 快速入门

### 1.5.1. Visual Studio Code Insider
vscode一个月发布一个新版本，而vscode insider每天发布新版本。

## 1.6. 设置
### 1.6.1. 两种不同的设置范围
- 用户设置（User Settings），是一个全局范围的设置。
- 工作区设置（Workspace Settings），设置被保存在相应的工作区，只会对相应的工作区生效。工作区设置会覆盖用户设置。

### 1.6.2. 打开JSON设置文件
通过Ctrl+Shift+P快捷键打开命令面板，然后输入并执行Preferences：Open Settings (JSON)命令。

### 1.6.3. 针对编程语言的特定设置
通过Ctrl+Shift+P快捷键打开命令面板，然后输入并执行Preferences：Configure Language Specific Settings命令。

### 1.6.4. 并排编辑
按住Alt快捷键，同时单击资源管理器的文件

### 1.6.5. 打开文件所在位置
首先单击选中资源管理器中的文件，然后按Shift+Alt+R快捷键。

### 1.6.6. 比较两个文件
按住Ctrl点选或按住Shift片选要比较的文件，单击右键并选择Compare Selected来比较两个文件。

### 1.6.7. 过滤文件
选中资源管理器，然后直接输入想查找的文件名。

### 1.6.8. 禅模式
先按住Ctrl+K，然后松开，再按Z键。

### 1.6.9. 多光标
- 按照Alt然后单击鼠标左键。
- 或者按Ctrl+Shift+L，给光标处单词所有出现的位置，添加光标。

### 1.6.10. 列选择
按住Shift+Alt，然后拖动光标。

### 1.6.11. 搜索
- Ctrl+F在单个文件搜索。
- Ctrl+Shift+F跨文件搜索。
- Ctrl+Shift+J调出高级搜索。

### 1.6.12. IntelliSense 智能提示
Ctrl+Space触发智能提示，Tab或Enter接受相应职能补全。

### 1.6.13. 代码折叠
- Ctrl+K, Ctrl+J展开所有代码块。
- Ctrl+K, Ctrl+0(零)折叠所有代码块。

### 1.6.14. 快捷键编辑器
Ctrl+K, Ctrl+s

### 1.6.15. 解决快捷键冲突
首先开打快捷键编辑器，然后找到可能发生冲突的快捷键组合，然后点击右键，在右键菜单中有一个Show Same Keybings选项。

### 1.6.16. 自定义配置快捷键
在命令面板上调用Preferences：Open Keyboard Shortcuts （JSON）命令，打开快捷键配置文件，其配置的快捷键优先级最高。

### 1.6.17. 关闭当前窗口
Ctrl+W

### 1.6.18. 在所有打开的文件中跳转
Ctrl+Tab

### 1.6.19. 删除或添加当前行的注释
Ctrl+/

### 1.6.20. 光标移动到当前行的起始/末尾
Home/End

### 1.6.21. 跳转到定义
F12

### 1.6.22. 替换
- Ctrl + H
- Ctrl + Shift + H

### 1.6.23. 选中当前行
Ctrl + L

### 1.6.24. 切换全屏模式
F11

### 1.6.25. 放大/缩小
Ctrl+=，Ctrl+-

### 1.6.26. 另存为 
Ctrl+Shift+S

### 1.6.27. 打开文件 
Ctrl+o

### 1.6.28. 打开集成终端 
Ctrl+· （backquaote）

### 1.6.29. 设置终端的打开路径 
默认情况下，终端会在当前文件资源管理器的文件夹所在位置打开。该打开路径可以通过terminal.integrated.cwd配置项进行更改。

## 1.7. 进阶应用

### 1.7.1. 代码导航右键菜单
在编辑器区域中，把鼠标放到任意一个符号上，单击右键，就会显示右键菜单。包括Go to Definition转到定义，Peek Definition查看定义，Go to Type Definition转到类型定义，Find All References查找所有引用和Peek References查看引用。

### 1.7.2. 跳转到定义
- 按F12可以跳转到一个符号的定义。
- 按Alt+F12，可以通过内联编辑器查看定义。
- 按住Ctrl，并悬停在一个符号上，可以看声明预览。
- 按Ctrl+Click，可以跳转到该声明的定义。
- 按Ctrl+Alt+Click，可以把定义所在文件在另一侧打开。

### 1.7.3. 查找所有引用
- 按Shift+F12，可以通过内联编辑器查看引用。
- 按Shift+Alt+F12，可以查看一个符号的所有引用。

### 1.7.4. 跳转到实现
按Ctrl+F12，跳转到一个符号的实现。

### 1.7.5. 跳转到文件中的符号
按Ctrl+Shift+O

### 1.7.6. 跳转到工作区中的符号
按Ctrl+T

### 1.7.7. 括号匹配
按Ctrl+Shift+\

### 1.7.8. 跳转到错误和警告
- 按Ctrl+Shift+M，调出Problems面板，现实所有的错误和警告。
- 按F8或Shift+F8，在当前文件的错误和警告之间循环跳转。

### 1.7.9. Git有关操作
- 命令面板键入Git：Clone来克隆Git仓库
- Ctrl+Shift+G，打开源代码管理视图
- 消息输入框键入信息后，按Ctrl+Enter，提交代码

### 1.7.10. 将VSCode作为Git编辑器
- 在命令行运行**git config --global core.editor "code --wait"**， 将VScode设置成Git的默认编辑器。
- 在命令行运行**git config --global -e**， 调用VSCode打开全局的.gitconfig文件，配置Git。

### 1.7.11. 创建可复用的代码片段
1. 插入代码片段
   1. 打开命令面板，键入Insert Snippet命令
   2. 或，通过职能提示插入代码片段
2. 创建自定义的代码片段
   1. 打开命令面板，键入Preferences： Configure User Snippets
3. 为代码片段添加快捷键
   1. 打开命令面板，键入Preferences：Open Keyboard Shortcuts（JSON）

### 1.7.12. task，把重复的工作自动化
- task可以运行脚本或启动进程
- task被配置在. vscode文件夹的tasks.json文件中
- 通过在顶部菜单栏Terminal->Configure Tasks->Create tasks.json file from template可以选择task模板

### 1.7.13. task快捷键绑定
- 对于经常适用的**task**，可以进行快捷键绑定。
- 打开命令面板，键入Preferences: Open Keyboard Shortcuts (JSON)，打开keybindings.json
> task这块内容其实没有学会。我最想用它实现的功能包括：打包输出exe文件等。有待后续学习

## Multi-root Workspaces
- 全栈工程师（Fullstack developer，掌握多种技能，用以独立完成产品的人），希望在同一个VSCode窗口打开多个不同文件夹下的项目，需要Multi-root Workspaces
- 添加文件夹：File->Add Folder to Workspace
- 打开工作区文件文件：File->Open Workspace，选择相应的文件区文件
- 关闭工作区：File->Close Workspace，或者适用Ctrl+K->F
- 设置：Preferences: Open Workspace Settings. 如果设置中字体颜色为灰色，则表示该设置无效。

## 调试与运行
- 调试模式：F5
- 运行模式：Ctrl+F5
### launch.json 调试配置
- 切换到调试视图
- 点击create a launch.json file
- 选择运行环境
- VSCode会在.vscode文件夹中穿件一个launch.json文件，文件中定义了调试所需要的配置。
- launch.json属性略……
- 添加更多的调试配置：在launch.json文件的右下角，单击Add Configuration

## 插件
- 打开插件管理视图：Ctrl+Shift+X
- 插件过滤器：在插件搜索框中输入@+过滤项，进行插件过滤。
- 插件安装目录：%USERPROFILE%\.vscode\extensions

## 语言深入
- 运行python代码片段：选择代码片段后，按Shift+Enter
- 添加调试断点：F9
- 创建调试配置：create a launch.json file
- 创建Jupyter Notebook：在命令面板键入Python：Create New Blank Jupyter Notebook

## 前端开发
- 略……

## 云计算开发
- Azure Account插件为Azure开发提供了最核心的支持
- 安装Azure App Service
- Web开发、数据库开发等，略……

## 物联网开发
- PlatformIO设备端开发工具
- 略……

## 远程开发
- VSCode提供了Remote Development插件。这个远程开发插件包，包含一下三种类型的远程开发插件：
- Remote - SSH插件： 通过SSH打开远程机器或虚拟机上的文件夹，以连接到任何位置的源代码。
- Remote - Containers插件：基于容器技术，把Docker作为开发环境。
- Remote - WSL插件：在windows上打开WSL的文件夹，可以获得犹如Linux般的开发体验。
- 具体配置，略……

## Visual Studio family
- 有了web版VSCode，可以直接在浏览器中连接自托管开发环境，这是完全免费的。
### VS Codespaces采取前后端分离架构设计。前端可以是本地的VSCode或VS，也可以是远程的Web版VSCode。后端可以是本地的机器，也可以是远程的物理机、虚拟机、Docker容器或WSL。
- 本地的前端+本地的后端：多数IDE/编辑器的使用场景。
- 本地的前端+远程的后端：VSCode远程开发的使用场景，把远程的SSH主机、容器或WSL作为开发环境。
- 远程的前端+本地的后端：VS Codespaces自托管模式，把自己本地及其作为自托管的开发环境。
- 远程的前端+远程的后端：VS Codespaces的全托管模式。
- VS Codespaces的登录、设置等，略……

## 成为VSCode的贡献者
- 略……