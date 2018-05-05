import twitter
import send_msg
import config
from time import sleep

api = twitter.Api(consumer_key = config.cuns_key,
                  consumer_secret = config.cuns_secret,
                  access_token_key = config.a_token_key,
                  access_token_secret = config.a_token_secret)

def w_last_tag(id):
    f = open('tag.txt', 'w')
    f.write(str(id))
    f.close()

def r_last_tag():
    f = open('tag.txt', 'r')
    my_id = f.read()
    f.close()
    return my_id

try:
    if r_last_tag() == []:
        # print('check')
        tag1 = api.GetSearch(term='#c_center_expo')
        w_last_tag(tag1[0].id)
except FileNotFoundError:
    tag2 = api.GetSearch(term='#c_center_expo')
    w_last_tag(tag2[0].id)

while True:
    sleep(900)
    print('sleeping 900')
    tweetSearch = api.GetSearch(term='#c_center_expo', since_id=r_last_tag())
    if (tweetSearch == []):
        print('tweetSearch: null')
        continue
    else:
        print('tweetSearch: new msg')
        w_last_tag(tweetSearch[0].id)
    print(tweetSearch)
    for i in range(len(tweetSearch)):
        api.PostUpdate(status='@' + tweetSearch[i].user.screen_name + 'Ваше обращение зарегистрировано. Ожидайте ответа от менеджера по предоставленным Вами контактным данным.', in_reply_to_status_id=tweetSearch[i].id)
        send_msg.send(tweetSearch[i].text, str(tweetSearch[i].id) + '@' + tweetSearch[i].user.screen_name)