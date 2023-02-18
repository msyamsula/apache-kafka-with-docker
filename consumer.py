from confluent_kafka import Consumer
import json

# configurasi + connect ke kafka
conf = {'bootstrap.servers': "kafka:9092",
        'group.id': "syamsul",
        'auto.offset.reset': 'smallest',
        # 'enable.auto.commit': False
        }
consumer = Consumer(conf)


# fungsi consume topic
running = True
def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0) # ngambil kemungkinan data yg masih ada di kafka
            if msg is None: continue

            if msg.error():
                # error handling block
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:

                # processing block
                key = int(msg.key().decode('utf-8'))
                value = json.loads(msg.value().decode('utf-8'))
                print("dapet data key = ", key)
                # print("DUMP TO BIGQUERY")
                # print(key)
                # print(value)
    except:
        print("error")
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def shutdown():
    running = False

topics = ["testing"]
basic_consume_loop(consumer, topics)


# things to consider
# load gimana
# error handling
# alerting, optional (digunakan secara bijak)
# data type, processing
# topic partition berapa? load balancing, topic