# travel_it
Just my first try of creation web appliacation


To install all lib that needed in project just run pip install -r requirements.txt
(please do not forget to create venv)

Docker installation:

    for Ubuntu - https://docs.docker.com/install/linux/docker-ce/ubuntu/
    for CentOS - https://docs.docker.com/install/linux/docker-ce/centos/
    for Debian - https://docs.docker.com/install/linux/docker-ce/debian/
    for Windows - https://docs.docker.com/docker-for-windows/install/
    for MacOS - https://docs.docker.com/docker-for-mac/install/
    
Install Docker-Compose:

    https://docs.docker.com/compose/install/
    
Post-installation step:
    - Make docker executable without sudo:
    
        sudo groupadd docker
        sudo usermod -aG docker $USER
        newgrp docker 
    
Run docker container with postgresql:
   - Download postgres docker image from DockerHub (need to run only once):
     
    docker pull postgres
        
   - Run docker container with normal syntax:
    
    docker volume create --name db_volume
    docker run -d --name postgres -p 5432:5432 \
       --env-file docker/database.conf \
       -v db_volume:/var/lib/postgresql postgres:latest
       
   NOTE!!!: If you do not have database.conf please ask Alex Plotnikov
             
   - OR run with docker-compose (docker_travel_it.yaml needed)
   
    sudo docker-compose -f docker_travel_it.yml up --build -d
        
Connect to the docker container:

    docker exec -it <docker_container_id> bash
    
Use direnv for env for your project:
    
    sudo apt install direnv
    tail -n1 ~/.bashrc
    eval "$(direnv hook bash)"
    
Then create .envrc file in your project directory with all needed environment (for ex. from database.conf). Example:

    export POSTGRES_USER="example"
    export POSTGRES_PASSWORD="example"
  
Then allow direnv
 
    cd <folder with project>
    direnv allow
    
