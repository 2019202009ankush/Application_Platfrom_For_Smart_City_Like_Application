gnome-terminal --tab --title="echo" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_sch; exec bash"
gnome-terminal --tab --title="echo1" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_app; exec bash"
gnome-terminal --tab --title="echo2" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_deploy; exec bash"
gnome-terminal --tab --title="echo3" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_log; exec bash"
gnome-terminal --tab --title="echo4" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_mon; exec bash"
gnome-terminal --tab --title="echo5" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_sensor; exec bash"
gnome-terminal --tab --title="echo6" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server; exec bash"
gnome-terminal --tab --title="echo7" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_service; exec bash"
#gnome-terminal --tab --title="echo8" -- bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_topo; exec bash"

#sudo docker run --rm --network=host lensesio/fast-data-dev
gnome-terminal --geometry=65x16+0+0 --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_action; exec bash"
gnome-terminal --geometry=65x16+1000+0 --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server1; exec bash"
gnome-terminal --geometry=65x16+0+1000 --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server2; exec bash"
gnome-terminal --geometry=65x16+1000+1000 --  bash -c "sudo docker run --rm --network=host -v $PWD/../../:/opt dock_server3; exec bash"

