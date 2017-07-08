# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from bs4 import BeautifulSoup
import requests, tweepy, random, praw, re, sys, json, time, yhanswers, urllib3, json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from subprocess import check_output   
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
re 


def noEmoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    newText = emoji_pattern.sub(r'', text) # no emoji
    finalText = re.sub('https:\/\/t.co\/\S*( |$)', '', newText)
    return finalText
    



def doLogins(both=True):
    #Log into twitter with twitter credentials 
    auth = tweepy.OAuthHandler('<your credentials>', '<your credentials>')
    auth.set_access_token('<your credentials>', '<your credentials>')
    api = tweepy.API(auth)
    
    if not both:
        return api
        
    #Log into PRAW with script credentials 

                           
    r = praw.Reddit(<your credentials>)


    return api, r


api, r = doLogins()

def spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    x = soup.prettify()
    x = str(x)
    x = x.replace("\\u003cb\\u003e", " ")
    x = x.replace("\\u003c/b\\u003e", " ")
    x = x.replace("\\u003cbr /\\u003e", " ")
    return x 

def getYT(website):
    index = website.index('=')
    global end_dex
    end_dex = len(website)
    if any (key in website for key in '&'):
        end_dex = website.index('&')
    video_id = (website[index+1:end_dex])
    print(video_id)
    template = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&videoId=variable&key=<your key>'
    final = template.replace("variable", video_id)
    print(final)
    x = spider(final)
    global top_comment, alength 
    top_comment = re.findall('"textDisplay":.*",', x)
    alength = len(top_comment)
    if alength > 60:
        top_comment = top_comment[random.randrange(40, len(top_comment)-1)].strip('"textDisplay":')
        top_comment = top_comment[2:len(top_comment)-2]
        return top_comment 
    else: 
        return None

#api = doLogins(both=False)
    
def getTwitterReply(url):
    print('HERE IS TWITTER')
    authName = url.split('.com/')[1].split('/status')[0]
    print('GOT HERE')
    tweetID = api.get_status(url.split('status/')[1]).id
    results = [status for status in tweepy.Cursor(api.search, q='@{}'.format(authName), since_id=tweetID).items(10) if str(status.in_reply_to_status_id) == str(tweetID)]
    filtered = [result.text for result in results if 'you' not in str(result.text).lower()]
    print(filtered)
    farray = list()
    for pros in filtered:
        newPros = []
        for word in pros.split(' '):
            if '@' not in word:
                newPros.append(word)
        if ' '.join(newPros).replace(' ','') != '':
            farray.append(' '.join(newPros))
    print(farray)
    return random.choice(farray)
    
    
def getWP(url):
    ourl = url.split('?')[0].strip('https').strip('http').replace('://','').strip(':').replace('/','%2F')
    template = '''https://comments-api.ext.nile.works/v2/mux?appkey=prod.washpost.com&requests=%5B%7B%22id%22%3A%22featuredPosts-search%22%2C%22method%22%3A%22search%22%2C%22q%22%3A%22((childrenof%3A+https%3A%2F%2F{url}+source%3Awashpost.com+(((state%3AUntouched++AND+user.state%3AModeratorApproved)+OR+(state%3AModeratorApproved++AND+user.state%3AModeratorApproved%2CUntouched)+OR+(state%3ACommunityFlagged%2CModeratorDeleted+AND+user.state%3AModeratorApproved)+)++AND+(+markers%3A+featured_comment++-markers%3Aignore+)+)+++))+itemsPerPage%3A+15+sortOrder%3AreverseChronological+safeHTML%3Aaggressive+children%3A+2+childrenSortOrder%3Achronological+childrenItemsPerPage%3A3++(((state%3AUntouched++AND+user.state%3AModeratorApproved)+OR+(state%3AModeratorApproved++AND+user.state%3AModeratorApproved%2CUntouched)+OR+(state%3ACommunityFlagged%2CModeratorDeleted+AND+user.state%3AModeratorApproved)+)++AND+(+markers%3A+featured_comment++-markers%3Aignore+)+)+%22%7D%2C%7B%22id%22%3A%22allPosts-search%22%2C%22method%22%3A%22search%22%2C%22q%22%3A%22((childrenof%3A+https%3A%2F%2F{url}+source%3Awashpost.com+(((state%3AUntouched++AND+user.state%3AModeratorApproved)+OR+(state%3AModeratorApproved++AND+user.state%3AModeratorApproved%2CUntouched)+OR+(state%3ACommunityFlagged%2CModeratorDeleted+AND+user.state%3AModeratorApproved)+)+)+++))+itemsPerPage%3A+15+sortOrder%3AreverseChronological+safeHTML%3Aaggressive+children%3A+2+childrenSortOrder%3Achronological+childrenItemsPerPage%3A3++(((state%3AUntouched++AND+user.state%3AModeratorApproved)+OR+(state%3AModeratorApproved++AND+user.state%3AModeratorApproved%2CUntouched)+OR+(state%3ACommunityFlagged%2CModeratorDeleted+AND+user.state%3AModeratorApproved)+)+)+%22%7D%5D'''.format(url=ourl)
    rtext = str(requests.get(template).text)
    found = re.findall('\"content\":.*",', rtext)
    if len(found) > 20:
        found = [f for f in found[10:] if 'you' not in f.lower()]
        comment = found[random.randrange(0, len(found)-1)].strip('"content":')
        comment = comment[2:-2]
        return re.sub('\<[^>]*\>', '', comment)
        
    
