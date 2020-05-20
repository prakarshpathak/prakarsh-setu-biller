# Prakarsh Setu Biller
* **URL** : https://sheltered-brushlands-07479.herokuapp.com/bills/fetchReceipt

* **Method:** : `GET`
* **Headers** : Authorization
  
*  **Request Body**
```
{
    "billerBillID"   : "2",
    "platformBillID" : "SETU121341312121",
    "paymentDetails" : {
        "platformTransactionRefID" : "TXN12121219",
        "uniquePaymentRefID"       : "XXXXAYYDDD999999",
        "amountPaid" : {
            "value" : 99000 
        },
        "billAmount" : {
            "value" : 99000
        }
    }
}
```    
* **Success Response:**
```
{
    "status": 200,
    "success": true,
    "data": {
        "billerBillID": "2",
        "platformBillID": "SETU121341312121",
        "platformTransactionRefID": "TXN12121219",
        "receipt": {
            "id": 11,
            "date": "2020-05-20T18:31:00.300"
        }
    }
}
```
  * **Code:** 200 

* **URL** :  https://sheltered-brushlands-07479.herokuapp.com/bills/fetch

* **Method:** : `GET`
* **Headers**: Authorization
  
*  **Request Body**
```
{
    "customerIdentifiers": [
        {
            "attributeName": "mobileNumber",
            "attributeValue": "123456889"
        }
    ]
}

```    
* **Success Response:**
```
{
    "status": 200,
    "success": true,
    "data": {
        "customer": {
            "name": "Ashok Kumar"
        },
        "billDetails": {
            "billFetchStatus": "AVAILABLE",
            "bills": [
                {
                    "billerBillID": 2,
                    "generatedOn": "2020-05-18T19:27:27.630Z",
                    "customerAccount": {
                        "id": 7
                    },
                    "aggregates": {
                        "total": {
                            "displayName": "Total Outstanding",
                            "amount": {
                                "value": 900056
                            }
                        }
                    }
                },
                {
                    "billerBillID": 3,
                    "generatedOn": "2020-05-18T19:29:44.023Z",
                    "customerAccount": {
                        "id": 7
                    },
                    "aggregates": {
                        "total": {
                            "displayName": "Total Outstanding",
                            "amount": {
                                "value": 900056
                            }
                        }
                    }
                }
            ]
        }
    }
}
```
  * **Code:** 200 

