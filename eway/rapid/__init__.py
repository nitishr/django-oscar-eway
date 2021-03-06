TRANSACTION_RESPONSE_CODES = {
    '00': 'Transaction Approved',
    '01': 'Refer to Issuer',
    '02': 'Refer to Issuer, special',
    '03': 'No Merchant',
    '04': 'Pick Up Card',
    '05': 'Do Not Honour',
    '06': 'Error',
    '07': 'Pick Up Card, Special',
    '08': 'Honour With Identification',
    '09': 'Request In Progress',
    '10': 'Approved For Partial Amount',
    '11': 'Approved, VIP',
    '12': 'Invalid Transaction',
    '13': 'Invalid Amount',
    '14': 'Invalid Card Number',
    '15': 'No Issuer',
    '16': 'Approved, Update Track 3',
    '19': 'Re-enter Last Transaction',
    '21': 'No Action Taken',
    '22': 'Suspected Malfunction',
    '23': 'Unacceptable Transaction Fee',
    '25': 'Unable to Locate Record On File',
    '30': 'Format Error',
    '31': 'Bank Not Supported By Switch',
    '33': 'Expired Card, Capture',
    '34': 'Suspected Fraud, Retain Card',
    '35': 'Card Acceptor, Contact Acquirer, Retain Card',
    '36': 'Restricted Card, Retain Card',
    '37': 'Contact Acquirer Security Department, Retain Card',
    '38': 'PIN Tries Exceeded, Capture',
    '39': 'No Credit Account',
    '40': 'Function Not Supported',
    '41': 'Lost Card',
    '42': 'No Universal Account',
    '43': 'Stolen Card',
    '44': 'No Investment Account',
    '51': 'Insufficient Funds',
    '52': 'No Cheque Account',
    '53': 'No Savings Account',
    '54': 'Expired Card',
    '55': 'Incorrect PIN',
    '56': 'No Card Record',
    '57': 'Function Not Permitted to Cardholder',
    '58': 'Function Not Permitted to Terminal',
    '59': 'Suspected Fraud',
    '60': 'Acceptor Contact Acquirer',
    '61': 'Exceeds Withdrawal Limit',
    '62': 'Restricted Card',
    '63': 'Security Violation',
    '64': 'Original Amount Incorrect',
    '66': 'Acceptor Contact Acquirer, Security',
    '67': 'Capture Card',
    '75': 'PIN Tries Exceeded',
    '82': 'CVV Validation Error',
    '84': 'Do Not Honour (Sandbox',
    '90': 'Cutoff In Progress',
    '91': 'Card Issuer Unavailable',
    '92': 'Unable To Route Transaction',
    '93': 'Cannot Complete, Violation Of The Law',
    '94': 'Duplicate Transaction',
    '96': 'System Error',
}

