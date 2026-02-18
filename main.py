from socket import * 
import time
startTime = time.time()
if __name__ == '__main__':
    target = input('enter the host to be scanned: ')
    t_Ip = gethostbyname(target)
    print('starting scanf on host: ',t_Ip)
    for i in range(50, 500):
        s= socket(AF_INET,SOCK_STREAM)
        conn = s.connect_ex((t_Ip,i))
        if(conn==0):
            print('port %d: OPEN' %(i,))
        s.close()
print('Time taken: ',time.time() - startTime)
