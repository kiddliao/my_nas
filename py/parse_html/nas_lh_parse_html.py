from lxml.html import etree
import traceback

text = open(r'py\parse_html\source_file\html.txt', 'r', encoding='utf-8').read()
total_html = etree.HTML(text)

metadatas = total_html.xpath("//div[@class='infinite-list-wrapper']/div[position()=1]/div[position()>1]")
res = []

for ii, metadata in enumerate(metadatas):
    try:
        byte = etree.tostring((metadata), encoding='utf-8')
        string = byte.decode('utf-8')
        meta_html = etree.HTML(string)

        tmp_status = meta_html.xpath("//div[position()=1]/div[position()=2]/span/text()")
        if len(tmp_status) == 2:
            status = tmp_status[1]
        else:
            status = tmp_status[0]

        # if '退款成功' in status:
        #     continue
        real_name = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=1]/div[position()=1]/span/text()")[1]
        phone = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=1]/div[position()=1]/span/text()")[2]
        tmp_user_name = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=2]/div[position()=2]/text()")
        if len(tmp_user_name) == 0:
            user_name = ''
        else:
            user_name = tmp_user_name[0]
        if not user_name:
            tmp_address = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=2]/div[position()=1]/text()")
            if len(tmp_address) == 0:
                address = ''
            else:
                address = tmp_address[0].replace('\n', ' ')
        else:
            tmp_address = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=3]/div[position()=1]/text()")
            if len(tmp_address) == 0:
                address = ''
            else:
                address = tmp_address[0].replace('\n', ' ')

        tmp_goods_name = meta_html.xpath("//div[position()=2]/div/div[position()=1]/div[position()=2]/div[position()=1]/div[position()=1]/div[position()=1]/text()")
        tmp_goods_name = list(filter(lambda x : '多多买菜门店配送费' not in x, tmp_goods_name))

        tmp_goods_count = meta_html.xpath("//div[position()=2]/div/div[position()=1]/div[position()=2]/div[position()=1]/div[position()=2]/text()")
        tmp_goods_count_new = []
        for v in tmp_goods_count:
            if v == '×':
                continue
            tmp_goods_count_new.append(v.replace('×', ''))

        assert len(tmp_goods_name) == len(tmp_goods_count_new)
        tmp_goods_info = []
        for jj, goods_name in enumerate(tmp_goods_name):
            cate_name = ''
            cate_no = ''
            if '土鸡蛋' in goods_name:
                cate_name = '土鸡蛋'
            elif '农家土猪带肋' in goods_name:
                cate_name = '猪肉'
            elif '三鲜菜包' in goods_name:
                cate_name = '三鲜菜包'
            elif '时蔬七菜组合' in goods_name:
                cate_name = '时蔬七菜组合'
            elif '居家调味大礼包' in goods_name:
                cate_name = '居家调味大礼包'
            else:
                cate_name = '-1' * 100
            cate_no = tmp_goods_count_new[jj]
            cate_info = cate_name + 'x' + cate_no
            tmp_goods_info.append(cate_info)
        goods_info = ','.join(tmp_goods_info)

        tmp_order_time = meta_html.xpath("//div[position()=1]/div[position()=3]//div[position()=2]/text()")
        if len(tmp_order_time) > 1:
            order_time = tmp_order_time[1]
        else:
            order_time = tmp_order_time[0].split('下单时间:')[1]
    except Exception as e:
        err = traceback.format_exc()
        print()
    meta_info = [real_name, phone, user_name, address, status, goods_info, order_time]
    print(ii + 1, meta_info)
    res.append('\t'.join(meta_info))

with open(r'py\parse_html\test\order_info.txt', 'w', encoding='utf-8') as f:
    for v in res:
        f.write(f'{v}\n')