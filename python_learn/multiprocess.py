from tqdm import tqdm
import multiprocessing as mp
import signal
import time

TOTAL = 100
def tqdm_worker(queue, num_bars=3):
    
    bar_status = tqdm(desc="[Status]", position=0)
    bars = []
    for i in range(num_bars):
        bar = tqdm(total=TOTAL, desc=f"Proccess id: {i}", position=i+1)
        bar.set_postfix({"test": 0})
        bars.append(bar)

    while True:
        if not queue.empty():
            bar_status.set_postfix_str("updating...")
            item = queue.get() # should get the id of the bar to update and the post fix info
            '''
            example
            {
                "id": 0,
                "postfix": {
                    "test": 1,
                    "total": 100
                    "category": "chair"
                }
            }
            '''
            try:
                id = item['id']
                if id == -1:
                    break
                bars[id].update(1)
                bars[id].set_postfix(item['postfix'])
            except IndexError:
                bar_status.set_postfix_str("IndexError")
        else:
            bar_status.set_postfix_str("queue empty...")
        # time.sleep(0.01) # 100 HZ frequency
        

def update_bars(queue, id, deplay):
    for i in range(TOTAL):
        time.sleep(deplay)
        bar_dict = {
            'id': id,
            'postfix': {
            }
        }
        queue.put(bar_dict)
        

if __name__ == "__main__":
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)

    q = mp.Queue()

    main_p = mp.Process(target=tqdm_worker, args=(q,))
    bar_p0 = mp.Process(target=update_bars, args=(q, 0, 0.1))
    bar_p1 = mp.Process(target=update_bars, args=(q, 1, 0.2))
    bar_p2 = mp.Process(target=update_bars, args=(q, 2, 0.3))
    
    bar_process = [bar_p0, bar_p1, bar_p2]

    try:
        main_p.start()
        time.sleep(1) # wait for the main process to start
        for p in bar_process:
            p.start()
            
        # catch Ctrl+C in the main process, subprocesses signal will be ignored
        signal.signal(signal.SIGINT, original_sigint_handler) 
            
        for p in bar_process:
            p.join()

        q.put({
            'id': -1,
            'postfix': {
            }
        })# exit the while loop of tqdm_worker
        # main_p.join()
    except KeyboardInterrupt:
        # exit all processes
        print("[EXCEPTION] KeyboardInterrupt, exiting...")
        for p in bar_process:
            p.terminate()
        while not q.empty():
            q.get()  # as docs say: Remove and return an item from the queue.
        q.put({
            'id': -1,
            'postfix': {
            }
        })
        # q.close()
        # main_p.terminate() # results in memory leak
        