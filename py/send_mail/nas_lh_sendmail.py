import smtplib
import datetime
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import glob
import random
import json
import platform
import requests
from lxml.html import etree

memorial_differences = [100]
memorial_date = datetime.date(2022, 2, 25)
now_date = datetime.date.today()
# now_date = datetime.date(2022, 6, 5)


def get_weather(city_url):
    response = requests.get(city_url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    district_name = html.xpath(
        "//div[@class='search_default']/em/text()")[0].split('，')[0]
    weather = html.xpath(
        "//div//div//div//ul[@class='days clearfix']//li/text()")[3].strip()
    temperature = html.xpath(
        "//div//div//div//ul[@class='days clearfix']//li/text()")[4].strip().split(' / ')
    wind = html.xpath("//div//div//div//ul[@class='days clearfix']//li//em/text()")[0].strip(
    ) + html.xpath("//div//div//div//ul[@class='days clearfix']//li//b/text()")[0].strip()
    air_quality = html.xpath(
        "//div//div//div//ul[@class='days clearfix']//li//strong/text()")[0].strip()
    tip = html.xpath("//div//div//div[@class='wea_tips clearfix']//em/text()")[
        0].strip().replace('，', ',').replace('。', '.')
    return district_name, weather, temperature, wind, air_quality, tip


def cal_memorial():
    flag = 0
    difference = 0
    memorial_difference = 0

    if now_date.month == memorial_date.month and now_date.day == memorial_date.day:
        flag = 1
        difference = now_date.year - memorial_date.year
        memorial_difference = 365
        return flag, difference, memorial_difference

    difference = (now_date - memorial_date).days
    for i, memorial_difference in enumerate(memorial_differences):
        if difference % memorial_difference == 0:
            flag = 1
            return flag, difference, memorial_difference
    return 0, difference, 0


def mail(mail_sub='纪念日', mail_content_text='3000天', image_final_path=None, res=None):
    def sendmail(sub, content, img=None, res=None):
        me = mail_from + "<" + mail_user + ">"
        mail = MIMEMultipart()
        msg = MIMEText(content, "html", "utf-8")
        # msg["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        if img:
            mail.attach(img)
        mail['Subject'] = sub
        mail['From'] = me
        # to_list = input("发送给: ").split(' ')
        to_list = ['love312805295@163.com', '136197651@qq.com']
        # to_list = ['love312805295@163.com', '1900447226@qq.com']
        mail['To'] = ",".join(to_list)
        mail.attach(msg)
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            server.login(mail_user, mail_password)
            server.sendmail(me, to_list, mail.as_string())
            server.close()
            return True
        except Exception as e:
            print(str(e))
            return False

    mail_user = 'love312805295@163.com'
    mail_password = 'VFTCUEFTTCZXTFHP'
    img_file = open(image_final_path, 'rb')
    img_data = img_file.read()
    img_file.close()
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'dns_config')    # 给一个content Id 供后面html内容引用
    mail_from = 'kiddliao'
    # mail_sub = '纪念日'
    # 例如: html格式的: "<a href='http://www.cnblogs.com/xiaowuyi'>小五义</a>"
    # mail_content = '狗逼'
    #mailto_list = input("")    #qq邮箱
    # mail_content = f"""
    #     <html>
    #         <body>
    #             <p>{mail_content_text}</p>
    #             <img src="cid:dns_config">
    #         </body>
    #     </html>
    #     """

    mail_content = """<!DOCTYPE html>    
<html><head>

<title>Push Email</title>
<link rel="shortcut icon" href="favicon.ico">

<style type="text/css">
table[name="blk_permission"], table[name="blk_footer"] {display:none;} 
</style>

<meta name="googlebot" content="noindex">
<meta name="ROBOTS" content="NOINDEX, NOFOLLOW"><link rel="stylesheet" href="/style/dhtmlwindow.css" type="text/css">
<script type="text/javascript" src="/script/dhtmlwindow.js">
/***********************************************
* DHTML Window Widget- © Dynamic Drive (www.dynamicdrive.com)
* This notice must stay intact for legal use.
* Visit www.dynamicdrive.com for full source code
***********************************************/
</script>
<link rel="stylesheet" href="/style/modal.css" type="text/css">
<script type="text/javascript" src="/script/modal.js"></script>
<script type="text/javascript">
	function show_popup(popup_name,popup_url,popup_title,width,height) {var widthpx = width +  "px";var heightpx = height +  "px";emailwindow = dhtmlmodal.open(popup_name , 'iframe', popup_url , popup_title , 'width=' + widthpx + ',height='+ heightpx + ',center=1,resize=0,scrolling=1');}
 function show_modal(popup_name,popup_url,popup_title,width,height){var widthpx = width +  "px";var heightpx = height +  "px";emailwindow = dhtmlmodal.open(popup_name , 'iframe', popup_url , popup_title , 'width=' + widthpx + ',height='+ heightpx + ',modal=1,center=1,resize=0,scrolling=1');}
var popUpWin=0;
	function popUpWindow(URLStr,PopUpName, width, height){if(popUpWin) { if(!popUpWin.closed) popUpWin.close();}var left = (screen.width - width) / 2;var top = (screen.height - height) / 2;popUpWin = open(URLStr, PopUpName,	'toolbar=0,location=0,directories=0,status=0,menub	ar=0,scrollbar=0,resizable=0,copyhistory=yes,width='+width+',height='+height+',left='+left+', 	top='+top+',screenX='+left+',screenY='+top+'');}
</script>
    
<meta content="width=device-width, initial-scale=1.0" name="viewport">    
<style type="text/css">    
/*** BMEMBF Start ***/    
[name=bmeMainBody]{min-height:1000px;}    
@media only screen and (max-width: 480px){table.blk, table.tblText, .bmeHolder, .bmeHolder1, table.bmeMainColumn{width:100% !important;} }        
@media only screen and (max-width: 480px){.bmeImageCard table.bmeCaptionTable td.tblCell{padding:0px 20px 20px 20px !important;} }        
@media only screen and (max-width: 480px){.bmeImageCard table.bmeCaptionTable.bmeCaptionTableMobileTop td.tblCell{padding:20px 20px 0 20px !important;} }        
@media only screen and (max-width: 480px){table.bmeCaptionTable td.tblCell{padding:10px !important;} }        
@media only screen and (max-width: 480px){table.tblGtr{ padding-bottom:20px !important;} }        
@media only screen and (max-width: 480px){td.blk_container, .blk_parent, .bmeLeftColumn, .bmeRightColumn, .bmeColumn1, .bmeColumn2, .bmeColumn3, .bmeBody{display:table !important;max-width:600px !important;width:100% !important;} }        
@media only screen and (max-width: 480px){table.container-table, .bmeheadertext, .container-table { width: 95% !important; } }        
@media only screen and (max-width: 480px){.mobile-footer, .mobile-footer a{ font-size: 13px !important; line-height: 18px !important; } .mobile-footer{ text-align: center !important; } table.share-tbl { padding-bottom: 15px; width: 100% !important; } table.share-tbl td { display: block !important; text-align: center !important; width: 100% !important; } }        
@media only screen and (max-width: 480px){td.bmeShareTD, td.bmeSocialTD{width: 100% !important; } }        
@media only screen and (max-width: 480px){td.tdBoxedTextBorder{width: auto !important;}}    
@media only screen and (max-width: 480px){table.blk, table[name=tblText], .bmeHolder, .bmeHolder1, table[name=bmeMainColumn]{width:100% !important;} }    
@media only screen and (max-width: 480px){.bmeImageCard table.bmeCaptionTable td[name=tblCell]{padding:0px 20px 20px 20px !important;} }    
@media only screen and (max-width: 480px){.bmeImageCard table.bmeCaptionTable.bmeCaptionTableMobileTop td[name=tblCell]{padding:20px 20px 0 20px !important;} }    
@media only screen and (max-width: 480px){table.bmeCaptionTable td[name=tblCell]{padding:10px !important;} }    
@media only screen and (max-width: 480px){table[name=tblGtr]{ padding-bottom:20px !important;} }    
@media only screen and (max-width: 480px){td.blk_container, .blk_parent, [name=bmeLeftColumn], [name=bmeRightColumn], [name=bmeColumn1], [name=bmeColumn2], [name=bmeColumn3], [name=bmeBody]{display:table !important;max-width:600px !important;width:100% !important;} }    
@media only screen and (max-width: 480px){table[class=container-table], .bmeheadertext, .container-table { width: 95% !important; } }    
@media only screen and (max-width: 480px){.mobile-footer, .mobile-footer a{ font-size: 13px !important; line-height: 18px !important; } .mobile-footer{ text-align: center !important; } table[class="share-tbl"] { padding-bottom: 15px; width: 100% !important; } table[class="share-tbl"] td { display: block !important; text-align: center !important; width: 100% !important; } }    
@media only screen and (max-width: 480px){td[name=bmeShareTD], td[name=bmeSocialTD]{width: 100% !important; } }    
@media only screen and (max-width: 480px){td[name=tdBoxedTextBorder]{width: auto !important;}}    
@media only screen and (max-width: 480px){.bmeImageCard table.bmeImageTable{height: auto !important; width:100% !important; padding:20px !important;clear:both; float:left !important; border-collapse: separate;} }    
@media only screen and (max-width: 480px){.bmeMblInline table.bmeImageTable{height: auto !important; width:100% !important; padding:10px !important;clear:both;} }    
@media only screen and (max-width: 480px){.bmeMblInline table.bmeCaptionTable{width:100% !important; clear:both;} }    
@media only screen and (max-width: 480px){table.bmeImageTable{height: auto !important; width:100% !important; padding:10px !important;clear:both; } }    
@media only screen and (max-width: 480px){table.bmeCaptionTable{width:100% !important;  clear:both;} }    
@media only screen and (max-width: 480px){table.bmeImageContainer{width:100% !important; clear:both; float:left !important;} }    
@media only screen and (max-width: 480px){table.bmeImageTable td{padding:0px !important; height: auto; } }    
@media only screen and (max-width: 480px){td.bmeImageContainerRow{padding:0px !important;}}    
@media only screen and (max-width: 480px){img.mobile-img-large{width:100% !important; height:auto !important;} }    
@media only screen and (max-width: 480px){img.bmeRSSImage{max-width:320px; height:auto !important;}}    
@media only screen and (min-width: 640px){img.bmeRSSImage{max-width:600px !important; height:auto !important;} }    
@media only screen and (max-width: 480px){.trMargin img{height:10px;} }    
@media only screen and (max-width: 480px){div.bmefooter, div.bmeheader{ display:block !important;} }    
@media only screen and (max-width: 480px){.tdPart{ width:100% !important; clear:both; float:left !important; } }    
@media only screen and (max-width: 480px){table.blk_parent1, table.tblPart {width: 100% !important; } }    
@media only screen and (max-width: 480px){.tblLine{min-width: 100% !important;}}     
@media only screen and (max-width: 480px){.bmeMblCenter img { margin: 0 auto; } }       
@media only screen and (max-width: 480px){.bmeMblCenter, .bmeMblCenter div, .bmeMblCenter span  { text-align: center !important; text-align: -webkit-center !important; } }    
@media only screen and (max-width: 480px){.bmeNoBr br, .bmeImageGutterRow, .bmeMblStackCenter .bmeShareItem .tdMblHide { display: none !important; } }    
@media only screen and (max-width: 480px){.bmeMblInline table.bmeImageTable, .bmeMblInline table.bmeCaptionTable, td.bmeMblInline { clear: none !important; width:50% !important; } }    
@media only screen and (max-width: 480px){.bmeMblInlineHide, .bmeShareItem .trMargin { display: none !important; } }    
@media only screen and (max-width: 480px){.bmeMblInline table.bmeImageTable img, .bmeMblShareCenter.tblContainer.mblSocialContain, .bmeMblFollowCenter.tblContainer.mblSocialContain{width: 100% !important; } }    
@media only screen and (max-width: 480px){.bmeMblStack> .bmeShareItem{width: 100% !important; clear: both !important;} }    
@media only screen and (max-width: 480px){.bmeShareItem{padding-top: 10px !important;} }    
@media only screen and (max-width: 480px){.tdPart.bmeMblStackCenter, .bmeMblStackCenter .bmeFollowItemIcon {padding:0px !important; text-align: center !important;} }    
@media only screen and (max-width: 480px){.bmeMblStackCenter> .bmeShareItem{width: 100% !important;} }    
@media only screen and (max-width: 480px){ td.bmeMblCenter {border: 0 none transparent !important;}}    
@media only screen and (max-width: 480px){.bmeLinkTable.tdPart td{padding-left:0px !important; padding-right:0px !important; border:0px none transparent !important;padding-bottom:15px !important;height: auto !important;}}    
@media only screen and (max-width: 480px){.tdMblHide{width:10px !important;} }    
@media only screen and (max-width: 480px){.bmeShareItemBtn{display:table !important;}}    
@media only screen and (max-width: 480px){.bmeMblStack td {text-align: left !important;}}    
@media only screen and (max-width: 480px){.bmeMblStack .bmeFollowItem{clear:both !important; padding-top: 10px !important;}}    
@media only screen and (max-width: 480px){.bmeMblStackCenter .bmeFollowItemText{padding-left: 5px !important;}}    
@media only screen and (max-width: 480px){.bmeMblStackCenter .bmeFollowItem{clear:both !important;align-self:center; float:none !important; padding-top:10px;margin: 0 auto;}}    
@media only screen and (max-width: 480px){    
.tdPart> table{width:100% !important;}    
}    
@media only screen and (max-width: 480px){.tdPart>table.bmeLinkContainer{ width:auto !important; }}    
@media only screen and (max-width: 480px){.tdPart.mblStackCenter>table.bmeLinkContainer{ width:100% !important;}}     
.blk_parent:first-child, .blk_parent{float:left;}    
.blk_parent:last-child{float:right;}    
/*** BMEMBF END ***/    
    
table[name="bmeMainBody"], body {background-color:#EFF5F9;}    
 td[name="bmePreHeader"] {background-color:transparent;}    
 td[name="bmeHeader"] {background:#ffffff;background-color:#EFF5F9;}    
 td[name="bmeBody"], table[name="bmeBody"] {background-color:#ffffff;}    
 td[name="bmePreFooter"] {background-color:#EFF5F9;}    
 td[name="bmeFooter"] {background-color:transparent;}    
 td[name="tblCell"], .blk {font-family:initial;font-weight:normal;font-size:initial;}    
 table[name="blk_blank"] td[name="tblCell"] {font-family:Arial, Helvetica, sans-serif;font-size:14px;}    
    
</style>    
</head>    
<body marginheight="0" marginwidth="0" topmargin="0" leftmargin="0" style="height: 100% !important; margin: 0; padding: 0; width: 100% !important;min-width: 100%;">    
    
<table width="100%" cellspacing="0" cellpadding="0" border="0" name="bmeMainBody" style="background-color: rgb(239, 245, 249);" bgcolor="#eff5f9"><tbody><tr><td width="100%" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" name="bmeMainColumnParentTable"><tbody><tr><td name="bmeMainColumnParent" style="border-collapse: separate;">     
<table name="bmeMainColumn" class="bmeHolder bmeMainColumn" style="max-width: 600px; overflow: visible;" cellspacing="0" cellpadding="0" border="0" align="center">    <tbody><tr><td width="100%" class="blk_container bmeHolder" name="bmePreHeader" valign="top" align="center" style="color: rgb(102, 102, 102); border: 0px none transparent;" bgcolor=""></td></tr> <tr><td width="100%" class="bmeHolder" valign="top" align="center" name="bmeMainContentParent" style="border-color: rgb(128, 128, 128); border-radius: 5px; border-collapse: separate; border-spacing: 0px;">     
<table name="bmeMainContent" style="border-radius: 5px; border-collapse: separate;border-spacing: 0px; overflow: hidden;" width="100%" cellspacing="0" cellpadding="0" border="0" align="center"> <tbody><tr><td width="100%" class="blk_container bmeHolder" name="bmeHeader" valign="top" align="center" style="border: 0px none transparent; background-color: rgb(239, 245, 249);" bgcolor="#eff5f9"><div id="dv_15" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_image"><tbody><tr><td>    
<table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td align="center" class="bmeImage" style="border-collapse: collapse; padding: 0px;"><img src="https://benchmarkemail.com/images/templates_n/new_editor/Templates/ChristmasCard/CardTop.png" class="mobile-img-large" width="600" style="max-width: 1200px; display: block; width: 600px;" alt="" border="0"></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_25" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_image"><tbody><tr><td>    
<table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td align="center" class="bmeImage" style="border-collapse: collapse; padding: 0px;"><img src="cid:dns_config" class="mobile-img-large" width="600" style="max-width: 1200px; display: block; width: 600px;" alt="" border="0"></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_26" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_image"><tbody><tr><td>    
<table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td align="center" class="bmeImage" style="border-collapse: collapse; padding: 0px;"><img src="https://benchmarkemail.com/images/templates_n/new_editor/Templates/ChristmasCard/CardBottom.png" class="mobile-img-large" width="600" style="max-width: 1200px; display: block; width: 600px;" alt="" border="0"></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_2" class="blk_wrapper" style="">    

<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider" style=""><tbody><tr><td class="tblCellMain" style="padding: 10px 20px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 0px; border-top-style: none; min-width: 1px;"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div></td></tr> <tr><td width="100%" class="blk_container bmeHolder bmeBody" name="bmeBody" valign="top" align="center" style="color: rgb(56, 56, 56); border: 0px none transparent; background-color: rgb(255, 255, 255);" bgcolor="#ffffff"><div id="dv_11" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider" style=""><tbody><tr><td class="tblCellMain" style="padding: 20px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 0px; border-top-style: none; min-width: 1px;"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_10" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 10px 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 125%; text-align: center;"><span style="font-size: 36px; font-family: Georgia, Palatino; color: #bb392f; line-height: 125%;">    
""" + f"""<em>RoseChen和廖抿抿<br>已经一起快落的度过{mail_content_text}啦</em></span>""" + """    
<br><span style="font-size: 12px; font-family: Arial, Helvetica, sans-serif; color: #cbd0d4; line-height: 125%;">__________</span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_12" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 150%; text-align: center;"><span style="font-size: 18px; font-family: Georgia, Palatino; color: #666666; line-height: 150%;">""" + f"""从2022年2月25日开始,我们已经在一起{mail_content_text}啦""" + """,以后也要开开心心的在一起奥</span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_20" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_button" style=""><tbody><tr><td width="20"></td><td align="center">    
<table class="tblContainer" cellspacing="0" cellpadding="0" border="0" width="100%"><tbody><tr><td height="20"></td></tr><tr><td align="center">    
<!-- <table cellspacing="0" cellpadding="0" border="0" class="bmeButton" align="center" style="border-collapse: separate;"><tbody><tr><td style="border-radius: 0px; border: 0px none transparent; text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: 14px; padding: 15px 30px; font-weight: normal; background-color: rgb(187, 57, 47);" class="bmeButtonText"><span style="font-family: Georgia, Palatino; font-size: 20px; color: rgb(255, 255, 255);">     -->
<!-- <a style="color:#FFFFFF;text-decoration:none;" target="_blank">Use Coupon Code</a></span></td></tr></tbody>     -->
<!-- </table></td></tr><tr><td height="20"></td></tr></tbody>     -->
</td></tr></tbody></table></td><td width="20"></td></tr></tbody>    
</table></div><div id="dv_24" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider" style="background-color: rgb(226, 226, 226);"><tbody><tr><td class="tblCellMain" style="padding: 0px 0px 10px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 40px; border-top-style: solid; min-width: 1px; border-top-color: rgb(255, 255, 255);"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div></td></tr> <tr><td width="100%" class="blk_container bmeHolder" name="bmePreFooter" valign="top" align="center" style="color: rgb(56, 56, 56); border: 0px none transparent; background-color: rgb(239, 245, 249);" bgcolor="#eff5f9"><div id="dv_5" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider"><tbody><tr><td class="tblCellMain" style="padding: 10px 20px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 0px; border-top-style: none; min-width: 1px;"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_3" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody> <tr><td width="100%" class="blk_container bmeHolder bmeBody" name="bmeBody" valign="top" align="center" style="color: rgb(56, 56, 56); border: 0px none transparent; background-color: rgb(255, 255, 255);" bgcolor="#ffffff"><div id="dv_11" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider" style=""><tbody><tr><td class="tblCellMain" style="padding: 20px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 0px; border-top-style: none; min-width: 1px;"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_10" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 10px 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 125%; text-align: center;"><span style="font-size: 36px; font-family: Georgia, Palatino; color: #bb392f; line-height: 125%;">    
""" + f"""<em>天气预报</em></span>""" + """    
<br><span style="font-size: 12px; font-family: Arial, Helvetica, sans-serif; color: #cbd0d4; line-height: 125%;">__________</span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_12" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 150%; text-align: center;"><span style="font-size: 18px; font-family: Georgia, Palatino; color: #666666; line-height: 150%;">""" + f"""<a style="color:black;" href="http://tianqi.moji.com/weather/china/shanghai/pudong-new-district">{res[1].split('区')[0]+'区'}</a>{res[1].split('区')[-1]}""" + f"""<div></div><a style="color:black;" href="http://tianqi.moji.com/weather/china/shanghai/changning-district">{res[0].split('区')[0]+'区'}</a>{res[0].split('区')[-1]}""" + """</span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_20" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_button" style=""><tbody><tr><td width="20"></td><td align="center">    
<table class="tblContainer" cellspacing="0" cellpadding="0" border="0" width="100%"><tbody><tr><td height="20"></td></tr><tr><td align="center">    
<!-- <table cellspacing="0" cellpadding="0" border="0" class="bmeButton" align="center" style="border-collapse: separate;"><tbody><tr><td style="border-radius: 0px; border: 0px none transparent; text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: 14px; padding: 15px 30px; font-weight: normal; background-color: rgb(187, 57, 47);" class="bmeButtonText"><span style="font-family: Georgia, Palatino; font-size: 20px; color: rgb(255, 255, 255);">     -->
<!-- <a style="color:#FFFFFF;text-decoration:none;" target="_blank">Use Coupon Code</a></span></td></tr></tbody>     -->
<!-- </table></td></tr><tr><td height="20"></td></tr></tbody>     -->
</td></tr></tbody></table></td><td width="20"></td></tr></tbody>    
</table></div><div id="dv_24" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider" style="background-color: rgb(226, 226, 226);"><tbody><tr><td class="tblCellMain" style="padding: 0px 0px 10px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 40px; border-top-style: solid; min-width: 1px; border-top-color: rgb(255, 255, 255);"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div></td></tr> <tr><td width="100%" class="blk_container bmeHolder" name="bmePreFooter" valign="top" align="center" style="color: rgb(56, 56, 56); border: 0px none transparent; background-color: rgb(239, 245, 249);" bgcolor="#eff5f9"><div id="dv_5" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_divider"><tbody><tr><td class="tblCellMain" style="padding: 10px 20px;">    
<table class="tblLine" cellspacing="0" cellpadding="0" border="0" width="100%" style="border-top-width: 0px; border-top-style: none; min-width: 1px;"><tbody><tr><td><span></span></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_3" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 10px 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 125%; text-align: center;"><span style="font-size: 24px; font-family: Georgia, Palatino; color: #bb392f; line-height: 125%;">    

<em>关于我们</em></span>    
<br><span style="font-size: 12px; font-family: Arial, Helvetica, sans-serif; color: #cbd0d4; line-height: 125%;">__________</span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_4" class="blk_wrapper" style="">    
<table width="600" cellspacing="0" cellpadding="0" border="0" class="blk" name="blk_text"><tbody><tr><td>    
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="bmeContainerRow"><tbody><tr><td class="tdPart" valign="top" align="center">    
<table cellspacing="0" cellpadding="0" border="0" width="600" name="tblText" style="float:left; background-color:transparent;" align="left" class="tblText"><tbody><tr><td valign="top" align="left" name="tblCell" style="padding: 5px 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-weight: 400; color: rgb(56, 56, 56); text-align: left;" class="tblCell"><div style="line-height: 200%; text-align: center;"><span style="font-size: 14px; font-family: Georgia, Palatino; color: #666666; line-height: 200%;">    
<em><a href="https://kiddliao.synology.me:10304" style="color:black;">rose &amp;&amp; 廖涵的主页 (ps:以后再搞) </a></em></span></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table></td></tr></tbody>    
</table></div><div id="dv_13" class="blk_wrapper" style="">    
</div></td></tr></tbody></table></td></tr></tbody>    
</table></td></tr> </tbody>    
</table></div></td></tr></tbody>    
</table></td></tr></tbody>    
</table>    

    
</td></tr></tbody></table></td></tr></tbody></table></body></html><img    
 src="cid:dns_config" alt='' border=0 style="display:none;" height=1 width=1>"""
    mail_host = "smtp.163.com"
    mail_postfix = "163.com"
    flag = sendmail(mail_sub, mail_content, img)
    print(datetime.datetime.now(), end='')

    if flag:
        print(f"发送成功!")
    else:
        print(f"发送失败!")


