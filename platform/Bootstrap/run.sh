sudo docker run --rm --network=host -v $PWD/../../:/opt dock_deploy &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_log &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_mon &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_sch &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_sensor &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_service &
sudo docker run --rm --network=host -v $PWD/../../:/opt dock_topo &
sudo docker run --rm --network=host lensesio/fast-data-dev
gnome-terminal --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_action; exec bash"
gnome-terminal --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server1; exec bash"
gnome-terminal --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server2; exec bash"
gnome-terminal --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_app; exec bash"