def getIND(url):
    sid = url[url.index('.html')-8:-5]
    print(sid)
    template = '''https://comments.us1.gigya.com/comments.getComments?categoryID=ArticleComments&streamID={}&includeSettings=true&threaded=true&includeStreamInfo=true&includeUserOptions=true&includeUserHighlighting=true&lang=en&ctag=comments_v2&APIKey=2_bkQWNsWGVZf-fA4GnOiUOYdGuROCvoMoEN4WMj6_YBq4iecWA-Jp9D2GZCLbzON4&cid=&source=showCommentsUI&sourceData=%7B%22categoryID%22%3A%22ArticleComments%22%2C%22streamID%22%3A%22a7788651%22%7D&sdk=js_7.2.40&authMode=cookie&format=jsonp&callback=gigya.callback&context=R1267091514'''.format(sid)
    rtext = requests.get(template).text
    found = re.findall('\"commentText\":.*",', rtext)
    if len(found) > 1:
        x=0
        ccom = random.choice(found)
        while 'you' in ccom.lower():
            if x > 50:
                raise Exception('No appropriate comments; avoiding loop!')
            ccom = random.choice(found)
            x+=1
        pproc = re.sub('\<[^>]*\>', '', ccom)
        pproc = pproc.strip('"commentText":')
        return pproc[2:-2]
        
  
def crawlGeneral(url):
    r = requests.get('http://www.independent.co.uk/news/world/americas/us-politics/jeff-sessions-testimony-russia-trump-never-met-election-campaign-a7788651.html')
    open('todisplay.html','w').write(r.text)

def finalize(textInput): 
    textInput = textInput.replace('you', random.choice(['you', 'u', 'u'])).replace('lol', random.choice([' lol ',' haha ',' haha '])).replace('amazing', random.choice(['great', 'impressive'])).replace(' video ', random.choice([' clip ', ' video '])).replace(', but', random.choice([', but', ', however'])).replace(' god ', random.choice([' God ', ' god '])).replace(' problem ', random.choice([' issue ', ' problem '])).replace('this', random.choice(['this', 'that', 'this'])).replace(' incredible ', random.choice(['amazing', 'awesome', 'incredible'])).replace('person ', random.choice(['person', 'individual'])).replace(' hated ', random.choice(['hated', 'despised'])).replace('thanks', random.choice(['thanks', 'thank you'])).replace('Thanks', random.choice(['Thanks', 'Thank you'])).replace('money', random.choice(['money', 'cash'])).replace(' he is ', random.choice([' he\'s ', ' he is '])).replace('he\'s', random.choice([' he\'s ', ' he i s'])).replace(' she\'s ', random.choice([' she\'s ', ' she is '])).replace(' she is ', random.choice([' she\'s ', ' she is '])).replace(' it\'s ', random.choice([' it\'s ', ' it is '])).replace(' it is ', random.choice([' it\'s ', ' it is ']))
    if 'donald' not in textInput.lower():
        textInput = textInput.replace('Trump', random.choice(['The President', 'Trump'])).replace('trump', random.choice(['the president', 'trump']))
    if textInput.lower().rstrip() != 'first':
        return textInput
    else:
        raise Exception("Annoying First Comment -- Ignore!")
