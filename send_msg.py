import requests

def send(msg, phone):

    url = "http://10.79.4.29:8080/eai_enu/start.swe?SWEExtSource=WebService&SWEExtCmd=Execute&WSSOAP=1"

    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://siebel.com/webservices" xmlns:ser="http://www.siebel.com/xml/Service Request IO" xmlns:ser1="http://www.siebel.com/xml/Service%20Request%20IO">
               <soapenv:Header>
                  <web:PasswordText>t5amor3</web:PasswordText>
                  <web:UsernameToken>sadmin</web:UsernameToken>
               </soapenv:Header>
               <soapenv:Body>
                  <ser:SRInsert>
                     <SiebelMessage>
                        <ser1:ListOfServiceRequestIo>
                           <!--Zero or more repetitions:-->
                           <ser1:ServiceRequest>
                              <!--Optional:-->
                              <ser1:Abstract>""" + msg + """</ser1:Abstract>
                              <!--Optional:-->
                              <ser1:Area>Цифровой запрос</ser1:Area>
                              <!--Optional:-->
                              <ser1:PhoneNumber>""" + phone + """</ser1:PhoneNumber>
                              <!--Optional:-->
                              <ser1:INSProduct>Обслуживание</ser1:INSProduct>
                              <!--Optional:-->
                              <ser1:Priority>3 - средний</ser1:Priority>
                              <!--Optional:-->
                              <ser1:Source>Social Media</ser1:Source>
                              <!--Optional:-->
                              <ser1:Sub-Area>Twitter</ser1:Sub-Area>
                           </ser1:ServiceRequest>
                        </ser1:ListOfServiceRequestIo>
                     </SiebelMessage>
                  </ser:SRInsert>
               </soapenv:Body>
            </soapenv:Envelope>"""

    headers = {'Content-Type': 'text/xml;charset=UTF-8',
               'Content-Length': str(len(body)),
               'Accept-Encoding': 'gzip,deflate',
               'SOAPAction': '"rpc/http://www.siebel.com/xml/Service Request IO:SRInsert"',
               'Host': '10.79.4.29:8080',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)'}

    response = requests.post(url, data=body.encode('UTF-8'), headers=headers)
    return response.content.decode('UTF-8')