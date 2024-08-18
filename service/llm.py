import qianfan
from config import DEFAULT_TOKEN


def get_qianfan_response(content, prompt):
    model_name = 'ernie-speed-128k'
    config = qianfan.get_config()
    config.ACCESS_TOKEN = DEFAULT_TOKEN
    # reference: https://qianfan.readthedocs.io/
    response = qianfan.Completion().do(
        model=model_name,
        prompt=content,
        system=prompt,
        stream=False
    )
    result = response['body']['result']
    return result


if __name__ == '__main__':
    content = 'I am very thankful to all of you for having me today'
    src_lg, dst_lg = '英语', '法语'
    prompt = f'你是一个精通各国语言的翻译专家，请把这段{src_lg}翻译成{dst_lg}'
    result = get_qianfan_response(content, prompt)
    print(result)