import time 

tcount = [0]


def leaveRandom(choice):
    if choice == 'ind':
        for post in [post for post in r.domain('independent.co.uk').new(limit=100) if post.url not in open('storage.txt','r').read().split('\n') and post.id not in open('storage.txt','r').read().split('\n') and time.time() - post.created_utc > 300 and 'auto' not in post.subreddit.display_name.lower()]:
            try:
                open('storage.txt','a').write(post.url + '\n')
                open('storage.txt','a').write(post.id + '\n')
                post.reply(finalize(getIND(post.url).replace('\\n','\n').replace('\\','')))
                break 
            except:
                pass 
    elif choice == 'tw':
        for post in [post for post in r.domain('twitter.com').new(limit=100) if post.url not in open('storage.txt','r').read().split('\n') and post.id not in open('storage.txt','r').read().split('\n') and time.time() - post.created_utc > 100 and time.time() - tcount[0] > 300 and 'auto' not in post.subreddit.display_name.lower()]:
            try:
                tcount[0] = time.time()
                open('storage.txt','a').write(post.url + '\n')
                open('storage.txt','a').write(post.id + '\n')
                tocomment = noEmoji(getTwitterReply(post.url))
                if 'href' not in tocomment:
                    post.reply(finalize(tocomment))
                break 
            except Exception as e:
                print('TW ERROR')
                print(str(e))
    elif choice == 'yt':
        for post in [post for post in r.domain('youtube.com').new(limit=100) if post.url not in open('storage.txt','r').read().split('\n') and post.id not in open('storage.txt','r').read().split('\n')  and time.time() - post.created_utc > 300 and 'auto' not in post.subreddit.display_name.lower()]:
            try:
                open('storage.txt','a').write(post.url + '\n')
                open('storage.txt','a').write(post.id + '\n')
                tocomment = noEmoji(getYT(post.url).replace('\\n','\n').replace('\\',''))
                if 'href' not in tocomment:
                    post.reply(finalize(tocomment))
                break 
            except:
                pass
    elif choice == 'wp':
        for post in [post for post in r.domain('washingtonpost.com').new(limit=100) if post.url not in open('storage.txt','r').read().split('\n') and post.id not in open('storage.txt','r').read().split('\n') and time.time() - post.created_utc > 300 and 'auto' not in post.subreddit.display_name.lower()]:
            try:
                open('storage.txt','a').write(post.url + '\n')
                open('storage.txt','a').write(post.id + '\n')
                post.reply(finalize(getWP(post.url).replace('\\n','\n').replace('\\','')))
                break 
            except:
                pass
    elif choice == 'ya':
        for post in [post for post in r.subreddit('askreddit').new(limit=10) if post.url not in open('storage.txt','r').read().split('\n') and post.id not in open('storage.txt','r').read().split('\n') and time.time() - post.created_utc > 0 and len(post.title) <= 50 and 'auto' not in post.subreddit.display_name.lower()]:
            try:
                open('storage.txt','a').write(post.url + '\n')
                open('storage.txt','a').write(post.id + '\n')
                potAns = yhanswers.get_answer(post.title)
                print(potAns)
                if len(potAns) <= 220:
                    post.reply(finalize(potAns))
                    break
            except Exception as e:
                print('AR ERROR')
                print(str(e))
                pass
def checkComments():
    for comment in r.redditor('messipro').new(limit=500):
        if comment.score <= -2:
            print(comment.score)
            print('https://www.reddit.com{}'.format(comment.permalink()))
            comment.delete()

        
while True:
    try:
        leaveRandom(random.choice(['wp','yt', 'tw', 'ind', 'ya', 'ya']))
        checkComments()
    except Exception as e:
        print('ERROR')
        print(str(e))