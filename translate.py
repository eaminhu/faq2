from deep_translator import GoogleTranslator

def translate_file(input_file, output_file):
   with open(input_file, 'r', encoding='utf-8') as source_file:
       source_text = source_file.read()
       translated_text = GoogleTranslator(source='zh-CN', target='en').translate(source_text)
   with open(output_file, 'w', encoding='utf-8') as target_file:
       target_file.write(translated_text)

if __name__ == "__main__":
   import sys
   if len(sys.argv) != 3:
       print("Usage: translate.py input_file output_file")
   else:
       input_file = sys.argv[1]
       output_file = sys.argv[2]
       translate_file(input_file, output_file)
