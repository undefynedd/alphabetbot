def check(message, letters):
    from unidecode import unidecode
    
    good = 0
    print("This was an alphabet channel.")
    
    if len(message.content) == 0:
        good = 1
        print("The message was empty, so I let it pass.")
    
    elif "youtu" in message.content:
        
        print("I think this is a youtube video.")
        
        if "youtu.be" in message.content:
            if "https://" in message.content:
                print("It was an https:// link.")
                id = message.content[17:].strip("/")
                
            elif "http://" in message.content:
                print("It was an http:// link.")
                id = message.content[16:].strip("/")
                
        else:
            id = parse_qs(urlparse(message.content).query).get('v')[0]   # the id comes out as a one value list for some reason
        
        print(id)
        
        try:
            params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % id}   # yeah i found this on stackoverflow
            url = "https://www.youtube.com/oembed"   # oh! this is the start of the url
            query_string = urllib.parse.urlencode(params)   # this gets the query string (id)
            url = url + "?" + query_string   # this adds the id onto the url!

            with urllib.request.urlopen(url) as response:   # this whole thing gets the data from the yt video
                response_text = response.read()   # i think this reads the json and puts it in var
                data = json.loads(response_text.decode())   # oh and this loads it into json
                title = data['title']    # and this gets the title
                print(f"The title was {title}.")   # useless debug code shut up
                
                for i in letters[message.channel.name]:    # i should make this a function
                
                    if title.lower().startswith(i):
                        print(f"The video started with {i}, so it's all good.")
                        good = 1
        
        except:
            print("I don't think it was a youtube video. I give up")
            good = 0
            
    for i in letters[message.channel.name]:
    
        if message.content.lower().strip("*_`~|").startswith(i):
            print("Success!")
            good = 1
            break
        
        elif unidecode(message.content.lower().strip("*_`~|")).startswith(i):
            print("Success!")
            good = 1
            break
                
    return good
