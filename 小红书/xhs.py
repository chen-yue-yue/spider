import requests

cookies = {
    'abRequestId': '76fdf6ce-1d25-57c6-ba6b-be434462fb8e',
    'xsecappid': 'xhs-pc-web',
    'a1': '19b590c4ba3zxx6opgphqj5m1ouoeiy17ro04a38n50000307578',
    'webId': '3531ad7fde17ed74023408f1a9b84c35',
    'gid': 'yjD2j8SKy2WfyjD2j8S4DF0q0quCCKlUkUxAlYIV26yl7828ld3vy4888q8W2WY8dqdi0jJK',
    'web_session': '040069b1a924e157854616897a3b4b11f1d0a1',
    'id_token': 'VjEAAPoaFs/UB6cjZ3yRrVu5KMzAgJH7FyS9KozOKRYJpZCLvZWmxtC21nYy9v+50/xvMjO/BUAhVpAZY/qJqoWLTucGkSLYIvYBDEReTSLjwCZuQluJxAsiUPTh6/N0kw6ZBkTI',
    'webBuild': '5.3.0',
    'acw_tc': '0a0bb1f417669034646482721e48fdb8999e11e8d0908c113f50193fb832c8',
    'websectiga': '3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad',
    'sec_poison_id': '0aa609c9-11b2-464d-91ae-6be0f88225b3',
    'loadts': '1766903480919',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-b3-traceid': 'bd10a2fc9f52e837',
    'x-s': 'XYS_2UQhPsHCH0c1PjhEHjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQTJdPIPAZlg946GLTlqDR0aoz8/0YgN9br4emk8BR8y9ph2f8awepnJaRx2bSkyFDUy0rM+7iF8bmz4nMo8epB+/SNLgSI+b8FLBbkG9HELorI40zc4/HE8om1qS+Cwr81yoYN49pPPr8Qc7kmnbPhanz9zLlm8F8DaFRmPrkHaMY/+MSnwe8T+pz+c9EIqMQCLDkcpnbLP9lQLDT/Jfznnfl0yLLIaSQQyAmOarEaLSzyPBc9ppLFLdmDyaHVHdWFH0ijJ9Qx8n+FHdF=',
    'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1PjhEHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHMN0P1PsHVHdWMH0ijP/Sj+/DIGAzjG/+C2oW9J7mdqBYly0pTPnRMJ9pk2/r7qfuI+BrAwBhMPeZIPePI+AL7wsHVHdW9H0ijHjIj2eqjwjHjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL08z/sVManD9q9z1J9p/8db8aob7JeQl4epsPrz6agW3Lr4ryaRApdz3agYDq7YM47HFqgzkanYMGLSbP9LA/bGIa/+nprSe+9LI4gzVPDbrJg+P4fprLFTALMm7+LSb4d+kpdzt/7b7wrQM498cqBzSpr8g/FSh+bzQygL9nSm7qSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMD6pMzd8/4SL7bF8aRr+7+rG7mkqBpD8pSUzozQcA8Szb87PDSb/d+/qgzVJfl/4LExpdzQ4fRSy7bFP9+y+7+nJAzdaLp/2LSiz/zzcdbMagYiJdbCwB4QyFSfJ7b7yFSenS4o+A+A8BlO8p8c4A+Q4DbSPB8d8ncIyFkQy/pAPFSUz0QM4rbQyLTAynz98nTy/fpLLocFJDbO8p4c4FpQ4S+1G/mD8nzc4ApdwLkAzb87LrDAy7QQ2rLM/op749bl4UTU8nTinDbw8/b+/fLILoqEaL+wqM8PJ9p/GDSBanT6qM+U+7+nJD8kanTdqM8n4rMQygpDqgb7t7zl4b4QPAmSPMm7aLSiJ9LA4gclanSOq9kM4e+74gz1qMm7nrSeG9lQPFSUP04VyAQQ+nLl4gzeaLp/NFSbadPILoz1qbSQcLuIafp88DclaLpULrRc4rT6qgqAa/+O8gYl4b4z/epSyn+mqA+Iyo4QyBRAPASOqA+M4o+0Lo4YaL+tqM4c4ApQyn4Sy9pl/rSea9px8sRA8SmF+LSh+7+h4g4r+BMrJDSkG0zQ2rESPUuIqMzY4d+DanpSyMm7cDSiL7YQcFGMNMm7cFSkzsRQPURSPrb3J0W7J9pDpd4UanSc/7kn4FSTnfpS8rMm8p4c474dqgcUanS+wLSiyozTpdzcLob7aDSk/fpDJrEAy7pFJSkl49+Qy/YN8p8FLrSeap8HcDMsanSSqA8r8BLIcDRSydpF+ozc4oQQPFYCa/P7qA8c4bpQcA4S8rz3prSeGfSsJb+daLPhzDSiafL94g4G2dbFcdzc4eYQPFlVaLLIqAP6cnp34g4naf8y/LSi/BzP4gzbLbmF/LSkLoQQynQVagY8/FS9/fp8JFbAyD8/8LkM474QP9lL2db7afpM4AQQy/8SprbgyFSbynY6JdrRHjIj2eDjw0rMP/c7+AHEwaIj2erIH0iINsQhP/rjwjQ1J7QTGnIjKc==',
    'x-t': '1766903486781',
    'x-xray-traceid': 'cdb1d3cc9a7846ed5b1bd9bc532ab82a',
    # 'cookie': 'abRequestId=76fdf6ce-1d25-57c6-ba6b-be434462fb8e; xsecappid=xhs-pc-web; a1=19b590c4ba3zxx6opgphqj5m1ouoeiy17ro04a38n50000307578; webId=3531ad7fde17ed74023408f1a9b84c35; gid=yjD2j8SKy2WfyjD2j8S4DF0q0quCCKlUkUxAlYIV26yl7828ld3vy4888q8W2WY8dqdi0jJK; web_session=040069b1a924e157854616897a3b4b11f1d0a1; id_token=VjEAAPoaFs/UB6cjZ3yRrVu5KMzAgJH7FyS9KozOKRYJpZCLvZWmxtC21nYy9v+50/xvMjO/BUAhVpAZY/qJqoWLTucGkSLYIvYBDEReTSLjwCZuQluJxAsiUPTh6/N0kw6ZBkTI; webBuild=5.3.0; acw_tc=0a0bb1f417669034646482721e48fdb8999e11e8d0908c113f50193fb832c8; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=0aa609c9-11b2-464d-91ae-6be0f88225b3; loadts=1766903480919',
}

