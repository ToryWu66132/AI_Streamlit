AI Blog Generator
一个基于 Streamlit 的简易 AI 博客生成器。用户输入博客主题并选择写作风格后，应用会调用大模型自动生成标题、章节大纲、分节正文和总结，并支持将结果下载为 Markdown 文件。

功能特点
基于 Streamlit 提供轻量 Web 界面
输入博客主题后自动生成完整文章
支持 专业、轻松、营销 三种写作风格
自动生成标题、大纲、正文和总结
使用线程池并发生成章节内容，提升生成速度
提供失败重试机制，提高接口调用稳定性
支持一键下载生成结果为 blog.md
项目结构
AI_streamit/
├── app.py
├── requirements.txt
├── .env
├── generator/
│   ├── api.py
│   ├── blog.py
│   └── prompt.py
└── utils/
    ├── logger.py
    └── retry.py
工作流程
用户在页面中输入博客主题并选择写作风格。
程序先生成博客标题。
再根据主题和标题生成 5 个章节标题。
使用线程池并发生成各章节正文内容。
根据标题和章节信息生成总结段落。
最终将全部内容拼接成 Markdown 格式并展示在页面中。
运行环境
Python 3.10 及以上
依赖包：
streamlit
requests
python-dotenv
安装与运行
1. 解压项目
将 AI_streamit.zip 解压到本地目录。

2. 安装依赖
pip install -r requirements.txt
如果你的 requirements.txt 当前内容较简略，建议改成下面这样：

streamlit
requests
python-dotenv
3. 配置环境变量
在项目根目录创建 .env 文件：

API_KEY=your_deepseek_api_key
说明：

API_KEY 用于调用 DeepSeek 接口
不建议把真实密钥提交到 Git 仓库
4. 启动应用
streamlit run app.py
启动后，浏览器会自动打开本地页面，通常地址为：

http://localhost:8501
使用说明
在输入框中填写博客主题。
在下拉框中选择文章风格。
点击“生成博客”按钮。
等待系统完成生成。
在页面中查看结果，并可点击按钮下载 Markdown 文件。
核心模块说明
app.py
项目入口，负责：

渲染 Streamlit 页面
接收用户输入
调用博客生成逻辑
展示结果并提供下载功能
generator/api.py
负责封装大模型接口调用逻辑，当前使用 DeepSeek Chat Completion API。

generator/prompt.py
负责构造提示词，包括：

标题生成提示词
大纲生成提示词
章节内容生成提示词
总结生成提示词
generator/blog.py
负责博客主流程编排：

调用标题生成
调用大纲生成
清洗重复章节
并发生成章节正文
汇总并拼接最终 Markdown
utils/retry.py
提供简单的失败重试机制，降低接口偶发失败带来的影响。

示例使用场景
运营人员快速生成内容初稿
自媒体写作者整理博客框架
学习 Prompt 工程与 LLM 应用开发
作为 Streamlit + 大模型项目的入门练习
可改进方向
增加 API 异常提示和日志记录
支持自定义章节数量和文章长度
支持更多文章风格和语言
增加历史记录保存功能
支持导出为 Word 或 PDF
将接口模型、温度和最大 token 配置为可调参数
补充单元测试和更完整的依赖声明
注意事项
当前项目依赖外部大模型接口，运行前必须配置有效的 API Key
.env 中的密钥不要上传到公开仓库
logger.py 当前为空文件，如需调试可扩展日志能力
requirements.txt 当前内容可能不完整，建议手动补充标准依赖名
License
如需开源发布，建议补充具体许可证，例如 MIT License。