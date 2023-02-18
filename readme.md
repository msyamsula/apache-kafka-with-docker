docker build -t kafka . (build image)

docker network create my-network (create network)

docker volume create my-volume (create volume)

docker-compose up -d (run kafka broker and zookeeper)

docker run -it --name producer -v "/path/to/project":/app/ -v my-volume:/backup --network=my-network kafka /bin/bash (run producer)

docker run -it --name consumer -v "/path/to/project":/app/ -v my-volume:/backup --network=my-network kafka /bin/bash (run consumer, different terminal with producer)
    
on consumer terminal run "python consumer.py"

on producer terminal run "python producerv2.py"


link to diagram: https://lucid.app/lucidchart/ab4eb4f7-7bba-47f5-8478-a83a4b9e844e/edit?viewport_loc=-44%2C185%2C1707%2C711%2C0_0&invitationId=inv_5883a8cd-5058-4ced-a730-0c4cbe9ff7c6

