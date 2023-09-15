from deep_translator import GoogleTranslator
import mistune  # 导入Markdown解析库

def extract_text_from_markdown(input_file):
    with open(input_file, 'r', encoding='utf-8') as source_file:
        source_text = source_file.read()
        # 使用mistune解析Markdown，提取文本内容
        markdown_parser = mistune.create_markdown()
        text_content = markdown_parser(source_text)
    return text_content

def translate_file(input_file, output_file):
    text_content = extract_text_from_markdown(input_file)
    # 将提取的文本内容翻译为俄文
    translated_text = GoogleTranslator(source='zh-CN', target='en').translate(text_content)
    with open(output_file, 'w', encoding='utf-8') as target_file:
        target_file.write(translated_text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: translate.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        target_lang = sys.argv[3]
        translate_file(input_file, output_file)
