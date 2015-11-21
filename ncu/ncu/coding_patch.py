import chardet


enable_coding=['UTF-8','GBK','GB2312']
# return a  fixed unicode code
def encode_content(resonse_encoding,content,response_body):
	if resonse_encoding.upper() in enable_coding:
		return content
	if response_body:
		ty=chardet.detect(response_body)['encoding']
		try:
			fix_content=content.encode(resonse_encoding).decode(ty,'xmlcharrefreplace')
		except Exception:
			fix_content=content.encode(resonse_encoding).decode(ty,'ignore')
		return fix_content
	
