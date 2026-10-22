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
    #[OLD]print("-"*30)
    #[OLD]print(f"Network Time: {network_time}")
    #[OLD]print(f"Local Time:   {local_time}")
    #[OLD]print(f"-"*30)

    return (
        f"{'-'*30}\n"
        f"Network Time: {network_time}\n"
        f"Local Time:   {local_time}\n"
        f"{'-'*30}"
    )



#---------------------------------------------------
if __name__ == "__main__":
    print(get_sntp_time())