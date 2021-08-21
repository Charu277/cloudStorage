import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)
def main():
    access_token='i6PNTHwJId8AAAAAAAAAAYf1sC3wkiUniZ63RBozwRFwgwzYIbxKtcwHHWFXB4vR'
    transferData=TransferData(access_token)
    filefrom=input("enter the path file to transfer")
    fileto= input("enter the path to upload to dropbox")
    transferData.uploadFile(filefrom,fileto)
    print("the files moved successfully")
main()

      
