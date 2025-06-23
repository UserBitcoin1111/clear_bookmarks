from bs4 import BeautifulSoup
import argparse

def remove_duplicate_bookmarks(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    urls_seen = set()
    titles_seen = set()
    duplicates = 0

    for tag in soup.find_all('a'):
        url = tag.get('href')
        title = tag.get_text().strip()

        key = (url, title)
        if key in urls_seen:
            tag.decompose()  # 删除标签
            duplicates += 1
        else:
            urls_seen.add(key)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f'✅ 完成！已删除重复书签 {duplicates} 个。输出文件: {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='清理 Firefox 导出书签文件中的重复项')
    parser.add_argument('--infile', type=str, required=True, help='原始书签HTML文件路径')
    parser.add_argument('--outfile', type=str, required=True, help='清理后的输出HTML文件路径')

    args = parser.parse_args()
    remove_duplicate_bookmarks(args.infile, args.outfile)
