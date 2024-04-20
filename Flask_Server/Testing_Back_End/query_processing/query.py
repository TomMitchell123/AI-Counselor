

def process_query(user_input:str) -> str:
    """ Takes in a user input and pipes it into a gpt which returns a sql query to get the data

    Args:
        user_input (str): natural language input that gets piped into a gpt

    Returns:
        str: an sql query to be executed by the database
    """    
    return "The cheating policy forbids the use of ChatGPT in assisting school work"