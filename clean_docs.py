import os
import re

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 移除YAML前置内容（在两个 --- 之间的内容）
    content = re.sub(r'^---\s*[\s\S]*?---\s*', '', content)
    
    # 移除页码HTML标签
    content = re.sub(r'<a class="en-page-number" id="\d+"></a>\s*', '', content)
    
    # 移除章节号HTML标签
    content = re.sub(r'<div class="chapter-number"><p class="chapter-number">{{ page.ch }}</p></div>\s*', '', content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    return True

def process_docs_directory(docs_path):
    processed_files = 0
    
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if clean_file(file_path):
                    processed_files += 1
                    print(f"已处理: {file_path}")
    
    return processed_files

if __name__ == "__main__":
    docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
    
    if not os.path.exists(docs_dir):
        print(f"错误: 目录 {docs_dir} 不存在!")
        exit(1)
    
    count = process_docs_directory(docs_dir)
    print(f"\n清理完成! 总共处理了 {count} 个文件。")
