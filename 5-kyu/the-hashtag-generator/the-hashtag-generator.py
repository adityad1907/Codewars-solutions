def generate_hashtag(s):
    words = s.split()
    
    if not words:
        return False
    
    hashtag = "#" + "".join(word.capitalize() for word in words)
    
    if len(hashtag) > 140 or len(hashtag) == 1:
        return False
        
    return hashtag
​