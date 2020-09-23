import requests

URL = "111"
res = requests.get(URL, params={'param1': 'value1', 'param2': 'value'})  # params - query string
res2 = requests.post(URL, data={'param1': 'value1', 'param2': 'value'})  # data - body

res3 = requests.post(URL, data={'outer': {'inner': 'value'}})

import json

data = {'outer': {'inner': 'value'}}
res4 = requests.post(URL, data=json.dumps(data))

res5 = requests.get(URL, headers={'token': 'token'}, cookies={'cookie': 'cookey'})  # headers, cookies

requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()
requests.post(uri, headers={'X-Auth-Token': token}, data=json.dumps({'commands': cmds})).json()

res.request # 내가 보낸 request 객체에 접근 가능
res.status_code # 응답 코드
res.text # body의 내용물을 text로 반환. encoding타입을 설정하는게 좋음
res.content # body를 byte로 변환
res.ok # Returns True if status_code is less than 400, False if not.
res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
res.json() # json response일 경우 딕셔너리 타입으로 바로 변환
'''
requests.request(method, url, **kwargs) - https://requests.readthedocs.io/en/master/api/#requests.request
Parameters:	
    method – method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
    url – URL for the new Request object.
    params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
    data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
    json – (optional) A JSON serializable Python object to send in the body of the Request.
    headers – (optional) Dictionary of HTTP Headers to send with the Request.
    cookies – (optional) Dict or CookieJar object to send with the Request.
    files – (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file.
    auth – (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    timeout (float or tuple) – (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
    allow_redirects (bool) – (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
    proxies – (optional) Dictionary mapping protocol to the URL of the proxy.
    verify – (optional) Either a boolean, in which case it controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
    stream – (optional) if False, the response content will be immediately downloaded.
    cert – (optional) if String, path to ssl client cert file (.pem). If Tuple, (‘cert’, ‘key’) pair.
Returns:	
Response object

Return type:	
requests.Response

--------------------------------------------------------------

requests.get(url, params=None, **kwargs)

Parameters:	
url – URL for the new Request object.
params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
**kwargs – Optional arguments that request takes.
Returns:	
Response object

Return type:

----------------------------------------------------------------------

requests.post(url, data=None, json=None, **kwargs)
Sends a POST request.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json data to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Returns:	
Response object

Return type:	
requests.Response

--------------------------------------------------------

requests.put(url, data=None, **kwargs)
Sends a PUT request.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json data to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Returns:	
Response object

Return type:	
requests.Response

-----------------------------------------------------

requests.patch(url, data=None, **kwargs)
Sends a PATCH request.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json data to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Returns:	
Response object

Return type:	
requests.Response

-------------------------------------------------------

requests.delete(url, **kwargs)
Sends a DELETE request.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Returns:	
Response object

Return type:	
requests.Response

-----------------------------------------------
class requests.Response[source] - https://requests.readthedocs.io/en/master/api/#requests.Response

close()[source]
    Releases the connection back to the pool. Once this method has been called the underlying raw object must not be accessed again.

content
    Content of the response, in bytes.
    
elapsed = None
    The amount of time elapsed between sending the request and the arrival of the response (as a timedelta). 
    This property specifically measures the time taken between sending the first byte of the request and finishing parsing the headers. 
    It is therefore unaffected by consuming the response content or the value of the stream keyword argument.

encoding = None
    Encoding to decode with when accessing r.text.

headers = None
    Case-insensitive Dictionary of Response Headers. For example, headers['content-encoding'] will return the value of a 'Content-Encoding' response header.

json(**kwargs)[source]
    Returns the json-encoded content of a response, if any.
    Parameters:	**kwargs – Optional arguments that json.loads takes.
    Raises:	ValueError – If the response body does not contain valid json.
    links
    Returns the parsed header links of the response, if any.

ok
    Returns True if status_code is less than 400, False if not.

raise_for_status()[source]
    Raises HTTPError, if one occurred.

raw = None
    File-like object representation of response (for advanced usage). 
    Use of raw requires that stream=True be set on the request. This requirement does not apply for use internally to Requests.

reason = None
    Textual reason of responded HTTP Status, e.g. “Not Found” or “OK”.

request = None
    The PreparedRequest object to which this is a response.

status_code = None
    Integer Code of responded HTTP Status, e.g. 404 or 200.

text
    Content of the response, in unicode.
    If Response.encoding is None, encoding will be guessed using chardet.
    The encoding of the response content is determined based solely on HTTP headers, following RFC 2616 to the letter. 
    If you can take advantage of non-HTTP knowledge to make a better guess at the encoding, you should set r.encoding appropriately before accessing this property.

url = None
    Final URL location of Response.
'''
