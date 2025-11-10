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

# 主程序
if __name__ == "__main__":
    # 测试用例 - 直接使用硬编码的测试数据
    test_texts = [
        "hello world",
        "programming is fun",
        "aabbcc",
        "测试文本"
    ]
    
    for i, text in enumerate(test_texts):
        print(f"测试 {i+1}: {text}")
        result = analyze_text(text)
        print("结果:", ", ".join(result))
        print()
