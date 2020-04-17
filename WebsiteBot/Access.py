#############################################
## This is the attempt to access a website ##
#############################################

import requests #imports requests module. You need this to perform requests.

#   links:
#       "https://www.google.com/"
#       "https://fabrizzioorderique.weebly.com/"
#       "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

google = requests.get("https://www.google.com/") 
print (google.text)
