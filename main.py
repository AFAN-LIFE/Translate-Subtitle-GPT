import os.path
import time

from tqdm import tqdm
from service.srt_io import read_srt, write_srt
from service.batch import batch_translate_subtitles
from config import DEFAULT_SLEEP, DEFAULT_BATCH_NUM


def translate_subtitles(input_file, src_lg, dst_lg, batch_size=DEFAULT_BATCH_NUM):
    parsed_data = read_srt(input_file)
    input_name = os.path.basename(input_file)
    input_path = os.path.dirname(input_file)
    indices = parsed_data['indices']
    subtitles = parsed_data['texts']
    timestamps = parsed_data['timestamps']
    translated_subtitles = []
    for i in tqdm(range(0, len(subtitles), batch_size)):
        # Take a batch of subtitles
        batch = subtitles[i:i + batch_size]
        # Translate the batch using the batch_translate_subtitles function
        translated_batch = batch_translate_subtitles(batch, src_lg, dst_lg)
        # Ensure the length of the translated batch matches the original batch
        if len(batch) > len(translated_batch):
            # Add empty strings to the translated list if it's shorter
            translated_batch.extend([''] * (len(batch) - len(translated_batch)))
        else:  # Truncate the translated list if it's longer
            translated_batch = translated_batch[:len(batch)]
        # Append the translated batch to the final list
        translated_subtitles.extend(translated_batch)
        time.sleep(DEFAULT_SLEEP)
    output_data = {
        'indices': indices,
        'timestamps': timestamps,
        'texts': translated_subtitles
    }
    output_name = input_name.split('.')[0] + f'_{src_lg}_to_{dst_lg}.srt'
    output_path = os.path.join(input_path, output_name)
    write_srt(output_data, output_path)
    return translated_subtitles

if __name__ == '__main__':
    print('start translate english to chinese')
    translate_subtitles('test/test_eg.srt', '英文', '中文')
    print('successful finished')

    print('start translate chinese to english')
    translate_subtitles('test/test_cn.srt', '中文', '英文')
    print('successful finished')