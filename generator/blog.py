from concurrent.futures import ThreadPoolExecutor
from generator.api import call_llm
from generator.prompt import (
    title_prompt,
    outline_prompt,
    section_prompt,
    summary_prompt
)
from utils.retry import retry


def generate_blog(topic, tone):
    # 标题
    title = retry(lambda: call_llm(title_prompt(topic)))

    # 大纲
    outline_text = retry(lambda: call_llm(outline_prompt(topic, title)))

    seen = set()
    outline = []

    for line in outline_text.splitlines():
        line = line.strip()
        if line and line not in seen:
            outline.append(line)
            seen.add(line)

    def clean_content(section_title, content):
        lines = content.strip().splitlines()

        # 如果第一行就是标题，删掉
        if lines and section_title in lines[0]:
            lines = lines[1:]

        return "\n".join(lines).strip()

    # 并发生成章节
    def gen_section(sec):
        raw = retry(lambda: call_llm(
            section_prompt(topic, title, sec, tone)
        ))

        cleaned = clean_content(sec, raw)

        return {
            "section_title": sec,
            "content": cleaned
        }

    with ThreadPoolExecutor(max_workers=3) as executor:
        sections = list(executor.map(gen_section, outline))

    # 拼接临时内容
    summary_input = f"标题：{title}\n\n"

    for s in sections:
        summary_input += f"{s['section_title']}\n"

    summary = retry(lambda: call_llm(summary_prompt(summary_input)))

    if title in summary:
        summary = summary.split("总结")[-1].strip()

    # Markdown
    blog = f"# {title}\n\n"
    for s in sections:
        blog += f"## {s['section_title']}\n{s['content']}\n\n"
    blog += f"## 总结\n{summary}"

    return blog