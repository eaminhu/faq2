import re
from deep_translator import GoogleTranslator

def translate_markdown_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as source_file:
        source_text = source_file.read()

    # 使用正则表达式提取Markdown中的文本内容
    text_content = re.sub(r'<.*?>', '', source_text)  # 移除所有标签

    # 使用Google翻译器翻译文本
    translated_text = GoogleTranslator(source='zh-CN', target='ru').translate(text_content)

    # 替换原始Markdown文件中的文本内容
    translated_source = re.sub(re.escape(text_content), translated_text, source_text)

    with open(output_file, 'w', encoding='utf-8') as target_file:
        target_file.write(translated_source)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: translate.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        translate_markdown_file(input_file, output_file)
