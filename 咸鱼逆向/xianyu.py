import requests
import execjs

cookies = {
    'cna': 'DyPQIaJikTMCASSNGA9Sdpdx',
    't': '6c69a4918c309892276941874a092888',
    'xlly_s': '1',
    'cookie2': '1b3d86401570e5aa28022cab3ebf4863',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '545b30d795ed9a31583c4723aedbbf0d_1766905157114',
    '_m_h5_tk_enc': '73faed33ac01df21dcbf8021ef2e5223',
    'tfstk': 'g3eSn9TOwUY55RsRJUS2laVAYDHC0iWwAHiLjkpyvYHJJeEtuzurUMXIJz04U4rre2pQ8kyz8JZHdDEL-g0FqsruqvDd7NJCQuqukf95j8gJMIEmbpnRgbLNOY5A7NWN3_Kxda_a4v0vPqnnk0nK20IjHcoIp03K9igxAcApyyHdciiiA2LJppBxMDiip2UKpiixjqn-pbULDiink2HUyFoCY4Z5bwfXOYS_5u3XppeRKbg6Nqom0-1-aVZ8YELAx0GSWu3fPeE-bjEnOJxHd4E8symTyUQZZkFbl0MC3QHTcWUsm8BwPmVzDluYfhpT4YN_CYF5oIDzP-HYe5tppoMSrjerGU_jW8qYIxhVBGZYnzruhk-dpmzZku2-dOIiFY3-hm2FoL3QMWerZvYR7bqLGriSBgWeQV6m1Btjspij7isXtBcXry0nBd0FhbnmVxsfcUMxwmmj7isXtBc-mmRfciTSH',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.goofish.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.goofish.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': 'cna=DyPQIaJikTMCASSNGA9Sdpdx; t=6c69a4918c309892276941874a092888; xlly_s=1; cookie2=1b3d86401570e5aa28022cab3ebf4863; mtop_partitioned_detect=1; _m_h5_tk=545b30d795ed9a31583c4723aedbbf0d_1766905157114; _m_h5_tk_enc=73faed33ac01df21dcbf8021ef2e5223; tfstk=g3eSn9TOwUY55RsRJUS2laVAYDHC0iWwAHiLjkpyvYHJJeEtuzurUMXIJz04U4rre2pQ8kyz8JZHdDEL-g0FqsruqvDd7NJCQuqukf95j8gJMIEmbpnRgbLNOY5A7NWN3_Kxda_a4v0vPqnnk0nK20IjHcoIp03K9igxAcApyyHdciiiA2LJppBxMDiip2UKpiixjqn-pbULDiink2HUyFoCY4Z5bwfXOYS_5u3XppeRKbg6Nqom0-1-aVZ8YELAx0GSWu3fPeE-bjEnOJxHd4E8symTyUQZZkFbl0MC3QHTcWUsm8BwPmVzDluYfhpT4YN_CYF5oIDzP-HYe5tppoMSrjerGU_jW8qYIxhVBGZYnzruhk-dpmzZku2-dOIiFY3-hm2FoL3QMWerZvYR7bqLGriSBgWeQV6m1Btjspij7isXtBcXry0nBd0FhbnmVxsfcUMxwmmj7isXtBc-mmRfciTSH',
}

params = {
    'jsv': '2.7.2',
    'appKey': '34839810',
    't': '1766896614617',
    'sign': 'f2260b1e666677d4e3c58cb3bd495b61',
    'v': '1.0',
    'type': 'originaljson',
    'accountSite': 'xianyu',
    'dataType': 'json',
    'timeout': '20000',
    'api': 'mtop.taobao.idlemtopsearch.pc.search',
    'sessionOption': 'AutoLoginOnly',
    'spm_cnt': 'a21ybx.search.0.0',
    'spm_pre': 'a21ybx.home.searchInput.0',
}

data = {
    'data': '{"pageNumber":1,"keyword":"热水袋","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"{}","userPositionJson":"{}"}',
}

response = requests.post(
    'https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
f=open('xianyu.js',encoding='utf-8')
js_code=f.read()
js= execjs.compile(js_code)
q=js.call('yu',data['data'])
params['t']=q[0]
params['sign']=q[1]

print(response.json())