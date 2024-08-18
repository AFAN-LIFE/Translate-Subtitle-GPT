from service.llm import get_qianfan_response

def batch_translate_subtitles(subtitles, src_lg, dst_lg):
    # Prepare the prompt for the translation model
    prompt = (f'你是一位精通多种语言的翻译专家。 '
              f'请将以下文本从 {src_lg} 翻译成 {dst_lg}。 '
              f'这个文本包含多行内容，每行由换行符“\\n”区分'
              f'每一行应单独翻译，并保持原有的换行符。 '          
              f'翻译后，请检查翻译文本中的换行符数量是否与原文本一致。 '
              f'如果存在不一致，请在对应的位置添加换行符。')
    # Combine all subtitles into a single content string with a special delimiter
    combined_content = '\n'.join(subtitles)

    # Get the translation result from the model
    translation_result = get_qianfan_response(combined_content, prompt)

    # Split the translation result back into individual lines
    translated_subtitles = translation_result.split('\n')

    # Strip any leading/trailing whitespace from each translated subtitle
    translated_subtitles = [subtitle.strip() for subtitle in translated_subtitles]

    return translated_subtitles


if __name__ == '__main__':
    from srt_io import read_srt
    # english to chinese
    parsed_data = read_srt('../test/test_eg.srt')
    result = batch_translate_subtitles(parsed_data['texts'][:20], '英文', '中文')
    print(len(parsed_data['texts']), len(result))
    print(result)
    # chinese to english
    parsed_data = read_srt('../test/test_cn.srt')
    result = batch_translate_subtitles(parsed_data['texts'][:20], '中文', '英文')
    print(len(parsed_data['texts']), len(result))
    print(result)