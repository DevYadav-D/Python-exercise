#To count the number of people who are online, from a dictionary
def online_count(d):
    result=0;
    for i in d:
        if d.get(i)=='online':              #get retrive the value by key from dict
            result+=1;
    return result
