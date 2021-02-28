ansible-playbook -i "test01.local,test02.local,"  main.yml -e target="test01.local,test02.local,"


### specify logging driver + storage driver add option  docker_storage_driver and docker_log_driver


ansible-playbook -i "test01.local,test02.local,"  main.yml -e target="test01.local,test02.local," -e "docker_storage_driver=devicemapper" -e "docker_log_driver=local"