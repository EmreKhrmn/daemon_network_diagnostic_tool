import ntplib
from time import ctime, time

def get_sntp_time():

    #network time
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    network_time= ctime(response.tx_time)

    #local system time
    local_time = ctime(time())

    #result
    print("-"*30)
    print(f"Network Time: {network_time}")
    print(f"Local Time:   {local_time}")
    print(f"-"*30)




#---------------------------------------------------
if __name__ == "__main__":
    get_sntp_time()