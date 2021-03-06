
:main
call :%*
goto :eof

:listim
echo docker images
docker images
goto :eof

:rmim
echo delete a docker image
for %%i in (%*) do (
    echo docker rmi %%i
    docker rmi %%i
    )
goto :eof

:listco
echo docker ps -a
docker ps -a
goto :eof

:stopco
echo docker stop $2
docker stop $2
goto :eof

:rmco
	# ~/building stopco $2
	# echo sudo docker rm $2
	# sudo docker rm $2
	echo stop and delete a docker container
	shift
	while (( "$#" ))
	do
	    echo docker stop $1
	    docker stop $1
	    echo docker rm $1
	    docker rm $1
	    shift
	done
goto :eof

:startco
echo docker start $2
docker start $2
goto :eof

:restartco
	~/building stopco $2
	~/building startco $2
goto :eof

:bashco
echo start a bash in a container
docker exec -it $2 bash
goto :eof

:dcup
echo docker-compose up -d
docker-compose up -d
goto :eof

:dcrund
echo docker-compose run -d $2
docker-compose run -d $2
goto :eof

:dcstop
echo docker-compose stop
docker-compose stop
goto :eof

:dcdown
echo docker-compose down
docker-compose down
goto :eof

:dcbuild
echo docker-compose build
docker-compose build
goto :eof

:dinfo
docker info
goto :eof

:dversion
docker version
goto :eof

:testloop
for %%i in (%*) do (
    echo docker %%i
    )
goto :eof

:scratches
echo Hello World
echo command line count: $#
cmd=$1
echo command to execute: $cmd
echo ${cmd,} ${cmd,,}

case ${cmd,,} in
    listim)
	echo sudo docker images
	sudo docker images
	;;
    rmim)
	# echo sudo docker rmi $2
	# sudo docker rmi $2
	echo delete a docker image
	shift
	while (( "$#" ))
	do
	    echo docker rmi $1
	    sudo docker rmi $1
	    shift
	done
	;;
    listco)
	echo sudo docker ps -a
	sudo docker ps -a
	;;
    stopco)
	echo sudo docker stop $2
	sudo docker stop $2
	;;
    rmco)
	# ~/building stopco $2
	# echo sudo docker rm $2
	# sudo docker rm $2
	echo stop and delete a docker container
	shift
	while (( "$#" ))
	do
	    echo docker stop $1
	    sudo docker stop $1
	    echo docker rm $1
	    sudo docker rm $1
	    shift
	done
	;;
    startco)
	echo sudo docker start $2
	sudo docker start $2
	;;
    restartco)
	~/building stopco $2
	~/building startco $2
	;;
    bashco)
	echo start a bash in a container
	sudo docker exec -it $2 bash
	;;
    dcup)
	echo docker-compose up -d
	sudo docker-compose up -d
	;;
    dcrund)
	echo docker-compose run -d $2
	sudo docker-compose run -d $2
	;;
    dcstop)
	echo docker-compose stop
	sudo docker-compose stop
	;;
    dcdown)
	echo docker-compose down
	sudo docker-compose down
	;;
    dcbuild)
	echo docker-compose build
	sudo docker-compose build
	;;
    dinfo)
	sudo docker info
	;;
    dversion)
	sudo docker version
	;;
    *)
	echo unknown command ${cmd,,}
	;;
esac
