currencyName=["0","XAF","ARS","AUD","BSD","BRL","BGN","CAD","CLP","CNY","COP","HRK","CYP","CZK","DKK","LTC","BTC","XCD","EEK","EUR","FJD","XPF","GHS","GTQ","HNL","HKD","HUF","ISK","INR","IDR","ILS","JMD","JPY","LVL","LTL","MYR","MXN","MAD","MMK","ANG","NZD","NOK","PKR","PAB","PEN","PHP","PLN","GOLD","QAR","RON","RUB","SAR","RSD","SGD","ZAR","KRW","LKR","SEK","CHF","TWD","THB","TTD","TND","TRY","AED","GBP","USD","VND","VEF"]

currencyValue=[0,582.43,14.32,1.30,1.0,3.74,1.73,1.2835,663.85,6.4825,2991.92,6.6401,0.519911,23.987,6.6060,0.3112,0.002376,2.6898,11.73,0.88,2.0501,105.90,3.8245,7.8792,22.550,7.7564,276.56,124.49,66.573,13232.29,3.7828,121.78,109.14,0.62,3.05,3.91,17.42,9.70,1178.2,1.79,1.45,8.24,104.67,1.0,3.27,46.14,3.82,0.000813,3.64,3.97,66.07,3.75,109.14,1.36,14.56,1151.75,146.25,8.14,0.97,32.41,35.11,6.60,2.02,2.85,3.67,0.71,1.0,22309.50,9.95,]
 
a = zip(currencyName, currencyValue) 
currencyDict = dict(a)

# Create a dictionary from the lists
#for i in currencyName:
	#if a key is not in the dictionary, it will create it automatically
    #keys are UNIQUE
#	currencyDict[currencyName] = currencyValue
	
#Taking Input	
number = float(input("Enter a value which you want to convert : "))
currency = input("Enter the currency to which you want to convert the amount : ")

result = number*currencyDict[currency]

if currency in currencyDict.keys():
	# calling a dictionary with a key returns the value associated to the key
	print (str(number) + 'USD represents ' + str(result) + str(currency) + '.')
else:
	print ("Invalid Currency")