RESPONSE_CODES = {
    # Transaction response codes
    'A2000': 'Transaction Approved Successful',
    'A2008': 'Honour With Identification Successful',
    'A2010': 'Approved For Partial Amount Successful',
    'A2011': 'Approved, VIP Successful',
    'A2016': 'Approved, Update Track 3 Successful',
    'D4401': 'Refer to Issuer Failed',
    'D4402': 'Refer to Issuer, special Failed',
    'D4403': 'No Merchant Failed',
    'D4404': 'Pick Up Card Failed',
    'D4405': 'Do Not Honour Failed',
    'D4406': 'Error Failed',
    'D4407': 'Pick Up Card, Special Failed',
    'D4409': 'Request In Progress Failed',
    'D4412': 'Invalid Transaction Failed',
    'D4413': 'Invalid Amount Failed',
    'D4414': 'Invalid Card Number Failed',
    'D4415': 'No Issuer Failed',
    'D4419': 'Re-enter Last Transaction Failed',
    'D4421': 'No Action Taken Failed',
    'D4422': 'Suspected Malfunction Failed',
    'D4423': 'Unacceptable Transaction Fee Failed',
    'D4425': 'Unable to Locate Record On File Failed',
    'D4430': 'Format Error Failed',
    'D4431': 'Bank Not Supported By Switch Failed',
    'D4433': 'Expired Card, Capture Failed',
    'D4434': 'Suspected Fraud, Retain Card Failed',
    'D4435': 'Card Acceptor, Contact Acquirer, Retain Card Failed',
    'D4436': 'Restricted Card, Retain Card Failed',
    'D4437': 'Contact Acquirer Security Department, Retain Card Failed',
    'D4438': 'PIN Tries Exceeded, Capture Failed',
    'D4439': 'No Credit Account Failed',
    'D4440': 'Function Not Supported Failed',
    'D4441': 'Lost Card Failed',
    'D4442': 'No Universal Account Failed',
    'D4443': 'Stolen Card Failed',
    'D4444': 'No Investment Account Failed',
    'D4451': 'Insufficient Funds Failed',
    'D4452': 'No Cheque Account Failed',
    'D4453': 'No Savings Account Failed',
    'D4454': 'Expired Card Failed',
    'D4455': 'Incorrect PIN Failed',
    'D4456': 'No Card Record Failed',
    'D4457': 'Function Not Permitted to Cardholder Failed',
    'D4458': 'Function Not Permitted to Terminal Failed',
    'D4459': 'Suspected Fraud Failed',
    'D4460': 'Acceptor Contact Acquirer Failed',
    'D4461': 'Exceeds Withdrawal Limit Failed',
    'D4462': 'Restricted Card Failed',
    'D4463': 'Security Violation Failed',
    'D4464': 'Original Amount Incorrect Failed',
    'D4466': 'Acceptor Contact Acquirer, Security Failed',
    'D4467': 'Capture Card Failed',
    'D4475': 'PIN Tries Exceeded Failed',
    'D4482': 'CVV Validation Error Failed',
    'D4490': 'Cut off In Progress Failed',
    'D4491': 'Card Issuer Unavailable Failed',
    'D4492': 'Unable To Route Transaction Failed',
    'D4493': 'Cannot Complete, Violation Of The Law Failed',
    'D4494': 'Duplicate Transaction Failed',
    'D4496': 'System Error Failed',
    # Beagle (Free and Beagle Alerts Fraud response
    'F7000': 'Undefined Fraud Error',
    'F7001': 'Challenged Fraud',
    'F7002': 'Country Match Fraud',
    'F7003': 'High Risk Country Fraud',
    'F7004': 'Anonymous Proxy Fraud',
    'F7005': 'Transparent Proxy Fraud',
    'F7006': 'Free Email Fraud',
    'F7007': 'International Transaction Fraud',
    'F7008': 'Risk Score Fraud',
    'F7009': 'Denied Fraud',
    'F9010': 'High Risk Billing Country',
    'F9011': 'High Risk Credit Card Country',
    'F9012': 'High Risk Customer IP Address',
    'F9013': 'High Risk Email Address',
    'F9014': 'High Risk Shipping Country',
    'F9015': 'Multiple card numbers for single email address',
    'F9016': 'Multiple card numbers for single location',
    'F9017': 'Multiple email addresses for single card number',
    'F9018': 'Multiple email addresses for single location',
    'F9019': 'Multiple locations for single card number',
    'F9020': 'Multiple locations for single email address',
    'F9021': 'Suspicious Customer First Name',
    'F9022': 'Suspicious Customer Last Name',
    'F9023': 'Transaction Declined',
    'F9024': 'Multiple transactions for same address with known credit card',
    'F9025': 'Multiple transactions for same address with new credit card',
    'F9026': 'Multiple transactions for same email with new credit card',
    'F9027': 'Multiple transactions for same email with known credit card',
    'F9028': 'Multiple transactions for new credit card',
    'F9029': 'Multiple transactions for known credit card',
    'F9030': 'Multiple transactions for same email address',
    'F9031': 'Multiple transactions for same credit card',
    'F9032': 'Invalid Customer Last Name',
    'F9033': 'Invalid Billing Street',
    'F9034': 'Invalid Shipping Street',
    # System response codes
    'S5000': 'System Error',
    'S5085': 'Started 3dSecure',
    'S5086': 'Routed 3dSecure',
    'S5087': 'Completed 3dSecure',
    'S5099': 'Incomplete (Access Code in progress/incomplete',
    # Validation response codes
    'V6000': 'Validation error',
    'V6001': 'Invalid CustomerIP',
    'V6002': 'Invalid DeviceID',
    'V6011': 'Invalid Payment TotalAmount',
    'V6012': 'Invalid Payment InvoiceDescription',
    'V6013': 'Invalid Payment InvoiceNumber',
    'V6014': 'Invalid Payment InvoiceReference',
    'V6015': 'Invalid Payment CurrencyCode',
    'V6016': 'Payment Required',
    'V6017': 'Payment CurrencyCode Required',
    'V6018': 'Unknown Payment CurrencyCode',
    'V6021': 'EWAY_CARDHOLDERNAME Required',
    'V6022': 'EWAY_CARDNUMBER Required',
    'V6023': 'EWAY_CARDCVN Required',
    'V6033': 'Invalid Expiry Date',
    'V6034': 'Invalid Issue Number',
    'V6035': 'Invalid Valid From Date',
    'V6040': 'Invalid TokenCustomerID',
    'V6041': 'Customer Required',
    'V6042': 'Customer FirstName Required',
    'V6043': 'Customer LastName Required',
    'V6044': 'Customer CountryCode Required',
    'V6045': 'Customer Title Required',
    'V6046': 'TokenCustomerID Required',
    'V6047': 'RedirectURL Required',
    'V6051': 'Invalid Customer FirstName',
    'V6052': 'Invalid Customer LastName',
    'V6053': 'Invalid Customer CountryCode',
    'V6058': 'Invalid Customer Title',
    'V6059': 'Invalid RedirectURL',
    'V6060': 'Invalid TokenCustomerID',
    'V6061': 'Invalid Customer Reference',
    'V6062': 'Invalid Customer CompanyName',
    'V6063': 'Invalid Customer JobDescription',
    'V6064': 'Invalid Customer Street1',
    'V6065': 'Invalid Customer Street2',
    'V6066': 'Invalid Customer City',
    'V6067': 'Invalid Customer State',
    'V6068': 'Invalid Customer PostalCode',
    'V6069': 'Invalid Customer Email',
    'V6070': 'Invalid Customer Phone',
    'V6071': 'Invalid Customer Mobile',
    'V6072': 'Invalid Customer Comments',
    'V6073': 'Invalid Customer Fax',
    'V6074': 'Invalid Customer URL',
    'V6075': 'Invalid ShippingAddress FirstName',
    'V6076': 'Invalid ShippingAddress LastName',
    'V6077': 'Invalid ShippingAddress Street1',
    'V6078': 'Invalid ShippingAddress Street2',
    'V6079': 'Invalid ShippingAddress City',
    'V6080': 'Invalid ShippingAddress State',
    'V6081': 'Invalid ShippingAddress PostalCode',
    'V6082': 'Invalid ShippingAddress Email',
    'V6083': 'Invalid ShippingAddress Phone',
    'V6084': 'Invalid ShippingAddress Country',
    'V6085': 'Invalid ShippingAddress ShippingMethod',
    'V6086': 'Invalid ShippingAddress Fax',
    'V6091': 'Unknown Customer CountryCode',
    'V6092': 'Unknown ShippingAddress CountryCode',
    'V6100': 'Invalid EWAY_CARDNAME',
    'V6101': 'Invalid EWAY_CARDEXPIRYMONTH',
    'V6102': 'Invalid EWAY_CARDEXPIRYYEAR',
    'V6103': 'Invalid EWAY_CARDSTARTMONTH',
    'V6104': 'Invalid EWAY_CARDSTARTYEAR',
    'V6105': 'Invalid EWAY_CARDISSUENUMBER',
    'V6106': 'Invalid EWAY_CARDCVN',
    'V6107': 'Invalid EWAY_ACCESSCODE',
    'V6108': 'Invalid CustomerHostAddress',
    'V6109': 'Invalid UserAgent',
    'V6110': 'Invalid EWAY_CARDNUMBER',
}
RESPONSE_CODES.update(TRANSACTION_RESPONSE_CODES)
