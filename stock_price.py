import streamlit as st



#..data enrty form...

with st.form("my_form"):
   st.write('##### App to Convert Stock Orders')
   entry = st.text_area('Paste Signal Below:',height=200)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write(entry)

#st.write('---')
#st.write('''##### Below is the formatted entry: First word capitalized, 'Limit' deleted and LMT added''')
#..caplitalizing first word and other operations...
def cap_first_word(entry):      #..defining function
    if entry:
        entry = entry.split()        #..splits string into list
        entry[0]= entry[0].upper()   #...capitalizes first word in the list
        new_entry = ' '.join(entry)  #...joins list back to string
        new_entry = new_entry.replace('Limit','')   #...deletes words Limit
        new_entry = new_entry +' ' + 'LMT'          #....adds LMT at end of the string
        return new_entry
    else:
        return 'Enter Your Order'
#st.write(cap_first_word(entry))


#..converting stock price from string to float...
def converting_to_float(entry):   #...converting price string to float...
    try:
        entry = entry.split()
        entry[4] = float(entry[4])    #...converting corresponding index to float
        return entry[4]
    except:
        return None
price = converting_to_float(entry)

#st.write(price)
#st.write(type(price))

#..calculatng $10k worth of stock....
def number_of_shares(price):
    try:
        cash = 10000
        stock = cash/price
        stock = stock
        stock = round(stock)    #...rounding to integers
        stock = stock//2*2     #...rounding to nearest even number
        
        return stock
    except:
        return entry
shares = number_of_shares(price)



#st.write('Buy',number_of_shares(price),'Shares')

#..ticker name....
def ticker(entry):
    if(entry):
        ticker_symbol = entry.split()[2]
        return ticker_symbol
    else: return entry
#...st.write(ticker(entry))

st.write('---')
st.write('##### This is the number of shares worth $10,000. Figures rounded to nearest even numbers')
st.write('BUY','+'+str(shares),ticker(entry),'@'+str(price),'LMT')


#..join to list....
data = ('BUY','+'+str(shares),ticker(entry),'@'+str(price),'LMT')
data = ' '.join(data)






