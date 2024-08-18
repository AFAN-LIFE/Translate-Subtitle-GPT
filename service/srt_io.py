import re

def read_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Store indices, timestamps, and subtitle texts separately
    indices = []
    timestamps = []
    texts = []

    # Match subtitle blocks
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\n([\s\S]+?)(?=\n\d|\Z)',
                         re.MULTILINE)
    matches = pattern.findall(content)

    for match in matches:
        index, timestamp, text = match
        indices.append(int(index))
        timestamps.append(timestamp)
        texts.append(text.strip())

    return {
        'indices': indices,
        'timestamps': timestamps,
        'texts': texts
    }

def write_srt(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, timestamp, text in zip(data['indices'], data['timestamps'], data['texts']):
            file.write(f"{index}\n")
            file.write(f"{timestamp}\n")
            file.write(f"{text}\n\n")

if __name__ == '__main__':
    # 调用函数并解析字幕文件
    parsed_data = read_srt('../test/test_eg.srt')

    # 打印结果
    print("Indices:", parsed_data['indices'])
    print("Timestamps:", parsed_data['timestamps'])
    print("Texts:", parsed_data['texts'])