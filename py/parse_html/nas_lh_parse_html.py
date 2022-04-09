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

        tmp_address = meta_html.xpath("//div[position()=1]/div[position()=1]/div[position()=3]/div[position()=1]/text()")
        if len(tmp_address) == 0:
            address = ''
        else:
            address = tmp_address[0].replace('\n', ' ')

        tmp_goods_name = meta_html.xpath("//div[position()=2]/div/div[position()=1]/div[position()=2]/div[position()=1]/div[position()=1]/div[position()=1]/text()")
        goods_name = ','.join(tmp_goods_name)

        tmp_order_time = meta_html.xpath("//div[position()=1]/div[position()=3]//div[position()=2]/text()")
        if len(tmp_order_time) > 1:
            order_time = tmp_order_time[1]
        else:
            order_time = tmp_order_time[0].split('下单时间:')[1]
    except Exception as e:
        err = traceback.format_exc()
        print()
    meta_info = [real_name, phone, user_name, address, status, goods_name, order_time]
    print(ii + 1, meta_info)
    res.append('\t'.join(meta_info))

with open(r'py\parse_html\test\order_info.txt', 'w', encoding='utf-8') as f:
    for v in res:
        f.write(f'{v}\n')