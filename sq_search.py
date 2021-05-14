import sqlite3




def find_names_in_db(query):
    
    conn = sqlite3.connect("sea.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sea WHERE Name LIKE ? ", (query,))
    name_matches= [i[2] for i in cur.fetchall()]
    conn.close()
    return name_matches



def find_ticker(query):

    conn = sqlite3.connect("sea.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sea WHERE Ticker = ? ", (query,))
    x=cur.fetchall()
    if x:
        chosen_firm=x[0]    # Using 1st item of the result list- which is tuple with values for requested ticker
        conn.close()
        return chosen_firm

    else:
        return None



def get_all_byname(query): 
    
    conn = sqlite3.connect("sea.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sea WHERE Name = ? ", (query,))
    all_byname=cur.fetchall()[0]
    conn.close()
    return all_byname



def browse_all():

    conn = sqlite3.connect("sea.db")
    cur = conn.cursor()
    cur.execute("SELECT Ticker, Name, Sector, HQ, Founded FROM sea")
    full_list= cur.fetchall()
    conn.close()
    return full_list

    

def starts_with_letter(letter):
    
    conn = sqlite3.connect("sea.db")
    cur = conn.cursor()
    cur.execute("SELECT Ticker, Name, Sector, HQ, Founded FROM sea WHERE Name LIKE ? ", (letter,))
    letter_matches= cur.fetchall()
    conn.close()
    return letter_matches







