import websocket
import threading
import json


class SocketConn(websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(url=url, on_open=self.on_open)

        self.on_message = lambda ws, msg: self.message(msg)
        self.on_error = lambda ws, e: print('ERROR: ',e)
        self.on_close = lambda ws: print('CLOSING')

        self.bids = []
        self.asks = []
        self.all = 0

        self.run_forever()

    def on_open(self, ws,):
        print("Websocket was opened")

    def message(self, msg):
        msg = json.loads(msg)

        ktr_b_back = []
        for bids in self.bids:
            for b in msg['b']:
                if bids == b:
                    ktr_b_back.append(bids)

        ktr_a_back = []
        for bids in self.bids:
            for b in msg['b']:
                if bids == b:
                    ktr_a_back.append(bids)

        db = 0
        da = 0

        for b in msg['b']:
            sum = True
            for back in ktr_b_back:
                if b == back:
                    sum = False

            if sum == True:
                db += float(b[0]) * float(b[1])

        for a in msg['a']:
            sum = True
            for back in ktr_a_back:
                if a == back:
                    sum = False

            if sum == True:
                da += float(a[0]) * float(a[1])

        #print(msg)
        #print(msg['b'])
        #print(msg['a'])
        #db = 0
        #da = 0
        #for pr,qua in msg['b']:
        #    db +=float(pr)*float(qua)
        #for pr,qua in msg['a']:
        #    da +=float(pr)*float(qua)

        #print(db)
        #print(da)

        oi = db - da
        self.all = self.all + oi
        self.bids = msg['b']
        self.asks = msg['a']
        print(f'all {self.all} : oi {oi}')





threading.Thread(target=SocketConn, args=('wss://fstream.binance.com/ws/oxtusdt@depth@500ms',)).start()#<symbol>@forceOrder
#threading.Thread(target=SocketConn, args=('wss://fstream.binance.com/stream?streams=nknusdt@depth@500ms/btcusdt@markPrice',)).start()#<symbol>@forceOrder