if __name__ == '__main__':
    if platform.system() == 'Linux':
        root_path = '/volume1/homes/liaohan/CODE'
        dir_path = os.path.join(root_path, 'send_mail')
        os.makedirs(dir_path, exist_ok=True)
        send_mail_images_record_path = os.path.join(
            dir_path, 'send_mail_images_record.txt')
        image_dir_paths = os.path.join('/volume1/photo/lh_sendmail')
    else:
        root_path = '.'
        dir_path = os.path.join(root_path, 'send_mail')
        os.makedirs(dir_path, exist_ok=True)
        send_mail_images_record_path = os.path.join(
            dir_path, 'send_mail_images_record.txt')
        image_dir_paths = os.path.join('lh_roserose')

    district_name, weather, temperature, wind, air_quality, tip = get_weather(
        'http://tianqi.moji.com/weather/china/shanghai/changning-district')
    res1 = f'{district_name}今日天气为{weather},气温在{temperature[0]}到{temperature[1]}之间,空气质量为{air_quality},风力为{wind},{tip}'
    district_name, weather, temperature, wind, air_quality, tip = get_weather(
        'https://tianqi.moji.com/weather/china/shanghai/pudong-new-district')
    res2 = f'{district_name}今日天气为{weather},气温在{temperature[0]}到{temperature[1]}之间,空气质量为{air_quality},风力为{wind},{tip}'

    image_paths = list(map(lambda x: x.strip(), glob.glob(
        os.path.join(image_dir_paths, '*'))))
    # print(image_paths)
    image_paths = list(filter(lambda x: x.split(
        '.')[-1].lower() in ('jpg', 'jpeg', 'png'), image_paths))
    # print(image_paths)
    image_send_num_dic = {}

    #随机发送图片,但是未发送过的图片优先级更高
    flag = os.path.exists(send_mail_images_record_path)
    if flag:
        with open(send_mail_images_record_path, 'r', encoding='utf_8') as f:
            image_send_num_dic = json.load(f)
            old_image_paths_set = set(image_send_num_dic)
            new_image_paths_set = set(image_paths)
            not_found_image_paths = old_image_paths_set - new_image_paths_set
            new_added_image_paths = new_image_paths_set - old_image_paths_set
            # 删除不存在图片,添加新图片
            for i, image_path in enumerate(list(new_added_image_paths)):
                image_send_num_dic[image_path] = 0
            for i, image_path in enumerate(list(not_found_image_paths)):
                image_send_num_dic.pop(image_path)
    if not flag:
        for i, image_path in enumerate(image_paths):
            image_path = image_path.strip()
            image_send_num_dic[image_path] = 0

    image_send_num_list = list(map(lambda x: x[1], image_send_num_dic.items()))
    min_image_send_num = min(image_send_num_list)
    image_paths_list = []
    for k, v in image_send_num_dic.items():
        if v == min_image_send_num:
            image_paths_list.append(k)
    random.shuffle(image_paths_list)
    image_final_path = image_paths_list[0]
    image_send_num_dic[image_final_path] += 1
    with open(send_mail_images_record_path, 'w', encoding='utf_8') as f:
        json.dump(image_send_num_dic, f, indent=1)

    flag, difference, memorial_difference = cal_memorial()
    if flag == 1:
        if memorial_difference == 365:
            mail_content_text = f'{difference}周年'
            mail_sub = f'今天是我们的{mail_content_text}恋爱纪念日呀!!!'
        else:
            mail_content_text = f'{difference}天'
            mail_sub = f'今天是我们的{mail_content_text}恋爱纪念日呀!!!'
        mail(mail_sub, mail_content_text, image_final_path, [res1, res2])
        mail(mail_sub, mail_content_text, image_final_path, [res1, res2])
        mail(mail_sub, mail_content_text, image_final_path, [res1, res2])
    else:
        mail_content_text = f'{difference}天'
        mail_sub = f'我们已经在一起{mail_content_text}啦'
        mail(mail_sub, mail_content_text, image_final_path, [res1, res2])
