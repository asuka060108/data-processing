# -*- coding: utf-8 -*-
"""实验01 配套工具模块：解析学生成绩记录。"""


def parse_student(line):
    """将一行 'name,score' 文本解析为字典。

    字段数量必须为 2，姓名不能为空，成绩必须是 0~100 的整数，
    否则抛出 ValueError。
    """
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量不是2: {line.strip()!r}")
    name, score_str = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是合法整数: {score_str!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return {"name": name, "score": score}
