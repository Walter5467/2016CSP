def how_eligible(essay):
    Missing = 4
    if '!' not in essay:
        Missing = Missing - 1
        print('There is no exclamation in this essay')
    if '"' not in essay:
        Missing = Missing - 1
        print('There is no quote in this essay')
    if '?' not in essay:
        Missing = Missing - 1
        print('There is not a question in this essay')
    if ',' not in essay:
        Missing = Missing - 1
        print('There is not a compound sentence in this essay')
    return Missing
                
        
        
            
            
        
