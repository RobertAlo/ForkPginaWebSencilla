#pip install speedtest-cli

import speedtest as st

    
#configuramos el servidor
def server_bajada():
    server=st.Speedtest()
    server.get_best_server()

#test de bajada
    down=server.download()
    down=down/1000000
    return round(down)
    
    




