def title_prompt(topic):
    return f"""
你是一位专业的博客写作助手。
请围绕主题“{topic}”生成一个吸引人的博客标题。

要求：
1. 标题清晰具体
2. 不要解释
3. 只输出一个标题
"""


def outline_prompt(topic, title):
    return f"""
你是一位专业的博客写作助手。

主题：{topic}
标题：{title}

要求：
1. 生成5个不同的章节标题
2. 每个标题必须内容不同，不能重复
3. 每行一个标题
4. 不要序号，不要解释
5. 如果有重复，请重新生成
"""


def section_prompt(topic, title, section_title, tone):
    return f"""
你是一位专业博客作者。

博客主题：{topic}
博客标题：{title}
章节标题：{section_title}

【严格要求】：
1. 只写正文内容
2. ❗ 不要重复章节标题
3. ❗ 不要在开头写标题
4. ❗ 第一行必须是正文句子，而不是标题
5. 字数150-250字
6. 风格：{tone}
"""


def summary_prompt(content):
    return f"""
你是一位专业博客编辑。

请根据下面提供的信息写总结。

【严格要求】：
1. 必须基于提供的内容
2. 不允许编造新的主题
3. 如果内容与“医疗、AI”无关，禁止提及这些词
4. 只写2-4句话总结
5. 不要复述全文
6. 不要输出“总结：”

内容如下：
{content}
"""