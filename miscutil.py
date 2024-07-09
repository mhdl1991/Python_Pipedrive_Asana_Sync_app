def fetch_line(filename, line = 0):
    '''
    Fetches a line from an external file
    '''
    lines = []
    try: 
        with open(filename) as f:
            lines = f.readlines()
            
    except Exception as e:
        print("Exception: {}".format(e) )
        
    return lines[line].strip('\n')