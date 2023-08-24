#pip install speedtest-cli

import speedtest as st


    
#configuramos el servidor
def server_subida():
    server=st.Speedtest()
    server.get_best_server()

#test de subida

    up=server.upload()
    up=up/1000000
    return round(up)
    
    
