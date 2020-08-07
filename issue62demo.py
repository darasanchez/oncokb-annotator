import requests
url = 'https://www.oncokb.org/api/v1/annotate/mutations/byProteinChange'
myobject ={
    "alteration": "V600E",
    "gene": {
    "hugoSymbol": "BRAF"
    },
    "tumorType": "Melanoma"
  }
x = requests.post(url).json()
print(x)