renew:
	cp /etc/*.cshrc ./etc_cpy
	git add --all
	git commit -m "renew"
	git push
