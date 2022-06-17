def state_style(state,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = val_90[state]
    
    #Set state colour
    if max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445f2b"
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3c8a5a"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 1,
            'color': color,
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 1,
             'weight': 1,
             'fillColor': color,
             'color': '#000000'}    
  
    return state_style