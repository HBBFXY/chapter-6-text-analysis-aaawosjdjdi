# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 创建字典统计字符频率
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # 按频率降序排序，频率相同则按字符本身排序
    sorted_chars = sorted(char_freq.keys(), key=lambda x: (-char_freq[x], x))
    
    return sorted_chars

# 主程序，已完整
if __name__ == "__main__":
    # 简化输出，避免额外文本干扰测试
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    text = "\n".join(lines)
    
    if text.strip():
        sorted_chars = analyze_text(text)
        # 最简单的输出格式，只输出结果
        print(", ".join(sorted_chars))
