sudo docker-compose exec kafka  \
  kafka-console-consumer --bootstrap-server localhost:29092 --topic foo --new-consumer --from-beginning --max-messages 42