
----
# prakarsh_setu_biller
* **URL**

https://sheltered-brushlands-07479.herokuapp.com/bills/fetchReceipt

* **Method:**
  `GET`
* **Headers**: Authorization
  
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
