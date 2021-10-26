# hello welcome to my code interview

# q: how are you doing today, code?
# a: i love existing

def check(message, letters):
    from unidecode import unidecode    # q: wow code, what does this do?
    
    good = 0                           # a: it variable
    print("This was an alphabet channel.")
    
    if len(message.content) == 0:
        good = 1                       # q: that's impressive, code!
        print("The message was empty, so I let it pass.")    # a: ikr just wish you wrote me better
    
    elif "youtu" in message.content:                         # q: shut up, what does this do?
                                                             # a: it is if i think it is a yt vid
        print("I think this is a youtube video.")            # can you read?
        
        if "youtu.be" in message.content:                    # q: yes, what about this?
            if "https://" in message.content:                # a: it is if it is an https or http
                print("It was an https:// link.")
                id = message.content[17:].strip("/")
                
            elif "http://" in message.content:               # q: why do you need to know that?
                print("It was an http:// link.")             # a: cuz hardcoding positions
                id = message.content[16:].strip("/")
                
        else:
            id = parse_qs(urlparse(message.content).query).get('v')[0]   # q: why does the id comes out as a one value list
        
        print(id)                                                        # a: good question
        
        try:
            params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % id}   # q: did you find this on stackoverflow?
            url = "https://www.youtube.com/oembed"                                          # a: yeah but i know this part is the start of the url,
            query_string = urllib.parse.urlencode(params)                                   # this gets the query string (id),
            url = url + "?" + query_string                                                  # and this adds the id onto the url!
                                                                                            # q: nice!
            with urllib.request.urlopen(url) as response:                                   # this whole thing gets the data from the yt video
                response_text = response.read()                                             # this reads the json and puts it in var
                data = json.loads(response_text.decode())                                   # this loads it into json
                title = data['title']
                print(f"The title was {title}.")                                            # q: if you knew all that, why didn't you write it?
                                                                                            # a: shut up
                for i in letters[message.channel.name]:
                
                    if title.lower().startswith(i):                                         # q: doesn't this just do the same thing as the next block?
                        print(f"The video started with {i}, so it's all good.")             # a: does it matter?
                        good = 1
        
        except:                                                                             # q: i love try except
            print("I don't think it was a youtube video. I give up")                        # a: same
            good = 0
            
    for i in letters[message.channel.name]:                                     # q: alright that's almost it, 12 more lines to go!
    
        if message.content.lower().strip("*_`~|").startswith(i):                # a: finally!
            print("Success!")
            good = 1
            break
        
        elif unidecode(message.content.lower().strip("*_`~|")).startswith(i):   # q: did you enjoy this?
            print("Success!")
            good = 1
            break
                
    return good                                                                 # a: return
