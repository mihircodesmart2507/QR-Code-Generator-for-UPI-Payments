import qrcode

#Taking UPI Id's as a Input 

upi_id = input("Enter UPI ID: ")

# upi= "upi://pay?pa=" + upi_id + "&pn=YourName&mc=YourMerchantCode&tid=TransactionId&am=Amount&cu=Currency&tn= Message"

#Defining the payment UPI based on the input UPI ID and the payment app
# You can modify these URL's based on the payment app you want to support 

phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234' 

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url) 

#Save the QR Codes as image files
phonepe_qr.save("phonepe_qr.png") 
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")  

#Display the QR Codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

