renew:
	cp /etc/*.cshrc ./etc_cpy
	git add --all
	git commit -m "renew"
	git push

setup_workstation:
	cp ./etc_cpy/*.cshrc /etc/
	if [ ! -d "/lib/lab-shell" ]; then
		mkdir "/lib/lab-shell"
	fi 	
	cp ./* /lib/lab-shell
