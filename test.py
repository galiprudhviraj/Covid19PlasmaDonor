 trans['password'] =  "ccc"
    trans['contact'] =  "9652861905"
    trans['email'] =  "kaleem.mmd@gmail.com"
    trans['address'] =  "hyd"
    print(trans)
    table.put_item(Item=trans)
'''
'''
def read(db):
    table = db.Table('Users')
    response = table.scan()
    data = response['Items']
    for i in range(len(data)):
        for k,v in data[i].items():
            print(k+" "+v)
'''
def sendEmail(uname,details,email):
    msg = EmailMessage()
    msg.set_content(uname+" "+details)
    msg['Subject'] = 'Message From Plasma Donor Requestor'
    msg['From'] = "examportalexam@gmail.com"
    msg['To'] = email


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("examportalexam@gmail.com", "lzqdyzrtfaallejh")
    s.send_message(msg)
    s.quit()
    return "Email Message Sent To donors"

if __name__ == '__main__':


    #dynamodb = boto3.resource('dynamodb',  endpoint_url = "http://dynamodb.us-east-2.amazonaws.com", region_name='us-east-2')

    #load_transactions(dynamodb)
    #read(dynamodb)
    sendEmail('aa','aa','kaleem.mmd@gmail.com')