json_data = {
    'keyword': '电影',
    'page': 1,
    'page_size': 20,
    'search_id': '2fs049lbqtbz2i2p764p3@2fs04a2eqkr3ozy4rp89b',
    'sort': 'general',
    'note_type': 0,
    'ext_flags': [],
    'filters': [
        {
            'tags': [
                'general',
            ],
            'type': 'sort_type',
        },
        {
            'tags': [
                '不限',
            ],
            'type': 'filter_note_type',
        },
        {
            'tags': [
                '不限',
            ],
            'type': 'filter_note_time',
        },
        {
            'tags': [
                '不限',
            ],
            'type': 'filter_note_range',
        },
        {
            'tags': [
                '不限',
            ],
            'type': 'filter_pos_distance',
        },
    ],
    'geo': '',
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
}

response = requests.post(
    'https://edith.xiaohongshu.com/api/sns/web/v1/search/notes',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"keyword":"电影","page":1,"page_size":20,"search_id":"2fs049lbqtbz2i2p764p3@2fs04a2eqkr3ozy4rp89b","sort":"general","note_type":0,"ext_flags":[],"filters":[{"tags":["general"],"type":"sort_type"},{"tags":["不限"],"type":"filter_note_type"},{"tags":["不限"],"type":"filter_note_time"},{"tags":["不限"],"type":"filter_note_range"},{"tags":["不限"],"type":"filter_pos_distance"}],"geo":"","image_formats":["jpg","webp","avif"]}'.encode()
#response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/search/notes', cookies=cookies, headers=headers, data=data)