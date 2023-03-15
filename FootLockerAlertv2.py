import bs4
import urllib.request
import re
import time
from discord_webhook import DiscordWebhook
WEBHOOKURL = ''



# This function handles the alert to discord channel using the discord webhook
def sendalert(productsPhotoes, indexesOfPhotoes):
    # Using discord webhook to alert everyone for stock
    for i in indexesOfPhotoes:
        msg = "**..***..**..**..**..**..*NEW SHOE IN STOCKK**..***..**..**..**..**..**\n Photo: " +productsPhotoes[i]+ "\n\n\nLink---> https://www.footlocker.co.il/release <---"
        webhook = DiscordWebhook(url=WEBHOOKURL, content="@everyone" '\n' + msg)
        response = webhook.execute()


#Checking for new stock, calling the sendalert function if there is.
def checkstock():
    try:
        #HTTP request to the launching API
        req = urllib.request.Request(
            "https://www.footlocker.co.il/api/v1/release-calendar/products?limit=16&offset=0",
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        f = urllib.request.urlopen(req)
        soup = bs4.BeautifulSoup(f, 'lxml')
        htmlbody = soup.getText()



        # Variables to hold if new products or instock products are found
        productsIds = []
        productsPhotoes = []
        productsAvailable = 0
        indexesOfPhotoes = []
        index = 0


        for i in htmlbody.split('isReleased'):
            # Loop using regular expression to search for models and available status
            if (i.find('"isPublish":true')):
                products = re.search(r'"sku_model":"(.+?)"', i)
                try:
                    # Fetching photos of shoes available in stock and making a list out of it
                    productPhoto = re.search(r'"fullUrl":"(.+?)"', i)
                    productsPhotoes.append(productPhoto.group(1))
                except:
                    pass

                if (products.group(1) not in productsIds):
                    # taking each product and making a index list of the available product to match with its photo, also let know of available product
                    productsIds.append(products.group(1))
                    productsavailable = re.search(r'"status":"(.+?)"', i)

                    if (productsavailable.group(1) == 'ON SITE'):
                        indexesOfPhotoes.append(index)
                        productsAvailable = productsAvailable + 1
                    index+=1

        print(productsIds, productsPhotoes, indexesOfPhotoes)
        try:
            return (productsAvailable, productsPhotoes, indexesOfPhotoes)
        except:
            time.sleep(60)
            checkstock()

    except:
        time.sleep(60)
        checkstock()
#
#
def main():
    previousAvailable = 0

    # Using the variable to check if stock number has been changed and alerting if it went up, otherwise change the stock num
    while True:
        try:

            productsAvailable, productsPhotoes, indexesOfPhotoes = checkstock()

            if(productsAvailable != previousAvailable):
                if (productsAvailable < previousAvailable):
                    previousAvailable = productsAvailable
                else:
                    previousAvailable = productsAvailable
                    sendalert(productsPhotoes,indexesOfPhotoes)


            time.sleep(30)
        except():
            time.sleep(60)





if __name__ == '__main__':
    main()

