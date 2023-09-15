from deep_translator import GoogleTranslator
import mistune

# 解析Markdown文件并提取文本内容
def extract_text_from_markdown(input_file):
    with open(input_file, 'r', encoding='utf-8') as source_file:
        source_text = source_file.read()
        # 使用mistune解析Markdown，提取文本内容
        markdown_parser = mistune.create_markdown()
        text_content = markdown_parser(source_text)
    return text_content

# 翻译文本并保留Markdown格式
def translate_markdown(input_file, output_file, target_language):
    text_content = extract_text_from_markdown(input_file)
    # 将提取的文本内容翻译为目标语言
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text_content)
    # 将翻译后的文本写入输出文件
    with open(output_file, 'w', encoding='utf-8') as target_file:
        target_file.write(translated_text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: translate_md.py input_file output_file target_language")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        target_language = sys.argv[3]
        translate_markdown(input_file, output_file, target_language)
